"""Recover independent REST 083 review without changing original evidence."""
import ast
import hashlib
import http.client
import json
import re
import socket
import urllib.request
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch

BASE = Path(__file__).resolve().parent
ROOT = BASE / 'feature015_rest083_review_20261029'
SKILL = ROOT / '.agents/skills/pal-found-dev'
REVIEWER = '/root/rest083_finalize_independent_review_20261029'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

original_paths = [BASE / ('rest083_' + name + '_20261029.' + ext)
                  for name in ('semantic_probe', 'independent_execution')
                  for ext in ('py', 'json')]
originals = [{'path': str(p), 'sha256': sha(p)} for p in original_paths]
source = (BASE / 'rest083_independent_execution_20261029.py').read_text()
source = source.replace("REVIEWER='/root/rest083_semantic_review_20261029'", 'REVIEWER=' + repr(REVIEWER))
source = source.replace("rest083_independent_execution_20261029.json", "rest083_finalize_execution_20261029.json")
source = source.replace("{'temperature':21.5,'time':STAMP}", "{'temperature':21.5,'time':STAMP,'position':{'type':'Point','coordinates':[23.3,42.7]}}")
exec(compile(source, str(BASE / 'rest083_independent_execution_20261029.py'), 'exec'),
     {'__file__': str(BASE / 'rest083_independent_execution_20261029.py'), '__name__': '__main__'})
execution = json.loads((BASE / 'rest083_finalize_execution_20261029.json').read_text())
probes = json.loads((BASE / 'rest083_semantic_probe_20261029.json').read_text())
register = json.loads((ROOT / 'maintainer/rest-domain-authoring-register.json').read_text())
registered = {r['id']: r for r in register['operations']}
network = []

def deny(*args, **kwargs):
    raise AssertionError('QA network boundary: connection/DNS/native HTTP denied')

guards = [(socket.socket, 'connect'), (socket.socket, 'connect_ex'),
          (socket, 'create_connection'), (socket, 'getaddrinfo'),
          (socket, 'gethostbyname'), (http.client.HTTPConnection, 'connect'),
          (http.client.HTTPSConnection, 'connect'), (urllib.request, 'urlopen')]
with ExitStack() as stack:
    for obj, name in guards:
        stack.enter_context(patch.object(obj, name, deny))
    for obj, name in guards:
        try:
            getattr(obj, name)('https://example.invalid')
        except AssertionError as error:
            network.append({'entrypoint': obj.__name__ + '.' + name,
                            'verdict': 'PASS', 'exception': str(error)})
        else:
            raise AssertionError('Network guard escaped: ' + name)

issues = {}
for op in ('apply', 'apply_batch', 'apply_batch_with_overrides', 'apply_with_overrides'):
    issues['v2.ontologies.Action.' + op] = [
        'SUCCESS={} is accepted by the response model, but demonstrates neither validation nor edits. Add representative validation for single apply and edit results for batch, with assertions that separate HTTP receipt from action success.'
    ]
issues['v2.ontologies.Action.apply_batch_with_overrides'].append(
    'Request contains no per-item overrides. Add synthetic UniqueIdentifier mappings and CurrentTime overrides and assert their serialized fields.')
issues['v2.ontologies.Action.apply_with_overrides'].append(
    'Empty uniqueIdentifierLinkIdValues and empty parameters do not demonstrate overrides; actionExecutionTime is absent. Add nonempty synthetic mapping, timestamp and meaningful parameters.')
issues['v2.ontologies.Attachment.upload'] = [
    'Request uploads 19 bytes; SUCCESS.sizeBytes is 1 and filename/mediaType do not match the upload. Assert metadata matches submitted content and filename.'
]
issues['v2.ontologies.Attachment.upload_with_rid'] = [
    'Request body has 18 bytes but content_length=1 and SUCCESS.sizeBytes=1. Set content_length from len(body), use meaningful media type, and assert returned RID and size.'
]
issues['v2.ontologies.GeotemporalSeriesProperty.load_geotemporal_series_entries'] = [
    'Absolute range omits both optional bounds: valid SDK shape, but no finite interval. SUCCESS.data=[{}] omits time and position despite method documentation saying both are always included. Add bounded range, representative entries, nextPageToken and bounded continuation assertions.',
    'Guide calls result ordered without a source ordering guarantee. Explain map entries and pagination; remove ordering claim or supply authoritative support.'
]
issues['v2.ontologies.TimeSeriesPropertyV2.stream_points'] = [
    'SUCCESS is arbitrary non-JSON bytes although frozen method documents JSON as default. No point parsing assertion. Add explicitly JSON synthetic points, bounded interval and decode/assert complete payload after assembling chunks.'
]
issues['v2.ontologies.TimeSeriesValueBankProperty.stream_values'] = [
    'SUCCESS is opaque arbitrary bytes and guide only counts bytes. No meaningful values or adaptation path for interpreting history. SDK source specifies bytes and no wire format, so do not assert a universal JSON default here. Use an explicitly labeled synthetic encoding, parse/assert values, explain that enrollment stream schema must be verified, and bound range/consumption.'
]

