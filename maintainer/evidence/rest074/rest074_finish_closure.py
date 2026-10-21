"""Verify preserved independent execution, then record and close its tracker task."""
import ast
import hashlib
import importlib.metadata
import json
import subprocess
import sys
import threading
from datetime import datetime, timezone
from pathlib import Path

TMP = Path(__file__).resolve().parent
ROOT = TMP.parent.parent
REPO = TMP / 'feature015_integration'
ACTOR = 'formal074-finish-closure'
IDENTITY = '/root/formal074_finish_closure'
TRANSCRIPT = TMP / 'rest074_closure_cli.jsonl'
TRANSCRIPT_LOCK = threading.Lock()

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def read(name):
    return json.loads((TMP / name).read_text(encoding='utf-8'))

def save(name, value):
    (TMP / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')

def cli(*args):
    run = subprocess.run([sys.executable, str(ROOT / '.ept/tools/tracker/tracker_cli.py'), *args, '--author', ACTOR], capture_output=True, text=True)
    with TRANSCRIPT_LOCK:
        with TRANSCRIPT.open('a', encoding='utf-8') as stream:
            stream.write(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(), args=args, author=ACTOR, exit_code=run.returncode, stdout=run.stdout, stderr=run.stderr)) + '\n')
    if run.returncode:
        raise RuntimeError((args, run.returncode, run.stdout, run.stderr))
    return run.stdout

def state(ticket):
    return cli('get', ticket).split('current_status: ', 1)[1].splitlines()[0]

def comment(subject, text):
    assert len(text) < 23000
    return cli('comment', 'create', 'TESTEXEC-076', '--subject', subject, '--text', text)

def verify():
    cases = read('rest074_formal_cases.json')
    approval = read('rest074_case_approval.json')
    correction = read('rest074_review_normalization_approval.json')
    execution = read('rest074_formal_execution.json')
    runner = read('rest074_formal_runner.json')
    discovery = read('rest074_exec_discovery.json')
    assert importlib.metadata.version('foundry-platform-sdk') == '1.101.0'
    assert cases['author_identity'] != approval['reviewer_identity'] != execution['executor_identity']
    assert execution['executor_identity'] != cases['author_identity']
    assert approval['verdict'] == correction['verdict'] == 'APPROVED'
    assert execution['execution'] == discovery['result'] == 'PASS'
    assert runner['exit_code'] == 0 and runner['bindings_unchanged_after_run']
    assert runner['executor_identity'] == execution['executor_identity']
    assert sha(TMP/'rest074_formal_cases.json') == runner['cases_sha256'] == execution['cases_sha256'] == approval['manifest']['sha256'] == correction['unchanged_manifest_sha256'] == discovery['manifest_sha256']
    assert sha(TMP/'rest074_formal_execute.py') == runner['harness_sha256'] == execution['harness_sha256'] == approval['harness']['sha256'] == correction['corrected_harness_sha256']
    assert len(cases['operations']) == len(discovery['operations']) == 52
    assert len(execution['results']) == 1060 and all(row['result']=='PASS' for row in execution['results'])
    assert sum(len(case['errors']) for case in cases['operations']) == execution['declared_errors'] == 288
    assert any(row['check']=='socket_traps_active' for row in execution['results'])
    for field in ('source_case_review', 'candidate_code_review', 'normalization_correction_review'):
        assert sha(ROOT / approval[field]['path']) == approval[field]['sha256']
    for path, digest in runner['sdk_assets_binding'].items():
        assert sha(path) == digest, path
    operations = []
    for case in cases['operations']:
        source = Path(case['source']['path'])
        assert sha(source) == case['source']['sha256']
        text = source.read_text(encoding='utf-8')
        resource, method = case['operation'].split('.')[-2:]
        cls = next(node for node in ast.parse(text).body if isinstance(node,ast.ClassDef) and node.name==resource+'Client')
        fn = next(node for node in cls.body if isinstance(node,ast.FunctionDef) and node.name==method)
        assert hashlib.sha256(ast.get_source_segment(text,fn).encode()).hexdigest() == case['source']['method_source_sha256']
        for asset in case['assets'].values():
            assert sha(REPO / '.agents/skills/pal-found-dev' / asset['path']) == asset['sha256']
        rows = [row for row in execution['results'] if row['case_id']==case['case_id']]
        checks = {row['check'] for row in rows}
        assert {'success_typed','success_raw_closed','async_typed','async_raw_closed','timeout_no_retry'} <= checks
        assert all('error_'+error['name'] in checks for error in case['errors'])
        found = next(row for row in discovery['operations'] if row['operation']==case['operation'])
        assert all(found['checks'].values())
        for key in ('catalog','index','contract','behavior','example'):
            assert sha(found[key]['path']) == found[key]['sha256']
        operations.append(dict(id=case['operation'], case_id=case['case_id'], verdict='PASS', checks=len(rows), assets=case['assets'], source=case['source'], local_discovery=found, actual_results=rows))
    attempts = []
    for path in sorted(TMP.glob('rest074_exec_attempt*_runner.json')):
        attempt = json.loads(path.read_text(encoding='utf-8'))
        for group in ('snapshots','outputs'):
            for item,digest in attempt[group].items():
                assert sha(item)==digest, item
        detail = read(path.name.replace('_runner.json','_rest074_formal_execution.json'))
        attempts.append(dict(runner=path.name, sha256=sha(path), attempt=attempt['attempt'], exit_code=attempt['exit_code'], elapsed_seconds=attempt['elapsed_seconds'], harness_sha256=attempt['harness_sha256'], cases_sha256=attempt['cases_sha256'], failure=detail.get('failure'), snapshots=attempt['snapshots'], outputs=attempt['outputs']))
    assert len(attempts)==2 and attempts[0]['exit_code']!=0 and attempts[1]['exit_code']==0
    result = dict(verified_at=datetime.now(timezone.utc).isoformat(), verifier=IDENTITY, result='PASS', operations=operations, attempts=attempts, current_candidate_sha=subprocess.check_output(['git','-C',str(REPO),'rev-parse','HEAD'],text=True).strip(), current_source_and_assets_match=True)
    save('rest074_closure_verification.json',result)
    return result

