"""Verify the resumed candidate without changing tracker state or source assets."""
import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

tmp = Path(__file__).resolve().parent
repo = tmp / "feature015_integration"
skill = repo / ".agents/skills/pal-found-dev"
started = datetime.now(timezone.utc)
clock = time.monotonic()
cases = json.loads((tmp / "rest072_formal_cases.json").read_text())
approval = json.loads((tmp / "rest072_case_approval.json").read_text())
case_hash = hashlib.sha256((tmp / "rest072_formal_cases.json").read_bytes()).hexdigest()
assert case_hash == approval["case_manifest_sha256"]
compiled = []
for case in cases["operations"]:
    for asset in case["assets"].values():
        path = skill / asset["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == asset["sha256"], path
        if path.suffix == ".py":
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
            compiled.append({"operation": case["operation"], **asset})
assert len(compiled) == 40
test = repo / "tests/test_offline_rest_072.py"
subprocess.run(["git", "-C", str(repo), "ls-files", "--error-unmatch", str(test.relative_to(repo))], check=True, capture_output=True)
report = {
    "agent": "/root/formal072_resume",
    "candidate_commit": subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip(),
    "started_at": started.isoformat(),
    "finished_at": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": time.monotonic() - clock,
    "activity": "Current source asset identities and example compilation; excludes historical author effort.",
    "case_manifest_sha256": case_hash,
    "compiled": compiled,
    "dedicated_test_sha256": hashlib.sha256(test.read_bytes()).hexdigest(),
    "result": "PASS",
}
(tmp / "rest072_resume_readiness.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({key: report[key] for key in ("candidate_commit", "elapsed_seconds", "result")}))