models = execution['models']
model_by_id = {m['id']: m for m in models}
for model in models:
    source_text = Path(model['source']).read_text(encoding='utf-8')
    symbol = model['id'].rsplit('.', 1)[-1]
    source_tree = ast.parse(source_text)
    def matches(node):
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            return node.name == symbol
        if isinstance(node, ast.AnnAssign):
            return isinstance(node.target, ast.Name) and node.target.id == symbol
        return isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == symbol for t in node.targets)
    definitions = [n for n in source_tree.body if matches(n)]
    local_text = '\n'.join((SKILL / p['path']).read_text(encoding='utf-8') for p in model['pages'])
    blocks = re.findall(r'```python\s*\n(.*?)```', local_text, re.S)
    parsed = []
    for block in blocks:
        try:
            parsed.extend(ast.parse(block).body)
        except SyntaxError:
            pass
    source_definitions = [ast.dump(n, include_attributes=False) for n in definitions]
    local_definitions = [ast.dump(n, include_attributes=False) for n in parsed]
    model['independent_definition_ast_equal'] = bool(definitions) and all(d in local_definitions for d in source_definitions)
    model['independent_source_definition'] = '\n\n'.join(ast.get_source_segment(source_text, n) for n in definitions)
    model['missing_dependency_ids'] = [d for d in model['dependencies'] if d not in model_by_id]
    model['review_boundary'] = 'Full definition AST, page hashes and dependency closure independently checked; existing semantic annotations retained, not represented as a fresh manual interpretation of every shared core model.'

operation_reports = []
executed = {r['id']: r for r in execution['operations']}
for probe in probes:
    oid = probe['id']
    row = registered[oid]
    behavior = SKILL / row['behavior']
    example = SKILL / row['example']
    contract = Path(probe['contract_path'])
    source_path = Path(probe['source_path'])
    fixture_namespace = {'__file__': str(example), '__name__': 'independent_final_fixture'}
    with ExitStack() as stack:
        for obj, name in guards:
            stack.enter_context(patch.object(obj, name, deny))
        exec(compile(example.read_text(), str(example), 'exec'), fixture_namespace)
        fixture_namespace['verify']()
    model_ids = sorted(m['id'] for m in models if oid in m['consumers'])
    operation_reports.append({
        'id': oid, 'verdict': 'FAIL' if oid in issues else 'PASS',
        'findings': issues.get(oid, []),
        'source': {'path': str(source_path), 'sha256': sha(source_path),
                   'matches_frozen_register': sha(source_path) == row['source_sha256'],
                   'method_definition': probe['source_function'], 'method_documentation': probe['source_doc']},
        'assets': [{'kind': kind, 'path': str(path), 'sha256': sha(path)}
                   for kind, path in [('behavior', behavior), ('example', example), ('contract', contract)]],
        'full_transitive_model_ids': model_ids,
        'transitive_dependency_gaps': sorted({d for m in models if m['id'] in model_ids for d in m['dependencies'] if d not in model_ids}),
        'reader_guidance': {
            'reviewed': ['purpose/lifecycle', 'prerequisites and beta restrictions', 'SDK/HTTP contract and model navigation', 'effects and result checks', 'failure recovery', 'sync/async/raw/streaming availability and lifetime guidance'],
            'boundary': 'Generic permission/timeout probes verify client handling. No named error mapping invented when method source lists none. Tenant permissions, values, side effects and platform ordering remain enrollment checks.',
            'result': 'Correction required: ' + ' '.join(issues[oid]) if oid in issues else 'Local behavior, complete source contract and synthetic response are sufficient for operation adaptation within the stated fixture/enrollment boundary.'
        },
        'author_fixture_rerun': 'PASS',
        'independent_actual_sdk_checks': executed[oid]['checks'],
        'bounded_author_fix_files': [str(example)] + ([str(behavior)] if 'Geotemporal' in oid or '.stream_' in oid else []) if oid in issues else []
    })

assert len(operation_reports) == 25
assert all(c['verdict'] == 'PASS' for r in execution['operations'] for c in r['checks'])
assert all(sha(Path(r['path'])) == r['sha256'] for r in originals)
report = {
    'story': 'DEV-STORY-083', 'reviewer': REVIEWER,
    'prior_independent_reviewer': '/root/rest083_semantic_review_20261029',
    'candidate': execution['candidate'], 'sdk_version': '1.101.0',
    'status': 'CORRECTIONS_REQUIRED', 'summary': {'operations': 25, 'PASS': 16, 'FAIL': 9,
        'independent_sdk_checks_passed': 75, 'author_fixtures_passed': 25,
        'transitive_models': len(models),
        'model_definition_ast_mismatches': [m['id'] for m in models if not m['independent_definition_ast_equal']],
        'model_dependency_gaps': [m['id'] for m in models if m['missing_dependency_ids']]},
    'network_denial_proof': network,
    'network_scope': 'Python process guards deny socket connections, DNS and native HTTP during SDK fake transport execution; explicit calls exercised every patched entrypoint. This is process-level denial evidence, not an OS firewall claim.',
    'original_evidence_preserved': originals,
    'rerun_evidence': {'path': str(BASE / 'rest083_finalize_execution_20261029.json'), 'sha256': sha(BASE / 'rest083_finalize_execution_20261029.json')},
    'reproduction': '.ept/tmp/feature015_shared_cli_qa_env/Scripts/python.exe .ept/tmp/rest083_finalize_review_20261029.py',
    'operations': operation_reports, 'full_transitive_models': models,
    'review_limits': 'No live Foundry calls, tracker writes, author/register edits, formal workflow promotion or release acceptance. Independent 093/integrated acceptance remain required. Arbitrary byte responses are SDK-valid; failures concern required meaningful reader examples. Absolute range bounds and Action result fields are optional in SDK models; empty fixtures are not schema failures.',
    'recoverable_read_errors': ['Initial guessed behavior path references/rest/behavior/... absent; corrected by register behavior path.', 'Initial guessed ActionExecutionOverrides model filename absent; closure resolved from exact registered symbols. Neither read error is a candidate defect.']
}
destination = BASE / 'feature015_rest083_semantic_review_20261029.json'
destination.write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report['summary'], indent=2))
print('REPORT', destination, sha(destination))
