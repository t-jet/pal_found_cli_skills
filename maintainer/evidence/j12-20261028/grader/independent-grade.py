"""Verify fresh J12 reader evidence and record an independent rubric grade."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[2]
TMP = ROOT / '.ept/tmp'
READER = TMP / 'j12_reader_recover_20261028'
CURRENT = TMP / 'feature015_integration/.agents/skills/pal-found-dev'
REPRO = TMP / 'feature015_j12_grade_repro_20261028'
OUT = TMP / 'feature015_j12_independent_grade_20261028.json'
PYTHON = TMP / 'feature015_shared_cli_qa_env/Scripts/python.exe'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_bytes())


answer = load(READER / 'reader_answer.json')
assert sha(READER / 'reader_answer.json') == '65cc2f91075a54a5902e948801d706c87a119ec404f6044bcb04bee559015fe8'
manifest = load(READER / 'artifact_hash_manifest.json')
verified = []
for item in manifest['files']:
    path = (READER / item['path']).resolve()
    assert path.is_relative_to(READER.resolve()) and path.is_file()
    assert sha(path) == item['sha256'] and path.stat().st_size == item['bytes']
    verified.append(item)
assert len(verified) == 32

snapshot = load(READER / 'snapshot_manifest.json')
assert snapshot['file_count'] == len(snapshot['files']) == 4437
for item in snapshot['files']:
    path = (READER / 'skill_snapshot' / item['path']).resolve()
    assert path.is_relative_to((READER / 'skill_snapshot').resolve())
    assert sha(path) == item['sha256'] and path.stat().st_size == item['bytes']
canonical = ''.join(f"{row['path']}\0{row['sha256']}\n" for row in snapshot['files']).encode()
assert hashlib.sha256(canonical).hexdigest() == snapshot['tree_sha256'] == answer['candidate']['tree_sha256']

consulted = load(READER / 'consulted_sources.json')['standalone_skill']
continuity = []
for item in consulted:
    relative = Path(item['path']).relative_to('skill_snapshot')
    actual = sha(CURRENT / relative)
    assert actual == item['sha256'] == sha(READER / item['path'])
    continuity.append({'path': relative.as_posix(), 'sha256': actual, 'current_match': True,
                       'headings_or_scope': item['headings_or_scope']})

original = load(READER / 'execution_results.json')
assert len(original['cases']) == 12
assert original['runtime']['sdk'] == '1.101.0'
assert all(len(case['denial_probes']) == 2 for case in original['cases'])
assert not REPRO.exists(), 'Preserve previous reproduction; choose a fresh directory.'
REPRO.mkdir()
shutil.copyfile(READER / 'reader_workflow.py', REPRO / 'reader_workflow.py')
assert sha(REPRO / 'reader_workflow.py') == sha(READER / 'reader_workflow.py')
started = datetime.now(timezone.utc).isoformat()
before = time.perf_counter()
command = [str(PYTHON), '-B', str(REPRO / 'reader_workflow.py')]
process = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, encoding='utf-8')
elapsed = time.perf_counter() - before
(REPRO / 'stdout.log').write_text(process.stdout, encoding='utf-8')
(REPRO / 'stderr.log').write_text(process.stderr, encoding='utf-8')
assert process.returncode == 0, process.stdout + process.stderr
reproduced = load(REPRO / 'execution_results.json')
fields = ('name', 'outcome', 'status_requested', 'fault', 'mutations', 'mutation_attempts', 'build_reads')
assert [{key: row[key] for key in fields} for row in original['cases']] == [
    {key: row[key] for key in fields} for row in reproduced['cases']]

trace_checks = []
for case in original['cases']:
    trace = load(READER / f"trace_{case['name']}.json")
    requests = trace['requests']
    journal = load(READER / trace['journal'])
    assert journal['dataset'] and journal['branch'] == 'reader-j12' and journal['payload_sha256']
    assert all('authorization' not in row['headers'] for row in requests)
    assert all(0 < row['timeout']['read'] <= 3 for row in requests)
    create_indices = [i for i, row in enumerate(requests) if row['path'].endswith('/transactions')]
    commit_indices = [i for i, row in enumerate(requests) if row['path'].endswith('/commit')]
    staged = [i for i, row in enumerate(requests)
              if row['method'] == 'GET' and dict(row['query']).get('startTransactionRid')]
    visible = [i for i, row in enumerate(requests)
               if '/files/' in row['path'] and row['method'] == 'GET' and dict(row['query']).get('branchName')]
    assert len(create_indices) == 1
    if commit_indices:
        assert staged and min(staged) < min(commit_indices)
    if case['outcome'] in ('success', 'unsuccessful', 'pending'):
        assert visible and max(commit_indices) < min(visible)
    if case['name'] == 'pending_resume':
        assert case['mutations'].count('build_create') == 1 and case['build_reads'] == 4
    if case['name'] == 'upload_recovery':
        assert case['mutation_attempts']['upload'] == 1
    if case['name'] == 'commit_recovery':
        assert case['mutation_attempts']['commit'] == 1
    if case['name'] == 'commit_safe_retry':
        assert case['mutation_attempts']['commit'] == 2 and case['mutations'].count('commit') == 1
    trace_checks.append({'case': case['name'], 'trace_sha256': sha(READER / f"trace_{case['name']}.json"),
                         'journal_sha256': sha(READER / trace['journal']), 'requests': len(requests),
                         'staged_read_before_commit': bool(staged) if commit_indices else 'no commit',
                         'postcommit_branch_file_read': bool(visible), 'verdict': 'PASS'})

rubric = [
    ('capability/lifecycle choice', 'APPEND transaction on an explicit existing branch; transaction-view checks precede commit; separate Build.create uses locally documented ManualTarget. RUNNING is incomplete, only SUCCEEDED succeeds.',
     ['reader_workflow.py:Workflow.dataset_commit', 'reader_workflow.py:Workflow.build', 'trace_success.json']),
    ('prerequisites/version/identity', 'Prepared SDK1.101, UserTokenAuth with synthetic token, synthetic host and explicit dataset/branch/path/RIDs are recorded. Fixture transport supplies only local synthetic responses. Reader identifies authorized enrollment identity and resource permissions as prerequisites for live calls; no live credential, administrator enablement or tenant effect is inferred.',
     ['reader_answer.json:dimensions.choices', 'reader_answer.json:dimensions.code_config.runtime', 'reader_answer.json:dimensions.validation.limits', 'consulted_sources.json']),
    ('exact steps/configuration', 'Reader-authored root-client calls use exact staged transaction bounds, committed branch selector, three-second request limits, bounded streams, at most two commit attempts and three polls. Journal records intent and returned identities.',
     ['reader_workflow.py:Workflow.verify_file', 'reader_workflow.py:Workflow.dataset_commit', 'reader_workflow.py:Workflow.build', 'journal_success.json']),
    ('complete example inputs/results', 'Complete executable code includes explicit CSV bytes, synthetic identities, stateful HTTP fixture, exact request body/query assertions and expected/actual outputs for twelve scenarios. Independent reproduction matches all semantic outcome/count fields.',
     ['reader_workflow.py', 'execution_results.json', 'raw_execution_output.txt']),
    ('success checks', 'Metadata, transaction-view bytes and size checked before commit; transaction COMMITTED, branch pointer and visible file metadata/content checked after commit. Build success/failure/cancel/pending classified separately; trace ordering independently verified.',
     ['trace_success.json', 'trace_failed.json', 'trace_canceled.json', 'trace_pending.json']),
    ('failure/recovery', 'Lost upload or applied commit replies do not duplicate writes. A no-effect commit timeout is retried only after OPEN transaction, unchanged branch and staged-content reconciliation. Pending resumes from journal without another create; corruption and wrong branch stop before build, confirmed OPEN bad staging aborts.',
     ['trace_upload_recovery.json', 'trace_commit_recovery.json', 'trace_commit_safe_retry.json', 'trace_pending_resume.json', 'trace_staging_corruption.json', 'trace_branch_mismatch.json']),
]
report = {
    'reviewer_agent': '/root/j12_independent_grade_20261028', 'review_date': '2026-10-28',
    'started_at_utc': started, 'finished_at_utc': datetime.now(timezone.utc).isoformat(),
    'ticket': 'BUG-SUB-025', 'journey': 'J12', 'verdict': 'PASS', 'score': '6/6',
    'reader_agent': '/root/j12_reader_recover_20261028',
    'reader_answer_sha256': sha(READER / 'reader_answer.json'),
    'rubric_source': '.ept/docs/deliverables/architecture/SA-DES-014-offline-development-knowledge/verification-and-delivery.md:40',
    'rubric_source_sha256': sha(ROOT / '.ept/docs/deliverables/architecture/SA-DES-014-offline-development-knowledge/verification-and-delivery.md'),
    'dimensions': [{'dimension': name, 'verdict': 'PASS', 'reason': reason, 'evidence': evidence}
                   for name, reason, evidence in rubric],
    'independence': {'reader_was_forked_without_parent_history': True,
                     'reader_declares_no_previous_answers_sdk_source_or_repo_tests': True,
                     'reader_code_not_shipped_example_import': True,
                     'grader_distinct_from_reader_and_content_author': True,
                     'limit': 'Reader knowledge isolation is based on the separate task instructions and reader declaration, not an OS capability sandbox.'},
    'integrity': {'verified_reader_artifact_count': len(verified), 'snapshot_files': 4437,
                  'snapshot_tree_sha256': snapshot['tree_sha256'],
                  'snapshot_manifest_sha256': sha(READER / 'snapshot_manifest.json'),
                  'artifact_manifest_sha256': sha(READER / 'artifact_hash_manifest.json'),
                  'consulted_current_continuity': continuity},
    'reproduction': {'command': command, 'exit_code': process.returncode, 'elapsed_seconds': elapsed,
                     'output_directory': str(REPRO.relative_to(ROOT)),
                     'reader_code_sha256': sha(READER / 'reader_workflow.py'),
                     'stdout_sha256': sha(REPRO / 'stdout.log'), 'stderr_sha256': sha(REPRO / 'stderr.log'),
                     'cases': 12, 'semantic_outcomes_counts_equal_original': True},
    'trace_checks': trace_checks,
    'closure_preconditions': [
        'Archive and commit this grade, reader code/output, manifests, consulted-source hashes and original failure references before BUG-SUB-025 resolution; the prior developer comment explicitly requires durable committed QA evidence.',
        'Developer checks current In Progress DoD and documents root cause/fix/regression/time with no invented contributor hours before moving to Resolved.',
        'Separate QA then checks Resolved DoD, removes only verified Blocks LINK-01894 and preserves RelatesTo LINK-01893 before closure.',
        'TESTEXEC-064 complete REST acceptance remains separate; this J12 grade does not waive its other namespaces/journeys or domain formal QA.'
    ],
    'scope_limits': [
        'Real SDK serialization and decoding against a declared stateful HTTP mock, not live Foundry writes, build execution, credentials, permissions or administrator grants.',
        'The reader reports single-writer fixture assumptions; its reconciliation is not an atomic concurrency guarantee.',
        'Per-process DNS/socket denial and explicit rejection probes do not demonstrate OS-wide isolation.',
        'Lost create response and abort-timeout branches are guarded but not executed; deadline exhaustion was not separately timed. Required bounded poll exhaustion and uncertain upload/commit cases were executed.',
        'The reader snapshot is immutable by its recorded content manifest; consulted files match current shared skill bytes. No claim that every current unconsulted file equals that snapshot or an immutable Git commit is made.'
    ],
    'reader_artifacts_for_archive': verified,
    'tracker_mutations': [], 'shared_source_or_ledger_mutations': []
}
regression_path = TMP / 'feature015_rest075_j12_readiness_20261027.json'
assert sha(regression_path) == 'c899180b39cf2a309b3382ef4d42d014b547f2caf25ff93242ce182f8b78b5e1'
regression = load(regression_path)['j12']
fixture = CURRENT / 'examples/rest/074/v2/datasets/staged_commit_journey.py'
assert sha(fixture) == regression['current_fixture_sha256']
assert regression['current_distributed_fixture']['exit_code'] == 0
report['existing_current_composed_regression'] = {
    'reviewer': '/root/j12_075_readiness_20261027',
    'evidence': str(regression_path.relative_to(ROOT)),
    'evidence_sha256': sha(regression_path),
    'current_fixture_sha256': sha(fixture),
    'result': regression['current_distributed_fixture'],
    'boundary': 'Previously executed current-byte regression, separately retained from this fresh reader and independent grader reproduction.'
}
report['preserved_failure_references'] = [
    {'path': '.ept/tmp/feature015-j12-reader/reader-results.md',
     'exists': (TMP / 'feature015-j12-reader/reader-results.md').is_file()},
    {'path': '.ept/tmp/feature015_rest_semantic_review/j12_independent_score.md',
     'exists': (TMP / 'feature015_rest_semantic_review/j12_independent_score.md').is_file()}
]
OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'verdict': report['verdict'], 'score': report['score'], 'consulted_sources': len(continuity),
                  'grade_sha256': sha(OUT), 'path': str(OUT)}))
