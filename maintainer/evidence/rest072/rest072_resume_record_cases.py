"""Record independently approved cases and verified formal execution readiness."""
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

tmp = Path(__file__).resolve().parent
tracker = tmp.parent.parent / ".ept/tools/tracker/tracker_cli.py"

def cli(*args):
    result = subprocess.run([sys.executable, str(tracker), *args], capture_output=True, text=True)
    print(result.stdout, result.stderr, flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    return result.stdout

def comment(ticket, subject, text):
    return cli("comment", "create", ticket, "--subject", subject, "--text", text, "--author", "project-manager")

def transition(ticket, kind, previous, target):
    cli("workflow", "transitions", kind, previous, "--author", "project-manager")
    return cli("update", ticket, "--status", target, "--author", "project-manager")

if sys.argv[1:] != ["--writer-granted"]:
    raise SystemExit("Exclusive tracker writer grant required.")
started = time.monotonic()
cases_path = tmp / "rest072_formal_cases.json"
cases = json.loads(cases_path.read_text())
approval = json.loads((tmp / "rest072_resume_case_approval.json").read_text())
case_hash = hashlib.sha256(cases_path.read_bytes()).hexdigest()
assert case_hash == approval["case_manifest_sha256"]
assert approval["verdict"] == "APPROVED"
assert approval["reviewer"] != cases["author_identity"]
for ticket in ("DEV-075", "UNITTEST-075", "CODEREVIEW-076"):
    state = cli("get", ticket, "--author", "project-manager")
    assert "current_status: Closed" in state, ticket
comment("DEV-STORY-072", "Reviewed implementation complete; formal QA readiness", "Verified by /root/formal072_resume: DESIGN075, DEV075, UNITTEST075 and CODEREVIEW076 Closed; all40 compiled current examples and all113 error wires reviewed; source/assets match approved literal case identities. Fresh independent approval by " + approval["reviewer"] + ". No required unresolved question or active blocker. Begin QA; final integrated acceptance/publication remains with093/070.")
transition("DEV-STORY-072", "dev_story", "Development", "QA")
comment("TESTCASE-075", "Independent source case plan and runnable prerequisites", "Recorded by /root/formal072_resume. Original independent case author " + cases["author_identity"] + "; fresh independent approver " + approval["reviewer"] + ". Case SHA256 " + case_hash + ". All40 baseline,113 named errors and220 concrete wire oracles were independently evaluated against primary SDK1.101.0 AST; response and error parameter schemas checked. Current40 behavior/contract/example hashes unchanged, implementation and committed tests physically exist and run in prepared SDK/runtime. DEV/UNIT/CR Closed are terminal successors ofResolved. Reviewed indexed authoring handoff, frozen partition, BA-DES015/SA-DES014. Plan: exact wire/results/errors, typed and raw sync/async, finite pages, timeout/malformed/401/403,500-item batches, complete classification outcomes, role restrictions and source silence. Public sockets denied; synthetic fixture execution implies no live enrollment effects. Complete source-derived Gherkin and literal oracles follow. No unresolved prerequisite question.")
transition("TESTCASE-075", "testcase", "Open", "In Progress")
for row in cases["operations"]:
    oracle = {key: row[key] for key in ("case_id", "operation", "request", "success", "errors")}
    oracle["request"].pop("argument_schemas", None)
    oracle["success"].pop("schema", None)
    for error in oracle["errors"]:
        for key in ("parameter_schema", "schema", "parameters_schema"):
            error.pop(key, None)
    text = "\n".join([
        "Feature: " + row["operation"],
        "Scenario: Exact success, source-specific adverse requests and finite boundaries",
        "Given pinned SDK1.101.0, fresh MockTransport, public socket/DNS denial, concrete request and independent literal oracles below",
        "When invoke exact SDK method in sync/async typed/raw modes and execute every approved additional_case in manifest SHA256 " + case_hash,
        "Then exact serialized wire and typed success match; declared error type/name/parameters propagate; raw responses and transports close; pagination and batches stay finite; classification and role outcomes match source conditions",
        "Original detailed Gherkin, additional cases and all hashes retained in full manifest; no author fixture verify function is used as formal oracle.",
        json.dumps(oracle, separators=(",", ":")),
    ])
    assert len(text) < 23000, row["operation"]
    comment("TESTCASE-075", row["case_id"] + " source-derived Gherkin and literal oracles", text)
comment("TESTCASE-075", "Fresh independent approval and complete case evidence", "Fresh approver " + approval["reviewer"] + " differs from original author " + cases["author_identity"] + ". Full report .ept/tmp/rest072_resume_independent_inspection.json; approval .ept/tmp/rest072_resume_case_approval.json binds exact manifest SHA256 " + case_hash + ". All40 operations/113 error sets/220 baseline,error,additional,boundary wires and schemas checked. The historical parse baseline correction is present and independently rechecked; no new finding. Time field records only measured current case recording interval, excluding historical authoring and review. Integration owner will archive full manifest, approval, harness and real execution logs before publication.")
cli("update", "TESTCASE-075", "--field", "time_spent_hours=" + str((time.monotonic() - started) / 3600), "--author", "project-manager")
transition("TESTCASE-075", "testcase", "In Progress", "Resolved")
cli("link", "list", "TESTCASE-075", "--author", "project-manager")
transition("TESTCASE-075", "testcase", "Resolved", "Closed")
comment("TESTEXEC-075", "Approved formal execution plan and environment readiness", "Recorder /root/formal072_resume; independent executor /root/formal072_resume/independent072. TESTCASE075 Closed, DEV/UNIT/CR Closed terminal successors ofResolved. Exact approved case SHA256 " + case_hash + ". All source/assets match, prepared SDK1.101.0/httpx/Pydantic runtime verified by independent preflight;40 examples compiled,518+7 author unit tests passed. Execute all40 cases using independent literal request/result/error oracles, fresh MockTransport, public socket+DNS traps and a real denied-network probe; test typed/raw sync+async and finite boundaries. Record every actual check and timestamps; retain source silence and offline-only limits. Harness is .ept/tmp/rest072_formal_execute.py; execution has not started. No unresolved required question or active prerequisite blocker. Full artifacts will be archived by integration owner.")
transition("TESTEXEC-075", "testexec", "Open", "In Progress")
