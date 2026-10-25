"""Capture actual formal execution timing, environment and process result."""
import hashlib
import importlib.metadata
import json
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
harness = root / 'rest072_resume_formal_execute.py'
manifest = root / 'rest072_formal_cases.json'
case_hash = hashlib.sha256(manifest.read_bytes()).hexdigest()
assert case_hash == '99cf3b938c7b7525bde7b9ffab42607128d1ca6e18cee183ee38e464bcc9d62c'
args = [sys.executable, str(harness), '--execute', '--testcase-closed', 'TESTCASE-075',
        '--approved-cases-sha256', case_hash, '--readiness-confirmed']
started_at = datetime.now(timezone.utc).isoformat()
started = time.perf_counter()
with (root / 'rest072_resume_formal_stdout.log').open('w', encoding='utf-8') as stdout, \
     (root / 'rest072_resume_formal_stderr.log').open('w', encoding='utf-8') as stderr:
    result = subprocess.run(args, stdout=stdout, stderr=stderr, check=False)
elapsed = time.perf_counter() - started
report = dict(executor_identity='/root/formal072_resume/independent072', command=args,
              started_at=started_at, completed_at=datetime.now(timezone.utc).isoformat(),
              elapsed_seconds=elapsed, exit_code=result.returncode,
              python=sys.version, platform=platform.platform(),
              packages={name: importlib.metadata.version(name) for name in
                        ('foundry-platform-sdk', 'httpx', 'pydantic')},
              harness_sha256=hashlib.sha256(harness.read_bytes()).hexdigest(),
              cases_sha256=case_hash)
(root / 'rest072_resume_formal_runner.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report))
raise SystemExit(result.returncode)
