"""Verify business outputs used by the actual snapshot/incremental examples."""

import pytest
from order_rules import build_orders, reconcile_orders


CUSTOMERS = [{"customer_id": "c1", "customer_name": "Ada"}]
ORDER = {"order_id": "o1", "customer_id": "c1", "total_cents": 1200}


def test_full_join_and_empty_schema_contract():
    assert build_orders([ORDER], CUSTOMERS) == [{
        "order_id": "o1", "customer_id": "c1", "customer_name": "Ada", "total_cents": 1200,
    }]
    assert build_orders([], CUSTOMERS) == []


@pytest.mark.parametrize("field,value,message", [
    ("order_id", None, "order_id must be a nonempty string"),
    ("order_id", "", "order_id must be a nonempty string"),
    ("customer_id", None, "customer_id does not identify a customer"),
    ("customer_id", "unknown", "customer_id does not identify a customer"),
    ("total_cents", None, "total_cents must be a nonnegative integer"),
    ("total_cents", True, "total_cents must be a nonnegative integer"),
    ("total_cents", 1.5, "total_cents must be a nonnegative integer"),
    ("total_cents", -1, "total_cents must be a nonnegative integer"),
])
def test_invalid_order_contract(field, value, message):
    with pytest.raises(ValueError, match=message):
        build_orders([{**ORDER, field: value}], CUSTOMERS)


def test_duplicate_order_and_customer_keys():
    with pytest.raises(ValueError, match="duplicate order_id"):
        build_orders([ORDER, ORDER], CUSTOMERS)
    with pytest.raises(ValueError, match="duplicate customer_id"):
        build_orders([ORDER], CUSTOMERS * 2)


def test_reference_name_must_be_nonempty():
    with pytest.raises(ValueError, match="customer_id and customer_name must be nonempty strings"):
        build_orders([ORDER], [{"customer_id": "c1", "customer_name": None}])


def test_incremental_append_matches_full_result_and_updates_old_reference():
    previous = build_orders([ORDER], CUSTOMERS)
    added = {"order_id": "o2", "customer_id": "c1", "total_cents": 500}
    renamed = [{"customer_id": "c1", "customer_name": "Grace"}]
    expected = [
        {"order_id": "o1", "customer_id": "c1", "customer_name": "Grace", "total_cents": 1200},
        {"order_id": "o2", "customer_id": "c1", "customer_name": "Grace", "total_cents": 500},
    ]
    assert reconcile_orders(previous, [added], renamed) == expected
    assert build_orders([ORDER, added], renamed) == expected
    assert reconcile_orders([], [ORDER, added], renamed) == expected


def test_incremental_replay_and_removed_reference_are_rejected():
    previous = build_orders([ORDER], CUSTOMERS)
    with pytest.raises(ValueError, match="duplicate order_id"):
        reconcile_orders(previous, [ORDER], CUSTOMERS)
    with pytest.raises(ValueError, match="customer_id does not identify a customer"):
        reconcile_orders(previous, [], [])
