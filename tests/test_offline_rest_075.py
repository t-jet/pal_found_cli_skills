"""Pipeline SDK examples checked against installed source and semantic invariants.

Synthetic HTTP responses demonstrate decoding and request/result correspondence.
They do not prove server-side scheduling, filter semantics or live health checks.
"""

import ast
import asyncio
import copy
import datetime
import hashlib
import importlib
import importlib.metadata
import inspect
import json
import runpy
import socket
import textwrap
from functools import lru_cache
from pathlib import Path
from typing import get_origin

import httpx
import pytest
from foundry_sdk import PalantirRPCException, ReadTimeout
from pydantic import TypeAdapter, ValidationError


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / ".agents/skills/pal-found-dev/examples/rest/075/v2"
REGISTER = json.loads((ROOT / "maintainer/rest-domain-authoring-register.json").read_text())
ORACLE = json.loads((ROOT / "tests/fixtures/offline/rest-acceptance/source-oracle.json").read_text())
OPERATIONS = {
    ("checkpoints", "Record"): ("get", "get_batch", "search"),
    ("data_health", "Check"): ("create", "delete", "get", "replace"),
    ("data_health", "CheckReport"): ("get", "get_latest"),
    ("orchestration", "Build"): ("cancel", "create", "get", "get_batch", "jobs", "search"),
    ("orchestration", "Job"): ("get", "get_batch"),
    ("orchestration", "Schedule"): ("create", "delete", "get", "get_affected_resources",
                                    "get_batch", "pause", "replace", "run", "runs", "unpause"),
    ("orchestration", "ScheduleVersion"): ("get", "schedule"),
}
CASES = [(service, resource, op) for (service, resource), ops in OPERATIONS.items() for op in ops]
BATCHES = [("checkpoints", "Record"), ("orchestration", "Build"),
           ("orchestration", "Job"), ("orchestration", "Schedule")]
FOUND = "ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001"
OMITTED = "ri.synthetic.main.resource.00000000-0000-0000-0000-000000000002"
OTHER = "ri.synthetic.main.resource.00000000-0000-0000-0000-000000000003"


@pytest.fixture(scope="module")
def offline_event_loop():
    # Windows creates its local socket pair before the public-network guard.
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def deny_public_network(monkeypatch, offline_event_loop):
    def denied(*args, **kwargs):
        raise AssertionError("REST075 attempted public network access")

    for name in ("connect", "connect_ex"):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ("create_connection", "getaddrinfo", "gethostbyname", "gethostbyname_ex"):
        monkeypatch.setattr(socket, name, denied)
    monkeypatch.setattr(httpx.HTTPTransport, "handle_request", denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, "handle_async_request", denied)


def example(service, resource, operation):
    return runpy.run_path(str(BASE / service / resource / f"{operation}.py"))["invoke"].__globals__


@lru_cache
def contract(service, resource, operation):
    snake = "".join(("_" if i else "") + c.lower() if c.isupper() else c
                    for i, c in enumerate(resource))
    module = importlib.import_module(f"foundry_sdk.v2.{service}.{snake}")
    client = getattr(module, resource + "Client")
    tree = ast.parse(textwrap.dedent(inspect.getsource(getattr(client, operation))))
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute) and node.func.attr == "RequestInfo"]
    assert len(calls) == 1
    fields = {kw.arg: kw.value for kw in calls[0].keywords}

    def source_value(node):
        return eval(compile(ast.Expression(node), "<installed SDK contract>", "eval"), vars(module))

    return {
        "client": client,
        "method": ast.literal_eval(fields["method"]),
        "path": ast.literal_eval(fields["resource_path"]),
        "headers": ast.literal_eval(fields["header_params"]),
        "response": source_value(fields["response_type"]),
        "errors": source_value(fields["throwable_errors"]),
        "source_hash": hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest(),
    }


