"""Illustrative Foundry transform for small, bounded input tables.

Requires the prepared current single-node transforms API and pandas.
Replace every /EXAMPLE path with an authorized enrollment resource path.
"""

import pandas as pd
from transforms.api import Check, Input, Output, transform
from transforms import expectations as E
from .order_rules import build_orders


@transform.using(
    output=Output("/EXAMPLE/Orders/clean", checks=[
        Check(E.primary_key("order_id"), "Unique order key", on_error="FAIL"),
        Check(E.col("customer_name").non_null(), "Customer resolved", on_error="FAIL"),
    ]),
    orders=Input("/EXAMPLE/Orders/raw"),
    customers=Input("/EXAMPLE/Customers/reference"),
)
def compute(output, orders, customers):
    rows = build_orders(orders.pandas().to_dict("records"),
                        customers.pandas().to_dict("records"))
    frame = pd.DataFrame(rows, columns=[
        "order_id", "customer_id", "customer_name", "total_cents",
    ]).astype({"order_id": "string", "customer_id": "string",
               "customer_name": "string", "total_cents": "int64"})
    output.write_table(frame)
