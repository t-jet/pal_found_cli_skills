"""Notebook-equivalent cells; requires registered Foundry aliases at runtime."""

from numbers import Number

from foundry.transforms import Dataset

orders = Dataset.get("orders").read_table(format="arrow").to_pandas()
assert {"customer_id", "amount"}.issubset(orders.columns)
assert orders["customer_id"].notna().all()
if not orders["amount"].dropna().map(
    lambda value: isinstance(value, Number) and not isinstance(value, (bool, complex))
).all():
    raise TypeError("amount must contain numeric values or nulls")
orders["amount"] = orders["amount"].fillna(0)
totals = orders.groupby("customer_id", as_index=False)["amount"].sum()
totals = totals.rename(columns={"amount": "total_amount"})
assert totals["customer_id"].is_unique
if not totals["total_amount"].map(
    lambda value: isinstance(value, Number) and not isinstance(value, (bool, complex))
).all():
    raise TypeError("total_amount must be numeric")
Dataset.get("customer_totals").write_table(totals)
