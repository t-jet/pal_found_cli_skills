import hashlib
import json
from pathlib import Path
import subprocess
import zipfile

base = Path(__file__).resolve().parent / 'rest079_acceptance_20261118'
repo = base / 'skills'
summary = json.loads((base / 'proposal_summary.json').read_text())
sha = lambda data: hashlib.sha256(data).hexdigest()
for key in ('canonical', 'acceptance', 'archive', 'inventory', 'metadata_validation'):
    item = summary[key]
    assert sha((repo / item['path']).read_bytes()) == item['sha256'], key
inventory = json.loads((repo / summary['inventory']['path']).read_text())
with zipfile.ZipFile(repo / summary['archive']['path']) as archive:
    names = archive.namelist()
    assert len(names) == len(set(names)) == 9119
    assert len(inventory['entries']) == 9118
    for item in inventory['entries']:
        body = archive.read(item['member'])
        assert sha(body) == item['sha256']
        assert len(body) == item['bytes']
relative = 'maintainer/rest-domain-authoring-register.json'
old = json.loads(subprocess.check_output(['git', '-C', str(repo), 'show', '51f594c:'+relative]))
new = json.loads((repo / relative).read_text())
before = {row['id']: row for row in old['operations']}
after = {row['id']: row for row in new['operations']}
assert before.keys() == after.keys()
changed = []
for key, row in after.items():
    if row == before[key]:
        continue
    fields = {field for field in row.keys() | before[key].keys() if row.get(field) != before[key].get(field)}
    assert fields == {'independent_qa_status', 'independent_qa_agent'}
    assert before[key]['independent_qa_status'] == 'pending'
    assert row['independent_qa_status'] == 'accepted'
    assert row['independent_qa_agent'] == '/root/rest079_distinct_formal_executor_20261118'
    changed.append(key)
assert len(changed) == 32
assert {k:v for k,v in old.items() if k != 'operations'} == {k:v for k,v in new.items() if k != 'operations'}
assert sum(r['independent_qa_status'] == 'accepted' for r in new['operations']) == 261
assert all(r['semantic_review_status'] == 'accepted' for r in new['operations'])
binding = json.loads((repo/'maintainer/evidence/rest079/independent_binding_review.json').read_text())
assert binding['all_bindings_current_and_unchanged'] is False
assert binding['relevant_domain_bindings_current'] is True
assert len(binding['current_reader_differences']) == 2
assert all('/third_party_applications/' in r['path'] for r in binding['current_reader_differences'])
result = {'outcome':'ROOT_METADATA_REVIEW_PASS', 'base':'51f594c08403ac49d848e0d8c4af9986377f64d2', 'archive_payload_hashes_verified':9118, 'changed_qa_rows':32, 'non_target_rows_preserved':393, 'formal_proposed':261, 'formal_pending':164, 'whole_bundle_execution_claim':False, 'formal_reruns':0, 'publication_approval':False}
(base/'root_metadata_review.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
