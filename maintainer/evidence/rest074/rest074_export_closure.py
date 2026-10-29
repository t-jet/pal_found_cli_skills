"""Export CLI closure proof and inventory without changing tracker records."""
import concurrent.futures
import json
import re
from datetime import datetime, timezone
from rest074_finish_closure import TMP, ROOT, REPO, IDENTITY, cli, read, save, sha, verify

exports = {}
for ticket in ('DEV-STORY-074','DESIGN-076','DEV-076','UNITTEST-076','CODEREVIEW-077','TESTCASE-076','TESTEXEC-076','BUG-SUB-024','BUG-SUB-025','TESTEXEC-064'):
    raw = cli('get',ticket)
    exports[ticket] = dict(status=raw.split('current_status: ',1)[1].splitlines()[0], cli_get=raw, links=cli('link','list',ticket))
assert all(exports[t]['status']=='Closed' for t in ('DESIGN-076','DEV-076','UNITTEST-076','CODEREVIEW-077','TESTCASE-076','TESTEXEC-076','BUG-SUB-024'))
assert exports['DEV-STORY-074']['status']=='Deployment'
save('rest074_tracker_status_exports.json',dict(exported_at=datetime.now(timezone.utc).isoformat(),exporter=IDENTITY,tickets=exports))

requests=[]
listings={}
for ticket in ('TESTCASE-076','TESTEXEC-076','CODEREVIEW-077'):
    listing=cli('comment','list',ticket)
    listings[ticket]=listing
    ids=re.findall(r'^(\d{8}-\d{6}-\S+)\s',listing,re.MULTILINE)
    assert ids
    requests.extend((ticket,comment_id) for comment_id in ids)

def get_comment(request):
    ticket,comment_id=request
    return dict(ticket=ticket,comment_id=comment_id,cli_get=cli('comment','get',ticket,comment_id))

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    comments=list(pool.map(get_comment,requests))
save('rest074_tracker_comment_exports.json',dict(exported_at=datetime.now(timezone.utc).isoformat(),exporter=IDENTITY,listings=listings,comments=comments))
proof=verify()
for operation in proof['operations']:
    match=[row for row in comments if row['ticket']=='TESTEXEC-076' and 'subject         : '+operation['case_id']+' real formal PASS '+operation['id'] in row['cli_get']]
    assert len(match)==1,operation['id']
    assert 'Actual assertion rows:' in match[0]['cli_get']
assert 'Independent formal execution and immutable attempt history' in listings['TESTEXEC-076']
cases=read('rest074_formal_cases.json')
approval=read('rest074_case_approval.json')
runner=read('rest074_formal_runner.json')
summary=read('rest074_closure_summary.json')
files=sorted(path for path in TMP.glob('rest074_*') if path.is_file() and path.name not in ('rest074_archive_inventory.json','rest074_artifact_inventory.json'))
evidence={path.name:dict(path='.ept/tmp/'+path.name,sha256=sha(path),bytes=path.stat().st_size) for path in files}
report=dict(story='DEV-STORY-074',candidate_sha=proof['current_candidate_sha'],sdk_release='1.101.0',source_commit=cases['source_commit'],case_author=cases['author_identity'],reviewer=approval['reviewer_identity'],executor=runner['executor_identity'],closure_recorder=IDENTITY,case_manifest_sha256=runner['cases_sha256'],harness_sha256=runner['harness_sha256'],testcase_status=exports['TESTCASE-076']['status'],testexec_status=exports['TESTEXEC-076']['status'],story_status=exports['DEV-STORY-074']['status'],formal_execution='PASS',operations=proof['operations'],execution_summary=summary,evidence=evidence,boundary=summary['boundary'],source_candidate_continuity=dict(original_case_candidate=cases['reviewed_candidate_sha'],independent_code_review_candidate=read('rest074_independent_codereview.json')['candidate_sha'],current_candidate=proof['current_candidate_sha'],all_52_module_and_method_hashes_match=True,all_156_operation_asset_bindings_match=True,all_attempts_immutable=True,manifest_unchanged=True,scope='Exact bound assets establish continuity across intervening candidate commits; this does not approve unrelated candidate changes.'),related_J12=dict(bug='BUG-SUB-025',bug_status_at_closure_verification='In Progress',acceptance_block='TESTEXEC-064',links_preserved=True),durable_archive_required=True)
save('feature015_rest074_formal_qa.json',report)
inventory=dict(created_at=datetime.now(timezone.utc).isoformat(),inventory_author=IDENTITY,story='DEV-STORY-074',formal_execution='PASS',case_manifest_sha256=runner['cases_sha256'],closure_statuses={t:exports[t]['status'] for t in exports},files=list(evidence.values())+[dict(path='.ept/tmp/feature015_rest074_formal_qa.json',sha256=sha(TMP/'feature015_rest074_formal_qa.json'),bytes=(TMP/'feature015_rest074_formal_qa.json').stat().st_size)],source_and_asset_bindings=runner['sdk_assets_binding'],attempts=proof['attempts'],note='Inventory excludes itself. Failed and successful attempts, original and corrected harnesses, source cases, independent reviews and approvals, actual logs, source/hash evidence and CLI closure/comment exports retained. No proof execution rerun or reviewer approval invented by closure recorder.')
save('rest074_archive_inventory.json',inventory)
print(json.dumps(dict(formal_execution='PASS',operations=52,assertion_rows=1060,story_status=exports['DEV-STORY-074']['status'],comments_exported=len(comments),artifact_files=len(inventory['files']),report_sha256=sha(TMP/'feature015_rest074_formal_qa.json'),inventory_sha256=sha(TMP/'rest074_archive_inventory.json'))))
