"""Export public tracker CLI status evidence without reading tracker storage."""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

tmp = Path(__file__).resolve().parent
cli = tmp.parent.parent / ".ept/tools/tracker/tracker_cli.py"
ids = ["DEV-STORY-072", "DESIGN-075", "DEV-075", "UNITTEST-075", "CODEREVIEW-076", "TESTCASE-075", "TESTEXEC-075", "BUG-SUB-029", "BUG-SUB-030", "BUG-SUB-031"]
records = {}
for ticket in ids:
    result = subprocess.run([sys.executable, str(cli), "get", ticket, "--author", "project-manager"], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    status = next(line.split(": ", 1)[1] for line in result.stdout.splitlines() if line.startswith("current_status:"))
    assert status in (("QA", "Deployment") if ticket == "DEV-STORY-072" else ("Closed",))
    records[ticket] = {"status": status, "cli_exit_code": result.returncode, "cli_get_output": result.stdout}
for ticket in ("CODEREVIEW-076", "TESTCASE-075", "TESTEXEC-075"):
    result = subprocess.run([sys.executable, str(cli), "comment", "list", ticket, "--author", "project-manager"], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    records[ticket]["cli_comment_list_output"] = result.stdout
report = {"exported_at": datetime.now(timezone.utc).isoformat(), "method": "Documented public tracking-system CLI get and comment list; no tracker storage access.", "records": records}
(tmp / "rest072_resume_tracker_closure.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({key: value["status"] for key, value in records.items()}))
