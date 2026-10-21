"""Record only independently verified real REST074 results, then export actual states."""
from rest074_record_workflow import *
from datetime import datetime, timezone

if sys.argv[1:] != ['--writer-granted']:
    raise SystemExit('Exclusive tracker writer grant required')

cases = bound()
# Allocate the shared readiness interval once across its two tracker fields.
ready = read('rest074_readiness.json')
import re
unit_seconds = float(re.search(r'73 passed in ([0-9.]+)s', ready['unit_stdout']).group(1))
for ticket, seconds in (('DEV-076', ready['elapsed_seconds'] - unit_seconds), ('UNITTEST-076', unit_seconds)):
    cli('update', ticket, '--field', 'time_spent_hours=' + str(seconds / 3600))
    comment(ticket, 'Measured readiness time allocation corrected', 'Shared readiness interval was initially copied to both DEV and UNIT fields. Correct allocation counts it once: UNIT receives actual pytest-reported ' + str(unit_seconds) + ' seconds; DEV receives remaining physical/tracked/hash/compile verification and process overhead. Combined interval is ' + str(ready['elapsed_seconds']) + ' seconds. Historical implementation/review effort remains unmeasured and unclaimed.')
approval = read('rest074_case_approval.json')
execution = read('rest074_formal_execution.json')
runner = read('rest074_formal_runner.json')
discovery = read('rest074_exec_discovery.json')
assert state('TESTCASE-076') == 'Closed'
assert state('TESTEXEC-076') == 'In Progress'
assert execution['execution'] == discovery['result'] == 'PASS'
assert runner['exit_code'] == 0 and runner['bindings_unchanged_after_run']
assert execution['executor_identity'] == runner['executor_identity'] == EXECUTOR
assert EXECUTOR not in (cases['author_identity'], approval['reviewer_identity'])
assert runner['cases_sha256'] == execution['cases_sha256'] == approval['manifest']['sha256'] == sha(TMP/'rest074_formal_cases.json')
assert runner['harness_sha256'] == execution['harness_sha256'] == approval['harness']['sha256'] == sha(TMP/'rest074_formal_execute.py')
assert discovery['manifest_sha256'] == execution['cases_sha256']
assert len(cases['operations']) == execution['operations'] == len(discovery['operations']) == 52
assert all(row['result']=='PASS' for row in execution['results'])
assert any(row['check']=='socket_traps_active' for row in execution['results'])
operations=[]
for case in cases['operations']:
    rows=[row for row in execution['results'] if row['case_id']==case['case_id']]
    checks={row['check'] for row in rows}
    assert {'success_typed','success_raw_closed','async_typed','async_raw_closed','timeout_no_retry'} <= checks
    assert all('error_'+error['name'] in checks for error in case['errors'])
    found=next(row for row in discovery['operations'] if row['operation']==case['operation'])
    assert all(found['checks'].values())
    text='\n'.join(['Actual independent executor '+EXECUTOR+'. '+case['operation'], 'Final run '+runner['started_at']+' to '+runner['finished_at']+'; exit0. Literal independent cases SHA256 '+runner['cases_sha256']+'; actual harness SHA256 '+runner['harness_sha256']+'. Original SDK1.101.0 source/error/module and156currentasset hashes remained unchanged before/after run.', 'Public socket/connect/connect_ex/create_connection/DNS denied; explicit network denial probes passed. Real SDK HTTP serializer, typed result/error APIs and transport lifetimes asserted through fresh MockTransport. Full actual log .ept/tmp/rest074_formal_execute.log SHA256 '+sha(TMP/'rest074_formal_execute.log')+'; execution JSON SHA256 '+sha(TMP/'rest074_formal_execution.json')+'.', 'Actual offline local discovery case follows catalog→versioned dataset index→exact operation contract→behavior method heading→runnable example. Source condition, complete inputs/results/errors and synthetic boundaries remain local. Discovery proof:',json.dumps(found,separators=(',',':')),'These runtime records were emitted only after actual assertions passed:',json.dumps(rows,separators=(',',':'))])
    comment('TESTEXEC-076',case['case_id']+' real formal PASS '+case['operation'],text)
    operations.append({'id':case['operation'],'case_id':case['case_id'],'verdict':'PASS','checks':len(rows),'assets':case['assets'],'source':case['source'],'local_discovery':found})

