"""Notebook-equivalent cells; requires registered Foundry aliases at runtime."""

from foundry.transforms import Dataset

orders = Dataset.get("orders").read_table(format="arrow").to_pandas()
assert {"customer_id", "amount"}.issubset(orders.columns)
assert orders["customer_id"].notna().all()
orders["amount"] = orders["amount"].fillna(0)
totals = orders.groupby("customer_id", as_index=False)["amount"].sum()
totals = totals.rename(columns={"amount": "total_amount"})
assert totals["customer_id"].is_unique
Dataset.get("customer_totals").write_table(totals)
