"""Independently reconcile REST091 test literals with frozen SDK source."""
import ast
import hashlib
import importlib
import inspect
import json
import runpy
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / '.ept/tmp/rest091_native_unit_author_20261118'
SDK_REPO = ROOT / '.ept/docs/customer_input/foundry-platform-python'
COMMIT = '168d51910570b6966afa2320333ab36f6a3f7ccf'
TEST = WORK / 'tests/test_offline_rest_091.py'
ns = runpy.run_path(str(TEST))
partitions = json.loads((ROOT / '.ept/docs/deliverables/development/FEATURE-015-rest-operation-partitions.json').read_text())
expected_ids = set(partitions['partitions']['DEV-STORY-091']['operation_ids'])
assert expected_ids == {'v2.' + key for key in ns['NATIVE_CONTRACTS']}
results = []
source_files = {}

def evaluate(node, globals_, locals_):
    return eval(compile(ast.Expression(node), '<frozen-sdk-expression>', 'eval'), globals_, locals_)

for key, (want_method, want_path, want_type) in ns['NATIVE_CONTRACTS'].items():
    service, resource, method = key.split('.')
    relative = f'foundry_sdk/v2/{service}/{ns["NATIVE_MODULES"][resource]}.py'
    raw = subprocess.check_output(['git', '-C', str(SDK_REPO), 'show', f'{COMMIT}:{relative}'])
    source_files[relative] = hashlib.sha256(raw).hexdigest()
    tree = ast.parse(raw)
    cls = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == resource + 'Client')
    fn = next(node for node in cls.body if isinstance(node, ast.FunctionDef) and node.name == method)
    requests = [node for node in ast.walk(fn) if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'RequestInfo']
    assert len(requests) == 1, key
    fields = {kw.arg: kw.value for kw in requests[0].keywords}
    assert ast.literal_eval(fields['method']) == want_method, key
    assert ast.literal_eval(fields['resource_path']) == '/v2' + want_path, key
    example, arguments, sync_type, async_type, _ = ns['native_operation'](key)
    module = importlib.import_module(sync_type.__module__)
    assert Path(inspect.getfile(sync_type)).read_bytes() == raw, (key, 'installed source differs')
    locals_ = {arg.arg: None for arg in (*fn.args.args, *fn.args.kwonlyargs)}
    locals_.update(arguments)
    locals_['preview'] = True
    response_type = evaluate(fields['response_type'], vars(module), locals_)
    assert response_type == want_type, (key, 'response type')
    errors = evaluate(fields['throwable_errors'], vars(module), locals_)
    named = {name: (status, parameters) for op, name, status, parameters in ns['NATIVE_NAMED_ERRORS'] if op == key}
    assert set(errors) == set(named), (key, 'typed errors')
    query = {name: value for name, value in evaluate(fields['query_params'], vars(module), locals_).items() if value is not None}
    want_query = dict(ns['NATIVE_QUERY'].get(key, {}))
    if 'preview' in locals_:
        want_query['preview'] = True
    assert query == want_query, (key, query, want_query)
    body_ast = ast.unparse(fields['body'])
    headers = {name: value for name, value in evaluate(fields['header_params'], vars(module), locals_).items() if value is not None}
    expected_headers = {'Accept': '*/*' if want_type is bytes else 'application/json'} if want_type is not None else {}
    if key in ns['NATIVE_JSON_BODIES']:
        expected_headers['Content-Type'] = 'application/json'
    elif key.endswith(('.upload', '.upload_media')):
        expected_headers['Content-Type'] = '*/*'
    elif key == 'widgets.Repository.publish':
        expected_headers['Content-Type'] = 'application/octet-stream'
    assert headers == expected_headers, (key, headers, expected_headers)
    expected_named_rows = []
    for name, error_type in errors.items():
        status, parameters = named[name]
        parsed = error_type(name=name, parameters=parameters, error_instance_id='00000000-0000-0000-0000-000000000004')
        assert parsed.name == name
        expected_named_rows.append({'name': name, 'status': status, 'parameters': parameters})
    results.append({'operation': 'v2.' + key, 'source': relative, 'line': fn.lineno,
                    'method': want_method, 'path': '/v2' + want_path,
                    'response_type': ast.unparse(fields['response_type']),
                    'headers': headers, 'query': query, 'body_expression': body_ast,
                    'declared_errors': expected_named_rows, 'verdict': 'PASS'})

out = {'reviewer': 'feature015_unit091_peer_recovery', 'candidate_commit': 'e0e02764d1cae275c515734ee4855a51bf99659f',
       'test_sha256': hashlib.sha256(TEST.read_bytes()).hexdigest(),
       'sdk_commit': COMMIT, 'operation_count': len(results), 'native_mode_count': len(ns['NATIVE_MODES']),
       'error_mode_count': len(ns['NATIVE_ERROR_MODES']), 'source_files': source_files, 'results': results,
       'probe_corrections': ['Initial probe compared source headers including None instead of omitted wire headers; corrected probe filtering',
                             'Error constructors require name; corrected probe constructor argument'],
       'limits': ['Independent test/source review only; no formal TESTEXEC or guide semantic approval',
                  'Prepared SDK1.101.0 fake HTTP transports; no live tenant or other SDK versions']}
target = ROOT / '.ept/tmp/unit091_peer_source_probe_20261121.json'
target.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'operations': len(results), 'native_modes': len(ns['NATIVE_MODES']), 'error_modes': len(ns['NATIVE_ERROR_MODES']), 'source_files': len(source_files), 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()}))
