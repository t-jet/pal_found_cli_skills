"""Record independent review of current candidate assets."""
import datetime
import hashlib
import json
import subprocess
from pathlib import Path

evidence = Path('.ept/tmp/rest074_review_static.json')
static = json.loads(evidence.read_text())
assert static['count'] == 52 and not static['failed_checks']
notes = {
    'Branch': 'Create/get identities match selected branch. Delete has no result body. List/history are terminal synthetic pages; history status does not claim current branch head or establish sort order.',
    'Dataset': 'Create/get retain dataset and parent identities. Explicit schema branch selectors match returned branch. CSV request has one returned data row within limit 2. Empty health-report and schema-batch maps are allowed and make no all-healthy or all-present claim. Jobs use explicit ascending sort. Schema payloads and Any limitations remain explicit.',
    'File': 'Get/upload metadata path equals actual requested path. v1 upload path comes from filePath query; other corrected paths come from URL. Read/content return opaque bytes. Delete has no body. Branch master is explicit; historical selectors are omitted in bounded examples. List has no prefix filter.',
    'Transaction': 'Get/abort/commit RID equals requested transaction. State is OPEN/ABORTED/COMMITTED respectively. v2 create requests APPEND; v1 does not claim optional type default. Build/job examples cover associated resources only. No persisted files, branch transition or rollback effect is demonstrated.',
    'View': 'Add/replace/create composition agrees with request. Add-primary-key response includes exact requested columns and resolution. Removal compares dataset-plus-effective-branch identities using actual serialized request; omitted backing branch inherits selected view branch master. Distinct survivor ...0003 remains; removed ...0002 is absent. Snapshot on next update is documented; transport example establishes no server transaction effects.'
}
report = {
    'story': 'DEV-STORY-074',
    'reviewer_identity': '/root/formal074_prepare/independent_review',
    'review_role': 'Fresh independent code and semantic reviewer',
    'candidate_sha': subprocess.check_output(['git','-C','.ept/tmp/feature015_integration','rev-parse','HEAD'],text=True).strip(),
    'completed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'verdict': 'PASS',
    'scope': 'Current 52 datasets contracts, behaviors and offline examples against pinned SDK 1.101.0 original source. This is code review, not formal TESTEXEC.',
    'static_evidence': {'path': str(evidence), 'sha256': hashlib.sha256(evidence.read_bytes()).hexdigest()},
    'counts': {'operations':52,'failed_source_asset_model_checks':0,'named_errors':sum(len(r['errors']) for r in static['operations'])},
    'method': 'Read current request/result literals and original SDK descriptions for all 52. Independently parse original method AST and evaluate RequestInfo expressions using invocation arguments, with defaults from original signature. Validate response and named-error parameter schemas using original SDK types. Bind every source and asset hash. No author fixture execution or formal harness execution performed.',
    'semantic_review': [{'id': r['id'], 'verdict':'PASS','evidence':notes[r['id'].split('.')[2]]} for r in static['operations']],
    'corrected_guard_review': ['Four File get/upload checks derive path from actual serialized URL/query.', 'Two schema checks derive branch from serialized query/body; put_schema also checks returned complete schema.', 'add_primary_key checks complete requested primaryKey from serialized body.', 'remove_backing_datasets normalizes omitted branch against body branch and permits unrelated surviving backings.'],
    'regression_test_review': {'path':'tests/test_offline_rest_074_semantics.py','purpose':'52 fixtures plus 21 negative/request-relation/survivor cases. Guards mutate response identities, primary-key columns/resolution, returned schema and actual serialized selector. Different backing survives without forcing empty composition.','execution':'Owned by coordinator; not executed by this reviewer.'},
    'historical_evidence': 'maintainer/rest-qa-074.json records prior reviewer work and eight failures. No historical execution is claimed as this reviewer\'s work.',
    'findings': [],
    'limits': ['Offline scope only. Tenant grants, permissions and live mutations untested.', 'No claim of actual persistence, rollback, branch movement, uniqueness verification, server graph validity or recovery execution.', 'Terminal authored pages do not demonstrate continuation. Formal independent manifest adds bounded continuation separately.', 'Formal CASE approval and TESTEXEC acceptance are separate records.']
}
Path('.ept/tmp/rest074_independent_codereview.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report['counts']))
