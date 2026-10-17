"""Offline decisions for recorded repository and dataset lifecycle evidence.

These functions interpret supplied records. They do not call Foundry or
simulate its preview, checks, build planner, or transaction service.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ReleaseEvidence:
    """Recorded evidence for one proposed production revision and output."""

    proposed_revision: str
    tests_passed: bool = False
    expectation_passed: bool = False
    checks_revision: str | None = None
    review_revision: str | None = None
    released_revision: str | None = None
    build_revision: str | None = None
    build_succeeded: bool = False
    transaction_state: str | None = None
    output_verified: bool = False


def next_release_action(evidence: ReleaseEvidence) -> str:
    """Return first missing gate for a recorded release and output."""

    revision = evidence.proposed_revision
    if not evidence.tests_passed:
        return "repair_or_run_tests"
    if not evidence.expectation_passed:
        return "repair_expectation_and_rebuild"
    if evidence.checks_revision != revision:
        return "run_checks_for_revision"
    if evidence.review_revision != revision:
        return "obtain_review_for_revision"
    if evidence.released_revision != revision:
        return "release_reviewed_revision"
    if evidence.build_revision != revision or not evidence.build_succeeded:
        return "build_production_context"
    if evidence.transaction_state != "COMMITTED":
        return "reconcile_output_transaction"
    if not evidence.output_verified:
        return "verify_output_and_consumers"
    return "delivery_verified"


def choose_computation(
    *,
    previous_output: bool,
    orders_change: str,
    schema_compatible: bool,
    resolved_input_expected: bool,
    require_incremental: bool = False,
) -> str:
    """Choose a safe local plan from recorded input and output history."""

    if not resolved_input_expected:
        return "inspect_branch_and_fallback"
    if not schema_compatible or orders_change != "APPEND":
        return "fail_and_plan_recompute" if require_incremental else "plan_snapshot_recompute"
    if not previous_output:
        return "snapshot_initialization"
    return "incremental_candidate"


def reconcile_known_transaction(
    transaction_id: str | None, state: str | None, remaining_reads: int = 2,
) -> str:
    """Choose follow-up for a recorded direct-write transaction."""

    if not transaction_id:
        return "locate_write_identity_before_retry"
    if state == "COMMITTED":
        return "verify_visible_files_and_build"
    if state in {"ABORTED", "FAILED"}:
        return "repair_before_new_write"
    if remaining_reads <= 0:
        return "stop_and_escalate_uncertain_write"
    return "read_known_transaction_again"