if __name__ == '__main__':
    assert sys.argv[1:]==['--writer-granted']
    proof = verify()
    assert state('TESTCASE-076')=='Closed'
    assert state('TESTEXEC-076')=='In Progress'
    for ticket in ('DESIGN-076','DEV-076','UNITTEST-076','CODEREVIEW-077','BUG-SUB-024'):
        assert state(ticket)=='Closed'
    assert state('BUG-SUB-025')=='In Progress'
    prior = cli('comment','list','TESTEXEC-076')
    case_comments = cli('comment','list','TESTCASE-076')
    assert all(case['case_id']+' independently derived Gherkin and concrete oracle' in case_comments for case in proof['operations'])
    before = {ticket: cli('link','list',ticket) for ticket in ('DEV-STORY-074','TESTEXEC-076','BUG-SUB-025','TESTEXEC-064')}
    save('rest074_closure_links_before.json',before)
    runner=read('rest074_formal_runner.json')
    if 'Verified independent execution evidence and closure plan' not in prior:
        comment('Verified independent execution evidence and closure plan', 'Closure recorder '+IDENTITY+' verifies retained artifacts; actual independent executor '+runner['executor_identity']+'. Original source author /root/formal074_prepare/source_cases; independent case/code reviewer /root/formal074_prepare/independent_review. Read indexed REST authoring contract and SA-DES-014 verification/delivery requirements. CASE076 and all implementation prerequisites are Closed. Fresh exact current module/method, approved manifest/harness, 156 per-operation asset bindings, navigation files and both immutable attempts verified. Record every actual case, measured execution time, then resolve and close only this execution task. J12 integration remains governed by BUG-SUB-025 and TESTEXEC-064; their relationships remain intact.')
    for op in proof['operations']:
        if op['case_id']+' real formal PASS '+op['id'] in prior:
            continue
        navigation = {key:value for key,value in op['local_discovery'].items() if key!='model_links'}
        navigation['full_model_links_evidence'] = dict(path='.ept/tmp/rest074_exec_discovery.json',sha256=sha(TMP/'rest074_exec_discovery.json'),operation=op['id'])
        comment(op['case_id']+' real formal PASS '+op['id'], '\n'.join([
            'Actual independent executor '+runner['executor_identity']+'. Recorded by '+IDENTITY+'. '+op['id'],
            'Actual run '+runner['started_at']+' to '+runner['finished_at']+'; exit 0. Cases SHA256 '+runner['cases_sha256']+'; harness SHA256 '+runner['harness_sha256']+'. SDK 1.101.0 source/module/method and current asset hashes match approved oracle.',
            'Fresh httpx.MockTransport, fake independent-qa-074 credential, literal requests/results/errors. Socket connect/connect_ex/create_connection and DNS denied; explicit denial probes passed. Logs .ept/tmp/rest074_formal_execute.log SHA256 '+sha(TMP/'rest074_formal_execute.log')+'; full result JSON SHA256 '+sha(TMP/'rest074_formal_execution.json')+'.',
            'Actual local discovery: '+json.dumps(navigation,separators=(',',':')),
            'Actual assertion rows: '+json.dumps(op['actual_results'],separators=(',',':')),
            'Offline serializer, typed/raw/stream/error and bounded control-flow evidence. Tenant effects and integrated J12 remain outside this execution.'
        ]))
        print(op['case_id']+' recorded',flush=True)
    measured=sum(row['elapsed_seconds'] for row in proof['attempts'])
    summary=dict(executor=runner['executor_identity'],case_author='/root/formal074_prepare/source_cases',case_reviewer='/root/formal074_prepare/independent_review',closure_recorder=IDENTITY,operations=52,declared_errors=288,check_records=1060,all_attempts=proof['attempts'],total_measured_execution_seconds=measured,final_runtime_seconds=runner['elapsed_seconds'],boundary='Offline SDK transport/request/result/error/local-discovery assertions; tenant and integrated J12 effect/recovery/deployment verification remain separate.')
    save('rest074_closure_summary.json',summary)
    comment('Independent formal execution and immutable attempt history',json.dumps(summary,separators=(',',':'))+'\nAttempt1 failed because JSON serialization converted core.Long to string and timestamps differed; independent reviewer approved Python-mode/date normalization correction before attempt2 PASS. Frozen cases and assets unchanged. Both harnesses, approvals, stdout/stderr, logs, failures and timestamps retained with hashes. 52 per-operation actual outcomes recorded; 52 sync/async typed/raw, 46 sync/async streams, 8 sync/async ordinary iterators plus 8 manual continuations, 52 timeouts, 42 malformed JSON and 0/1001 batch rejection assertions passed. No product defect identified by this run. Historical BUG-SUB-024 remains Closed; separate BUG-SUB-025 remains In Progress under story075 and Blocks TESTEXEC-064. Time field counts both measured runner intervals only. Historical authoring/review effort remains unmeasured. Root/070 must archive complete proof before publication.')
    cli('update','TESTEXEC-076','--field','time_spent_hours='+str(measured/3600))
    cli('workflow','transitions','testexec','In Progress')
    cli('update','TESTEXEC-076','--status','Resolved')
    assert state('TESTEXEC-076')=='Resolved'
    save('rest074_closure_resolved_readback.json',dict(cli_get=cli('get','TESTEXEC-076')))
    for ticket, links in before.items():
        assert cli('link','list',ticket)==links
    cli('workflow','transitions','testexec','Resolved')
    cli('update','TESTEXEC-076','--status','Closed')
    print('WRITERDONE: no further live tracker mutations',flush=True)
