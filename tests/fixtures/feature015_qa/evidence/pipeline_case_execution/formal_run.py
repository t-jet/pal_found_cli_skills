"""Run nine approved pipeline QA cases against the isolated skill snapshot."""

import hashlib
import io
import json
import runpy
import socket
import subprocess
import sys
from contextlib import redirect_stdout
from dataclasses import replace
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
SNAPSHOT = ROOT / ".ept/tmp/feature015_j7j8_addendum_resume_skill"
MANIFEST = HERE.parent / "j7_j8_addendum/snapshot_manifest.txt"
EXPECTED_MANIFEST = "5cbf2fc67b3bc706262884b40942caf7a345738edb965dfc0a979e3d785b56b8"
EXAMPLES = SNAPSHOT / "examples/pipelines"


def verify_snapshot():
    assert hashlib.sha256(MANIFEST.read_bytes()).hexdigest() == EXPECTED_MANIFEST
    entries = [line.rsplit(" ", 1) for line in MANIFEST.read_text(encoding="utf-8").splitlines()]
    assert len(entries) == 4379
    for relative, expected in entries:
        assert hashlib.sha256((SNAPSHOT / relative).read_bytes()).hexdigest() == expected, relative
    return len(entries)


def deny(*_args, **_kwargs):
    raise AssertionError("PUBLIC_NETWORK_DENIED")


def capture_case(case_id, heading, test_data, expected, actual):
    assert actual == expected, (case_id, expected, actual)
    page, section = heading
    assert f"## {section}" in (SNAPSHOT / page).read_text(encoding="utf-8"), heading
    return {
        "case": case_id,
        "consulted_local_heading": f"{page}#{section}",
        "test_data": test_data,
        "expected": expected,
        "actual": actual,
        "status": "PASS",
        "mode": "synthetic recorded state or local procedure; no Foundry tenant execution",
    }


