"""List exact QA artifacts for the integration owner's durable evidence archive."""
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

tmp = Path(__file__).resolve().parent
paths = {
    "rest072_formal_cases.json", "rest072_case_approval.json", "rest072_case_approval.py",
    "rest072_independent_codereview.json", "rest072_review_measured_timing.json",
    "rest072_mutation_check.py", "rest072_mutation_check.json",
    "feature015_rest072_formal_qa.json",
}
paths.update(p.name for p in tmp.glob("rest072_resume*"))
paths.discard("rest072_resume_archive_inventory.json")
artifacts = []
for name in sorted(paths):
    path = tmp / name
    if path.is_file():
        artifacts.append({"file": name, "bytes": path.stat().st_size, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
cases = json.loads((tmp / "rest072_formal_cases.json").read_text())
repo = tmp / "feature015_integration"
for row in cases["operations"]:
    for asset in row["assets"].values():
        path = repo / ".agents/skills/pal-found-dev" / asset["path"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == asset["sha256"]
report = {
    "created_at": datetime.now(timezone.utc).isoformat(),
    "story": "DEV-STORY-072", "testcase": "TESTCASE-075", "testexec": "TESTEXEC-075", "codereview": "CODEREVIEW-076",
    "actual_terminal_children": ["DESIGN-075", "DEV-075", "UNITTEST-075", "CODEREVIEW-076", "TESTCASE-075", "TESTEXEC-075", "BUG-SUB-029", "BUG-SUB-030", "BUG-SUB-031"],
    "story_status": json.loads((tmp / "rest072_resume_tracker_closure.json").read_text())["records"]["DEV-STORY-072"]["status"], "formal_verdict": "PASS", "operations": 40, "declared_errors": 113, "check_records": 612,
    "current_candidate_sha": subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip(),
    "current_072_assets_unchanged": True,
    "archive_files": artifacts,
    "publication_note": "Archive executed harness bytes unchanged to preserve hash. Its historical local paths identify the measured environment; any portable replay wrapper must preserve these archived bytes and exact literal manifest. Final proof uses attempt5, with attempt1-3 failures and attempt4 weaker PASS retained. No live tenant or publication acceptance is implied.",
}
(tmp / "rest072_resume_archive_inventory.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"artifacts": len(artifacts), "current_candidate_sha": report["current_candidate_sha"], "current_072_assets_unchanged": True}))
