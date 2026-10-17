"""Reject mismatched transaction views before claiming a build outcome."""

import runpy
from pathlib import Path

import pytest


EXAMPLE = (
    Path(__file__).parents[1]
    / ".agents/skills/pal-found-dev/examples/rest/074/v2/datasets/staged_commit_journey.py"
)
exercise = runpy.run_path(str(EXAMPLE))["exercise"]


@pytest.mark.parametrize(
    ("fault_at", "timeout_at", "expected_mutations"),
    [
        ("staged-content", None, ["create", "upload"]),
        ("staged-content", "upload", ["create", "upload"]),
        ("branch-pointer", None, ["create", "upload", "commit"]),
        ("visible-content", None, ["create", "upload", "commit"]),
    ],
)
def test_j12_stops_before_build_on_unverified_file_or_branch(
    fault_at, timeout_at, expected_mutations
):
    trace = {}

    with pytest.raises(AssertionError):
        exercise("SUCCEEDED", timeout_at=timeout_at, fault_at=fault_at, trace=trace)

    assert trace["mutations"] == expected_mutations
    assert trace["build_reads"] == 0


@pytest.mark.parametrize(
    ("build_status", "expected_outcome"),
    [
        ("SUCCEEDED", "success"),
        ("FAILED", "unsuccessful"),
        ("CANCELED", "unsuccessful"),
        ("RUNNING", "unknown-after-budget"),
    ],
)
def test_j12_build_outcome_follows_terminal_status_or_finite_budget(
    build_status, expected_outcome
):
    result = exercise(build_status)

    assert result["build_status"] == build_status
    assert result["outcome"] == expected_outcome
    assert result["build_rid"]


@pytest.mark.parametrize("timeout_at", ["upload", "commit"])
def test_j12_lost_write_reply_reconciles_known_transaction_without_replay(timeout_at):
    trace = {}

    result = exercise("SUCCEEDED", timeout_at=timeout_at, trace=trace)

    assert result["outcome"] == "success"
    assert trace["mutations"] == ["create", "upload", "commit"]
    assert trace["staged_reads"] >= 2
    assert trace["visible_reads"] == 2


def test_j12_abort_discards_only_open_transaction():
    trace = {}

    result = exercise("RUNNING", abort=True, trace=trace)

    assert result == {"case": "abort", "outcome": "ABORTED"}
    assert trace["mutations"] == ["create", "upload", "abort"]
    assert trace["build_reads"] == 0
