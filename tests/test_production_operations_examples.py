"""Behavior checks for standalone production incident example."""

from __future__ import annotations

import importlib.util
from pathlib import Path


EXAMPLE = (
    Path(__file__).resolve().parents[1]
    / ".agents/skills/pal-found-dev/examples/operations/incident.py"
)
spec = importlib.util.spec_from_file_location("production_incident", EXAMPLE)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def healthy_record() -> dict[str, str]:
    """Build, consumer and check agree on same committed output."""
    return {
        "consumer_branch": "master",
        "build_branch": "master",
        "required_input": "input-42",
        "build_input": "input-42",
        "job_status": "SUCCEEDED",
        "output_transaction": "output-9",
        "consumer_transaction": "output-9",
        "check_evaluated_at": "2026-01-01T10:01:00Z",
        "output_committed_at": "2026-01-01T10:00:00Z",
        "check_status": "PASS",
    }


def test_branch_and_input_mismatches_are_distinct() -> None:
    record = healthy_record()
    record["build_branch"] = "demo"
    assert module.assess(record)["cause"] == "consumer reads a different branch"
    record["build_branch"] = "master"
    record["build_input"] = "input-41"
    assert module.assess(record)["cause"] == "build used an older input transaction"


def test_failed_job_and_unread_output_are_distinct() -> None:
    record = healthy_record()
    record["job_status"] = "FAILED"
    assert module.assess(record)["cause"] == "target job failed"
    record["job_status"] = "SUCCEEDED"
    record["consumer_transaction"] = "output-8"
    assert module.assess(record)["cause"] == "consumer has not read committed output"


def test_check_evaluation_time_and_result_are_distinct() -> None:
    record = healthy_record()
    record["check_evaluated_at"] = "2026-01-01T09:00:00Z"
    assert module.assess(record)["cause"] == "health result predates output"
    record["check_evaluated_at"] = "2026-01-01T10:01:00Z"
    record["check_status"] = "FAIL"
    assert module.assess(record)["cause"] == "latest health check failed"
    record["check_status"] = "PASS"
    assert module.assess(record)["cause"] == "no discrepancy in supplied evidence"
