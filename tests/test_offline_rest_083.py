"""Offline REST 083 checks use real SDK serialization and local HTTP responses."""

import http.client
import json
import runpy
import socket
import urllib.request
from pathlib import Path

import httpx
import pytest
from foundry_sdk import PermissionDeniedError, TimeoutError as SDKTimeoutError
from foundry_sdk.v2.ontologies import models


BASE = Path(__file__).resolve().parents[1] / ".agents/skills/pal-found-dev/examples/rest/083/v2/ontologies"
EXAMPLES = sorted(BASE.rglob("invoke_*.py"))
CORRECTED = [
    ("Action", "apply"), ("Action", "apply_batch"),
    ("Action", "apply_with_overrides"), ("Action", "apply_batch_with_overrides"),
    ("Attachment", "upload"), ("Attachment", "upload_with_rid"),
    ("GeotemporalSeriesProperty", "load_geotemporal_series_entries"),
    ("TimeSeriesPropertyV2", "stream_points"),
    ("TimeSeriesValueBankProperty", "stream_values"),
]


@pytest.fixture(autouse=True)
def deny_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("REST083 external connection or DNS denied")

    for name in ("connect", "connect_ex"):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ("create_connection", "getaddrinfo", "gethostbyname", "gethostbyname_ex"):
        monkeypatch.setattr(socket, name, denied)
    monkeypatch.setattr(http.client.HTTPConnection, "connect", denied)
    monkeypatch.setattr(http.client.HTTPSConnection, "connect", denied)
    monkeypatch.setattr(urllib.request, "urlopen", denied)
    monkeypatch.setattr(httpx.HTTPTransport, "handle_request", denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, "handle_async_request", denied)


def example(resource, operation):
    return runpy.run_path(str(BASE / resource / f"invoke_{operation}.py"))["invoke"].__globals__


def resource_class(example_module):
    return next(value for key, value in example_module.items()
                if key.endswith("Client") and isinstance(value, type))


@pytest.mark.parametrize("path", EXAMPLES, ids=lambda path: f"{path.parent.name}.{path.stem}")
def test_reader_fixture(path):
    runpy.run_path(str(path))["verify"]()


@pytest.mark.parametrize("resource,operation", CORRECTED)
@pytest.mark.parametrize("failure", ["permission", "timeout"])
def test_corrected_calls_propagate_failure_without_business_success(resource, operation, failure):
    module = example(resource, operation)
    requests = []

    def handler(request):
        requests.append(request)
        if failure == "timeout":
            raise httpx.ReadTimeout("synthetic uncertain response", request=request)
        return httpx.Response(403, json={
            "errorName": "PermissionDenied", "errorCode": "PERMISSION_DENIED",
            "errorInstanceId": "00000000-0000-0000-0000-000000000009", "parameters": {},
        })

    with module["mock_resource"](resource_class(module), handler) as client:
        with pytest.raises(PermissionDeniedError if failure == "permission" else SDKTimeoutError):
            raw = module["invoke"](client)
            try:
                raw.decode()
            finally:
                raw.close()
    assert len(requests) == 1


@pytest.mark.parametrize("operation", ["apply", "apply_with_overrides"])
@pytest.mark.parametrize("result", [None, "INVALID"])
def test_single_action_requires_positive_validation_from_http_200(operation, result):
    module = example("Action", operation)
    body = {} if result is None else {"validation": {
        "result": result, "submissionCriteria": [], "parameters": {},
    }}
    with module["mock_resource"](resource_class(module), lambda request: httpx.Response(200, json=body)) as client:
        raw = module["invoke"](client)
        try:
            decoded = raw.decode()
        finally:
            raw.close()
    with pytest.raises(ValueError, match="validation"):
        module["check_outcome"](decoded)


@pytest.mark.parametrize("operation", ["apply_batch", "apply_batch_with_overrides"])
def test_batch_empty_response_is_schema_valid_but_unconfirmed(operation):
    module = example("Action", operation)
    decoded = models.BatchApplyActionResponseV2.model_validate({})
    with pytest.raises(ValueError, match="evidence is absent"):
        module["check_outcome"](decoded)


@pytest.mark.parametrize("operation", ["apply_with_overrides", "apply_batch_with_overrides"])
def test_override_ids_and_current_time_reach_wire(operation):
    module = example("Action", operation)
    seen = []

    def handler(request):
        body = json.loads(request.content)
        item = body["requests"][0] if "requests" in body else body
        assert item["overrides"]["uniqueIdentifierLinkIdValues"] == {
            "00000000-0000-0000-0000-000000000001": "00000000-0000-0000-0000-000000000002"
        }
        assert item["overrides"]["actionExecutionTime"] == "2026-01-01T00:00:00+00:00"
        parameters = item["parameters"] if "parameters" in item else item["request"]["parameters"]
        assert parameters == {"assetId": "A-1", "status": "ready"}
        seen.append(body)
        return httpx.Response(200, json={})

    with module["mock_resource"](resource_class(module), handler) as client:
        raw = module["invoke"](client)
        raw.close()
    assert len(seen) == 1


