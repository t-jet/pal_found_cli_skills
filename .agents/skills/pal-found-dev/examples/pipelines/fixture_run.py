"""Run business-rule fixtures without Foundry, public access or Spark.

These checks do not execute a Foundry decorator, expectation, preview or build.
"""

from order_rules import build_orders, reconcile_orders


def main():
    customers = [{"customer_id": "c1", "customer_name": "Ada"}]
    orders = [{"order_id": "o1", "customer_id": "c1", "total_cents": 1200}]
    assert build_orders(orders, customers) == [
        {"order_id": "o1", "customer_id": "c1", "customer_name": "Ada", "total_cents": 1200},
    ]
    assert build_orders([], customers) == []
    failures = [
        (orders * 2, customers, "duplicate order_id"),
        (orders, customers * 2, "duplicate customer_id"),
        ([{**orders[0], "customer_id": None}], customers, "customer_id does not identify a customer"),
        ([{**orders[0], "total_cents": -1}], customers, "total_cents must be a nonnegative integer"),
    ]
    for values, references, message in failures:
        try:
            build_orders(values, references)
        except ValueError as error:
            assert str(error) == message
        else:
            raise AssertionError("bad input unexpectedly accepted")
    prior = build_orders(orders, customers)
    added = [{"order_id": "o2", "customer_id": "c1", "total_cents": 500}]
    assert reconcile_orders(prior, added, customers) == build_orders(orders + added, customers)
    renamed = [{"customer_id": "c1", "customer_name": "Grace"}]
    assert reconcile_orders(prior, added, renamed) == [
        {"order_id": "o1", "customer_id": "c1", "customer_name": "Grace", "total_cents": 1200},
        {"order_id": "o2", "customer_id": "c1", "customer_name": "Grace", "total_cents": 500},
    ]
    assert reconcile_orders([], orders + added, renamed) == build_orders(orders + added, renamed)
    try:
        reconcile_orders(prior, orders, customers)
    except ValueError as error:
        assert str(error) == "duplicate order_id"
    else:
        raise AssertionError("replayed order key unexpectedly accepted")
    print("business fixtures passed: joined row, empty input and four rejected inputs")
    print("incremental fixtures passed: append/full equivalence, renamed reference, recompute and replay rejection")


if __name__ == "__main__":
    main()
