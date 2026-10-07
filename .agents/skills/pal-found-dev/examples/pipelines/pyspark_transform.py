"""Illustrative distributed variant; requires prepared PySpark transforms.

Input order schema: order_id/customer_id strings, total_cents long.
Customer schema: customer_id/customer_name strings. Replace /EXAMPLE paths.
"""

from transforms.api import Check, Input, Output, transform_df
from transforms import expectations as E


def shape_orders(orders, customers):
    return orders.join(customers, "customer_id", "left").select(
        "order_id", "customer_id", "customer_name", "total_cents",
    )


@transform_df(
    Output("/EXAMPLE/Orders/clean", checks=[
        Check(E.primary_key("order_id"), "Unique order key", on_error="FAIL"),
        Check(E.col("customer_name").non_null(), "Customer resolved", on_error="FAIL"),
        Check(E.col("total_cents").non_null(), "Amount present", on_error="FAIL"),
        Check(E.col("total_cents").gte(0), "Nonnegative amount", on_error="FAIL"),
    ]),
    orders=Input("/EXAMPLE/Orders/raw"),
    customers=Input("/EXAMPLE/Customers/reference"),
)
def compute(orders, customers):
    return shape_orders(orders, customers)
