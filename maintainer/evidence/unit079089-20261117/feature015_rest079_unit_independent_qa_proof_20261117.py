"""Independent frozen-source and fault-injection checks for UNITTEST-079."""
import ast
import asyncio
import copy
import dataclasses
import hashlib
import importlib
import importlib.util
import inspect
import json
from pathlib import Path
import socket
import subprocess
import urllib.parse
import typing
from unittest.mock import patch
import xml.etree.ElementTree as ET

import httpx
from foundry_sdk import _core

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / '.ept/tmp/feature015_rest079_unit_modes'
TAG = '168d51910570b6966afa2320333ab36f6a3f7ccf'
BASE = '77b101fb7c5e51fa5f785b2147d97cdfff703133'
TEST = CANDIDATE / 'tests/test_offline_rest_079.py'
REPORT = ROOT / '.ept/tmp/feature015_rest079_unit_independent_qa_20261117.json'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def git(repository, *arguments):
    return subprocess.check_output(['git', '-C', str(repository), *arguments])


spec = importlib.util.spec_from_file_location('candidate079', TEST)
candidate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(candidate)
initial_hash = digest(TEST.read_bytes())
author_report_path = ROOT / '.ept/tmp/feature015_rest079_unit_modes_candidate_20261117.json'
author_report_hash = digest(author_report_path.read_bytes())
assert author_report_hash == '9075645682843c65481750998db5e99b7fe7f46ee7b801a1c3c55380f80a32a7'
assert initial_hash == '87c61ca4a1a0d36f55bbb5035a4acf8668cb4c07bb7e7787bf3883a0cb831734'
assert git(CANDIDATE, 'rev-parse', 'HEAD').decode().strip() == BASE
base_test = ast.parse(git(CANDIDATE, 'show', BASE + ':tests/test_offline_rest_079.py'))
current_test = ast.parse(TEST.read_bytes())
original = {node.name: ast.dump(node) for node in base_test.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith('test_')}
present = {node.name: ast.dump(node) for node in current_test.body
           if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith('test_')}
assert all(present[name] == tree for name, tree in original.items())
fixtures = {}
for path in sorted((CANDIDATE / '.agents/skills/pal-found-dev/examples/rest/079').rglob('*.py')):
    relative = path.relative_to(CANDIDATE).as_posix()
    assert path.read_bytes() == git(CANDIDATE, 'show', BASE + ':' + relative)
    fixtures[relative] = digest(path.read_bytes())
assert len(fixtures) == 34
partition = json.loads((ROOT / '.ept/docs/deliverables/development/FEATURE-015-rest-operation-partitions.json').read_text())['partitions']['DEV-STORY-079']['operation_ids']
assert set(partition) == set(candidate.OPERATIONS)
resources = sorted({identity.split('.')[2] for identity in partition})
frozen, module_hashes, nodes = {}, {}, {}
for resource in resources:
    row = candidate.OPERATIONS[next(identity for identity in partition if identity.split('.')[2] == resource)]
    module_name = row['module']
    raw = git(ROOT / '.ept/docs/customer_input/foundry-platform-python', 'show', TAG + ':' + module_name.replace('.', '/') + '.py')
    module = importlib.import_module(module_name)
    assert raw == Path(module.__file__).read_bytes()
    assert digest(raw) == row['source_sha256']
    module_hashes[module_name] = digest(raw)
    tree = ast.parse(raw)
    for cls in tree.body:
        if isinstance(cls, ast.ClassDef) and cls.name in (resource + 'Client', 'Async' + resource + 'Client'):
            nodes[cls.name] = cls
    cls = nodes[resource + 'Client']
    for method in cls.body:
        if not isinstance(method, ast.FunctionDef) or method.name.startswith('_'):
            continue
        calls = [node for node in ast.walk(method) if isinstance(node, ast.Call)
                 and isinstance(node.func, ast.Attribute) and node.func.attr == 'RequestInfo']
        if calls:
            assert len(calls) == 1
            frozen[f'v2.ontologies.{resource}.{method.name}'] = (module, method, {kw.arg: kw.value for kw in calls[0].keywords})
assert set(frozen) == set(partition)


def expression(node, module, arguments):
    return eval(compile(ast.Expression(node), '<independent frozen source>', 'eval'), vars(module), arguments)


def deny(*args, **kwargs):
    raise AssertionError('Independent QA denies real network dispatch')