attempts=[]
for path in sorted(TMP.glob('rest074_exec_attempt*_runner.json')):
    row=json.loads(path.read_text(encoding='utf-8'))
    detail_path=path.with_name(path.name.replace('_runner.json','_rest074_formal_execution.json'))
    detail=json.loads(detail_path.read_text(encoding='utf-8'))
    attempts.append({'runner':path.name,'sha256':sha(path),'attempt':row['attempt'],'exit_code':row['exit_code'],'elapsed_seconds':row['elapsed_seconds'],'harness_sha256':row['harness_sha256'],'cases_sha256':row['cases_sha256'],'failure':detail.get('failure'),'snapshots':row['snapshots'],'outputs':row['outputs']})
elapsed=sum(row['elapsed_seconds'] for row in attempts)
summary={'executor':EXECUTOR,'case_author':cases['author_identity'],'case_reviewer':approval['reviewer_identity'],'operations':52,'declared_errors':execution['declared_errors'],'check_records':len(execution['results']),'actual_discovery_cases':52,'final_exit_code':runner['exit_code'],'final_runtime_seconds':runner['elapsed_seconds'],'all_attempts':attempts,'total_measured_execution_seconds':elapsed,'boundary':'Offline SDK transport/request/result/error/local-discovery assertions only; no live enrollment or integrated J12 effect/recovery/deployment verification.'}
comment('TESTEXEC-076','Independent formal execution and immutable attempt history',json.dumps(summary,separators=(',',':'))+'\nAll approved source case literals remain unchanged since CASEClosed. First failed harness attempt compared JSON-mode long serialization against typed Python values; source ModelBase.to_dict aliases/Python values independently reviewed, precise harness correction approved and new hash bound before rerun. Original manifest, all approvals, harness versions, execution outputs and failures preserved immutably under rest074_exec_attemptN_*. Full source/error/currentasset bindings match.52 per-operation runtime and local-heading comments recorded. Time field includes only measured runner intervals; unmeasured authoring/review not invented. Separate root/070 must archive full evidence before publication. Related BUG-SUB025 remains separately governed under J12/075; historicalBUGSUB024 closure preserved.')
cli('update','TESTEXEC-076','--field','time_spent_hours='+str(elapsed/3600))
transition('TESTEXEC-076','testexec','In Progress','Resolved')
cli('link','list','TESTEXEC-076')
transition('TESTEXEC-076','testexec','Resolved','Closed')

exports={}
for ticket in ('DEV-STORY-074','DESIGN-076','DEV-076','UNITTEST-076','CODEREVIEW-077','TESTCASE-076','TESTEXEC-076','BUG-SUB-024','BUG-SUB-025'):
    raw=cli('get',ticket)
    exports[ticket]={'status':raw.split('current_status: ',1)[1].splitlines()[0],'cli_get':raw,'links':cli('link','list',ticket)}
assert all(exports[t]['status']=='Closed' for t in ('DESIGN-076','DEV-076','UNITTEST-076','CODEREVIEW-077','TESTCASE-076','TESTEXEC-076','BUG-SUB-024'))
assert exports['BUG-SUB-025']['status']=='In Progress'
assert exports['DEV-STORY-074']['status']=='Deployment'
(TMP/'rest074_tracker_status_exports.json').write_text(json.dumps({'exported_at':datetime.now(timezone.utc).isoformat(),'tickets':exports},indent=2)+'\n',encoding='utf-8')
report={'story':'DEV-STORY-074','candidate_sha':subprocess.check_output(['git','-C',str(REPO),'rev-parse','HEAD'],text=True).strip(),'sdk_release':'1.101.0','source_commit':cases['source_commit'],'case_author':cases['author_identity'],'reviewer':approval['reviewer_identity'],'executor':EXECUTOR,'case_manifest_sha256':runner['cases_sha256'],'testcase_status':exports['TESTCASE-076']['status'],'testexec_status':exports['TESTEXEC-076']['status'],'story_status':exports['DEV-STORY-074']['status'],'formal_execution':'PASS','operations':operations,'execution_summary':summary,'boundary':summary['boundary'],'durable_archive_required':True}
(TMP/'rest074_formal_qa.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
files=sorted(path for path in TMP.glob('rest074_*') if path.is_file())
(TMP/'rest074_artifact_inventory.json').write_text(json.dumps({'created_at':datetime.now(timezone.utc).isoformat(),'files':[{'path':path.name,'sha256':sha(path),'bytes':path.stat().st_size} for path in files]},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'formal_execution':'PASS','operations':52,'errors':execution['declared_errors'],'checks':len(execution['results']),'story_status':exports['DEV-STORY-074']['status'],'artifact_files':len(files)}))