def normalized(value):
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json", by_alias=True, exclude_none=True)
    if isinstance(value, dict):
        return {key: normalized(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalized(child) for child in value]
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    return value


def execute(namespace, source, handler):
    with namespace["mock_resource"](source["client"], handler) as client:
        raw = namespace["invoke"](client)
        try:
            return normalized(raw.decode())
        finally:
            raw.close()


def check_wire(source, request):
    path = source["path"]
    for field in ("recordRid", "checkRid", "checkReportRid", "buildRid", "jobRid",
                  "scheduleRid", "scheduleVersionRid"):
        path = path.replace("{" + field + "}", FOUND)
    assert request.method == source["method"]
    assert request.url.path == "/api" + path
    assert request.headers["Authorization"] == "Bearer offline-fixture-token"
    for key, value in source["headers"].items():
        assert request.headers[key] == value


def check_batch(requested, result):
    # These examples deliberately demonstrate one found and one inaccessible ID.
    assert set(requested) == {FOUND, OMITTED}
    assert set(result["data"]) == {FOUND}
    assert result["data"][FOUND]["rid"] == FOUND
    assert OMITTED not in result["data"]


def check_schedule_action(body, result):
    target = body["action"]["target"]
    returned = result["action"]["target"]
    assert target["type"] == returned["type"] == "upstream"
    assert returned["targetRids"] == target["targetRids"]
    assert returned["ignoredRids"] == target.get("ignoredRids", [])
    assert set(returned["targetRids"]).isdisjoint(returned["ignoredRids"])


def check_check_type_change(parameters, requested_type):
    assert parameters["newCheckType"] == requested_type
    assert parameters["originalCheckType"] != parameters["newCheckType"]


def check_business(resource, operation, request, result):
    body = json.loads(request.content) if request.content else None
    if operation == "get_batch":
        key = resource[0].lower() + resource[1:] + "Rid"
        check_batch([element[key] for element in body], result)
    if resource == "Schedule" and operation in ("create", "replace"):
        check_schedule_action(body, result)
    if resource == "Build" and operation == "search":
        where = body["where"]
        assert where["type"] == "gte" and where["field"] == "STARTED_TIME"
        # SDK value: Any does not validate this illustrative UTC filter literal.
        assert datetime.datetime.fromisoformat(where["value"].replace("Z", "+00:00")).tzinfo
    if operation == "get" and resource != "ScheduleVersion":
        assert result["rid"] == request.url.path.rsplit("/", 1)[1]
    if resource == "Check" and operation in ("create", "replace"):
        assert result["config"]["type"] == body["config"]["type"]
    if operation in ("cancel", "delete", "pause", "unpause"):
        assert result is None


def successful_example(service, resource, operation):
    namespace = example(service, resource, operation)
    source = contract(service, resource, operation)
    requests = []

    def handler(request):
        check_wire(source, request)
        requests.append(request)
        payload = namespace["SUCCESS"]
        return httpx.Response(204) if payload is None else httpx.Response(200, json=payload)

    result = execute(namespace, source, handler)
    assert len(requests) == 1
    return namespace, requests[0], result


def test_owned_operations_match_frozen_source_and_register():
    assert importlib.metadata.version("foundry-platform-sdk") == "1.101.0"
    rows = [row for row in REGISTER["operations"] if row["story"] == "DEV-STORY-075"]
    assert {row["id"] for row in rows} == {f"v2.{s}.{r}.{op}" for s, r, op in CASES}
    for row in rows:
        _, service, resource, operation = row["id"].split(".")
        source = contract(service, resource, operation)
        frozen = ORACLE["operations"][row["id"]]
        assert source["source_hash"] == row["source_sha256"] == frozen["source_sha256"]
        assert source["method"] == frozen["documentation"]["method"]
        assert source["path"] == frozen["documentation"]["resource_path"]


@pytest.mark.parametrize("service,resource,operation", CASES)
def test_each_operation_uses_source_wire_and_meaningful_result(service, resource, operation):
    _, request, result = successful_example(service, resource, operation)
    check_business(resource, operation, request, result)
    model = contract(service, resource, operation)["response"]
    if model is not None:
        TypeAdapter(model).validate_python(result)


@pytest.mark.parametrize("service,resource,operation", CASES)
def test_declared_errors_keep_sdk_types_and_semantic_parameters(service, resource, operation):
    namespace = example(service, resource, operation)
    source = contract(service, resource, operation)
    cases = {case["name"]: case for case in namespace["ERRORS"]}
    assert cases.keys() == source["errors"].keys()
    for name, error_type in source["errors"].items():
        case = cases[name]
        if name == "ModifyingCheckTypeNotSupported":
            check_check_type_change(case["parameters"], namespace["EXPECTED_BODY"]["config"]["type"])

        def failure(request):
            check_wire(source, request)
            return httpx.Response(case["status"], json={
                "errorName": name, "errorCode": case["code"], "parameters": case["parameters"],
                "errorInstanceId": "00000000-0000-0000-0000-000000000004",
            })

        with pytest.raises(error_type) as raised:
            execute(namespace, source, failure)
        assert isinstance(raised.value, PalantirRPCException)
        assert raised.value.name == name
        assert normalized(raised.value.parameters) == case["parameters"]


@pytest.mark.parametrize("service,resource", BATCHES)
@pytest.mark.parametrize("fault", ("empty_found", "wrong_key", "wrong_model_rid", "unrequested"))
def test_batch_oracle_rejects_uncorrelated_or_empty_demonstrations(service, resource, fault):
    _, request, result = successful_example(service, resource, "get_batch")
    key = resource[0].lower() + resource[1:] + "Rid"
    requested = [element[key] for element in json.loads(request.content)]
    damaged = copy.deepcopy(result)
    if fault == "empty_found":
        damaged["data"].clear()
    elif fault == "wrong_key":
        damaged["data"][OTHER] = damaged["data"].pop(FOUND)
    elif fault == "wrong_model_rid":
        damaged["data"][FOUND]["rid"] = OTHER
    else:
        damaged["data"][OTHER] = copy.deepcopy(damaged["data"][FOUND])
    with pytest.raises(AssertionError):
        check_batch(requested, damaged)


@pytest.mark.parametrize("operation", ("create", "replace"))
@pytest.mark.parametrize("fault", ("ignore_only_target", "change_target"))
def test_schedule_oracle_rejects_changed_submitted_target(operation, fault):
    _, request, result = successful_example("orchestration", "Schedule", operation)
    body = json.loads(request.content)
    damaged = copy.deepcopy(result)
    target = damaged["action"]["target"]
    if fault == "ignore_only_target":
        target["ignoredRids"] = target["targetRids"][:]
    else:
        target["targetRids"] = [OTHER]
    with pytest.raises(AssertionError):
        check_schedule_action(body, damaged)


@pytest.mark.parametrize("fault", ("same_type", "different_requested_type"))
def test_check_type_error_oracle_rejects_non_change_or_unrelated_request(fault):
    namespace = example("data_health", "Check", "replace")
    parameters = copy.deepcopy(next(case["parameters"] for case in namespace["ERRORS"]
                                    if case["name"] == "ModifyingCheckTypeNotSupported"))
    requested = namespace["EXPECTED_BODY"]["config"]["type"]
    if fault == "same_type":
        parameters["originalCheckType"] = parameters["newCheckType"]
    else:
        parameters["newCheckType"] = "columnType"
    with pytest.raises(AssertionError):
        check_check_type_change(parameters, requested)


def test_build_search_example_rejects_non_timestamp_filter(monkeypatch):
    namespace = example("orchestration", "Build", "search")
    source = contract("orchestration", "Build", "search")
    damaged = copy.deepcopy(namespace["EXPECTED_BODY"])
    damaged["where"]["value"] = "synthetic-value"
    monkeypatch.setitem(namespace, "EXPECTED_BODY", damaged)

    def handler(request):
        check_wire(source, request)
        result = namespace["SUCCESS"]
        with pytest.raises(ValueError, match="Invalid isoformat"):
            check_business("Build", "search", request, result)
        return httpx.Response(200, json=result)

    execute(namespace, source, handler)


@pytest.mark.parametrize("service,resource", BATCHES)
def test_batch_missing_rid_fails_sdk_validation_before_http(service, resource):
    namespace = example(service, resource, "get_batch")
    source = contract(service, resource, "get_batch")

    def unexpected(request):
        raise AssertionError("Invalid batch reached HTTP")

    with namespace["mock_resource"](source["client"], unexpected) as client:
        with pytest.raises(ValidationError):
            client.with_raw_response.get_batch(body=[{}])


def operation_arguments(namespace):
    """Read adaptable example inputs; installed SDK remains the response oracle."""
    class Arguments:
        @property
        def with_raw_response(self):
            return self

        def __getattr__(self, name):
            return lambda **arguments: arguments

    return copy.deepcopy(namespace["invoke"](Arguments()))


def async_client(source):
    module = importlib.import_module(source["client"].__module__)
    return getattr(module, "Async" + source["client"].__name__)


def synthetic_response(payload):
    return httpx.Response(204) if payload is None else httpx.Response(200, json=payload)


@pytest.mark.parametrize("service,resource,operation", CASES)
@pytest.mark.parametrize("mode", ("raw", "native"))
def test_every_async_response_uses_source_return_mode_and_closes(
        service, resource, operation, mode, offline_event_loop):
    namespace = example(service, resource, operation)
    source = contract(service, resource, operation)
    mock_async = importlib.import_module("mock_transport").mock_async_resource
    responses = []

    def handler(request):
        check_wire(source, request)
        assert request.extensions["timeout"]["read"] == 30
        response = synthetic_response(namespace["SUCCESS"])
        responses.append(response)
        return response

    async def exercise():
        async with mock_async(async_client(source), handler) as client:
            target = client.with_raw_response if mode == "raw" else client
            pending = getattr(target, operation)(**operation_arguments(namespace))
            expected = normalized(TypeAdapter(source["response"]).validate_python(namespace["SUCCESS"]))
            if mode == "native" and hasattr(pending, "__aiter__"):
                annotation = inspect.signature(getattr(async_client(source), operation)).return_annotation
                assert isinstance(pending, get_origin(annotation))
                assert not inspect.isawaitable(pending)
                assert [normalized(row) async for row in pending] == expected["data"]
            else:
                assert inspect.isawaitable(pending) and not hasattr(pending, "__aiter__")
                result = await pending
                if mode == "raw":
                    try:
                        assert normalized(result.decode()) == expected
                    finally:
                        await result.aclose()
                else:
                    assert normalized(result) == expected

    offline_event_loop.run_until_complete(exercise())
    assert len(responses) == 1 and responses[0].is_closed


STREAM_CASES = [case for case in CASES if contract(*case)["response"] is not None]
PAGED_CASES = [case for case in CASES
               if "page_token" in inspect.signature(getattr(contract(*case)["client"], case[2])).parameters]


class TrackedSyncStream(httpx.SyncByteStream):
    def __init__(self):
        self.chunks_read = 0
        self.closed = False

    def __iter__(self):
        for chunk in (b"part", b"two!", b"unread"):
            self.chunks_read += 1
            yield chunk

    def close(self):
        self.closed = True


class TrackedAsyncStream(httpx.AsyncByteStream):
    def __init__(self):
        self.chunks_read = 0
        self.closed = False

    async def __aiter__(self):
        for chunk in (b"part", b"two!", b"unread"):
            self.chunks_read += 1
            yield chunk

    async def aclose(self):
        self.closed = True


@pytest.mark.parametrize("service,resource,operation", STREAM_CASES)
@pytest.mark.parametrize("asynchronous", (False, True))
def test_stream_context_releases_response_when_caller_byte_budget_interrupts(
        service, resource, operation, asynchronous, offline_event_loop):
    namespace = example(service, resource, operation)
    source = contract(service, resource, operation)
    responses = []
    body = TrackedAsyncStream() if asynchronous else TrackedSyncStream()

    def handler(request):
        check_wire(source, request)
        assert request.extensions["timeout"]["read"] == 30
        response = httpx.Response(200, stream=body)
        assert not response.is_closed and not body.closed
        responses.append(response)
        return response

    arguments = operation_arguments(namespace)
    if asynchronous:
        async def exercise():
            mock_async = importlib.import_module("mock_transport").mock_async_resource
            async with mock_async(async_client(source), handler) as client:
                with pytest.raises(RuntimeError, match="Caller byte budget exhausted"):
                    async with getattr(client.with_streaming_response, operation)(**arguments) as response:
                        count = 0
                        async for chunk in response.aiter_bytes(chunk_size=4):
                            count += len(chunk)
                            if count > 4:
                                raise RuntimeError("Caller byte budget exhausted")
        offline_event_loop.run_until_complete(exercise())
    else:
        with namespace["mock_resource"](source["client"], handler) as client:
            with pytest.raises(RuntimeError, match="Caller byte budget exhausted"):
                with getattr(client.with_streaming_response, operation)(**arguments) as response:
                    count = 0
                    for chunk in response.iter_bytes(chunk_size=4):
                        count += len(chunk)
                        if count > 4:
                            raise RuntimeError("Caller byte budget exhausted")
    assert len(responses) == 1 and responses[0].is_closed
    assert body.closed and body.chunks_read == 2


@pytest.mark.parametrize("service,resource,operation", PAGED_CASES)
@pytest.mark.parametrize("asynchronous", (False, True))
def test_native_iterator_or_manual_response_pagination_stops_after_finite_final_page(
        service, resource, operation, asynchronous, offline_event_loop):
    namespace = example(service, resource, operation)
    source = contract(service, resource, operation)
    arguments = operation_arguments(namespace)
    calls, responses = [], []

    def handler(request):
        check_wire(source, request)
        body = json.loads(request.content) if request.content else {}
        token = request.url.params.get("pageToken", body.get("pageToken"))
        calls.append(token)
        assert calls == ([None] if len(calls) == 1 else [None, "next-fixture"])
        assert len(calls) <= 2, "Pagination must stop after the finite final page"
        assert request.extensions["timeout"]["read"] == 30
        payload = copy.deepcopy(namespace["SUCCESS"])
        if len(calls) == 1:
            payload["nextPageToken"] = "next-fixture"
        else:
            payload["data"] = []
            payload.pop("nextPageToken", None)
        response = httpx.Response(200, json=payload)
        responses.append(response)
        return response

    expected_rows = normalized(TypeAdapter(source["response"]).validate_python(namespace["SUCCESS"]))["data"]
    if asynchronous:
        async def exercise():
            mock_async = importlib.import_module("mock_transport").mock_async_resource
            async with mock_async(async_client(source), handler) as client:
                pending = getattr(client, operation)(**arguments)
                if hasattr(pending, "__aiter__"):
                    assert not inspect.isawaitable(pending)
                    return [normalized(row) async for row in pending]
                assert inspect.isawaitable(pending)
                first = await pending
                assert first.next_page_token == "next-fixture"
                second = await getattr(client, operation)(**dict(arguments, page_token=first.next_page_token))
                assert second.next_page_token is None
                return normalized(first.data + second.data)
        actual = offline_event_loop.run_until_complete(exercise())
    else:
        with namespace["mock_resource"](source["client"], handler) as client:
            first = getattr(client, operation)(**arguments)
            if hasattr(first, "__next__"):
                actual = [normalized(row) for row in first]
            else:
                assert first.next_page_token == "next-fixture"
                second = getattr(client, operation)(**dict(arguments, page_token=first.next_page_token))
                assert second.next_page_token is None
                actual = normalized(first.data + second.data)
    assert actual == expected_rows
    assert calls == [None, "next-fixture"] and all(response.is_closed for response in responses)


@pytest.mark.parametrize("service,resource", OPERATIONS)
@pytest.mark.parametrize("asynchronous", (False, True))
def test_read_timeout_preserves_cause_and_does_not_repeat_request(
        service, resource, asynchronous, offline_event_loop):
    namespace = example(service, resource, "get")
    source = contract(service, resource, "get")
    calls = []

    def stalled(request):
        check_wire(source, request)
        assert request.extensions["timeout"]["read"] == 30
        calls.append(request)
        raise httpx.ReadTimeout("Synthetic request deadline", request=request)

    if asynchronous:
        async def exercise():
            mock_async = importlib.import_module("mock_transport").mock_async_resource
            async with mock_async(async_client(source), stalled) as client:
                await client.get(**operation_arguments(namespace))
        with pytest.raises(ReadTimeout, match="Synthetic request deadline") as raised:
            offline_event_loop.run_until_complete(exercise())
    else:
        with namespace["mock_resource"](source["client"], stalled) as client:
            with pytest.raises(ReadTimeout, match="Synthetic request deadline") as raised:
                client.get(**operation_arguments(namespace))
    assert isinstance(raised.value.__cause__, httpx.ReadTimeout)
    assert len(calls) == 1
