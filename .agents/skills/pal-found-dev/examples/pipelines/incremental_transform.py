"""Single-node incremental example using a full customer snapshot each run.

Requires prepared transforms and pandas. Orders must be append-only between
incremental runs; duplicate order keys fail. /EXAMPLE paths are placeholders.
"""

import pandas as pd
from transforms.api import Check, Input, Output, incremental, transform
from transforms import expectations as E

from .order_rules import reconcile_orders


@incremental(semantic_version=1, snapshot_inputs=["customers"])
@transform.using(
    orders=Input("/EXAMPLE/Orders/raw"),
    customers=Input("/EXAMPLE/Customers/reference"),
    output=Output("/EXAMPLE/Orders/clean_incremental", checks=[
        Check(E.primary_key("order_id"), "Unique order key", on_error="FAIL"),
    ]),
)
def compute(ctx, orders, customers, output):
    previous = output.pandas(mode="previous").to_dict("records") if ctx.is_incremental else []
    rows = reconcile_orders(
        previous,
        orders.pandas().to_dict("records"),
        customers.pandas().to_dict("records"),
    )
    frame = pd.DataFrame(rows, columns=[
        "order_id", "customer_id", "customer_name", "total_cents",
    ]).astype({
        "order_id": "string", "customer_id": "string",
        "customer_name": "string", "total_cents": "int64",
    })
    output.set_mode("replace")
    output.write_table(frame)