def main():
    verified = verify_snapshot()
    sys.path.insert(0, str(EXAMPLES))
    from journey_decisions import ReleaseEvidence, choose_computation, next_release_action, reconcile_known_transaction
    from order_rules import build_orders, reconcile_orders

    rows = []
    order = {"order_id": "o1", "customer_id": "c1", "total_cents": 1200}
    added = {"order_id": "o2", "customer_id": "c1", "total_cents": 500}
    customers = [{"customer_id": "c1", "customer_name": "Ada"}]
    renamed = [{"customer_id": "c1", "customer_name": "Grace"}]
    base = ReleaseEvidence("commit-a", tests_passed=True, expectation_passed=True,
                           checks_revision="commit-a", review_revision="commit-a",
                           released_revision="commit-a", build_revision="commit-a",
                           build_succeeded=True, transaction_state="COMMITTED", output_verified=True)

    rows.append(capture_case("CASE062-1", ("references/pipelines/releases.md", "Procedure"),
        {"proposed_revision": "commit-a", "checks_revision": "commit-old"},
        ["run_checks_for_revision", "build_production_context"],
        [next_release_action(replace(base, checks_revision="commit-old")),
         next_release_action(replace(base, build_succeeded=False))]))

    joined = build_orders([order], customers)
    rows.append(capture_case("CASE062-2", ("references/pipelines/python-transforms.md", "Worked example"),
        {"orders": [order], "customers": customers, "empty_orders": []},
        {"joined": [{**order, "customer_name": "Ada"}], "empty": []},
        {"joined": joined, "empty": build_orders([], customers)}))

    failures = []
    for orders, references in (([order, order], customers), ([order], customers * 2),
                               ([{**order, "customer_id": None}], customers),
                               ([{**order, "total_cents": -1}], customers)):
        try:
            build_orders(orders, references)
        except ValueError as exc:
            failures.append(str(exc))
    rows.append(capture_case("CASE062-3", ("references/pipelines/testing.md", "Failures and recovery"),
        {"bad_inputs": "duplicate order/customer, null customer, negative cents"},
        ["duplicate order_id", "duplicate customer_id", "customer_id does not identify a customer",
         "total_cents must be a nonnegative integer", "repair_expectation_and_rebuild"],
        failures + [next_release_action(replace(base, expectation_passed=False))]))

    with patch.object(socket, "getaddrinfo", deny), patch.object(socket.socket, "connect", deny), \
         patch.object(socket, "create_connection", deny):
        try:
            socket.getaddrinfo("example.invalid", 443)
        except AssertionError as exc:
            denied = str(exc)
        output = io.StringIO()
        with redirect_stdout(output):
            runpy.run_path(str(EXAMPLES / "fixture_run.py"), run_name="__main__")
    fixture_lines = output.getvalue().strip().splitlines()
    rows.append(capture_case("CASE062-4", ("references/pipelines/local-development.md", "Expected result and checks"),
        {"fixture": "examples/pipelines/fixture_run.py", "public_probe": "example.invalid:443"},
        ["PUBLIC_NETWORK_DENIED", "business fixtures passed", "incremental fixtures passed"],
        [denied, fixture_lines[0].split(":")[0], fixture_lines[1].split(":")[0]]))

    previous = build_orders([order], customers)
    recomputed = build_orders([order, added], renamed)
    actual_five = {
        "choice": choose_computation(previous_output=True, orders_change="APPEND",
                                     schema_compatible=True, resolved_input_expected=True),
        "rows": reconcile_orders(previous, [added], renamed),
        "update": choose_computation(previous_output=True, orders_change="UPDATE",
                                     schema_compatible=True, resolved_input_expected=True),
        "schema": choose_computation(previous_output=True, orders_change="APPEND",
                                     schema_compatible=False, resolved_input_expected=True),
        "missing_prior": choose_computation(previous_output=False, orders_change="APPEND",
                                             schema_compatible=True, resolved_input_expected=True),
        "fallback": choose_computation(previous_output=True, orders_change="APPEND",
                                       schema_compatible=True, resolved_input_expected=False),
    }
    rows.append(capture_case("CASE062-5", ("references/pipelines/transactions.md", "Worked example"),
        {"previous": previous, "added": [added], "customers": renamed},
        {"choice": "incremental_candidate", "rows": recomputed,
         "update": "plan_snapshot_recompute", "schema": "plan_snapshot_recompute",
         "missing_prior": "snapshot_initialization", "fallback": "inspect_branch_and_fallback"}, actual_five))

    variants = {
        "tests": replace(base, tests_passed=False),
        "checks": replace(base, checks_revision="commit-old"),
        "review": replace(base, review_revision="commit-old"),
        "release": replace(base, released_revision="commit-old"),
        "build": replace(base, build_succeeded=False),
        "transaction": replace(base, transaction_state="OPEN"),
        "output": replace(base, output_verified=False),
        "complete": base,
    }
    rows.append(capture_case("CASE062-6", ("references/pipelines.md", "Follow the output through delivery"),
        {"revision": "commit-a", "varied_gate": list(variants)},
        {"tests": "repair_or_run_tests", "checks": "run_checks_for_revision",
         "review": "obtain_review_for_revision", "release": "release_reviewed_revision",
         "build": "build_production_context", "transaction": "reconcile_output_transaction",
         "output": "verify_output_and_consumers", "complete": "delivery_verified"},
        {key: next_release_action(value) for key, value in variants.items()}))

    states = [(None, None, 2), ("tx-1", "OPEN", 2), ("tx-1", "OPEN", 0),
              ("tx-1", "COMMITTED", 2), ("tx-1", "ABORTED", 2), ("tx-1", "FAILED", 2)]
    rows.append(capture_case("CASE062-7", ("references/pipelines/transactions.md", "Failures and recovery"),
        {"transactions": states},
        ["locate_write_identity_before_retry", "read_known_transaction_again",
         "stop_and_escalate_uncertain_write", "verify_visible_files_and_build",
         "repair_before_new_write", "repair_before_new_write"],
        [reconcile_known_transaction(*state) for state in states]))

    rows.append(capture_case("CASE062-8", ("references/pipelines/transactions.md", "Expected result and checks"),
        {"direct_write": "tx-1 COMMITTED", "transform_build": "not succeeded"},
        ["verify_visible_files_and_build", "build_production_context"],
        [reconcile_known_transaction("tx-1", "COMMITTED"),
         next_release_action(replace(base, build_succeeded=False))]))

    guide = (SNAPSHOT / "references/pipelines/repositories.md").read_text(encoding="utf-8").lower()
    reader = (HERE.parent / "feature015_reader_j1_j3_j6.md").read_text(encoding="utf-8").lower()
    rows.append(capture_case("CASE062-9", ("references/pipelines/repositories.md", "Failures and recovery"),
        {"condition": "repository access denied or remote runtime unavailable"},
        {"guide_names_permission": True, "reader_names_identity": True, "network_denied": True},
        {"guide_names_permission": "permission" in guide, "reader_names_identity": "identity" in reader,
         "network_denied": denied == "PUBLIC_NETWORK_DENIED"}))

    command = [sys.executable, "-B", "-m", "pytest", "-vv",
               "examples/pipelines/test_order_rules.py", "examples/pipelines/test_journey_decisions.py",
               "examples/pipelines/test_transform_entrypoints.py"]
    process = subprocess.run(command, cwd=SNAPSHOT, capture_output=True, text=True, timeout=90)
    assert process.returncode == 0 and "38 passed" in process.stdout, process.stdout + process.stderr
    captured_stdout = process.stdout.replace(str(SNAPSHOT), "<FROZEN_SNAPSHOT>").replace(
        sys.executable, "<PYTHON>"
    )
    captured_stderr = process.stderr.replace(str(SNAPSHOT), "<FROZEN_SNAPSHOT>").replace(
        sys.executable, "<PYTHON>"
    )
    evidence = {
        "executed_utc": datetime.now(timezone.utc).isoformat(),
        "snapshot_manifest_sha256": EXPECTED_MANIFEST,
        "snapshot_files_verified": verified,
        "python_version": sys.version.split()[0],
        "live_tenant_tested": False,
        "network_boundary": "cooperative Python DNS/socket denial for fixture and probe; pytest journey tests patch DNS/socket",
        "cases": rows,
        "pytest": {"command": ["python", "-B", "-m", "pytest", "-vv", *command[5:]],
                   "exit_code": process.returncode, "stdout": captured_stdout,
                   "stderr": captured_stderr},
    }
    (HERE / "formal_run_output.json").write_bytes((json.dumps(evidence, indent=2) + "\n").encode())
    print(json.dumps({"cases": len(rows), "passed": sum(row["status"] == "PASS" for row in rows),
                      "pytest": "38 passed", "manifest": EXPECTED_MANIFEST}))


if __name__ == "__main__":
    main()
