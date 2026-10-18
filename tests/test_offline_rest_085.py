"""Source-derived Functions edge cases beyond the distributed examples."""

import json
import sys
from pathlib import Path

import httpx
from foundry_sdk.v2.functions.execution import ExecutionClient
from foundry_sdk.v2.functions.query import QueryClient


COMMON = (
    Path(__file__).resolve().parents[1]
    / ".agents/skills/pal-found-dev/examples/rest/common"
)
sys.path.insert(0, str(COMMON))
from mock_transport import mock_resource  # noqa: E402


def test_execute_async_optional_selectors_and_immediate_completion() -> None:
    """SDK sends selectors to documented locations and decodes completed variant."""
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"type": "completed", "value": 6})

    with mock_resource(QueryClient, handle) as queries:
        result = queries.execute_async(
            "scale",
            parameters={"amount": 2, "factor": 3},
            branch="master",
            ontology="sample-ontology",
            preview=True,
            transaction_id="synthetic-transaction",
            version="1.0.0",
            request_timeout=5,
        )

    assert len(requests) == 1
    request = requests[0]
    assert request.method == "POST"
    assert request.url.path == "/api/v2/functions/queries/scale/executeAsync"
    assert dict(request.url.params) == {
        "preview": "true",
        "transactionId": "synthetic-transaction",
    }
    assert json.loads(request.content) == {
        "ontology": "sample-ontology",
        "parameters": {"amount": 2, "factor": 3},
        "version": "1.0.0",
        "branch": "master",
    }
    assert result.type == "completed"
    assert result.value == 6


def test_get_result_omits_default_long_poll_timeout() -> None:
    """SDK leaves timeout absent for an immediate status check."""
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"type": "running"})

    with mock_resource(ExecutionClient, handle) as executions:
        result = executions.get_result("synthetic-execution", request_timeout=5)

    assert len(requests) == 1
    request = requests[0]
    assert request.method == "POST"
    assert request.url.path == "/api/v2/functions/executions/synthetic-execution/getResult"
    assert json.loads(request.content) == {}
    assert result.type == "running"
