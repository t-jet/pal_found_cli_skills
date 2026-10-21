from rest074_record_workflow import *
assert sys.argv[1:]==['--writer-granted']
cases=bound()
approved=read('rest074_case_approval.json')
assert approved['manifest']['sha256']==sha(TMP/'rest074_formal_cases.json')
assert approved['harness']['sha256']==sha(TMP/'rest074_formal_execute.py')
assert state('DEV-STORY-074')=='QA'
assert all(state(t)=='Closed' for t in ('DEV-076','UNITTEST-076','CODEREVIEW-077'))
started=time.monotonic()
comment('TESTCASE-076', 'Runnable prerequisites, source-derived case plan and independent approval', 'Actual independent case author ' + cases['author_identity'] + '; fresh independent approver ' + REVIEWER + '. DESIGN/DEV/UNIT/CR Closed; all52 committed examples compile;73 actual unit tests PASS; prepared SDK1.101.0/httpx/Pydantic runtime functional. Read indexed designs/handoff, complete source-derived52 partition and primary model/error schemas. Public sockets/DNS denied. Plan:52 exact wire/typed results/all288 named errors, required/optional variants,401/403/timeouts/malformed JSON, real ordinary sync/async finite pages, raw and streaming lifetimes, bytes/schema/transaction/View semantics and batch bounds. Literal Gherkin/oracles and all114 extras in manifest SHA256 ' + approved['manifest']['sha256'] + '. Approval .ept/tmp/rest074_case_approval.json binds exact manifest+harness. Source silence and missing enrollment/runtime boundary explicit; no live tenant or integrated J12 claim.')
transition('TESTCASE-076','testcase','Open','In Progress')
for row in cases['operations']:
    reduced = {key: copy.deepcopy(row[key]) for key in ('case_id','operation','gherkin','request','success','errors')}
    reduced['request'].pop('argument_schemas',None)
    reduced['success'].pop('schema',None)
    for error in reduced['errors']:
        for key in ('parameter_schema','schema','parameters_schema'):
            error.pop(key,None)
    errors = reduced.pop('errors')
    comment('TESTCASE-076', row['case_id'] + ' independently derived Gherkin and concrete oracle', json.dumps(reduced,separators=(',', ':')))
    for offset in range(0,len(errors),3):
        comment('TESTCASE-076', row['case_id'] + ' concrete named-error oracles ' + str(offset+1) + '-' + str(min(offset+3,len(errors))), json.dumps({'operation':row['operation'],'case_manifest_sha256':approved['manifest']['sha256'],'errors':errors[offset:offset+3]},separators=(',', ':')))
comment('TESTCASE-076','Independent complete case approval and access boundary', 'APPROVED by actual fresh reviewer ' + REVIEWER + ', distinct from independent source case author ' + cases['author_identity'] + '.52 primary-source literal cases,288 named errors,114 additional scenarios; allrequest/result/error schemas checked against original SDK1.101.0 and all156 currentasset hashes. ManifestSHA256 ' + approved['manifest']['sha256'] + '; harnessSHA256 ' + approved['harness']['sha256'] + '. Full manifest records exact optional omission, paging, bounded batch and binary inputs/results; error targets are source-contextual. Raw/stream response closure and ordinary iterator modes inspected. No unresolved case question. Formal execution NOT_RUN. Time covers measured current recording only, not historical case authoring/review.')
cli('update','TESTCASE-076','--field','time_spent_hours='+str((time.monotonic()-started)/3600))
transition('TESTCASE-076','testcase','In Progress','Resolved')
transition('TESTCASE-076','testcase','Resolved','Closed')
comment('TESTEXEC-076','Approved formal execution plan and runnable environment', 'Actual independent executor ' + EXECUTOR + '. TESTCASE076 Closed; DEV/UNIT/CR Closed terminal successors ofResolved. Exact approved manifest/harness hashes ' + approved['manifest']['sha256'] + '/' + approved['harness']['sha256'] + '. Fresh readiness52 compiled,73 unit PASS; source hashes and SDK1.101.0 runtime match. Execute real SDK serializer+typed/raw/stream sync/async results, finite automatic/manual pagination, literal bytes, source-specific errors/local invalid/batch bounds, corrected file/schema/View identities with socket/DNS denial and explicit denial probes. Record real assertions and timestamps; preserve failures. Fixture execution proves offline transport and local guidance only; no enrollment effects, integratedJ12 or production deployment claim. No unresolved execution prerequisite. Final logs/cases/review/harness archived by root/070 before publication.')
transition('TESTEXEC-076','testexec','Open','In Progress')