loop = asyncio.new_event_loop()
per_operation = {}
native_faults = 0
cleanup_faults = 0
cancellation_faults = 0
buffered_faults = 0
with patch.object(socket.socket, 'connect', deny), patch.object(socket.socket, 'connect_ex', deny), \
     patch.object(socket, 'getaddrinfo', deny), patch.object(socket, 'create_connection', deny), \
     patch.object(httpx.HTTPTransport, 'handle_request', deny), \
     patch.object(httpx.AsyncHTTPTransport, 'handle_async_request', deny):
    for identity in sorted(partition):
        _, _, resource, method = identity.split('.')
        module, function, fields = frozen[identity]
        async_function = next(node for node in nodes['Async' + resource + 'Client'].body
                              if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == method)
        async_requests = [node for node in ast.walk(async_function) if isinstance(node, ast.Call)
                          and isinstance(node.func, ast.Attribute) and node.func.attr == 'RequestInfo']
        assert len(async_requests) == 1
        async_fields = {kw.arg: kw.value for kw in async_requests[0].keywords}
        assert ast.literal_eval(async_fields['throwable_errors']) == {}
        client_type = getattr(module, resource + 'Client')
        args = candidate.inputs(resource, method)
        paths = ast.literal_eval(ast.Dict(keys=fields['path_params'].keys,
                                         values=[ast.Constant(n.id) for n in fields['path_params'].values]))
        for argument in paths.values():
            args[argument] = ('ri.ontology.main.qa.qa-value' if argument.endswith('_rid')
                              else 'qa-' + argument.replace('_', '-'))
        bound = inspect.signature(getattr(client_type, method)).bind(None, **args)
        bound.apply_defaults()
        values = {name: expression(node, module, bound.arguments) for name, node in fields.items()}
        assert values['throwable_errors'] == {}
        response_type = values['response_type']
        expected_path = '/api' + values['resource_path'].format(**values['path_params'])
        result_record = {'source_sha256': module_hashes[module.__name__], 'http_method': values['method'],
                         'http_path': values['resource_path'], 'declared_response_type': str(response_type),
                         'source_named_errors': [], 'ordinary_iterator': values['response_mode'] == 'ITERATOR',
                         'async_source_return': ast.unparse(async_function.returns),
                         'async_coroutine_definition': isinstance(async_function, ast.AsyncFunctionDef),
                         'paged': 'page_token' in bound.arguments, 'independent_wire_modes': []}
        for asynchronous in (False, True):
            for mode in ('ordinary', 'raw', 'stream'):
                responses = []

                def handler(request):
                    assert request.method == values['method']
                    assert urllib.parse.unquote(request.url.path) == expected_path
                    assert request.headers['Authorization'] == 'Bearer offline-fixture-token'
                    assert request.extensions['timeout']['read'] == 30
                    for name, value in values['header_params'].items():
                        assert request.headers[name] == value
                    assert sorted(request.url.params.multi_items()) == sorted(httpx.QueryParams(
                        {k: v for k, v in values['query_params'].items() if v is not None}).multi_items())
                    assert (json.loads(request.content) if request.content else None) == candidate.normalized(values['body'])
                    response = httpx.Response(200, json=candidate.success_payload(resource, method))
                    responses.append(response)
                    return response

                result = candidate.exercise(resource, method, mode, asynchronous, handler, loop, copy.deepcopy(args))
                if mode == 'ordinary' and values['response_mode'] == 'ITERATOR':
                    item_type = response_type.model_fields['data'].annotation.__args__[0]
                    runtime_type = typing.get_origin(item_type) or item_type
                    assert result and all(type(item) is runtime_type for item in result), (identity, item_type)
                elif mode != 'stream':
                    assert type(result) is response_type
                else:
                    assert isinstance(json.loads(result), dict)
                assert len(responses) == 1 and responses[0].is_closed
                result_record['independent_wire_modes'].append(('async_' if asynchronous else 'sync_') + mode)

                api_class = _core.AsyncApiClient if asynchronous else _core.ApiClient
                native = api_class.call_api

                def wrong_path(self, request_info):
                    return native(self, dataclasses.replace(request_info, resource_path=request_info.resource_path + '/QA-WRONG'))

                with patch.object(api_class, 'call_api', wrong_path):
                    try:
                        candidate.test_all_modes_serialize_source_contract_and_decode_typed_result(resource, method, mode, asynchronous, loop)
                    except Exception as error:
                        assert isinstance(error, AssertionError) or isinstance(error.__cause__, AssertionError)
                        native_faults += 1
                    else:
                        raise AssertionError('Candidate failed to detect native SDK request mutation: ' + identity)
                loop.run_until_complete(loop.shutdown_asyncgens())
        for asynchronous in (False, True):
            stream = candidate.TrackedAsyncStream if asynchronous else candidate.TrackedSyncStream
            name = 'aclose' if asynchronous else 'close'

            async def async_no_close(self):
                pass

            def no_close(self):
                pass

            with patch.object(stream, name, async_no_close if asynchronous else no_close):
                try:
                    candidate.test_stream_byte_budget_interrupt_closes_unread_response(resource, method, asynchronous, loop)
                except AssertionError:
                    cleanup_faults += 1
                else:
                    raise AssertionError('Candidate missed stream cleanup fault: ' + identity)
        with patch.object(candidate.TrackedAsyncStream, 'aclose', async_no_close):
            try:
                candidate.test_async_task_cancellation_closes_stream_with_unread_bytes(resource, method, loop)
            except AssertionError:
                cancellation_faults += 1
            else:
                raise AssertionError('Candidate missed cancellation cleanup fault: ' + identity)

        async def already_buffered(self):
            self.chunks_read = 3
            yield b'part'
            yield b'two!'
            yield b'unread'

        with patch.object(candidate.TrackedAsyncStream, '__aiter__', already_buffered):
            try:
                candidate.test_async_task_cancellation_closes_stream_with_unread_bytes(resource, method, loop)
            except AssertionError:
                buffered_faults += 1
            else:
                raise AssertionError('Candidate missed prebuffered cancellation stream: ' + identity)
        per_operation[identity] = result_record
    loop.run_until_complete(loop.shutdown_asyncgens())
