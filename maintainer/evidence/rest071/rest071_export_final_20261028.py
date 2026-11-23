"""Export closed tracker evidence and a durable-ready REST071 acceptance package."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

TMP = Path(__file__).resolve().parent
ROOT = TMP.parents[1]
CLI = ROOT / '.ept/tools/tracker/tracker_cli.py'
transcript = []
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def run(*args):
    proc = subprocess.run([sys.executable, str(CLI), *args], cwd=ROOT, text=True, encoding='utf-8',
        capture_output=True, env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    transcript.append({'args': list(args), 'exit_code': proc.returncode, 'stdout': proc.stdout, 'stderr': proc.stderr})
    (TMP / 'rest071_final_export_cli_20261028.json').write_text(json.dumps(transcript, indent=2) + '\n', encoding='utf-8')
    if proc.returncode:
        raise RuntimeError(proc.stdout + proc.stderr)
    return proc.stdout

tickets = ('DEV-STORY-071', 'DESIGN-074', 'DEV-074', 'UNITTEST-074', 'CODEREVIEW-075', 'TESTCASE-074',
    'TESTEXEC-074', 'BUG-SUB-027', 'BUG-SUB-028')
exported = []
for ticket in tickets:
    listing = run('comment', 'list', ticket, '--author', 'project-manager')
    ids = re.findall(r'^(\d{8}-\d{6}-\S+)\s', listing, re.M)
    comments = []
    for identity in ids:
        comments.append({'comment_id': identity, 'output': run('comment', 'get', ticket, identity, '--author', 'project-manager')})
    value = {'ticket': ticket, 'comment_count': len(comments), 'listing': listing, 'comments': comments}
    path = TMP / (ticket + '-comments-20261028.json')
    path.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')
    exported.append(path)

closure = json.loads((TMP / 'rest071_recovered_closure_cli_20261028.json').read_bytes())
proof = json.loads((TMP / 'feature015_rest071_recovered_formal_qa_20261028.json').read_bytes())
initial_inventory = json.loads((TMP / 'rest071_recovered_inventory_20261028.json').read_bytes())
assert closure['writer_done'] is True
assert closure['closure']['DEV-STORY-071']['status'] == 'Deployment'
names = {Path(row['path']).name for row in initial_inventory['files']}
names.update(path.name for path in exported)
names.update(['rest071_recover_verify_20261028.py', 'rest071_recovered_close_20261028.py',
    'rest071_export_final_20261028.py', 'rest071_final_export_cli_20261028.json',
    'rest071_recovered_closure_cli_20261028.json', 'feature015_rest071_recovered_formal_qa_20261028.json',
    'rest071_recovered_inventory_20261028.json', 'rest071_source_build_cases.py', 'rest071_fresh_review_report.py'])
names.update(Path(row['path']).name for row in closure['closure'].values())
for pattern in ('rest071_initial_*', 'rest071_20261027_before_*'):
    names.update(path.name for path in TMP.glob(pattern) if path.is_file())
files = []
for name in sorted(names):
    path = TMP / name
    assert path.is_file(), name
    files.append({'path': str(path.relative_to(ROOT)).replace('\\', '/'), 'bytes': path.stat().st_size, 'sha256': sha(path)})
inventory = {'recorder': '/root/rest071_closure_recover_20261028', 'files': files,
    'scope': 'Original raw execution, approved cases and harness, independent reviews, preserved earlier authoring attempts, serialized closure CLI and full current ticket comments. No test was rerun during recovery.'}
inventory_path = TMP / 'rest071_archive_inventory_20261028.json'
inventory_path.write_text(json.dumps(inventory, indent=2) + '\n', encoding='utf-8')
report = dict(proof)
report.update({'formal_execution': 'PASS', 'formal_workflow_acceptance': 'accepted',
    'recorder_identity': '/root/rest071_closure_recover_20261028',
    'recorded_at_utc': datetime.now(timezone.utc).isoformat(),
    'closure': closure['closure'],
    'closure_cli_sha256': sha(TMP / 'rest071_recovered_closure_cli_20261028.json'),
    'full_comment_exports': [{'path': str(path.relative_to(ROOT)).replace('\\', '/'), 'sha256': sha(path)} for path in exported],
    'archive_inventory': {'path': str(inventory_path.relative_to(ROOT)).replace('\\', '/'), 'sha256': sha(inventory_path)},
    'bug_closure': {'BUG-SUB-027': 'Closed/Done after policy replacement regression and F071-14 formal PASS',
        'BUG-SUB-028': 'Closed/Done after batch identity regressions and F071-04/F071-19 formal PASS'},
    'live_links_changed_in_recovery': [],
    'limits': ['Original independent executor and raw results are preserved; this agent recovered proof and recorded workflow outcomes.',
        'Offline SDK1.101.0 synthetic responses with public sockets/DNS denied; no live Foundry tenant claim.',
        'DEV-STORY-071 reached Deployment automatically; final integrated REST093 acceptance, publication070, GitHub/main and parent pins are separate gates.']})
target = TMP / 'feature015_rest071_formal_qa.json'
if target.exists():
    raise RuntimeError('Refusing to replace an existing formal QA report')
target.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'report': str(target), 'report_sha256': sha(target), 'inventory': str(inventory_path),
    'inventory_sha256': sha(inventory_path), 'files': len(files), 'comment_count': sum(json.loads(path.read_bytes())['comment_count'] for path in exported)}))
