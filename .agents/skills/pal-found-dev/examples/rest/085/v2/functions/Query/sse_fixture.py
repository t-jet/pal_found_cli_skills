"""Bounded, offline SSE examples for the two Query streaming operations."""

from dataclasses import dataclass
import json
from pathlib import Path
import sys
import time
from typing import Any, Callable

import httpx
from foundry_sdk import PalantirRPCException
from foundry_sdk.v2.functions.query import QueryClient

sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "common"))
from mock_transport import mock_resource

QUERY_NAME = "synthetic-value"
ERROR_ID = "00000000-0000-0000-0000-000000000004"


@dataclass(frozen=True)
class StreamOutcome:
    batches: list[list[Any]]
    reason: str
    error: Any = None
    events: int = 0
    payload_bytes: int = 0


def consume_sse(
    response: Any,
    *,
    max_events: int,
    max_payload_bytes: int,
    deadline: float,
    clock: Callable[[], float] = time.monotonic,
) -> StreamOutcome:
    """Stop within finite decoded-payload and event budgets; caller owns context."""
    if max_events < 1 or max_payload_bytes < 1:
        raise ValueError("SSE event and payload byte budgets must be positive")

    batches: list[list[Any]] = []
    count = 0
    used_bytes = 0
    events = iter(response.iter_sse())
    while count < max_events:
        if clock() >= deadline:
            return StreamOutcome(batches, "deadline", events=count, payload_bytes=used_bytes)
        try:
            event = next(events)
        except StopIteration:
            return StreamOutcome(batches, "complete", events=count, payload_bytes=used_bytes)
        if clock() >= deadline:
            return StreamOutcome(batches, "deadline", events=count, payload_bytes=used_bytes)

        payload = event.data.model_dump(mode="json", by_alias=True, exclude_none=True)
        size = len(json.dumps(payload, separators=(",", ":")).encode("utf-8"))
        if used_bytes + size > max_payload_bytes:
            return StreamOutcome(batches, "payload_byte_limit", events=count, payload_bytes=used_bytes)
        used_bytes += size
        count += 1

        if event.data.type == "error":
            return StreamOutcome(batches, "query_error", event.data, count, used_bytes)
        if event.data.type != "data" or not isinstance(event.data.value, list):
            raise ValueError("Query SSE data event must contain a result batch")
        batches.append(event.data.value)
    return StreamOutcome(batches, "event_limit", events=count, payload_bytes=used_bytes)


class TrackingStream(httpx.SyncByteStream):
    def __init__(self, body: bytes):
        self.body = body
        self.closed = False

    def __iter__(self):
        midpoint = len(self.body) // 2
        yield self.body[:midpoint]
        yield self.body[midpoint:]

    def close(self):
        self.closed = True


def framed(*payloads: dict[str, Any]) -> bytes:
    return b"".join(
        b"data: " + json.dumps(payload).encode("utf-8") + b"\n\n"
        for payload in payloads
    )


def verify(operation: str, permission_error: str) -> None:
    path = f"/api/v2/functions/queries/{QUERY_NAME}/" + (
        "streamingExecuteEvents" if operation == "streaming_execute_events" else "streamingExecute"
    )

    def check_request(request: httpx.Request) -> None:
        assert request.method == "POST"
        assert request.url.path == path
        assert request.headers["Authorization"] == "Bearer offline-fixture-token"
        assert request.headers["Content-Type"] == "application/json"
        assert request.headers["Accept"] == "text/event-stream"
        assert json.loads(request.content) == {"parameters": {}}
        assert not request.url.params

    def invoke(client: QueryClient):
        return getattr(client, operation)(QUERY_NAME, parameters={}, request_timeout=5)

    def exercise(payloads: tuple[dict[str, Any], ...], **budgets: Any) -> StreamOutcome:
        stream = TrackingStream(framed(*payloads))

        def success(request: httpx.Request) -> httpx.Response:
            check_request(request)
            return httpx.Response(
                200, headers={"content-type": "text/event-stream"}, stream=stream
            )

        with mock_resource(QueryClient, success) as client:
            with invoke(client) as response:
                outcome = consume_sse(
                    response,
                    max_events=budgets.get("max_events", 8),
                    max_payload_bytes=budgets.get("max_payload_bytes", 1024),
                    deadline=budgets.get("deadline", time.monotonic() + 10),
                )
        assert stream.closed
        return outcome

    data = {"type": "data", "value": [6]}
    failure = {
        "type": "error",
        "errorCode": "INVALID_ARGUMENT",
        "errorName": "QueryRuntimeError",
        "errorInstanceId": ERROR_ID,
        "errorDescription": "synthetic failure",
        "parameters": {},
    }
    complete = exercise((data,))
    assert complete.reason == "complete" and complete.batches == [[6]]
    assert complete.events == 1 and complete.payload_bytes > 0

    partial_error = exercise((data, failure))
    assert partial_error.reason == "query_error" and partial_error.batches == [[6]]
    assert partial_error.error.error_name == "QueryRuntimeError"
    assert partial_error.error.error_code == "INVALID_ARGUMENT"

    limited = exercise((data, data), max_events=1)
    assert limited.reason == "event_limit" and limited.batches == [[6]]
    byte_limited = exercise((data,), max_payload_bytes=1)
    assert byte_limited.reason == "payload_byte_limit" and not byte_limited.batches
    expired = exercise((data,), deadline=time.monotonic() - 1)
    assert expired.reason == "deadline" and not expired.batches

    def denied(request: httpx.Request) -> httpx.Response:
        check_request(request)
        return httpx.Response(
            403,
            json={
                "errorName": permission_error,
                "errorCode": "PERMISSION_DENIED",
                "parameters": {"queryApiName": QUERY_NAME},
                "errorInstanceId": ERROR_ID,
            },
        )

    with mock_resource(QueryClient, denied) as client:
        try:
            with invoke(client):
                raise AssertionError("Permission denial opened an SSE response")
        except PalantirRPCException as error:
            assert error.name == permission_error
            assert error.parameters == {"queryApiName": QUERY_NAME}
        else:
            raise AssertionError(f"Expected {permission_error}")
