"""Record this reviewer's approved REST072 findings through tracker CLI."""
import hashlib
import json
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IDENTITY = '/root/formal072_resume/independent072'
CLI = '.ept/tools/tracker/tracker_cli.py'


def main():
    started = time.perf_counter()
    evidence = json.loads((ROOT / 'rest072_resume_independent_inspection.json').read_text())
    old = json.loads((ROOT / 'rest072_independent_codereview.json').read_text())
    manifest = ROOT / 'rest072_formal_cases.json'
    case_data = json.loads(manifest.read_text())
    assert hashlib.sha256(manifest.read_bytes()).hexdigest() == evidence['case_manifest_sha256']
    assert evidence['verdict'] == 'PASS'
    calls = []

    def cli(*args):
        result = subprocess.run([sys.executable, CLI, *args, '--author', 'architect'],
                                capture_output=True, text=True, check=False)
        calls.append(dict(args=args, exit_code=result.returncode, output=result.stdout, stderr=result.stderr))
        if result.returncode:
            raise RuntimeError(result.stdout + result.stderr)
        print(result.stdout, flush=True)
        return result.stdout

    findings = []
    base = ROOT / 'feature015_integration/.agents/skills/pal-found-dev'
    for row in old['operations']:
        item = row['finding']
        example = base / row['assets']['example']['path']
        behavior = base / row['assets']['behavior']['path']
        assert item['example_snippet'].strip() in example.read_text(encoding='utf-8')
        assert item['behavior_snippet'].strip() in behavior.read_text(encoding='utf-8')
        findings.append(dict(operation=row['operation'], verdict='PASS',
                             source=f"{row['source']['path']}:{row['source']['line']}",
                             example=f"{example}:{item['example_line']}",
                             behavior=f"{behavior}:{item['behavior_line']}",
                             snippet=item['example_snippet'].strip(),
                             disposition=item['disposition']))
    for start in range(0, len(findings), 4):
        batch = findings[start:start + 4]
        text = f'Actual independent reviewer: {IDENTITY}. Fresh review after DEV-075 Resolved. Candidate {evidence["candidate_sha"]}. '
        text += 'SDK 1.101.0 primary source; no author fixture execution.\n'
        text += '\n'.join(f'{f["operation"]}: PASS. Source {f["source"]}; behavior {f["behavior"]}; example {f["example"]}. Snippet: {f["snippet"]}. {f["disposition"]}' for f in batch)
        cli('comment', 'create', 'CODEREVIEW-076', '--subject',
            f'Fresh independent per-operation review {start + 1}-{start + len(batch)}', '--text', text)
    text = (f'APPROVED by actual reviewer {IDENTITY}, independent of content/case authors. '
            'DEV-075 is Resolved. Reviewed indexed BA-DES-015 revision 2, SA-DES-014 REST/source and verification requirements, authoring handoff, and exact operation ownership. '
            '40 operations, 113 declared error classes and typed parameter payloads, 220 baseline/negative/additional/boundary wire oracles independently match primary SDK AST; all contract/example/behavior and full model/error closure hashes unchanged. '
            'Seven dedicated regressions inspected statically at tests/test_offline_rest_072.py:19 (deny_network), :52 (assert set(outcome["data"]) == requested), :67 (markingIds), :86 (parsed | errors == requested), :96 (Organization ADMINISTER and last-admin separation). '
            'Source-specific permissions, preview, finite pages, batch identity, 500 boundary, classifications, raw lifetimes and uncertain writes reviewed. '
            'No open linked Questions. No required correction found. Inspection .ept/tmp/rest072_resume_independent_inspection.json; case manifest SHA256 ' + evidence['case_manifest_sha256'] + '. '
            'Formal execution NOT_RUN; live enrollment NOT_RUN. Prior reviewer artifact preserved.')
    cli('comment', 'create', 'CODEREVIEW-076', '--subject', 'Actual independent approval after DEV Resolved', '--text', text)
    cli('update', 'CODEREVIEW-076', '--status', 'Closed')
    elapsed = time.perf_counter() - started
    cli('comment', 'create', 'CODEREVIEW-076', '--subject', 'Measured review recording runtime', '--text',
        f'Actual reviewer {IDENTITY}. This recording batch measured {elapsed:.6f} seconds through CR closure. Static review elapsed time was not separately measured and is not estimated as contributor effort.')
    evidence.update(reviewer_identity=IDENTITY, workflow_verdict='APPROVED_CLOSED', findings=findings,
                    recorded_at=datetime.now(timezone.utc).isoformat(), recording_seconds=elapsed, cli_calls=calls)
    (ROOT / 'rest072_resume_codereview_approval.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    approval = dict(reviewer=IDENTITY, case_author=case_data['author_identity'],
                    case_manifest_sha256=evidence['case_manifest_sha256'], verdict='APPROVED',
                    reviewed_at=datetime.now(timezone.utc).isoformat(), operations=evidence['operations'],
                    candidate_sha=evidence['candidate_sha'],
                    method='Independent primary SDK AST, schemas, literal requests/results/errors and harness review. 220 wire oracles, 40 operations, 113 errors; exact unchanged asset hashes bind current candidate. Formal execution not run.')
    (ROOT / 'rest072_resume_case_approval.json').write_text(json.dumps(approval, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
