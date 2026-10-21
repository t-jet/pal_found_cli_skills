"""Record real independent execution results and close only the QA execution task."""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

tmp = Path(__file__).resolve().parent
tracker = tmp.parent.parent / ".ept/tools/tracker/tracker_cli.py"

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def cli(*args):
    result = subprocess.run([sys.executable, str(tracker), *args], capture_output=True, text=True)
    print(result.stdout, result.stderr, flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    return result.stdout

def transition(previous, target):
    cli("workflow", "transitions", "testexec", previous, "--author", "project-manager")
    return cli("update", "TESTEXEC-075", "--status", target, "--author", "project-manager")

if sys.argv[1:] != ["--writer-granted"]:
    raise SystemExit("Exclusive tracker writer grant required.")
cases_path = tmp / "rest072_formal_cases.json"
cases = json.loads(cases_path.read_text())
execution_path = tmp / "rest072_resume_formal_execution.json"
execution = json.loads(execution_path.read_text())
runner_path = tmp / "rest072_resume_formal_runner.json"
runner = json.loads(runner_path.read_text())
assert runner["exit_code"] == 0
assert execution["execution"] == "PASS"
assert execution["cases_sha256"] == digest(cases_path) == runner["cases_sha256"]
assert execution["harness_sha256"] == digest(tmp / "rest072_resume_formal_execute.py")
assert len(cases["operations"]) == execution["operations"] == 40
assert execution["executor_identity"] != cases["author_identity"]
assert all(row["result"] == "PASS" for row in execution["results"])
assert any(row["check"] == "socket_traps_active" for row in execution["results"])
operations = []
for case in cases["operations"]:
    rows = [row for row in execution["results"] if row["case_id"] == case["case_id"]]
    checks = {row["check"] for row in rows}
    assert rows and {"success_typed", "success_raw_closed", "async_typed", "async_raw_closed", "timeout_no_retry"} <= checks
    assert all("error_" + error["name"] in checks for error in case["errors"])
    text = "\n".join([
        "Actual independent executor " + execution["executor_identity"] + ". " + case["operation"],
        "Final run interval " + runner["started_at"] + " to " + runner["completed_at"] + "; exit0. Prepared SDK1.101.0, synthetic manifest data, httpx MockTransport, public socket/DNS denial verified. Exact case manifest SHA256 " + digest(cases_path) + ".",
        "Full final log .ept/tmp/rest072_resume_formal_execute.log SHA256 " + digest(tmp / "rest072_resume_formal_execute.log") + "; execution JSON SHA256 " + digest(execution_path) + ". Full source/request/result/error oracles reside in approved manifest. These check records were emitted only after their runtime assertions passed:",
        json.dumps(rows, separators=(",", ":")),
    ])
    assert len(text) < 23000
    cli("comment", "create", "TESTEXEC-075", "--subject", case["case_id"] + " actual formal PASS " + case["operation"], "--text", text, "--author", "project-manager")
    operations.append({"id": case["operation"], "case_id": case["case_id"], "verdict": "PASS", "checks": len(rows), "assets": case["assets"], "source": case["source"]})
prior = []
for path in sorted(tmp.glob("rest072_resume_attempt*_formal_runner.json")):
    row = json.loads(path.read_text())
    detail_path = path.with_name(path.name.replace("_formal_runner.json", "_formal_execution.json"))
    detail = json.loads(detail_path.read_text())
    prior.append({"runner": path.name, "exit_code": row["exit_code"], "elapsed_seconds": row["elapsed_seconds"], "sha256": digest(path), "failure": detail.get("failure")})
elapsed = runner["elapsed_seconds"] + sum(row["elapsed_seconds"] for row in prior)
summary = {
    "executor": execution["executor_identity"], "operations": len(operations), "declared_errors": execution["declared_errors"],
    "check_records": len(execution["results"]), "final_exit_code": runner["exit_code"], "final_runtime_seconds": runner["elapsed_seconds"],
    "prior_harness_attempts": prior, "total_measured_execution_seconds": elapsed,
    "boundary": "Offline SDK serialization, typed results, errors and bounded lifecycle assertions only; no live enrollment/deployment verification.",
}
cli("comment", "create", "TESTEXEC-075", "--subject", "Independent formal execution complete; measured evidence and attempt history", "--text", json.dumps(summary) + "\nEarlier failed runs are retained as temporary QA harness defects: named-exception error API, SDKInternalError decoding wrapper, and ordinary paged iterator mode handling. Corrected assertions use the primary SDK exception API, error causes and exact decoded-page versus ordinary sync/async iterator modes; approved cases/candidate assets unchanged. No product defect found. All40 cases and113 declared error conditions now pass; every case has its own runtime result comment. Time field includes measured harness run intervals only, excludes unmeasured historical effort. Integration owner must archive all approved manifest, inspection, approval, harness, logs and failed attempts before publication.", "--author", "project-manager")
cli("update", "TESTEXEC-075", "--field", "time_spent_hours=" + str(elapsed / 3600), "--author", "project-manager")
transition("In Progress", "Resolved")
cli("link", "list", "TESTEXEC-075", "--author", "project-manager")
transition("Resolved", "Closed")
state = cli("get", "TESTEXEC-075", "--author", "project-manager")
assert "current_status: Closed" in state
case_state = cli("get", "TESTCASE-075", "--author", "project-manager")
assert "current_status: Closed" in case_state
report = {"story": "DEV-STORY-072", "candidate_sha": subprocess.check_output(["git", "-C", str(tmp / "feature015_integration"), "rev-parse", "HEAD"], text=True).strip(), "sdk_release": "1.101.0", "case_author": cases["author_identity"], "reviewer": execution["executor_identity"], "case_manifest_sha256": digest(cases_path), "testcase_status": "Closed", "testexec_status": "Closed", "formal_execution": "PASS", "operations": operations, "execution_summary": summary, "evidence": {name: {"path": name, "sha256": digest(tmp / name)} for name in ("rest072_formal_cases.json", "rest072_resume_case_approval.json", "rest072_resume_codereview_approval.json", "rest072_resume_independent_inspection.json", "rest072_resume_formal_execute.py", "rest072_resume_formal_execute.log", "rest072_resume_formal_execution.json", "rest072_resume_formal_runner.json")}, "boundary": summary["boundary"], "durable_archive_required": True}
(tmp / "feature015_rest072_formal_qa.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(summary))