@pytest.mark.parametrize("operation", ["upload", "upload_with_rid"])
@pytest.mark.parametrize("field,value", [("sizeBytes", "1"), ("filename", "wrong.txt"), ("mediaType", "wrong/type")])
def test_upload_rejects_inconsistent_metadata(operation, field, value):
    module = example("Attachment", operation)
    module["SUCCESS"][field] = value
    with pytest.raises(AssertionError):
        module["verify"]()


def test_geotemporal_range_bounds_are_optional_in_sdk():
    assert models.AbsoluteTimeRange.model_validate({"type": "absolute"}).start_time is None


@pytest.mark.parametrize("fault", ["repeated", "budget", "missing_position", "empty_continuation"])
def test_geotemporal_pagination_completeness(fault):
    module = example("GeotemporalSeriesProperty", "load_geotemporal_series_entries")
    requests = []

    def handler(request):
        body = json.loads(request.content)
        assert body["range"]["startTime"] == "2026-01-01T00:00:00+00:00"
        assert body["range"]["endTime"] == "2026-01-01T00:02:00+00:00"
        requests.append(body)
        if fault == "missing_position":
            return httpx.Response(200, json={"data": [{"time": "2026-01-01T00:00:00Z"}]})
        if fault == "empty_continuation" and len(requests) == 2:
            return httpx.Response(200, json={"data": [{
                "time": "2026-01-01T00:01:00Z", "position": {"type": "Point", "coordinates": [23.3, 42.7]}
            }]})
        return httpx.Response(200, json={"data": [], "nextPageToken": "same" if fault == "repeated" else str(len(requests))})

    with module["mock_resource"](resource_class(module), handler) as client:
        if fault == "empty_continuation":
            entries = module["load_entries"](client)
            assert len(entries) == 1
            assert requests[1]["pageToken"] == "1"
        else:
            message = {"repeated": "Repeated", "budget": "budget exceeded", "missing_position": "time and position"}[fault]
            with pytest.raises(ValueError, match=message):
                module["load_entries"](client, page_budget=2)
    assert len(requests) <= 2


@pytest.mark.parametrize("resource,operation", CORRECTED[-2:])
@pytest.mark.parametrize("payload,message", [
    (b'[{"time":"2026-01-01T00:00:30Z","value":23.5}]', None),
    (b'[{"time":"2026-01-01T00:02:00Z","value":23.5}]', "outside requested"),
    (b'[{"time":"2026-01-01T00:00:30Z"}]', "time and value"),
    (b'{}', "JSON array"), (b'[{', None),
])
def test_stream_decoding_requires_complete_records(resource, operation, payload, message):
    module = example(resource, operation)
    chunks = [payload[index:index+3] for index in range(0, len(payload), 3)]
    if payload == b'[{':
        with pytest.raises(json.JSONDecodeError):
            module["parse_records"](chunks)
    elif message:
        with pytest.raises(ValueError, match=message):
            module["parse_records"](chunks)
    else:
        records = module["parse_records"](chunks)
        assert records[0]["value"] == 23.5


@pytest.mark.parametrize("resource,operation", CORRECTED[-2:])
@pytest.mark.parametrize("payload,byte_budget,error", [
    (b"x" * 20, 4, ValueError),
    (b"[{", 4096, json.JSONDecodeError),
    (b'[{}]', 4096, ValueError),
])
def test_stream_closes_response_on_failure(resource, operation, payload, byte_budget, error):
    module = example(resource, operation)
    replies = []

    def handler(request):
        response = httpx.Response(200, content=payload)
        replies.append(response)
        return response

    with module["mock_resource"](resource_class(module), handler) as client:
        kwargs = dict(ontology="synthetic-value", object_type="Asset", primary_key="A-1", property="synthetic-value", range=module["EXPECTED_BODY"]["range"], request_timeout=30)
        if operation == "stream_points":
            kwargs["format"] = "JSON"
        with pytest.raises(error):
            with getattr(client.with_streaming_response, operation)(**kwargs) as response:
                module["parse_records"](response.iter_bytes(chunk_size=3), byte_budget=byte_budget)
    assert replies[0].is_closed


def test_network_guards_are_active():
    for call in (lambda: socket.getaddrinfo("example.invalid", 443),
                 lambda: socket.create_connection(("example.invalid", 443)),
                 lambda: urllib.request.urlopen("https://example.invalid")):
        with pytest.raises(AssertionError, match="denied"):
            call()
