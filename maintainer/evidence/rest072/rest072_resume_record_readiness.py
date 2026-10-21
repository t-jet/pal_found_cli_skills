"""Record measured readiness after the coordinator grants exclusive tracker access."""
import json
import subprocess
import sys
from pathlib import Path

tmp = Path(__file__).resolve().parent
root = tmp.parent.parent
cli_path = root / ".ept/tools/tracker/tracker_cli.py"

def cli(*args):
    result = subprocess.run([sys.executable, str(cli_path), *args], capture_output=True, text=True)
    print(result.stdout, result.stderr, flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
    return result.stdout

def transition(ticket, kind, previous, target):
    cli("workflow", "transitions", kind, previous, "--author", "project-manager")
    cli("update", ticket, "--status", target, "--author", "project-manager")

if sys.argv[1:] != ["--writer-granted"]:
    raise SystemExit("Exclusive tracker writer grant required.")
readiness = json.loads((tmp / "rest072_resume_readiness.json").read_text())
cases = json.loads((tmp / "rest072_formal_cases.json").read_text())
assert readiness["result"] == "PASS"
files = sorted({asset["path"] for row in cases["operations"] for asset in row["assets"].values()})
text = "\n".join([
    "Current verifier: /root/formal072_resume. Candidate commit " + readiness["candidate_commit"] + ".",
    "Reviewed indexed BA-DES-015 revision2, SA-DES-014 REST/source design, REST authoring handoff and exact partition. DESIGN-075 and BUG-SUB-029/030/031 are Closed; no required unresolved question or active implementation blocker found. Existing registered parent, paired review and dependency links remain valid.",
    "All40 current examples physically exist and compile. Their behavior, contract and example hashes equal the independently reviewed case manifest. Dedicated tests/test_offline_rest_072.py is committed at a8695c8. Prior measured unit evidence: shared wave1 518 passed in4.16s; dedicated7 passed in0.22s; ruff passed; all7 historical defect mutants rejected. These are author unit results; formal QA remains pending.",
    "Distributed reader changes cover exact operation behaviors and examples; shared core contract/model references retain their ownership. Indexed handoff and operation partitions already describe these deliverables, so no document-index change is required for unchanged scope. Complete review/case/execution evidence will be archived by integration owner after formal QA.",
    "Created/modified deliverables relative to .agents/skills/pal-found-dev (no deletion claimed):",
    *files,
    "Additional created deliverable: tests/test_offline_rest_072.py. Current compilation verification interval " + readiness["started_at"] + " to " + readiness["finished_at"] + "; recorded time covers only measured verification runtime, excluding unmeasured historical implementation.",
])
cli("comment", "create", "DEV-075", "--subject", "Current committed implementation and measured readiness verified", "--text", text, "--author", "project-manager")
cli("update", "DEV-075", "--field", "time_spent_hours=" + str(readiness["elapsed_seconds"] / 3600), "--author", "project-manager")
transition("DEV-075", "development", "In Progress", "Resolved")
cli("comment", "create", "UNITTEST-075", "--subject", "Committed offline coverage verified for review handoff", "--text", "Verifier /root/formal072_resume. Dedicated tests/test_offline_rest_072.py committed at a8695c8; source-based regressions cover CBAC marking IDs, exact requested batch identity, complete disjoint classification outcomes, Organization marking USE/DECLASSIFY success and contextual ADMINISTER rejection. Existing measured results: shared518 in4.16seconds plus dedicated7 in0.22seconds, allPASS;7 historical mutants rejected. Network denial isolates unit tests. Recorded time0.001216667hours covers measured4.38seconds pytest runtime only. Current source hashes unchanged; no unmeasured authoring hours reconstructed. Parent/review links registered; no unresolved required question.", "--author", "project-manager")
cli("update", "UNITTEST-075", "--field", "time_spent_hours=0.001216667", "--author", "project-manager")
transition("UNITTEST-075", "unittest", "In Progress", "Resolved")
cli("link", "remove", "LINK-01806", "--author", "project-manager")
cli("comment", "create", "CODEREVIEW-076", "--subject", "Paired DEV Resolved; independent approval now ready", "--text", "DEV-075 and UNITTEST-075 are Resolved. LINK-01806 blocked review only until DEVResolved, per original prerequisite comment; removed after prerequisite met. Return priorOpen. Fresh actual independent reviewer /root/formal072_resume/independent072 will record approval against exact unchanged072 assets and committed dedicated tests. Earlier source review retains its original reviewer identity and historical WAIT_DEV_RESOLVED verdict.", "--author", "project-manager")
transition("CODEREVIEW-076", "codereview", "Blocked", "Open")
