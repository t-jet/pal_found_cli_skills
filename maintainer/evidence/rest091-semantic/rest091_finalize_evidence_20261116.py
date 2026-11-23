import hashlib
import json
import subprocess
from pathlib import Path

tmp = Path(__file__).resolve().parent
sha = lambda path: hashlib.sha256(Path(path).read_bytes()).hexdigest()
report_path = tmp / 'feature015_rest091_semantic_final_retest_20261116.json'
report = json.loads(report_path.read_text())
freeze_path = tmp / 'feature015_rest091_correction_manifest_second_20261029.json'
freeze = json.loads(freeze_path.read_text())
root = Path(freeze['worktree'])
assert report['counts'] == {'PASS':29}
assert all(sha(root / row['path']) == row['sha256'] for row in freeze['changed_files'])
assert all(sha(path) == digest for path,digest in freeze['source_bindings'].items())
status = subprocess.check_output(['git','-C',str(root),'status','--porcelain'], text=True).splitlines()
assert len(status) == 11
execution_path = tmp / 'rest091_final_execution_20261116.json'
execution = {
    'reviewer':'/root/rest091_final_retest_20261116',
    'runtime':{'foundry-platform-sdk':'1.101.0','httpx':'0.28.1'},
    'pytest':{'command':'python -B -m pytest tests/test_offline_rest_091.py -q -p no:cacheprovider -o addopts= --basetemp=<workspace>/.ept/tmp/rest091_final_pytest_20261116','exit_code':0,'result':'66 passed in 0.48s'},
    'candidate_post_pytest':{'frozen_file_hashes_match':True,'source_hashes_match':True,'dirty_files':status},
    'raw_artifact_boundary':'Raw report preserves reused first-review reason labels (22 PASS/7 FAIL). Final report applies independently checked correction predicates and is authoritative for final 29 PASS verdicts.',
    'boundaries':['No tracker writes, author edits, register edits, commit, push or promotion.','SDK MockTransport with DNS/socket/native HTTP negative probes. No live Foundry authorization or behavior claims.']
}
execution_path.write_text(json.dumps(execution,indent=2),encoding='utf-8')
manifest_path = tmp / 'feature015_rest091_semantic_final_retest_20261116_manifest.json'
manifest = json.loads(manifest_path.read_text())
paths = [freeze_path, execution_path, Path(__file__), tmp/'build_rest091_final_retest_20261116.py', tmp/'feature015_rest091_semantic_retest_20261029.json', tmp/'feature015_rest091_semantic_review_20261029.json', tmp/'feature015_rest091_semantic_review_20261029_rejected_harness_enum.json', tmp/'rest091_independent_semantics_20261029.py', tmp/'rest091_independent_retest_20261029.py', tmp/'rest091_retest_official_manifest_20261029.ts', tmp/'rest091_retest_official_builder_20261029.ts']
manifest['artifacts'].update({str(path):sha(path) for path in paths})
manifest_path.write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'report_sha256':sha(report_path),'proof_sha256':sha(tmp/'rest091_independent_final_retest_20261116.py'),'raw_sha256':sha(tmp/'rest091_final_retest_raw_20261116.json'),'manifest_sha256':sha(manifest_path),'freeze_sha256':sha(freeze_path),'execution_sha256':sha(execution_path),'counts':report['counts'],'model_counts':report['model_counts'],'sdk_requests':report['network']['sdk_requests'],'semantic_checks':sum(len(row['semantic_checks']) for row in report['operations'])}))
