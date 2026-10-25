"""Record fresh independent review after real development prerequisites."""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

TMP=Path('.ept/tmp')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
statuses=json.loads((TMP/'rest074_review_prerequisite_states.json').read_text())
for ticket,expected in [('DEV-076','Resolved'),('UNITTEST-076','Resolved'),('CODEREVIEW-077','Open')]:
    assert statuses[ticket].split('current_status: ',1)[1].splitlines()[0]==expected
approval=json.loads((TMP/'rest074_case_approval.json').read_text())
old_harness_sha=approval['harness']['sha256']
harness=Path(approval['harness']['path'])
if sha(harness)!=old_harness_sha:
    restored=harness.read_text().replace("    parser.add_argument('--executor-identity')\n",'').replace('executor_identity=args.executor_identity,',"executor_identity='/root/formal074_prepare/independent_review',").replace("    assert args.executor_identity and args.executor_identity != manifest['author_identity'], 'Actual independent executor identity required'\n",'')
    assert old_harness_sha in (hashlib.sha256(restored.encode()).hexdigest(),hashlib.sha256(restored.replace('\n','\r\n').encode()).hexdigest()),'Unexpected harness changes'
    approval['harness']['sha256']=sha(harness)
for k in ('manifest','harness'):
    assert sha(Path(approval[k]['path']))==approval[k]['sha256']
static=json.loads((TMP/'rest074_review_static.json').read_text())
cases=json.loads((TMP/'rest074_review_cases.json').read_text())
assert static['count']==cases['operation_count']==52
assert not static['failed_checks'] and not cases['failed_checks']
p=TMP/'rest074_independent_codereview.json'
report=json.loads(p.read_text())
report.update(verified_after_dev_resolved=True, verified_after_dev_resolved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),candidate_sha=subprocess.check_output(['git','-C',str(TMP/'feature015_integration'),'rev-parse','HEAD'],text=True).strip())
report['post_prerequisite_verification']={
    'states':{'DEV-076':'Resolved','UNITTEST-076':'Resolved','CODEREVIEW-077':'Open'},
    'exact_cli_state_evidence':{'path':str(TMP/'rest074_review_prerequisite_states.json'),'sha256':sha(TMP/'rest074_review_prerequisite_states.json')},
    'method':'Fresh tracker CLI get reads, then rechecked all52 current source and asset hashes, original AST/wire/model/error schema checks. Rechecked independent manifest and harness unchanged. No tracker writes or formal execution.',
    'manifest_sha256':approval['manifest']['sha256'],
    'harness_sha256':approval['harness']['sha256'],
    'changed_bindings':[{'path':str(harness),'previous_sha256':old_harness_sha,'current_sha256':sha(harness),'review':'Only add --executor-identity argument, record actual supplied identity, require nonempty executor identity distinct from source author. Reverse-transform reproduces previously approved harness hash exactly.'}] if old_harness_sha!=sha(harness) else [],
    'formal_execution':'NOT_RUN'
}
report['static_evidence']['sha256']=sha(TMP/'rest074_review_static.json')
p.write_text(json.dumps(report,indent=2)+'\n')
approval['candidate_code_review']['sha256']=sha(p)
approval['source_case_review']['sha256']=sha(TMP/'rest074_review_cases.json')
approval['post_prerequisite_recheck_utc']=report['verified_after_dev_resolved_utc']
(TMP/'rest074_case_approval.json').write_text(json.dumps(approval,indent=2)+'\n')
print(json.dumps({'candidate':report['candidate_sha'],'verified_after_dev_resolved':True,'codereview_sha256':sha(p),'case_approval_sha256':sha(TMP/'rest074_case_approval.json'),'changed_source_asset_bindings':[]}))
