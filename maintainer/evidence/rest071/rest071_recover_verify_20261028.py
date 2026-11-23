"""Recover independent execution proof without re-running accepted REST071 tests."""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

TMP = Path(__file__).resolve().parent
ROOT = TMP.parents[1]
REPO = TMP / 'feature015_integration'
OWNER = REPO / '.agents/skills/pal-found-dev'
IDENTITY = '/root/rest071_closure_recover_20261028'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read(name):
    return json.loads((TMP / name).read_bytes())

runner = read('rest071_executor_attempt1_runner.json')
execution = read('rest071_executor_attempt1_rest071_formal_execution.json')
cases = read('rest071_executor_attempt1_rest071_formal_cases.json')
approval = read('rest071_executor_attempt1_rest071_case_approval.json')
assert runner['exit_code'] == 0 and runner['bindings_unchanged_after_run'] is True
assert execution['execution'] == 'PASS'
assert runner['executor_identity'] == execution['executor_identity'] == '/root/rest071_execute_20261027'
assert approval['verdict'] == 'APPROVED'
assert len({execution['executor_identity'], cases['author_identity'],
            cases['correction_author_identity'], approval['reviewer_identity']}) == 4
assert sha(TMP / 'rest071_formal_cases.json') == runner['cases_sha256'] == approval['manifest']['sha256'] == 'eaa4126766a52b28eb99d7d26b392d2ec997c20479022f7e3eafeacfa38295e7'
assert sha(TMP / 'rest071_formal_execute.py') == runner['harness_sha256'] == approval['harness']['sha256'] == 'd36df0fb9824d603944971a702cabf7694e0dada1a08c953797798db99fb7876'
assert sha(TMP / 'rest071_case_approval.json') == '8998fb2f9c816841dd7c7c3bcc1374d5349144f14f780848dcae1f1768aa7229'
assert sha(TMP / 'rest071_formal_execution.json') == sha(TMP / 'rest071_executor_attempt1_rest071_formal_execution.json')
for key in ('snapshots', 'outputs', 'sdk_assets_binding'):
    for name, expected in runner[key].items():
        assert sha(Path(name)) == expected, (key, name)
assert len(runner['sdk_assets_binding']) == 72
raw_checks = [json.loads(line) for line in (TMP / 'rest071_executor_attempt1_rest071_formal_execute.log').read_text().splitlines()]
assert raw_checks == execution['results']
assert len(raw_checks) == 486 and all(row['result'] == 'PASS' for row in raw_checks)
assert len({(row['case_id'], row['check'], row.get('status')) for row in raw_checks}) == 486
assert {'case_id': 'REST071', 'check': 'socket_traps_active', 'result': 'PASS'} in raw_checks
assert execution['operations'] == len(cases['operations']) == 27
assert execution['declared_errors'] == sum(len(row['errors']) for row in cases['operations']) == 74
register = read('feature015_integration/maintainer/rest-domain-authoring-register.json')
rows = {row['id']: row for row in register['operations'] if row['story'] == 'DEV-STORY-071'}
assert set(rows) == {row['operation'] for row in cases['operations']}
operation_results = []
for case in cases['operations']:
    checks = [row for row in raw_checks if row['case_id'] == case['case_id']]
    actual_errors = {row['check'][6:] for row in checks if row['check'].startswith('error_')}
    expected_errors = {error['name'] for error in case['errors']}
    assert actual_errors == expected_errors | {'IndependentPermissionDenied'}, case['operation']
    assert {row['status'] for row in checks if row['check'] == 'error_IndependentPermissionDenied'} == {401, 403}
    assert checks and 'success_typed' in {row['check'] for row in checks}
    assert sha(Path(case['source']['path'])) == case['source']['sha256'] == rows[case['operation']]['source_sha256']
    for asset in case['assets'].values():
        assert sha(OWNER / asset['path']) == asset['sha256']
    operation_results.append({'id': case['operation'], 'case_id': case['case_id'],
        'verdict': 'PASS', 'checks': len(checks), 'declared_errors': sorted(expected_errors),
        'check_results': checks, 'source_sha256': case['source']['sha256'], 'assets': case['assets']})

