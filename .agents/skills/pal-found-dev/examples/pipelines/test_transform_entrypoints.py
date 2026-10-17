"""Exercise actual single-node entry points with local decorator stubs.

The stubs register source functions only. They do not emulate Foundry's
incremental planner, checks, repository preview, or transaction service.
"""

import importlib
import socket
import sys
import types
from pathlib import Path

import pandas as pd
import pytest


class TableInput:
    """Supply deterministic rows through the transform input protocol."""

    def __init__(self, rows):
        self.frame = pd.DataFrame(rows)

    def pandas(self):
        return self.frame


class TableOutput:
    """Record requested output mode and complete written table."""

    def __init__(self, previous=()):
        self.previous = pd.DataFrame(previous)
        self.mode = None
        self.written = None

    def pandas(self, *, mode):
        assert mode == "previous"
        return self.previous

    def set_mode(self, mode):
        self.mode = mode

    def write_table(self, frame):
        self.written = frame


@pytest.fixture
def transform_modules(monkeypatch):
    """Load real source with inert local substitutes for missing decorators."""

    def blocked(*args, **kwargs):
        raise AssertionError("network request in offline transform fixture")

    monkeypatch.setattr(socket, "getaddrinfo", blocked)
    monkeypatch.setattr(socket.socket, "connect", blocked)
    monkeypatch.setattr(socket.socket, "connect_ex", blocked)
    monkeypatch.setattr(socket, "create_connection", blocked)

    def decorator(*args, **kwargs):
        return lambda function: function

    package = types.ModuleType("offline_pipeline_fixture")
    package.__path__ = [str(Path(__file__).parent)]
    transforms = types.ModuleType("transforms")
    api = types.ModuleType("transforms.api")
    api.transform = types.SimpleNamespace(using=decorator)
    api.incremental = decorator
    api.Check = api.Input = api.Output = lambda *args, **kwargs: None
    expectations = types.ModuleType("transforms.expectations")
    expectations.primary_key = lambda *args: None
    expectations.col = lambda *args: types.SimpleNamespace(non_null=lambda: None)
    transforms.expectations = expectations
    monkeypatch.setitem(sys.modules, package.__name__, package)
    monkeypatch.setitem(sys.modules, "transforms", transforms)
    monkeypatch.setitem(sys.modules, "transforms.api", api)
    monkeypatch.setitem(sys.modules, "transforms.expectations", expectations)
    for name in ("order_rules", "single_node_transform", "incremental_transform"):
        monkeypatch.delitem(sys.modules, f"{package.__name__}.{name}", raising=False)
    return (
        importlib.import_module(f"{package.__name__}.single_node_transform"),
        importlib.import_module(f"{package.__name__}.incremental_transform"),
    )


def test_single_node_entrypoint_writes_complete_result_and_rejects_duplicate(transform_modules):
    single_node, _ = transform_modules
    order = {"order_id": "o1", "customer_id": "c1", "total_cents": 1200}
    customers = [{"customer_id": "c1", "customer_name": "Ada"}]
    output = TableOutput()
    single_node.compute(output, TableInput([order]), TableInput(customers))
    assert output.written.to_dict("records") == [
        {"order_id": "o1", "customer_id": "c1", "customer_name": "Ada", "total_cents": 1200}
    ]
    assert list(output.written.columns) == [
        "order_id", "customer_id", "customer_name", "total_cents"
    ]
    with pytest.raises(ValueError, match="duplicate order_id"):
        single_node.compute(TableOutput(), TableInput([order, order]), TableInput(customers))


@pytest.mark.parametrize("is_incremental,expected_name", [(False, "Ada"), (True, "Grace")])
def test_incremental_entrypoint_uses_previous_only_when_selected(
    transform_modules, is_incremental, expected_name,
):
    _, incremental = transform_modules
    previous = [{
        "order_id": "o1", "customer_id": "c1", "customer_name": "Ada", "total_cents": 1200,
    }]
    new = [{"order_id": "o2", "customer_id": "c1", "total_cents": 500}]
    customers = [{"customer_id": "c1", "customer_name": "Grace" if is_incremental else "Ada"}]
    output = TableOutput(previous)
    context = types.SimpleNamespace(is_incremental=is_incremental)
    incremental.compute(context, TableInput(new), TableInput(customers), output)
    expected = [
        {"order_id": "o1", "customer_id": "c1", "customer_name": expected_name, "total_cents": 1200},
        {"order_id": "o2", "customer_id": "c1", "customer_name": expected_name, "total_cents": 500},
    ] if is_incremental else [
        {"order_id": "o2", "customer_id": "c1", "customer_name": expected_name, "total_cents": 500},
    ]
    assert output.mode == "replace"
    assert output.written.to_dict("records") == expected
