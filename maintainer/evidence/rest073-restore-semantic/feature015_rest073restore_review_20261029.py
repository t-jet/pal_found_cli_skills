"""Independent restore review. Evidence only; synthetic transport, network denied."""
import ast
import hashlib
import importlib.metadata
import importlib
import inspect
import json
import re
import runpy
import socket
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import httpx
from foundry_sdk import Config, UserTokenAuth
from foundry_sdk.v2.filesystem.resource import ResourceClient
from foundry_sdk.v2.filesystem import errors

TMP = Path(__file__).resolve().parent
ROOT = TMP / 'feature015_integration'
SKILL = ROOT / '.agents/skills/pal-found-dev'
OUT = TMP / 'feature015_rest073_restore_semantic_review_20261029.json'
RID = 'ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

contract = SKILL / 'references/rest/contracts/v2/filesystem/Resource/restore.md'
behavior = SKILL / 'references/rest/v2/filesystem/Resource.md'
example = SKILL / 'examples/rest/073/v2/filesystem/Resource/restore.py'
source = Path(inspect.getfile(ResourceClient))
source_text = source.read_text(encoding='utf8')
tree = ast.parse(source_text)
client = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == 'ResourceClient')
method = next(n for n in client.body if isinstance(n, ast.FunctionDef) and n.name == 'restore')
method_text = ast.get_source_segment(source_text, method)
docstring = ast.get_docstring(method)
seeds = [contract, behavior, example, source,
    SKILL / 'references/rest/authentication.md',
    SKILL / 'references/rest/client-behavior.md',
    SKILL / 'references/rest/models/v2/filesystem/models/Resource.md',
    SKILL / 'references/rest/contracts/v2/filesystem/Resource/get.md',
    SKILL / 'examples/rest/common/mock_transport.py',
    TMP / 'feature015_rest073_current_semantic_review.json',
    TMP / 'feature015_rest073_semantic_retest.json']
model_docs = set()
pending = [contract, seeds[6]]
unresolved = []
while pending:
    page = pending.pop()
    for target in re.findall(r'\]\(([^)]+)\)', page.read_text(encoding='utf8')):
        if '://' in target or target.startswith('#'):
            continue
        target_path = (page.parent / target.split('#')[0]).resolve()
        if 'references/rest/models/' not in target_path.as_posix():
            continue
        if not target_path.is_file():
            unresolved.append(str(target_path))
        elif target_path not in model_docs:
            model_docs.add(target_path)
            pending.append(target_path)
seeds += sorted(model_docs)
sdk_root = source.parents[3]
for page in sorted(model_docs):
    heading = page.read_text(encoding='utf8').splitlines()[0].removeprefix('# ')
    if heading.startswith('foundry_sdk.'):
        module, symbol = heading.rsplit('.', 1)
        snake = re.sub(r'(?<!^)(?=[A-Z])', '_', symbol).lower()
        loaded = importlib.import_module(module)
        candidate = Path(inspect.getfile(loaded))
        if candidate.is_file():
            seeds.append(candidate)
seeds = sorted(set(seeds))
before = {str(p): sha(p) for p in seeds}
proof = []
network_calls = []

def denied(*args, **kwargs):
    network_calls.append('denied')
    raise AssertionError('Network/DNS denied by independent QA')

def execute_case(name, status, payload=None, exception=None, raw=False):
    requests = []
    def handler(request):
        observed = {'method': request.method, 'path': request.url.path,
                    'query': str(request.url.query), 'body': request.content.decode(),
                    'timeout': request.extensions.get('timeout')}
        requests.append(observed)
        assert observed['method'] == 'POST'
        assert observed['path'] == '/api/v2/filesystem/resources/' + RID + '/restore'
        assert request.url.query == b''
        assert request.content == b''
        assert request.headers['authorization'] == 'Bearer independent-offline-token'
        assert observed['timeout']['read'] == 30
        return httpx.Response(status, json=payload) if payload is not None else httpx.Response(status)
    with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
        with patch('foundry_sdk._core.api_client.HttpClient', return_value=transport):
            resource = ResourceClient(auth=UserTokenAuth(token='independent-offline-token'),
                hostname='offline.example.invalid', config=Config(timeout=30, max_retries=1))
        try:
            if raw:
                result = resource.with_raw_response.restore(RID, request_timeout=30)
                try:
                    assert result.status_code == status
                    assert result.decode() is None
                finally:
                    result.close()
                outcome = {'status': status, 'decoded': None, 'closed': result._response.is_closed}
            else:
                result = resource.restore(RID, request_timeout=30)
                assert result is None
                outcome = {'decoded': None}
            assert exception is None
        except Exception as exc:
            if exception is None or type(exc) is not exception:
                raise
            assert exc.parameters == {'resourceRid': RID}
            outcome = {'error_type': type(exc).__name__, 'name': exc.name,
                       'parameters': exc.parameters}
        assert len(requests) == 1
        proof.append({'case': name, 'verdict': 'PASS', 'request': requests[0], 'result': outcome})

with patch.object(socket, 'getaddrinfo', denied), patch.object(socket.socket, 'connect', denied), patch.object(socket.socket, 'connect_ex', denied):
    execute_case('ordinary 204 returns None; fixture does not establish server state', 204)
    execute_case('raw 204 decode and close', 204, raw=True)
    for error_name, status, code in [
        ('ResourceNotDirectlyTrashed', 400, 'INVALID_ARGUMENT'),
        ('ResourceNotFound', 404, 'NOT_FOUND'),
        ('RestoreResourcePermissionDenied', 403, 'PERMISSION_DENIED')]:
        execute_case(error_name, status, {'errorName': error_name, 'errorCode': code,
            'parameters': {'resourceRid': RID},
            'errorInstanceId': '00000000-0000-0000-0000-000000000004'}, getattr(errors, error_name))
    runpy.run_path(str(example), run_name='__main__')
    proof.append({'case': 'current reader example under independent DNS/connect denial', 'verdict': 'PASS'})

