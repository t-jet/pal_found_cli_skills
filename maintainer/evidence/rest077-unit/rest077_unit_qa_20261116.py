"""Independent REST077 unit review evidence; no candidate changes."""
import ast
import hashlib
import importlib.metadata
import inspect
import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANDIDATE = ROOT / '.ept/tmp/feature015_rest077_unit_modes'
SHARED = ROOT / '.ept/tmp/feature015_integration'
TEST = Path('tests/test_offline_rest_077.py')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def tests(path):
    return {node.name: ast.dump(node, include_attributes=False)
            for node in ast.parse(path.read_text()).body
            if isinstance(node, ast.FunctionDef) and node.name.startswith('test_')}

baseline = tests(SHARED / TEST)
candidate = tests(CANDIDATE / TEST)
assert all(candidate[name] == value for name, value in baseline.items())
def globals_ast(path):
    return {ast.unparse(node.targets[0]): ast.dump(node, include_attributes=False)
            for node in ast.parse(path.read_text()).body if isinstance(node, ast.Assign)}
baseline_globals = globals_ast(SHARED / TEST)
candidate_globals = globals_ast(CANDIDATE / TEST)
assert all(candidate_globals[name] == value for name, value in baseline_globals.items())
namespace = runpy.run_path(str(CANDIDATE / TEST))
partition = json.loads((ROOT / '.ept/docs/deliverables/development/FEATURE-015-rest-operation-partitions.json').read_text())
expected = set(partition['partitions']['DEV-STORY-077']['operation_ids'])
actual = {f'v1.ontologies.{r}.{o}' for r, o in namespace['CASES']}
assert actual == expected and len(actual) == 23
assert importlib.metadata.version('foundry-platform-sdk') == '1.101.0'
assets = []
for directory in ('examples/rest/077', 'references/rest/v1/ontologies'):
    base = Path('.agents/skills/pal-found-dev') / directory
    for shared in (SHARED / base).rglob('*'):
        if shared.is_file() and '__pycache__' not in shared.parts:
            relative = shared.relative_to(SHARED)
            assert sha(CANDIDATE / relative) == sha(shared), str(relative)
            assets.append(str(relative))
rows = []
for resource, operation in namespace['CASES']:
    source = namespace['contract'](resource, operation)
    client = source['client']
    module_path = Path(inspect.getfile(client))
    async_client = namespace['async_client'](source)
    for cls in (client, async_client):
        assert hasattr(cls, operation)
        initializer = inspect.getsource(cls.__init__)
        assert 'with_raw_response' in initializer
        assert 'with_streaming_response' in initializer
    rows.append({
        'id': f'v1.ontologies.{resource}.{operation}',
        'source_path': str(module_path), 'source_sha256': sha(module_path),
        'method': source['method'], 'path': source['path'],
        'response': str(source['response']),
        'native_iterator': source['iterator'],
        'async_signature': str(inspect.signature(getattr(async_client, operation))),
        'named_errors': sorted(source['errors']),
        'modes_executed': ['sync/native', 'sync/raw', 'sync/stream',
                           'async/native', 'async/raw', 'async/stream'],
        'generic_denial': '403 PermissionDenied',
        'timeout': 'ReadTimeout; preserved httpx cause; one request',
        'stream_interruption_and_cancellation': (resource, operation) in namespace['STREAM_CASES'],
        'two_page_finite_pagination': (resource, operation) in namespace['PAGED_CASES'],
    })
report = {
    'reviewer': '/root/rest077_unit_review_20261116 (independent QA)',
    'verdict': 'PASS for dedicated UNITTEST-078 candidate only; commit/integration remain pending',
    'candidate_base': '0be7645cb64b6e70a828aa3dafdb0575c389d0ff',
    'shared_source': '3d5536cfe024bed6d8dbfbdc27cc65f700b7e95f',
    'test_sha256': sha(CANDIDATE / TEST),
    'sdk_version': importlib.metadata.version('foundry-platform-sdk'),
    'baseline_test_functions_preserved': sorted(baseline),
    'baseline_cases': 56,
    'baseline_global_assignments_preserved': sorted(baseline_globals),
    'shared_source_asset_count_equal': len(assets),
    'tests': [
        {'command': 'python -m pytest -p no:cacheprovider tests/test_offline_rest_077.py -q', 'exit': 0, 'passed': 553},
        {'command': 'ruff check --no-cache tests/test_offline_rest_077.py', 'exit': 0},
        {'command': "python -m pytest -p no:cacheprovider tests/test_offline_rest_wave1.py -q -k 'v1.ontologies or network or external'", 'exit': 0, 'passed': 73, 'deselected': 445},
    ],
    'scope_limits': [
        'Fixture unit verification only; TESTEXEC-078 and REST093 acceptance remain gated.',
        'Candidate deny_network blocks DNS/socket/real httpx dispatch in process; no OS-wide network claim.',
        'Selected wave1 guards additionally exercise requests/urllib/subprocess denial.',
        'Error effect ledger is synthetic; no live server effects proven.',
        'Response closure after buffered reads is partly ensured by httpx eager consumption; tracked stream interruption/cancellation proves unread body closure.',
        'Expected fixture payloads remain author-provided; source hashes/types/errors and preserved semantic mutation guards provide separate checks.',
        'AsyncApiResponse.decode is synchronous; AsyncApiResponse.aclose is asynchronous, independently inspected.',
    ],
    'operations': rows,
}
destination = ROOT / '.ept/tmp/rest077_unit_qa_20261116.json'
destination.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'report': str(destination), 'test_sha256': report['test_sha256'],
                  'operations': len(rows), 'named_errors': sum(len(row['named_errors']) for row in rows),
                  'stream_cases': len(namespace['STREAM_CASES']), 'paged_cases': len(namespace['PAGED_CASES']),
                  'baseline_functions': len(baseline), 'shared_assets_equal': len(assets)}))
