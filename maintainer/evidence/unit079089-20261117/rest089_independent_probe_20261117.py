"""Independent UNITTEST-083 candidate provenance and destructive-in-memory controls."""
import ast
import asyncio
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import subprocess
import sys
from unittest.mock import patch
import xml.etree.ElementTree as ET

import httpx
import pytest

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / '.ept/tmp/feature015_rest089_unit_modes'
SDK = ROOT / '.ept/docs/customer_input/foundry-platform-python'
BASE = '77b101fb7c5e51fa5f785b2147d97cdfff703133'
PIN = '168d51910570b6966afa2320333ab36f6a3f7ccf'
TEST = CANDIDATE / 'tests/test_offline_rest_089.py'
OUT = ROOT / '.ept/tmp/feature015_rest089_unit_independent_qa_20261117.json'

def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])

def digest(data):
    return hashlib.sha256(data).hexdigest()

sys.path.insert(0, str(CANDIDATE / '.agents/skills/pal-found-dev/examples/rest/common'))
spec = importlib.util.spec_from_file_location('independent_rest089_candidate', TEST)
t = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t)
before = TEST.read_bytes()
base_test = git(CANDIDATE, 'show', BASE + ':tests/test_offline_rest_089.py')
base_tree, tree = ast.parse(base_test), ast.parse(before)
functions = {n.name: ast.dump(n) for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
preserved = [n.name for n in base_tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name != 'deny_network']
assert all(functions[n.name] == ast.dump(n) for n in base_tree.body
           if isinstance(n, (ast.FunctionDef, ast.ClassDef)) and n.name != 'deny_network')
assert git(CANDIDATE, 'diff', '--name-only', BASE).decode().splitlines() == ['tests/test_offline_rest_089.py']
assert git(SDK, 'rev-parse', '1.101.0^{}').decode().strip() == PIN
product_files = sorted((CANDIDATE / '.agents/skills/pal-found-dev').rglob('*'))
product_hashes = {str(p.relative_to(CANDIDATE)): digest(p.read_bytes()) for p in product_files
                  if p.is_file() and '__pycache__' not in str(p) and p.suffix != '.pyc'}
source_proofs = {}

def pinned_module(module):
    path = Path(module.__file__)
    relative = 'foundry_sdk/' + path.as_posix().split('/foundry_sdk/', 1)[1]
    if relative in source_proofs:
        assert digest(path.read_bytes()) == source_proofs[relative]
        return relative
    frozen = git(SDK, 'show', PIN + ':' + relative)
    assert frozen == path.read_bytes(), relative
    source_proofs[relative] = digest(frozen)
    return relative

bindings = []
for identity in t.IDS:
    module, client, method, fields = t.source_contract(identity)
    source = pinned_module(module)
    frozen_tree = ast.parse(git(SDK, 'show', PIN + ':' + source))
    source_class = next(n for n in frozen_tree.body if isinstance(n, ast.ClassDef) and n.name == client.__name__)
    source_method = next(n for n in source_class.body if isinstance(n, ast.FunctionDef) and n.name == identity.rsplit('.', 1)[1])
    request_nodes = [n for n in ast.walk(source_method) if isinstance(n, ast.Call)
                     and isinstance(n.func, ast.Attribute) and n.func.attr == 'RequestInfo']
    assert len(request_nodes) == 1
    independent_fields = {k.arg: k.value for k in request_nodes[0].keywords}
    assert {k: ast.dump(v) for k, v in independent_fields.items()} == {k: ast.dump(v) for k, v in fields.items()}
    example = t.owned_example(identity)
    arguments = t.operation_inputs(example)
    errors = t.expected_field(identity, 'throwable_errors')
    fixtures = {item['name']: item for item in example['ERRORS']}
    error_rows = []
    for name, cls in errors.items():
        cls_module = sys.modules[cls.__module__]
        error_source = pinned_module(cls_module)
        annotation = cls.__annotations__['parameters']
        parameters = t.TypeAdapter(annotation).validate_python(fixtures[name]['parameters'])
        error_rows.append({'name': name, 'runtime_class': cls.__module__ + '.' + cls.__qualname__,
                           'source': error_source, 'parameter_type': str(annotation),
                           'validated_parameters': t.normalized(parameters)})
    modes = []
    import mock_transport
    for async_ in (False, True):
        cls = getattr(module, ('Async' if async_ else '') + client.__name__)
        with mock_transport.mock_resource(cls, lambda request: httpx.Response(204)) as instance:
            wrappers = {'ordinary': instance, 'raw': instance.with_raw_response,
                        'streaming': instance.with_streaming_response}
        for mode, prefix in [('ordinary', ''), ('raw', 'WithRawResponse'), ('streaming', 'WithStreamingResponse')]:
            target = wrappers[mode]
            owner = type(target)
            pinned_module(sys.modules[owner.__module__])
            available = hasattr(target, identity.rsplit('.', 1)[1])
            assert available == (mode != 'streaming' or t.expected_field(identity, 'response_type') is not None), (identity, async_, mode, owner, available)
            modes.append({'async': async_, 'mode': mode, 'available': available,
                          'class': owner.__module__ + '.' + owner.__qualname__,
                          'signature': str(inspect.signature(getattr(target, identity.rsplit('.', 1)[1]))) if available else None})
    bindings.append({'identity': identity, 'source': source, 'signature': str(inspect.signature(method)),
                     'response_type': str(t.expected_field(identity, 'response_type')),
                     'wire_ast': {k: ast.unparse(v) for k, v in fields.items()},
                     'arguments': t.normalized(arguments), 'modes': modes, 'errors': error_rows})

loop = asyncio.new_event_loop()
mp = pytest.MonkeyPatch()
guard = t.deny_network.__wrapped__(mp, loop)
controls = []
runtime_results = []
runtime_errors = []

def killed(label, callback, expected=(AssertionError,)):
    try:
        callback()
    except expected as exc:
        controls.append({'control': label, 'detected': True, 'exception': type(exc).__name__, 'message': str(exc)[:250]})
    else:
        raise AssertionError('Mutant survived: ' + label)

try:
    t.test_public_network_dns_and_native_http_guards_are_active(loop)
    for identity, asynchronous, mode in t.AVAILABLE_MODES:
        example = t.owned_example(identity)
        payload = t.payload_for(identity, example)
        actual = t.execute_mode(identity, example, lambda request: t.response_for(payload), asynchronous, mode, loop)
        expected = t.TypeAdapter(t.expected_field(identity, 'response_type')).validate_python(payload)
        if mode == 'ordinary' and identity.endswith('.list'):
            expected = expected.data
        expected_class = type(expected)
        if identity == 'v2.sql_queries.SqlQuery.get_results' and mode == 'ordinary':
            from foundry_sdk._core.table import ArrowTableResponse
            pinned_module(sys.modules[ArrowTableResponse.__module__])
            expected_class = ArrowTableResponse
        assert type(actual) is expected_class and actual == expected, (identity, asynchronous, mode, type(actual), expected_class)
        if isinstance(actual, list):
            assert all(type(a) is type(e) for a, e in zip(actual, expected))
        runtime_results.append({'identity': identity, 'async': asynchronous, 'mode': mode,
                                'actual_type': type(actual).__module__ + '.' + type(actual).__qualname__,
                                'expected_type': expected_class.__module__ + '.' + expected_class.__qualname__,
                                'exact_runtime_type_match': True})
    real_execute = t.execute_mode
    def observe_errors(identity, example, handler, asynchronous, mode, event_loop, arguments=None):
        try:
            return real_execute(identity, example, handler, asynchronous, mode, event_loop, arguments)
        except Exception as exc:
            runtime_errors.append({'identity': identity, 'async': asynchronous, 'mode': mode,
                                   'name': exc.name, 'actual_class': type(exc).__module__ + '.' + type(exc).__qualname__,
                                   'parameters': t.normalized(exc.parameters)})
            raise
    with patch.object(t, 'execute_mode', observe_errors):
        for identity, asynchronous, mode in t.AVAILABLE_MODES:
            t.test_all_source_error_classes_and_generic_denial_in_available_modes(identity, asynchronous, mode, loop)
    assert len(runtime_errors) == 1038
    # Independent mutations of actual serialized HTTP requests, across every operation.
    for identity in t.IDS:
        example = t.owned_example(identity)
        args = t.operation_inputs(example)
        requests = []
        def capture(request):
            requests.append(request)
            return t.response_for(t.payload_for(identity, example))
        t.execute_mode(identity, example, capture, False, 'raw', loop)
        original = requests[0]
        for fault in ('authorization', 'query', 'timeout'):
            headers, extensions = dict(original.headers), dict(original.extensions)
            url = original.url
            if fault == 'authorization':
                headers['authorization'] = 'Bearer wrong'
            elif fault == 'query':
                url = url.copy_add_param('independentWrongQuery', '1')
            else:
                extensions['timeout'] = dict(extensions['timeout'], read=999)
            damaged = httpx.Request(original.method, url, headers=headers, content=original.content, extensions=extensions)
            killed(identity + ':' + fault, lambda: t.check_source_request(identity, args, damaged))
    for identity in t.STREAM_IDS:
        for asynchronous in (False, True):
            with patch.object(t.TrackedStream, 'close', lambda self: None):
                killed(identity + ':skip_stream_close:' + str(asynchronous), lambda:
                       t.test_unbuffered_stream_caller_interrupt_or_cancel_closes_unread_body(identity, asynchronous, loop))
    identity = 'v2.streams.Stream.get_end_offsets'
    payload = t.payload_for(identity, t.owned_example(identity))
    killed('typed_result_changed_value', lambda: t.assert_typed_result(identity, payload, {}))
    # A real registered error must reject demotion to a generic HTTP error.
    original_execute = t.execute_mode
    def wrong_error(*args, **kwargs):
        from foundry_sdk._errors import PermissionDeniedError
        raise PermissionDeniedError({'errorName': 'UnregisteredOfflineDenial', 'errorCode': 'PERMISSION_DENIED',
                                    'parameters': {'reason': 'fixture denial'},
                                    'errorInstanceId': '00000000-0000-0000-0000-000000000004'})
    with patch.object(t, 'execute_mode', wrong_error):
        killed('named_error_demoted_to_generic', lambda:
               t.test_all_source_error_classes_and_generic_denial_in_available_modes(identity, False, 'raw', loop), (t.PermissionDeniedError,))
finally:
    loop.run_until_complete(loop.shutdown_asyncgens())
    mp.undo()
    loop.close()

assert before == TEST.read_bytes()
assert all(digest((CANDIDATE / p).read_bytes()) == h for p, h in product_hashes.items())
suite = ET.parse(ROOT / '.ept/tmp/rest089_units_independent_20261117.xml').getroot().find('testsuite')
assert suite.attrib['tests'] == '1155' and suite.attrib['failures'] == '0' and suite.attrib['errors'] == '0'
report = {'verdict': 'PASS_READY_FOR_REVIEW_AND_COMMIT',
          'boundary': 'Independent unit candidate review only. No formal acceptance, tracker writes, commits, push, or live platform claims.',
          'candidate': str(CANDIDATE), 'base': BASE, 'test_sha256': digest(before), 'test_lines': len(before.splitlines()),
          'source_commit': PIN, 'source_tag': '1.101.0', 'source_proofs': source_proofs,
          'scope': {'operations': 40, 'named_error_entries': sum(len(x['errors']) for x in bindings),
                    'available_success_forms': len(t.AVAILABLE_MODES),
                    'named_error_runtime_combinations': sum(len(t.expected_field(i, 'throwable_errors')) for i,a,m in t.AVAILABLE_MODES),
                    'streaming_supported_operations': len(t.STREAM_IDS), 'absent_stream_forms': 18,
                    'pagers': t.PAGED_IDS, 'baseline_AST_nodes_preserved': preserved,
                    'baseline_collected_cases': 52, 'final_cases': 1155, 'discarded_no_op_cases': 54},
          'pytest': suite.attrib, 'ruff': 'D:/app/Python/Scripts/ruff.exe check tests/test_offline_rest_089.py; separately captured exit 0',
          'product_unchanged_hashes': product_hashes, 'bindings': bindings, 'independent_controls': controls,
          'independent_runtime_result_identities': runtime_results,
          'actual_error_class_and_parameter_executions': runtime_errors,
          'source_derivation': 'Independently parsed complete frozen Git-tag modules and selected exact Client method RequestInfo AST; compared every field to installed-source unit oracle. Errors and wrapper modules byte-identical to frozen commit.',
          'fixture_change': 'Existing deny_network fixture additionally binds pre-created Windows loop and denies both native HTTP transports. All original test/helper AST preserved.',
          'sql_format_boundary': 'Default get_results independently uses valid Arrow IPC. Accepted product transport placeholder remains unchanged; linked reader lifecycle requests CSV and decodes CSV. execute_ontology decodes actual Arrow with row/byte budgets.',
          'offline_boundary': 'DNS/socket/native HTTP calls denied; Windows event-loop local self-pipe created before guard. Constructor replacement remains confined to version-specific mock transport context; no SDK global policy change.'}
OUT.write_text(json.dumps(report, indent=2, default=str) + '\n')
print(json.dumps({'output': str(OUT), 'controls_killed': len(controls), 'source_modules': len(source_proofs), 'scope': report['scope']}))
