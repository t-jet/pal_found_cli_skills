"""Approve source case design and bind reviewed execution harness."""
import datetime
import hashlib
import json
from pathlib import Path

def binding(name):
    p=Path('.ept/tmp')/name
    return {'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}

manifest=Path('.ept/tmp/rest074_formal_cases.json')
m=json.loads(manifest.read_text())
check=json.loads(Path('.ept/tmp/rest074_review_cases.json').read_text())
assert hashlib.sha256(manifest.read_bytes()).hexdigest()==check['manifest_sha256']
assert check['operation_count']==52 and check['error_count']==288 and not check['failed_checks']
approval={
    'story':'DEV-STORY-074',
    'testcase':'TESTCASE-076',
    'reviewer_identity':'/root/formal074_prepare/independent_review',
    'author_identity':m['author_identity'],
    'verdict':'APPROVED',
    'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'manifest':binding('rest074_formal_cases.json'),
    'harness':binding('rest074_formal_execute.py'),
    'source_case_review':binding('rest074_review_cases.json'),
    'candidate_code_review':binding('rest074_independent_codereview.json'),
    'counts':{'operations':52,'declared_errors':288,'additional_cases':114},
    'review_method':'Independently parsed original SDK AST and annotations; compared all source and asset hashes, stored wire literals, argument/result/error schemas, concrete payloads and status/code/class expectations. Reviewed concrete request/result semantics and harness source. Did not run clients or formal execution.',
    'semantic_changes_verified':['CSV header matches requested inspection_id/status columns and row limit.', 'File.list finite pages preserve requested inspections-independent/ prefix.', 'Resource RID roles distinguish dataset, transaction, build, job, check and schedule.', 'Error target parameters bind serialized path/query/body values.', 'Primary key exactly equals requested columns/resolution; removal retains distinct backing survivor.'],
    'harness_review':['Sync and async ordinary iterator continuation is finite, carries returned token, preserves filters, consumes two distinct nonempty pages and stops at terminal token.', 'Sync and async typed, raw and streaming success compare returned values with frozen manifest literals; wrappers and httpx clients close.', 'Bytes are decoded from manifest hex before calls and compared after response consumption.', 'Named errors compare exact SDK classes, names, parameters and instance identifiers; network denied and retries disabled.', 'Required argument and 0/1001 batch cases reject before transport; malformed JSON and timeout paths remain explicit.'],
    'formal_execution':'NOT_RUN',
    'execution_preconditions':['Coordinator confirms actual TESTCASE-076 Closed state.', 'Coordinator grants formal execution after readiness evidence.', 'Execute only this manifest and harness hash, or obtain fresh review after changes.'],
    'limits':['Mock transport verifies client requests, decoding and bounded control flow. It does not prove tenant grants, actual data lifecycle effects or server validation.', 'Historical manual evidence belongs to prior reviewers and is not reported as this identity\'s execution.']
}
assert approval['reviewer_identity']!=approval['author_identity']
Path('.ept/tmp/rest074_case_approval.json').write_text(json.dumps(approval,indent=2)+'\n')
print(json.dumps({'verdict':approval['verdict'],'manifest':approval['manifest']['sha256'],'harness':approval['harness']['sha256']}))
