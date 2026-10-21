"""SQLite arithmetic fixture; does not verify Spark types or Foundry SQL publication."""

import sqlite3
from pathlib import Path


query = Path(__file__).with_name("customer_totals.sql").read_text(encoding="utf-8")
with sqlite3.connect(":memory:") as connection:
    connection.execute("CREATE TABLE `/Demo/orders` (order_id TEXT, customer_id TEXT, amount NUMERIC)")
    connection.execute("CREATE TABLE `/Demo/customers` (customer_id TEXT, region TEXT)")
    connection.executemany("INSERT INTO `/Demo/orders` VALUES (?, ?, ?)",
                           [("o1", "c1", 10), ("o2", "c1", 7.5), ("o3", "c2", None)])
    connection.executemany("INSERT INTO `/Demo/customers` VALUES (?, ?)",
                           [("c1", "West"), ("c2", "East")])
    connection.execute(query)
    actual = connection.execute("SELECT * FROM `/Demo/customer_totals` ORDER BY customer_id").fetchall()
    assert actual == [("c1", "West", 17.5, 2), ("c2", "East", 0, 1)], actual
    connection.execute("INSERT INTO `/Demo/customers` VALUES ('c1', 'West')")
    duplicates = connection.execute(
        "SELECT customer_id FROM `/Demo/customers` GROUP BY customer_id HAVING COUNT(*) > 1"
    ).fetchall()
    assert duplicates == [("c1",)], duplicates
    connection.execute("DROP TABLE `/Demo/customer_totals`")
    connection.execute(query)
    multiplied = connection.execute(
        "SELECT total_amount, order_count FROM `/Demo/customer_totals` WHERE customer_id = 'c1'"
    ).fetchone()
    assert multiplied == (35, 4), multiplied
print("Synthetic SQL arithmetic fixture passed; Spark/Foundry execution not tested.")
