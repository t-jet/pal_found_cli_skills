"""Business rules shared by the small single-node transform and fixtures."""

def build_orders(orders, customers):
    customer_names = {}
    for customer in customers:
        key = customer.get("customer_id")
        name = customer.get("customer_name")
        if not isinstance(key, str) or not key or not isinstance(name, str) or not name:
            raise ValueError("customer_id and customer_name must be nonempty strings")
        if key in customer_names:
            raise ValueError("duplicate customer_id")
        customer_names[key] = name

    result = []
    seen = set()
    for order in orders:
        key = order.get("order_id")
        customer = order.get("customer_id")
        amount = order.get("total_cents")
        if not isinstance(key, str) or not key:
            raise ValueError("order_id must be a nonempty string")
        if key in seen:
            raise ValueError("duplicate order_id")
        if customer not in customer_names:
            raise ValueError("customer_id does not identify a customer")
        if type(amount) is not int or amount < 0:
            raise ValueError("total_cents must be a nonnegative integer")
        seen.add(key)
        result.append({"order_id": key, "customer_id": customer,
                       "customer_name": customer_names[customer], "total_cents": amount})
    return result


def reconcile_orders(previous_output, added_orders, current_customers):
    """Rejoin accumulated raw orders against the current customer snapshot."""
    raw_previous = [
        {key: row[key] for key in ("order_id", "customer_id", "total_cents")}
        for row in previous_output
    ]
    return build_orders(raw_previous + list(added_orders), current_customers)
