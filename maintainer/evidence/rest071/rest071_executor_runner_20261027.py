"""Capture immutable evidence for one coordinator-authorized formal execution."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone

TMP = Path(__file__).resolve().parent
ROOT = TMP.parent.parent
IDENTITY = '/root/rest071_execute_20261027'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--coordinator-confirmed', required=True)
    args = parser.parse_args()
    assert args.coordinator_confirmed == 'TESTCASE-074 Closed; TESTEXEC-074 InProgress; ready'
    harness = TMP / 'rest071_formal_execute.py'
    cases = TMP / 'rest071_formal_cases.json'
    approval_path = TMP / 'rest071_case_approval.json'
    approval = json.loads(approval_path.read_text(encoding='utf-8'))
    assert approval['verdict'] == 'APPROVED'
    assert approval['manifest']['sha256'] == sha(cases)
    assert approval['harness']['sha256'] == sha(harness)
    manifest = json.loads(cases.read_text(encoding='utf-8'))
    assert IDENTITY not in (manifest['author_identity'], approval['reviewer_identity'])
    bound = {}
    skill = TMP / 'feature015_integration/.agents/skills/pal-found-dev'
    for case in manifest['operations']:
        for source in [case['source'], *case['assets'].values()]:
            path = Path(source['path']) if source is case['source'] else skill / source['path']
            actual = sha(path)
            assert actual == source['sha256'], str(path)
            bound[str(path)] = actual
        for error in case['errors']:
            path = Path(error['error_source'])
            actual = sha(path)
            assert actual == error['error_source_sha256'], str(path)
            bound[str(path)] = actual
    attempt = 1
    while list(TMP.glob(f'rest071_executor_attempt{attempt}_*')):
        attempt += 1
    prefix = TMP / f'rest071_executor_attempt{attempt}'
    snapshot = {}
    for path in (harness, cases, approval_path, TMP / 'rest071_readiness.json'):
        dest = Path(str(prefix) + '_' + path.name)
        with dest.open('xb') as out:
            out.write(path.read_bytes())
        snapshot[str(dest)] = sha(dest)
    command = [sys.executable, str(harness), '--execute', '--executor-identity', IDENTITY,
               '--testcase-closed', 'TESTCASE-074', '--approved-cases-sha256', sha(cases),
               '--readiness-confirmed']
    start = datetime.now(timezone.utc).isoformat()
    clock = time.monotonic()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', TMP=str(TMP), TEMP=str(TMP))
    stdout_path = Path(str(prefix) + '_stdout.log')
    stderr_path = Path(str(prefix) + '_stderr.log')
    with stdout_path.open('xb') as stdout, stderr_path.open('xb') as stderr:
        run = subprocess.run(command, cwd=ROOT, env=env, stdout=stdout, stderr=stderr)
    elapsed = time.monotonic() - clock
    end = datetime.now(timezone.utc).isoformat()
    outputs = {}
    for name in ('rest071_formal_execution.json', 'rest071_formal_execute.log'):
        src = TMP / name
        if src.exists():
            dest = Path(str(prefix) + '_' + name)
            with dest.open('xb') as out:
                out.write(src.read_bytes())
            outputs[str(dest)] = sha(dest)
    for path in (stdout_path, stderr_path):
        outputs[str(path)] = sha(path)
    unchanged = all(sha(path) == expected for path, expected in bound.items())
    report = dict(executor_identity=IDENTITY, attempt=attempt, command=command,
                  coordinator_confirmation=args.coordinator_confirmed, started_at=start,
                  finished_at=end, elapsed_seconds=elapsed, exit_code=run.returncode,
                  cases_sha256=sha(cases), harness_sha256=sha(harness),
                  sdk_assets_binding=bound, bindings_unchanged_after_run=unchanged,
                  snapshots=snapshot, outputs=outputs)
    dest = Path(str(prefix) + '_runner.json')
    with dest.open('x', encoding='utf-8') as out:
        json.dump(report, out, indent=2)
        out.write('\n')
    shutil.copyfile(dest, TMP / 'rest071_formal_runner.json')
    print(json.dumps(dict(attempt=attempt, exit_code=run.returncode,
                         elapsed_seconds=elapsed, runner=str(dest),
                         bindings_unchanged_after_run=unchanged)))
    raise SystemExit(run.returncode or (0 if unchanged else 1))


if __name__ == '__main__':
    main()