after = {str(p): sha(p) for p in seeds}
assert before == after
prior = json.loads((TMP / 'feature015_rest073_current_semantic_review.json').read_text())
retest = json.loads((TMP / 'feature015_rest073_semantic_retest.json').read_text())
historical = {r['id']: r for r in prior['operations']}
historical.update({r['id']: r for r in retest['operations']})
accepted = sorted(k for k,v in historical.items() if v['verdict'] == 'PASS')
assert len(accepted) == 47
report = {
    'story': 'DEV-STORY-073', 'development': 'DEV-068',
    'reviewer': 'independent qa-engineer /root/rest073_restore_uncertainty_review_20261029',
    'candidate_sha': subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD'], text=True).strip(),
    'sdk_version': importlib.metadata.version('foundry-platform-sdk'),
    'scope': 'Only v2.filesystem.Resource.restore semantic acceptance; formal QA pending',
    'operations': [{
        'id': 'v2.filesystem.Resource.restore', 'verdict': 'FAIL',
        'runtime_contract_verdict': 'PASS',
        'server_policy_verdict': 'UNCERTAIN',
        'independent_expectations': [
            'POST exact RID /restore, empty query/body, Bearer auth and request_timeout=30',
            '204 decodes to None; raw result is closed; result does not contain restored state',
            'Each source-declared error decodes to its exact SDK exception and RID parameters',
            'Do not infer server no-op policy, idempotency, or ancestor-state behavior from fake responses',
            'Reader must distinguish DIRECTLY_TRASHED, ANCESTOR_TRASHED, NOT_TRASHED from local TrashStatus guidance',
            'Source disagreement must be explicit; denial or uncertain state stops mutation until authorized reconciliation'],
        'acceptance_assessment': {
            'decision_and_prerequisites': 'PARTIAL: identity, RID, enrollment, scopes silence and trash model available; restore-specific state decision absent',
            'expected_result_and_safe_validation': 'PARTIAL: None and exact-RID read available, but active-state no-op asserted unconditionally',
            'reconciliation_stop_and_recovery': 'FAIL: generic read-before-replay guidance exists; source conflict and ResourceNotDirectlyTrashed response decision absent',
            'model_and_error_navigation': 'PASS: restore and reconciliation Resource model links resolve transitively',
            'BD-015-08': 'FAIL: unexplained task-critical source difference remains',
            'DEV-068': 'FAIL: required constraints, lifecycle decision and bounded recovery incomplete'},
        'source_conflict': {
            'exact_error': 'ResourceNotDirectlyTrashed',
            'source_docstring': docstring,
            'source_method_sha256': hashlib.sha256(method_text.encode()).hexdigest(),
            'disposition': 'Open. Source prose says non-trashed restore is ignored, while same method declares ResourceNotDirectlyTrashed. Neither fixture proves which server policy applies. Current behavior repeats unconditional active-state no-op and does not explain disagreement.',
            'task_critical': True,
            'gate': 'Cannot accept while approved BD-015-08 source-difference and seven-element recovery requirements remain unmet. Explicit bounded uncertainty could support a later review; unknown server behavior alone is not a waiver.'},
        'exact_author_fix_requirements': [
            'Qualify active-resource no-op statement in behavior and linked contract: attribute to SDK prose and explicitly pair with ResourceNotDirectlyTrashed declaration; state server behavior is unverified and do not promise idempotency.',
            'Add restore decision using exact RID and local TrashStatus values. Explain DIRECTLY_TRASHED direct restore; ANCESTOR_TRASHED requires original folder restoration per model, without inventing a universal server outcome or mutating arbitrary ancestors.',
            'For ResourceNotDirectlyTrashed, stop replay and read exact RID/state plus authorized ancestor context; distinguish confirmed NOT_TRASHED desired state, ancestor trash, and unresolved/denied read. Preserve uncertainty and escalate unresolved state/policy to authorized owner.',
            'State success None/204 does not itself prove restored hierarchy; validate exact RID, trash_status, parent_folder_rid and path with authorized reads. Bound reconciliation and stop when unavailable, denied or conflicting; never substitute old-path RID.',
            'Keep fake HTTP success/errors explicitly synthetic and source-backed; add adaptable restore/read/reconcile decision example or equivalent concrete code using declared local models. No live server assertion is required or authorized.',
            'Record task-critical source-conflict disposition through approved workflow before acceptance; QA will re-review author changes without editing them.']
    }],
    'raw_proof': proof, 'network': {'dns_and_connect_denied': True, 'attempt_count': len(network_calls), 'live_calls': 0},
    'model_closure': {'documents': len(model_docs), 'unresolved': unresolved},
    'bindings_before': before, 'bindings_after': after, 'all_bindings_unchanged': before == after,
    'historical_accepted_operations': {'count': 47, 'ids': accepted, 'disposition': 'Preserved unchanged; not re-reviewed or replaced by this narrow assessment'},
    'formal_qa': 'Pending. No tracker, author content or review register changed.'}
OUT.write_text(json.dumps(report, indent=2) + '\n', encoding='utf8')
print(json.dumps({'artifact': str(OUT), 'verdict': 'FAIL', 'runtime_cases': len(proof), 'accepted_history': len(accepted), 'model_docs': len(model_docs)}))
