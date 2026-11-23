"""Package reader-authored evidence without changing shared files."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SNAPSHOT = ROOT / "skill_snapshot"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(name, data):
    (ROOT / name).write_text(json.dumps(data, indent=2), encoding="utf-8")


sources = [
    ("SKILL.md", "Read by task; Evidence before delivery"),
    ("references/rest-api.md", "Discover and author any frozen SDK REST operation; Failures and recovery"),
    ("references/rest/authentication.md", "Prepared client; Resolve authorization prerequisites locally"),
    ("references/rest/client-behavior.md", "Client and API version; Timeouts, throttling and uncertain writes; Errors and cleanup"),
    ("references/rest/v2/datasets/Transaction.md", "Stage a file, commit, and verify the branch; commit; create; get; abort"),
    ("references/rest/v2/datasets/File.md", "Client route and bounded content read; upload; Operations and outcome checks"),
    ("references/rest/v2/orchestration/Build.md", "Wait for a submitted build; create; get"),
    ("examples/rest/074/v2/datasets/staged_commit_journey.py", "Read adaptable exercise implementation; did not execute or import it"),
    ("references/rest/contracts/v2/datasets/File/upload.md", "SDK invocation contract; Wire request; Documented operation errors"),
    ("references/rest/contracts/v2/datasets/File/get.md", "Purpose and parameter meaning; SDK invocation contract; Wire request (first 145 lines)"),
    ("references/rest/contracts/v2/datasets/File/content.md", "Purpose and parameter meaning; SDK invocation contract; Wire request (first 125 lines)"),
    ("references/rest/contracts/v2/datasets/Branch/get.md", "SDK invocation contract; Wire request (first 110 lines)"),
    ("references/rest/contracts/v2/datasets/Transaction/create.md", "SDK invocation contract; Wire request (first 110 lines)"),
    ("references/rest/contracts/v2/datasets/Transaction/commit.md", "SDK invocation contract; Wire request (first 110 lines)"),
    ("references/rest/contracts/v2/orchestration/Build/create.md", "SDK invocation contract; Wire request; Complete referenced models and errors"),
    ("references/rest/contracts/v2/orchestration/Build/get.md", "Purpose and parameter meaning; SDK invocation contract; Wire request"),
    ("references/rest/models/v2/orchestration/models/BuildTarget.md", "Exact SDK definition"),
    ("references/rest/models/v2/orchestration/models/ManualTarget.md", "Fields and wire names; Exact SDK definition"),
    ("references/rest/models/v2/orchestration/models/Build.md", "Fields and wire names; Exact SDK definition"),
    ("references/rest/models/v2/datasets/models/Transaction.md", "Fields and wire names; Exact SDK definition"),
    ("references/rest/models/v2/datasets/models/File.md", "Fields and wire names; Exact SDK definition"),
    ("references/rest/models/v2/datasets/errors/FileNotFoundOnTransactionRangeParameters.md", "Exact SDK definition; consulted while planning, no missing-file error fabricated in execution"),
    ("references/pipelines/transactions.md", "Concept and lifecycle; Failures and recovery"),
]
consulted = [{"path": f"skill_snapshot/{path}", "sha256": sha(SNAPSHOT / path), "headings_or_scope": scope}
             for path, scope in sources]
workspace = ROOT.parents[2]
control = [".ept/resources/skills/caveman/SKILL.md", ".ept/resources/skills/humanizer/SKILL.md",
           ".ept/resources/skills/work-instructions/SKILL.md", ".ept/resources/skills/tracking-system/SKILL.md",
           ".ept/resources/skills/tracking-system/references/REFERENCE.md"]
control_sources = [{"path": path, "sha256": sha(workspace / path)} for path in control]
snapshot_files = [{"path": path.relative_to(SNAPSHOT).as_posix(), "sha256": sha(path),
                   "bytes": path.stat().st_size} for path in sorted(SNAPSHOT.rglob("*")) if path.is_file()]
canonical = "".join(f"{item['path']}\0{item['sha256']}\n" for item in snapshot_files).encode()
snapshot_digest = hashlib.sha256(canonical).hexdigest()
write("snapshot_manifest.json", {"algorithm": "SHA256(sorted relative-path NUL file-SHA256 LF)",
    "tree_sha256": snapshot_digest, "file_count": len(snapshot_files), "files": snapshot_files})
write("consulted_sources.json", {"standalone_skill": consulted, "required_control_skills": control_sources})
execution = json.loads((ROOT / "execution_results.json").read_text())
answer = {
    "reader": "J12 reader recover 20261028",
    "tickets": {"TESTEXEC-064": "Open", "BUG-SUB-025": "In Progress"},
    "scope": "Independent offline staged dataset transaction, file verification, commit recovery, and asynchronous Build interpretation",
    "candidate": {"snapshot": "skill_snapshot", "tree_sha256": snapshot_digest,
                  "file_count": len(snapshot_files), "git_commit_claim": None,
                  "snapshot_created_before_implementation": True},
    "constraints_observed": {
        "tracker_reads": ["python .ept/tools/tracker/tracker_cli.py get TESTEXEC-064", "python .ept/tools/tracker/tracker_cli.py get BUG-SUB-025"],
        "tracker_exit_codes": [0, 0], "tracker_mutations": [],
        "previous_comments_or_answers_read": False, "old_reader_artifacts_read": False,
        "repo_tests_or_sdk_source_read": False, "public_browsing": False,
        "standalone_example_imported_or_executed": False,
        "only_write_directory": str(ROOT), "live_foundry_claim": False,
    },
    "acceptance_understood": [
        "Read staged file metadata and content before commit, using both transaction range bounds.",
        "Verify COMMITTED transaction, branch pointer, and same-branch file metadata/content after commit.",
        "Interpret RUNNING, SUCCEEDED, FAILED, CANCELED, and bounded pending separately.",
        "Reconcile upload or commit timeout before deciding whether replay is safe.",
        "Preserve evidence and leave independent grading and ticket disposition to another agent.",
    ],
    "dimensions": {
        "choices": {
            "identity": "Synthetic UserTokenAuth, synthetic host/RIDs/branch/path; authorized metadata and resource permission remain prerequisites for live work.",
            "version": "Root FoundryClient public v2 routes; prepared SDK 1.101.0.",
            "transaction": "APPEND on explicitly named reader-j12 branch; one staged CSV path, explicit transaction RID for upload.",
            "views": "Before commit, start_transaction_rid=end_transaction_rid=known RID. After commit, branch_name=reader-j12.",
            "build": "Separately call Build.create with ManualTarget(target_rids=[synthetic dataset RID]); submission RUNNING remains incomplete.",
            "concurrency": "Synthetic fixture has one writer. Read reconciliation does not establish an atomic compare-and-set guarantee under concurrent external writers.",
            "expected": "Only SUCCEEDED produces success; other terminal statuses unsuccessful; exhausted budget pending.",
            "actual_evidence": ["reader_workflow.py:Workflow", "journal_success.json", "journal_failed.json", "journal_pending.json"],
        },
        "code_config": {
            "implementation": "reader_workflow.py", "runtime": execution["runtime"],
            "config": {"timeout_seconds": 3, "max_retries": 1, "propagate_qos": "PROPAGATE_429_AND_503_TO_CALLER",
                       "commit_attempt_limit": 2, "max_build_polls_per_run": 3,
                       "build_deadline_seconds": 3, "poll_interval_seconds": 0.3, "content_byte_limit": 1024},
            "journal": "Journal atomically replaces JSON in own directory after flush/fsync, recording intent before mutations and known RIDs afterward. Resume loads and validates dataset/branch/path/payload hash.",
            "expected": "No SDK automatic retry or duplicate create; finite upload/commit/poll work.",
            "actual_evidence": ["trace_upload_recovery.json", "trace_commit_safe_retry.json", "journal_pending_resume.json"],
        },
        "validation": {
            "method": "Own stateful httpx.MockTransport invokes real SDK root client serializers and result decoders. Own service asserts exact method/path/query/body, selected header semantics, auth presence, finite timeout, stage/branch state, and mutation ordering.",
            "requests": "Per-case trace JSON preserves timestamp, method, path, query, non-secret headers, body, timeout, response/transport exception. Synthetic Authorization is checked but omitted from evidence.",
            "network": "DNS getaddrinfo, socket.connect, and socket.connect_ex patched to deny during execution; explicit DNS/public-IP connection probes each rejected in every case.",
            "expected": "12 scenario outcomes and mutation counts match; corruption/branch faults halt before build submission.",
            "actual": "Exit 0. Twelve scenarios matched expected outcomes. 24 explicit denial probes rejected; mock transport provided every SDK response.",
            "command": ".ept/tmp/feature015_shared_cli_qa_env/Scripts/python.exe -B .ept/tmp/j12_reader_recover_20261028/reader_workflow.py",
            "raw_output": "raw_execution_output.txt",
            "limits": "No tenant deployment, OAuth exchange, transform execution, or live permissions checked. Deadline-exhaustion timing, lost create response, abort timeout, and arbitrary concurrent writer behavior are not exercised.",
        },
        "results": {
            "cases": execution["cases"],
            "expected_actual": {
                "success": "RUNNING then SUCCEEDED -> success; actual success after 2 reads.",
                "failed": "RUNNING then FAILED -> unsuccessful; actual unsuccessful after 2 reads.",
                "canceled": "RUNNING then CANCELED -> unsuccessful; actual unsuccessful after 2 reads.",
                "pending": "RUNNING for 3 reads -> pending; actual pending, known RID retained.",
                "upload_recovery": "Upload takes effect then loses reply -> verify staged view, continue; actual one upload attempt/effect.",
                "commit_recovery": "Commit takes effect then loses reply -> reconcile transaction+branch; actual one commit attempt/effect.",
                "commit_safe_retry": "First commit times out without effect -> reconcile OPEN+original branch+staged bytes, retry once; actual two requests, one commit effect.",
                "pending_resume": "Reload journal and re-read retained build after pending; actual success with unchanged mutation list.",
                "staging_corruption": "Mismatch -> abort confirmed OPEN transaction, no commit/build; actual stopped, one abort.",
                "visible_corruption": "Postcommit mismatch -> stop, no build/replay; actual stopped with committed transaction retained.",
                "branch_mismatch": "Wrong branch pointer -> stop, no build/replay; actual stopped.",
                "reconciliation_unavailable": "Cannot validate staged bytes -> abort confirmed OPEN, stop; actual stopped, no commit/build.",
            },
            "evidence_is": "SDK serialization and application behavior against declared synthetic service states.",
        },
        "recovery": {
            "upload": "Never repeat uncertain upload. Read known OPEN transaction and exact transaction-view metadata/content; continue when bytes match. Unverifiable staged data stops and aborts only confirmed OPEN transaction.",
            "commit": "Before every attempt, read transaction and branch plus staged content. After lost reply, COMMITTED suppresses replay. OPEN with unchanged original branch and verified staged bytes permits at most second attempt. Other states stop.",
            "build": "FAILED/CANCELED stay unsuccessful. Read branch and retain RID for job review. Pending retains RID for later reads. Journal resume demonstrated no second Build.create.",
            "unknown_creates": "Recorded create/build intent without returned RID blocks replay; owner reconciliation required. Code guard exists; lost-create transport scenario not executed.",
            "evidence": ["journal_upload_recovery.json", "journal_commit_recovery.json", "journal_commit_safe_retry.json", "journal_pending_resume.json"],
        },
        "local_sources": {
            "consulted": consulted,
            "control_skills": control_sources,
            "snapshot_manifest": "snapshot_manifest.json", "consulted_source_manifest": "consulted_sources.json",
            "guidance_gaps": [
                {"finding": "Integrated standalone example begins with a known synthetic Build RID and polls it; it does not submit Build.create.",
                 "impact": "I composed Build.create using local operation contract plus BuildTarget/ManualTarget definitions. No essential fact required external lookup."},
                {"finding": "Local guidance requires retaining identifiers and reconciling uncertainty but does not prescribe a durable journal schema.",
                 "impact": "Journal format and resume guards are reader-authored application decisions."},
            ],
            "essential_missing_guidance_encountered": False,
            "grading": "No reader score or BUG-SUB-025 approval asserted; independent grader decides acceptance.",
        },
    },
}
write("reader_answer.json", answer)
write("reader_prompt.json", {"task": "Fresh independent J12 offline reader for FEATURE-015 / BUG-SUB-025. Snapshot entire current standalone pal-found-dev skill, use prepared SDK 1.101.0 runtime only, derive staged dataset upload/commit/build interpretation, recovery and journal. Read current TESTEXEC-064 and BUG-SUB-025 instructions/AC only; exclude previous comments/answers, old artifacts, maintainer reports, repo tests and SDK source. Use own synthetic httpx.MockTransport with public socket/DNS denied. May read adaptable staged_commit_journey example but must independently implement. Record six dimensions, own code, raw execution and SHA manifests. Own directory only; no shared tracker/source/ledger writes; separate grader decides acceptance.",
                            "controls": "caveman ultra internal/full responses; humanizer prose; work-instructions/tracking-system + public reference read"})
artifacts = [{"path": path.relative_to(ROOT).as_posix(), "sha256": sha(path), "bytes": path.stat().st_size}
             for path in sorted(ROOT.iterdir()) if path.is_file() and path.name != "artifact_hash_manifest.json"]
write("artifact_hash_manifest.json", {"snapshot_tree_sha256": snapshot_digest, "files": artifacts})
print(json.dumps({"snapshot_tree_sha256": snapshot_digest, "snapshot_files": len(snapshot_files),
                  "authored_artifacts": len(artifacts), "reader_answer_sha256": sha(ROOT / "reader_answer.json")}))
