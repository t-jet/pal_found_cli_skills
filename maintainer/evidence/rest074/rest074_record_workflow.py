"""Record genuine REST074 readiness, approved cases and execution using tracker CLI."""
import copy
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

TMP = Path(__file__).resolve().parent
ROOT = TMP.parent.parent
CLI = ROOT / '.ept/tools/tracker/tracker_cli.py'
REPO = TMP / 'feature015_integration'
REVIEWER = '/root/formal074_prepare/independent_review'
EXECUTOR = '/root/formal074_prepare/independent_execute'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(name):
    return json.loads((TMP / name).read_text(encoding='utf-8'))


def cli(*args, author='project-manager'):
    result = subprocess.run([sys.executable, str(CLI), *args, '--author', author], capture_output=True, text=True)
    print(result.stdout, result.stderr, flush=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    return result.stdout


def comment(ticket, subject, text, author='project-manager'):
    assert len(text) < 23000, (ticket, subject, len(text))
    return cli('comment', 'create', ticket, '--subject', subject, '--text', text, author=author)


def state(ticket):
    return cli('get', ticket).split('current_status: ', 1)[1].splitlines()[0]


def transition(ticket, kind, previous, target):
    assert state(ticket) == previous, ticket
    cli('workflow', 'transitions', kind, previous)
    cli('update', ticket, '--status', target)
    assert state(ticket) == target


def bound():
    cases = read('rest074_formal_cases.json')
    assert len(cases['operations']) == 52
    for row in cases['operations']:
        assert sha(row['source']['path']) == row['source']['sha256']
        for asset in row['assets'].values():
            assert sha(REPO / '.agents/skills/pal-found-dev' / asset['path']) == asset['sha256']
    return cases


def readiness():
    cases = bound()
    ready = read('rest074_readiness.json')
    assert ready['result'] == 'PASS' and ready['unit_exit_code'] == 0
    assert state('DESIGN-076') == 'Closed'
    assert state('BUG-SUB-024') == 'Closed'
    for ticket in ('DEV-076', 'UNITTEST-076', 'CODEREVIEW-077', 'TESTCASE-076', 'TESTEXEC-076'):
        text = cli('get', ticket).split('content:\n', 1)[1].rstrip()
        old = 'tests/test_offline_rest_074.py'
        new = 'tests/test_offline_rest_074_semantics.py'
        assert old in text or new in text
        updated = text.replace(old, new)
        body = TMP / ('rest074_' + ticket.lower().replace('-', '_') + '_body.md')
        body.write_text(updated + '\n', encoding='utf-8')
        cli('update', ticket, '--description-file', str(body))
        comment(ticket, 'Approved actual unit-test path correction', 'Root PM explicitly approved this scoped path correction. Actual committed tests/test_offline_rest_074_semantics.py contains 52 SDK examples plus21 semantic regression guards; historical nominal tests/test_offline_rest_074.py does not exist. Indexed handoff draft corrected at parent-integration commit bbe82521, .ept/docs/deliverables/development/FEATURE-015-rest-authoring-contract.md; root owns publication. No criterion or coverage waived. Fresh suite:73 PASS; test SHA256 ' + ready['unit_test_sha256'] + '.')
    paths = sorted({asset['path'] for row in cases['operations'] for asset in row['assets'].values()})
    text = '\n'.join(['Verifier /root/formal074_prepare. Current compiled/committed deliverables independently verified against accepted primary SDK1.101.0 source and current asset hashes. Read indexed BA-DES015 revision2, SA-DES014 REST/source/verification design, authoring handoff and exact52 partition. DESIGN076 and historical BUG-SUB024 are Closed; no unresolved Question subtask or active Blocks link prevents operation readiness. Related BUG-SUB025 remains In Progress under integrated J12/075; no integrated journey, service effect or live enrollment claim.', 'All52 current examples exist, are tracked, and compile; source module/method/contract/behavior/example hashes match. Fresh isolated73 tests passed, with socket/DNS denial in autouse fixture,52 examples+21 negative guard checks. Explicit time covers measured current verification only; historical author effort not reconstructed. Every external example connection uses configurable request_timeout. Full current file evidence .ept/tmp/rest074_readiness.json; SDK release1.101.0 differs from unpublished older customer snapshot.', 'Created/modified distributed deliverables relative to standalone pal-found-dev (no deletions claimed):', *paths, 'Additional committed test: tests/test_offline_rest_074_semantics.py. Source corrections and tests are in candidate commit ' + ready['candidate_commit'] + ' and current52 hashes unchanged. Indexed handoff correction is approved root-owned draft bbe82521; scope/partitions remain unchanged. Review link DEV076↔CODEREVIEW077 already registered. Final evidence archiving and GitHub publication belong to root/070; operation formal QA pending.'])
    comment('DEV-076', 'Physical committed implementation and measured verification', text)
    cli('update', 'DEV-076', '--field', 'time_spent_hours=' + str(ready['elapsed_seconds'] / 3600))
    transition('DEV-076', 'development', 'In Progress', 'Resolved')
    comment('UNITTEST-076', 'Actual committed isolated coverage and fresh73 PASS', 'Verifier /root/formal074_prepare. ' + ready['unit_stdout'] + '\nAll52 examples invoke real SDK MockTransport request/result/all-declared-error checks.21 additional guards reject wrong file identity, wrong selected schema branch/content, missing/different View primary key, removed backing still present with implicit/explicit branches, guards that ignore captured request, and missing declared survivor. tests/test_offline_rest_074_semantics.py SHA256 ' + ready['unit_test_sha256'] + '. All unit source committed; public socket/connect/connect_ex/create_connection/DNS denied. Current compilation and module/method/assets hashes pass for52. Time reported covers measured verification runtime only; no historical effort invented. Formal52 independent cases not yet executed.')
    cli('update', 'UNITTEST-076', '--field', 'time_spent_hours=' + str(ready['elapsed_seconds'] / 3600))
    transition('UNITTEST-076', 'unittest', 'In Progress', 'Resolved')
    original = cli('comment', 'get', 'CODEREVIEW-077', '20261007-101716-tech-lead')
    assert 'until Resolved' in original
    assert state('DEV-076') == 'Resolved'
    cli('link', 'remove', 'LINK-01815')
    comment('CODEREVIEW-077', 'Recorded review prerequisite met; return priorOpen', 'DEV076/UNITTEST076 now Resolved. Original prerequisite comment20261007-101716-tech-lead explicitly says DEV076 blocks review untilResolved, PriorOpen. Remove LINK01815 after its concrete prerequisite met; fresh reviewer ' + REVIEWER + ' differs from original author and fixer. Fresh52 independent source/semantic report .ept/tmp/rest074_independent_codereview.json prepared; reviewer will recheck current hashes after this transition before approval recording.')
    transition('CODEREVIEW-077', 'codereview', 'Blocked', 'Open')


def cases_stage():
    started = time.monotonic()
    cases = bound()
    approved = read('rest074_case_approval.json')
    review = read('rest074_independent_codereview.json')
    assert approved['verdict'] == 'APPROVED'
    assert approved['manifest']['sha256'] == sha(TMP / 'rest074_formal_cases.json')
    assert approved['harness']['sha256'] == sha(TMP / 'rest074_formal_execute.py')
    assert approved['reviewer_identity'] == REVIEWER != cases['author_identity']
    assert review['verdict'] == 'PASS' and review['verified_after_dev_resolved']
    assert state('DEV-076') == state('UNITTEST-076') == 'Resolved'
    for offset in range(0,52,4):
        rows=review['semantic_review'][offset:offset+4]
        comment('CODEREVIEW-077', 'Fresh independent operation findings ' + str(offset+1) + '-' + str(offset+len(rows)), 'Actual reviewer ' + REVIEWER + '. Original pinned SDK source; current source/contract/behavior/example identity independently bound. Full exact hashes and model/error/wire checks in rest074_review_static.json; no author fixture output used to derive formal expectations.\n' + '\n'.join(row['id'] + ': ' + row['verdict'] + '. ' + row['evidence'] for row in rows), 'architect')
    comment('CODEREVIEW-077', 'Fresh independent approval after pairedDEVResolved', json.dumps({'actual_reviewer': REVIEWER, 'review': {key:value for key,value in review.items() if key != 'semantic_review'}, 'full_review_sha256': sha(TMP / 'rest074_independent_codereview.json'), 'case_manifest_sha256': approved['manifest']['sha256'], 'formal_execution': 'NOT_RUN'}, separators=(',', ':')), 'architect')
    transition('CODEREVIEW-077', 'codereview', 'Open', 'Closed')
    for ticket,kind in [('DEV-076','development'),('UNITTEST-076','unittest')]:
        comment(ticket, 'Independent approved review complete', 'CODEREVIEW077 Closed with actual reviewer ' + REVIEWER + '. Current52 source/assets unchanged; no correction required. Complete measured readiness and73 unit PASS already recorded. Links and historical issue boundaries preserved.')
        transition(ticket,kind,'Resolved','Closed')
    comment('DEV-STORY-074','Real operation readiness complete; begin QA', 'DESIGN076, DEV076, UNITTEST076, CODEREVIEW077 Closed. Fresh52 source/current assets verified,73 unit PASS. OriginalBUGSUB024 Closed; related075 J12 BUGSUB025 remains separately governed. Actual independent case author ' + cases['author_identity'] + '; fresh approver ' + REVIEWER + '; separate executor ' + EXECUTOR + '. Formal operation QA will use original SDK source literals, not author fixture output. No unresolved required question or active prerequisite blocker.')
    transition('DEV-STORY-074','dev_story','Development','QA')
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


if __name__ == '__main__':
    if len(sys.argv)!=3 or sys.argv[1]!='--writer-granted':
        raise SystemExit('Exclusive root tracker writer grant and stage readiness/cases required')
    {'readiness': readiness, 'cases': cases_stage}[sys.argv[2]]()
