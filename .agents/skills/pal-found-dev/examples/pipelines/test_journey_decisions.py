"""Offline J1/J2 fixtures for pipeline decisions and result contracts."""

import socket
from dataclasses import replace

import pytest

from journey_decisions import (
    ReleaseEvidence,
    choose_computation,
    next_release_action,
    reconcile_known_transaction,
)
from order_rules import build_orders, reconcile_orders


@pytest.fixture(autouse=True)
def deny_network(monkeypatch):
    """Reject DNS and socket connections within this Python test process."""

    def blocked(*args, **kwargs):
        raise AssertionError("network request in offline pipeline fixture")

    monkeypatch.setattr(socket, "getaddrinfo", blocked)
    monkeypatch.setattr(socket.socket, "connect", blocked)
    monkeypatch.setattr(socket.socket, "connect_ex", blocked)
    monkeypatch.setattr(socket, "create_connection", blocked)


def test_network_denial_probe():
    with pytest.raises(AssertionError, match="network request"):
        socket.getaddrinfo("example.invalid", 443)


def test_preview_sample_does_not_clear_failed_expectation_or_release():
    order = {"order_id": "o1", "customer_id": "c1", "total_cents": 1200}
    customers = [{"customer_id": "c1", "customer_name": "Ada"}]
    assert build_orders([order], customers) == [
        {"order_id": "o1", "customer_id": "c1", "customer_name": "Ada", "total_cents": 1200}
    ]
    with pytest.raises(ValueError, match="duplicate order_id"):
        build_orders([order, order], customers)
    recorded = ReleaseEvidence("commit-a", tests_passed=True)
    assert next_release_action(recorded) == "repair_expectation_and_rebuild"
    assert next_release_action(ReleaseEvidence("commit-a")) == "repair_or_run_tests"


@pytest.mark.parametrize("change,expected", [
    ({"checks_revision": "commit-old"}, "run_checks_for_revision"),
    ({"review_revision": "commit-old"}, "obtain_review_for_revision"),
    ({"released_revision": "commit-old"}, "release_reviewed_revision"),
    ({"build_revision": "commit-old"}, "build_production_context"),
    ({"transaction_state": "OPEN"}, "reconcile_output_transaction"),
    ({"output_verified": False}, "verify_output_and_consumers"),
])
def test_revision_and_data_visibility_gates(change, expected):
    complete = ReleaseEvidence(
        "commit-a", tests_passed=True, expectation_passed=True,
        checks_revision="commit-a", review_revision="commit-a",
        released_revision="commit-a", build_revision="commit-a",
        build_succeeded=True, transaction_state="COMMITTED",
        output_verified=True,
    )
    assert next_release_action(replace(complete, **change)) == expected
    assert next_release_action(complete) == "delivery_verified"


def test_release_does_not_imply_completed_build():
    released = ReleaseEvidence(
        "commit-a", tests_passed=True, expectation_passed=True,
        checks_revision="commit-a", review_revision="commit-a",
        released_revision="commit-a", build_revision="commit-a",
    )
    assert next_release_action(released) == "build_production_context"


def test_append_matches_snapshot_and_changed_reference_rejoins_old_rows():
    old = {"order_id": "o1", "customer_id": "c1", "total_cents": 1200}
    added = {"order_id": "o2", "customer_id": "c1", "total_cents": 500}
    original = [{"customer_id": "c1", "customer_name": "Ada"}]
    renamed = [{"customer_id": "c1", "customer_name": "Grace"}]
    previous = build_orders([old], original)
    expected = [
        {"order_id": "o1", "customer_id": "c1", "customer_name": "Grace", "total_cents": 1200},
        {"order_id": "o2", "customer_id": "c1", "customer_name": "Grace", "total_cents": 500},
    ]
    assert choose_computation(
        previous_output=True, orders_change="APPEND",
        schema_compatible=True, resolved_input_expected=True,
    ) == "incremental_candidate"
    assert reconcile_orders(previous, [added], renamed) == expected
    assert build_orders([old, added], renamed) == expected
    with pytest.raises(ValueError, match="duplicate order_id"):
        reconcile_orders(previous, [old, added], renamed)


@pytest.mark.parametrize("conditions,expected", [
    ({"previous_output": False}, "snapshot_initialization"),
    ({"orders_change": "UPDATE"}, "plan_snapshot_recompute"),
    ({"schema_compatible": False}, "plan_snapshot_recompute"),
    ({"resolved_input_expected": False}, "inspect_branch_and_fallback"),
    ({"orders_change": "DELETE", "require_incremental": True}, "fail_and_plan_recompute"),
])
def test_initial_state_unsupported_history_schema_and_fallback(conditions, expected):
    baseline = dict(
        previous_output=True, orders_change="APPEND",
        schema_compatible=True, resolved_input_expected=True,
    )
    assert choose_computation(**(baseline | conditions)) == expected


@pytest.mark.parametrize("identity,state,expected", [
    (None, None, "locate_write_identity_before_retry"),
    ("tx-1", None, "read_known_transaction_again"),
    ("tx-1", "OPEN", "read_known_transaction_again"),
    ("tx-1", "COMMITTED", "verify_visible_files_and_build"),
    ("tx-1", "ABORTED", "repair_before_new_write"),
    ("tx-1", "FAILED", "repair_before_new_write"),
])
def test_uncertain_write_uses_known_transaction_before_replay(identity, state, expected):
    assert reconcile_known_transaction(identity, state) == expected


def test_uncertain_transaction_stops_after_read_budget():
    assert reconcile_known_transaction("tx-1", "OPEN", remaining_reads=0) == (
        "stop_and_escalate_uncertain_write"
    )
