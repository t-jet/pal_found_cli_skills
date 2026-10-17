"""Regression checks for SDK Query SSE framing and fixture lifetimes."""

import json
from pathlib import Path
import socket
import sys

import httpx
import pytest
from foundry_sdk.v2.functions.query import QueryClient

EXAMPLES = (
    Path(__file__).parents[1]
    / ".agents/skills/pal-found-dev/examples/rest/085/v2/functions/Query"
)
sys.path.insert(0, str(EXAMPLES))
from sse_fixture import TrackingStream, framed, mock_resource, verify  # noqa: E402


@pytest.mark.parametrize(
    ("operation", "permission_error"),
    [
        ("streaming_execute", "StreamingExecuteQueryPermissionDenied"),
        ("streaming_execute_events", "StreamingExecuteEventsQueryPermissionDenied"),
    ],
)
def test_typed_sse_fixture_handles_data_errors_budgets_and_cleanup(
    monkeypatch, operation, permission_error
):
    def deny_network(*_args, **_kwargs):
        raise AssertionError("SSE fixture attempted a network connection")

    monkeypatch.setattr(socket.socket, "connect", deny_network)
    verify(operation, permission_error)


@pytest.mark.parametrize("operation", ["streaming_execute", "streaming_execute_events"])
def test_prior_raw_decode_fails_on_valid_sse_frame(operation):
    stream = TrackingStream(framed({"type": "data", "value": [6]}))

    def handler(_request):
        return httpx.Response(
            200, headers={"content-type": "text/event-stream"}, stream=stream
        )

    with mock_resource(QueryClient, handler) as client:
        raw = getattr(client.with_raw_response, operation)(
            "synthetic-value", parameters={}, request_timeout=5
        )
        try:
            with pytest.raises(json.JSONDecodeError):
                raw.decode()
        finally:
            raw.close()
    assert stream.closed


def test_rid_metadata_prerelease_selector_is_explicit():
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(200, json={})

    rid = "ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001"
    with mock_resource(QueryClient, handler) as client:
        for include in (None, True):
            response = client.with_raw_response.get_by_rid(
                rid=rid, include_prerelease=include, request_timeout=5
            )
            response.close()
            body = {"rid": rid}
            if include is not None:
                body["includePrerelease"] = include
            response = client.with_raw_response.get_by_rid_batch(
                body=[body], request_timeout=5
            )
            response.close()

    assert len(requests) == 4
    assert "includePrerelease" not in requests[0].url.params
    assert json.loads(requests[1].content) == [{"rid": rid}]
    assert requests[2].url.params["includePrerelease"] == "true"
    assert json.loads(requests[3].content) == [
        {"rid": rid, "includePrerelease": True}
    ]
