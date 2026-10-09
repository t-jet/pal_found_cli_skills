"""Pinned SDK fixture for a submitted global Query and bounded result polling.

The synthetic Query `scale(amount, factor)` returns an integer. This fixture
uses SDK 1.101.0 with an in-process HTTP transport; no Query runs in Foundry.
"""

import json
import sys
from pathlib import Path

import httpx
from foundry_sdk.v2.functions.execution import ExecutionClient
from foundry_sdk.v2.functions.query import QueryClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from mock_transport import mock_resource


def verify() -> None:
    execution_id = "synthetic-scale-run-1"

    def submitted(request: httpx.Request) -> httpx.Response:
        assert request.method == "POST"
        assert request.url.path == "/api/v2/functions/queries/scale/executeAsync"
        assert json.loads(request.content) == {
            "parameters": {"amount": 2, "factor": 3}, "version": "1.0.0"
        }
        return httpx.Response(200, json={"type": "submitted", "executionId": execution_id})

    with mock_resource(QueryClient, submitted) as queries:
        submission = queries.execute_async(
            "scale", parameters={"amount": 2, "factor": 3}, version="1.0.0",
            request_timeout=30,
        )
        assert submission.type == "submitted"
        assert submission.execution_id == execution_id

    polls = 0

    def result(request: httpx.Request) -> httpx.Response:
        nonlocal polls
        assert request.method == "POST"
        assert request.url.path == f"/api/v2/functions/executions/{execution_id}/getResult"
        assert json.loads(request.content) == {"timeout": 1}
        polls += 1
        return httpx.Response(200, json=(
            {"type": "running"} if polls == 1 else {"type": "succeeded", "value": 6}
        ))

    with mock_resource(ExecutionClient, result) as executions:
        for _ in range(3):  # Finite budget; production code also needs an overall deadline.
            outcome = executions.get_result(execution_id, timeout=1, request_timeout=5)
            if outcome.type == "succeeded":
                assert outcome.value == 6
                break
        else:
            raise AssertionError("Execution did not finish within polling budget")
    assert polls == 2


if __name__ == "__main__":
    verify()
    print("Query submitted, running then succeeded; bounded SDK polling passed")