names = ['rest071_executor_attempt1_runner.json', 'rest071_executor_runner_20261027.py',
    'rest071_executor_preflight_20261027.json', 'rest071_executor_preflight_20261027.py',
    'rest071_executor_attempt1_rest071_formal_execute.py', 'rest071_executor_attempt1_rest071_formal_cases.json',
    'rest071_executor_attempt1_rest071_case_approval.json', 'rest071_executor_attempt1_rest071_readiness.json',
    'rest071_executor_attempt1_rest071_formal_execution.json', 'rest071_executor_attempt1_rest071_formal_execute.log',
    'rest071_executor_attempt1_stdout.log', 'rest071_executor_attempt1_stderr.log',
    'rest071_developer_handoff_20261027.json', 'rest071_case_handoff_20261027.json',
    'feature015_rest071_code_review_20261027.json', 'feature015_rest071_architect_source_review_20261027.json',
    'feature015_rest071_architect_closure_20261027.json', 'rest071_case_approval.json',
    'rest071_fresh_static_review.py', 'rest071_fresh_static_review.json']
inventory = {'recorder_identity': IDENTITY, 'files': [
    {'path': str((TMP / name).relative_to(ROOT)).replace('\\', '/'), 'bytes': (TMP / name).stat().st_size,
     'sha256': sha(TMP / name)} for name in names]}
inventory_path = TMP / 'rest071_recovered_inventory_20261028.json'
inventory_path.write_text(json.dumps(inventory, indent=2) + '\n', encoding='utf-8')
report = {'story': 'DEV-STORY-071', 'testcase': 'TESTCASE-074', 'testexec': 'TESTEXEC-074',
    'recorder_identity': IDENTITY, 'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
    'executor': execution['executor_identity'], 'case_author': cases['author_identity'],
    'correction_author': cases['correction_author_identity'], 'case_reviewer': approval['reviewer_identity'],
    'execution': 'PASS', 'formal_workflow_acceptance': 'pending tracker verification and closure',
    'observed_run': {'started_at': runner['started_at'], 'finished_at': runner['finished_at'],
        'elapsed_seconds': runner['elapsed_seconds'], 'attempt': 1, 'exit_code': 0,
        'command': runner['command'], 'coordinator_confirmation': runner['coordinator_confirmation']},
    'checks': 486, 'operations_count': 27, 'declared_error_count': 74,
    'cases_sha256': runner['cases_sha256'], 'harness_sha256': runner['harness_sha256'],
    'case_approval_sha256': sha(TMP / 'rest071_case_approval.json'),
    'source_asset_bindings_checked': 72, 'all_bindings_current_and_unchanged': True,
    'raw_log_equals_every_result_in_order': True, 'unique_case_check_status_triples': 486,
    'unique_case_check_pairs': 459,
    'check_name_reuse': 'Each operation reuses error_IndependentPermissionDenied for distinct HTTP401 and HTTP403 probes; status disambiguates all54 probes.',
    'no_execution_repeated': True, 'operations': operation_results,
    'inventory': {'path': str(inventory_path.relative_to(ROOT)).replace('\\', '/'), 'sha256': sha(inventory_path)},
    'limits': ['Recorder recovered immutable proof after executor usage interruption; executor identity and raw results are preserved.',
        'Real SDK 1.101.0 with synthetic mocked responses and denied public sockets/DNS; no tenant behavior or live authorization claim.',
        'Workflow closure and BUG-SUB-027/028 acceptance still require live ticket DoD checks and serialized writer authorization.']}
output = TMP / 'feature015_rest071_recovered_formal_qa_20261028.json'
output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'report': str(output), 'sha256': sha(output), 'inventory_sha256': sha(inventory_path),
    'operations': 27, 'checks': 486, 'declared_errors': 74, 'bindings': 72, 'workflow': 'pending'}))