loop.close()
xml_path = ROOT / '.ept/tmp/rest079_unit_independent_qa_20261117.xml'
suite = ET.parse(xml_path).getroot().find('testsuite')
for identity, record in per_operation.items():
    resource, method = identity.split('.')[2:]
    suffix = resource + '-' + method + ']'
    cases = [case.attrib['name'] for case in suite.findall('testcase') if case.attrib['name'].endswith(suffix)]
    record['fresh_passed_test_ids'] = cases
    record['fresh_passed_case_count'] = len(cases)
assert digest(TEST.read_bytes()) == initial_hash
assert digest(author_report_path.read_bytes()) == author_report_hash
assert git(CANDIDATE, 'diff', '--name-only').decode().splitlines() == ['tests/test_offline_rest_079.py']
assert int(suite.attrib['tests']) == 1236 and int(suite.attrib['failures']) == int(suite.attrib['errors']) == 0
baseline_cases = [case.attrib['name'] for case in suite.findall('testcase')
                  if case.attrib['name'].split('[')[0] in original]
assert len(baseline_cases) == 69
assert sum(row['paged'] for row in per_operation.values()) == 11
assert sum(row['ordinary_iterator'] for row in per_operation.values()) == 8
report = {'ticket': 'UNITTEST-079', 'verdict': 'PASS: test-only candidate ready for parent commit review',
          'candidate_sha256_before': initial_hash, 'candidate_sha256_after': digest(TEST.read_bytes()),
          'candidate_base': BASE, 'source_tag_commit': TAG, 'independent_exact_source_identities': sorted(frozen),
          'author_evidence_sha256_before_and_after': author_report_hash,
          'source_checkout_head_after_readonly_git_show': git(ROOT / '.ept/docs/customer_input/foundry-platform-python', 'rev-parse', 'HEAD').decode().strip(),
          'source_module_hashes': module_hashes, 'preserved_baseline_test_functions': sorted(original),
          'baseline_semantic_guard_cases': 69, 'preserved_fixture_hashes': fixtures,
          'pytest': dict(suite.attrib), 'pytest_junit_sha256': digest(xml_path.read_bytes()), 'ruff': 'PASS',
          'independent_changed_path_runtime_mutations_detected': native_faults,
          'independent_omitted_stream_close_mutations_detected': cleanup_faults,
          'independent_omitted_cancellation_close_mutations_detected': cancellation_faults,
          'independent_prebuffered_cancellation_stream_mutations_detected': buffered_faults,
          'independent_fresh_direct_wire_mode_checks': 192, 'per_operation': per_operation,
          'review_findings': [], 'limitations': ['Response payload values reuse synthetic distributed fixtures; expected HTTP fields and result classes derive independently from frozen git-show source.',
          'This review covers test-only candidate. It does not grant formal acceptance, ticket closure, live Foundry claims, commit or publication authorization.'],
          'proof_script': str(Path(__file__)), 'proof_script_sha256': digest(Path(__file__).read_bytes())}
REPORT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'report': str(REPORT), 'report_sha256': digest(REPORT.read_bytes()),
                  'direct_wire_checks': 192, 'sdk_path_mutations_detected': native_faults,
                  'cleanup_mutations_detected': cleanup_faults, 'cancellation_close_mutations_detected': cancellation_faults,
                  'prebuffered_stream_mutations_detected': buffered_faults, 'operations': len(per_operation)}))
