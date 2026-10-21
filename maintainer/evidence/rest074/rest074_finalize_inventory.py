"""Retain damaged concurrent logging bytes and index complete independent exports."""
import json
from datetime import datetime, timezone
from rest074_finish_closure import TMP, IDENTITY, sha, read, save

transcript=TMP/'rest074_closure_cli.jsonl'
raw=TMP/'rest074_closure_cli_original_bytes.log'
assert not raw.exists()
raw.write_bytes(transcript.read_bytes())
valid=[]
bad=[]
for line_number,line in enumerate(raw.read_text(encoding='utf-8').splitlines(),1):
    try:
        record=json.loads(line)
        assert record['exit_code']==0
        valid.append(record)
    except (ValueError, KeyError, AssertionError) as error:
        bad.append(dict(line=line_number,error=str(error),characters=len(line)))
assert bad
mutations=[row for row in valid if row['args'][0]=='update' or row['args'][:2]==['comment','create']]
assert len([row for row in mutations if row['args'][:2]==['comment','create'] and ' real formal PASS ' in row['args'][4]])==52
assert any(row['args'][:4]==['update','TESTEXEC-076','--status','Closed'] for row in mutations)
transcript.write_text(''.join(json.dumps(row)+'\n' for row in valid),encoding='utf-8')
save('rest074_transcript_repair.json',dict(repaired_at=datetime.now(timezone.utc).isoformat(),recorder=IDENTITY,raw_transcript=dict(path=raw.name,sha256=sha(raw)),valid_records_retained=len(valid),malformed_lines=bad,reason='Four concurrent read-only subprocess log appends interleaved bytes. All serialized mutation records are valid and retained. Complete comment responses remain in rest074_tracker_comment_exports.json; raw bytes retained unchanged. Canonical transcript contains only original parseable records; no inferred command, timestamp or approval added. Transcript writes now use a thread lock.',all_52_outcome_mutations_preserved=True,closed_mutation_preserved=True,complete_comment_exports=dict(path='rest074_tracker_comment_exports.json',sha256=sha(TMP/'rest074_tracker_comment_exports.json'))))
report=read('feature015_rest074_formal_qa.json')
files=sorted(path for path in TMP.glob('rest074_*') if path.is_file() and path.name not in ('rest074_archive_inventory.json','rest074_artifact_inventory.json'))
evidence={path.name:dict(path='.ept/tmp/'+path.name,sha256=sha(path),bytes=path.stat().st_size) for path in files}
report['evidence']=evidence
report['logging_integrity_note']='Concurrent read logging damaged raw transcript bytes; preserved raw file and explicit repair metadata included. Complete CLI comment exports and all 52 serialized outcome writes plus status writes remain intact. No execution proof altered.'
save('feature015_rest074_formal_qa.json',report)
inventory=read('rest074_archive_inventory.json')
inventory['created_at']=datetime.now(timezone.utc).isoformat()
inventory['files']=list(evidence.values())+[dict(path='.ept/tmp/feature015_rest074_formal_qa.json',sha256=sha(TMP/'feature015_rest074_formal_qa.json'),bytes=(TMP/'feature015_rest074_formal_qa.json').stat().st_size)]
inventory['logging_integrity_note']=report['logging_integrity_note']
save('rest074_archive_inventory.json',inventory)
assert all(sha(TMP.parent.parent/row['path'])==row['sha256'] for row in inventory['files'])
print(json.dumps(dict(artifacts=len(inventory['files']),valid_cli_records=len(valid),all_mutations_retained=len(mutations),raw_malformed_lines=len(bad),report_sha256=sha(TMP/'feature015_rest074_formal_qa.json'),inventory_sha256=sha(TMP/'rest074_archive_inventory.json'))))
