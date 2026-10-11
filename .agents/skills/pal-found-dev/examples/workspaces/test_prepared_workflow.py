"""Prepared SQL and workspace examples; no Foundry service is contacted."""

import runpy
import sqlite3
import sys
import types
from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pytest


WORKSPACE = Path(__file__).with_name("transform.py")
SQL = Path(__file__).parents[1] / "sql" / "customer_totals.sql"


def run_workspace(rows: list[dict], *, reject_write: bool = False) -> pd.DataFrame | None:
    """Run the actual notebook cells with registered, in-memory Dataset aliases."""

    class Dataset:
        written: pd.DataFrame | None = None

        def __init__(self, alias: str) -> None:
            self.alias = alias

        @classmethod
        def get(cls, alias: str) -> "Dataset":
            if alias not in {"orders", "customer_totals"}:
                raise KeyError(alias)
            return cls(alias)

        def read_table(self, *, format: str) -> "Dataset":
            assert self.alias == "orders"
            assert format == "arrow"
            return self

        def to_pandas(self) -> pd.DataFrame:
            return pd.DataFrame(rows)

        def write_table(self, frame: pd.DataFrame) -> None:
            assert self.alias == "customer_totals"
            if reject_write:
                raise PermissionError("output alias is not writable")
            Dataset.written = frame.copy()

    foundry = types.ModuleType("foundry")
    transforms = types.ModuleType("foundry.transforms")
    transforms.Dataset = Dataset
    foundry.transforms = transforms
    with patch.dict(sys.modules, {"foundry": foundry, "foundry.transforms": transforms}):
        runpy.run_path(str(WORKSPACE))
    return Dataset.written


def test_workspace_null_and_repeated_orders_produce_declared_output() -> None:
    """Repeated order keys aggregate; null amount uses the example's zero rule."""

    written = run_workspace(
        [
            {"customer_id": "c1", "amount": 10.0},
            {"customer_id": "c1", "amount": 7.5},
            {"customer_id": "c2", "amount": None},
        ]
    )
    assert written is not None
    assert list(written.columns) == ["customer_id", "total_amount"]
    assert written.to_dict("records") == [
        {"customer_id": "c1", "total_amount": 17.5},
        {"customer_id": "c2", "total_amount": 0.0},
    ]
    assert written["customer_id"].is_unique


@pytest.mark.parametrize(
    "rows, error",
    [
        ([{"customer_id": "c1"}], AssertionError),
        ([{"amount": 10}], AssertionError),
        ([{"customer_id": None, "amount": 10}], AssertionError),
    ],
)
def test_workspace_rejects_missing_schema_null_key_and_invalid_amount(
    rows: list[dict], error: type[Exception]
) -> None:
    """Bad prepared inputs must not yield a saved output frame."""

    with pytest.raises(error):
        run_workspace(rows)


def test_workspace_propagates_rejected_output_write() -> None:
    """A permission failure cannot be mistaken for published data."""

    with pytest.raises(PermissionError, match="not writable"):
        run_workspace([{"customer_id": "c1", "amount": 10}], reject_write=True)


@pytest.mark.parametrize("amount", ["invalid", "12.0", True, 1 + 2j])
def test_workspace_rejects_non_numeric_amount(amount: object) -> None:
    """A schema mismatch must stop before writing an invalid total."""

    with pytest.raises(TypeError, match="amount must contain numeric"):
        run_workspace([{"customer_id": "c1", "amount": amount}])


def test_workspace_all_null_amounts_follow_zero_policy() -> None:
    """The type guard must allow null-only input before the zero fill."""

    written = run_workspace([{"customer_id": "c1", "amount": None}])
    assert written is not None
    assert written.to_dict("records") == [{"customer_id": "c1", "total_amount": 0}]


def test_workspace_rejects_nonnumeric_aggregate_before_write() -> None:
    """An unexpected aggregation result must not pass the output type check."""

    with patch.object(
        pd.core.groupby.generic.DataFrameGroupBy,
        "sum",
        return_value=pd.DataFrame({"customer_id": ["c1"], "amount": ["invalid"]}),
    ):
        with pytest.raises(TypeError, match="total_amount must be numeric"):
            run_workspace([{"customer_id": "c1", "amount": 10}])


def test_workspace_requires_prepared_foundry_runtime() -> None:
    """Without the provided Dataset runtime, the notebook cannot run locally."""

    with patch.dict(sys.modules, {"foundry": None, "foundry.transforms": None}):
        with pytest.raises(ModuleNotFoundError, match="foundry"):
            runpy.run_path(str(WORKSPACE))


def test_sql_authored_query_output_and_join_multiplication() -> None:
    """Execute the authored query in SQLite to check arithmetic, not Spark grammar."""

    query = SQL.read_text(encoding="utf-8")
    assert query.startswith("CREATE TABLE `/Demo/customer_totals` AS\n")
    assert not query.rstrip().endswith(";")
    with sqlite3.connect(":memory:") as db:
        db.execute("CREATE TABLE `/Demo/orders` (order_id TEXT, customer_id TEXT, amount NUMERIC)")
        db.execute("CREATE TABLE `/Demo/customers` (customer_id TEXT, region TEXT)")
        db.executemany(
            "INSERT INTO `/Demo/orders` VALUES (?, ?, ?)",
            [("o1", "c1", 10), ("o2", "c1", 7.5), ("o3", "c2", None)],
        )
        db.executemany(
            "INSERT INTO `/Demo/customers` VALUES (?, ?)",
            [("c1", "West"), ("c2", "East")],
        )
        db.execute(query)
        assert [column[1] for column in db.execute("PRAGMA table_info('/Demo/customer_totals')")] == [
            "customer_id",
            "region",
            "total_amount",
            "order_count",
        ]
        assert db.execute(
            "SELECT * FROM `/Demo/customer_totals` ORDER BY customer_id"
        ).fetchall() == [("c1", "West", 17.5, 2), ("c2", "East", 0, 1)]
        db.execute("INSERT INTO `/Demo/customers` VALUES ('c1', 'West')")
        assert db.execute(
            "SELECT customer_id FROM `/Demo/customers` GROUP BY customer_id HAVING COUNT(*) > 1"
        ).fetchall() == [("c1",)]
        db.execute("DROP TABLE `/Demo/customer_totals`")
        db.execute(query)
        assert db.execute(
            "SELECT total_amount, order_count FROM `/Demo/customer_totals` WHERE customer_id = 'c1'"
        ).fetchone() == (35, 4)
