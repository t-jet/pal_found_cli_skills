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


# Native transport expectations come from SDK source, independently of reader constants.
import ast  # noqa: E402
import asyncio  # noqa: E402
import copy  # noqa: E402
import hashlib  # noqa: E402
import importlib  # noqa: E402
import importlib.metadata  # noqa: E402
import inspect  # noqa: E402
import textwrap  # noqa: E402
import typing  # noqa: E402
from contextlib import asynccontextmanager, contextmanager  # noqa: E402
from functools import lru_cache  # noqa: E402
from unittest.mock import patch  # noqa: E402
from urllib.parse import quote  # noqa: E402

from foundry_sdk import Config, ReadTimeout, UserTokenAuth  # noqa: E402
from pydantic import TypeAdapter, ValidationError  # noqa: E402


NATIVE_RESOURCES = {
    "Action": "action", "Attachment": "attachment",
    "AttachmentProperty": "attachment_property", "CipherTextProperty": "cipher_text_property",
    "GeotemporalSeriesProperty": "geotemporal_series_property",
    "MediaReferenceProperty": "media_reference_property", "Query": "query",
    "TimeSeriesPropertyV2": "time_series_property_v2",
    "TimeSeriesValueBankProperty": "time_series_value_bank_property",
}
# SHA-256 of official resource files at SDK101 commit 168d51910570b6966afa2320333ab36f6a3f7ccf.
NATIVE_SOURCE_HASHES = {
    "Action": "97d67d3a550ce372d2b39363e7373afc32ade7ecd803c022098a9d3ffca48ad5",
    "Attachment": "9e98375a9a5c81554e08b0ba84ee5a19443a05a987d288aded730b315ae72902",
    "AttachmentProperty": "85d69f0af4a9c4aeade893a39867cf826c58d3fcdf3ccd81c0b4097cb39e5af2",
    "CipherTextProperty": "e65e4718460fb27bc864cf40127f1e71bb619ae0720edc68b350b744ed356f28",
    "GeotemporalSeriesProperty": "9181bfce75792d85e8bc112a2d386e2b76e57f725e2922ccbb7e85bff159d72a",
    "MediaReferenceProperty": "e769b3499240f98d9342c20b2b1e1e3c3f5c43e4f12002ae17e5463381992180",
    "Query": "2c7c151396abb7f7c57850e7b435c6118c20091563ee8b19cd2cb4bbda38fa91",
    "TimeSeriesPropertyV2": "ab169537962d6af9ed747be3c2a2ee8707fa2432efadb2d0f5a15b49be574e55",
    "TimeSeriesValueBankProperty": "59d0d58422b167c574a9714bfe19fc628dccd317be841ff0b7c3ef4dc8f3ba38",
}
NATIVE_IDS = [(resource, path.stem.removeprefix("invoke_"))
              for resource in NATIVE_RESOURCES for path in sorted((BASE / resource).glob("invoke_*.py"))]
NATIVE_FORMS = [(resource, operation, asynchronous, mode)
                for resource, operation in NATIVE_IDS for asynchronous in (False, True)
                for mode in ("ordinary", "raw", "streaming")]


@pytest.fixture(scope="module")
def native_loop():
    # Windows creates its self-pipe before test-scoped network denial starts.
    loop = asyncio.new_event_loop()
    yield loop
    loop.run_until_complete(loop.shutdown_asyncgens())
    loop.close()


@lru_cache
def native_contract(resource, operation):
    """Read RequestInfo definitions from the prepared, pinned SDK."""
    module = importlib.import_module("foundry_sdk.v2.ontologies." + NATIVE_RESOURCES[resource])
    client = getattr(module, resource + "Client")
    method = getattr(client, operation)
    tree = ast.parse(textwrap.dedent(inspect.getsource(method)))
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute) and node.func.attr == "RequestInfo"]
    assert len(calls) == 1
    return module, client, method, {item.arg: item.value for item in calls[0].keywords}


def native_field(resource, operation, field, arguments=None):
    module, _, method, fields = native_contract(resource, operation)
    bound = inspect.signature(method).bind_partial(None, **(arguments or {}))
    bound.apply_defaults()
    return eval(compile(ast.Expression(fields[field]), "<SDK101 REST083>", "eval"),
                vars(module), bound.arguments)


def native_inputs(resource, operation):
    """Capture call inputs without consulting reader wire expectations."""
    class Capture:
        @property
        def with_raw_response(self):
            return self

        def __getattr__(self, name):
            return lambda **kwargs: kwargs

    arguments = copy.deepcopy(example(resource, operation)["invoke"](Capture()))
    arguments["request_timeout"] = 7
    signature = inspect.signature(native_contract(resource, operation)[2])
    # Exercise escaping and optional query/header serialization on every supported call.
    path_values = native_field(resource, operation, "path_params", arguments)
    for name in arguments:
        if name != "attachment_rid" and isinstance(arguments[name], str) and arguments[name] in path_values.values():
            arguments[name] = "offline /asset?x=# café"
    optional = {"branch": "review /branch", "sdk_package_rid": "ri.sdk.main.package.offline",
                "sdk_version": "1.2.3", "preview": True, "scenario_rid": "ri.scenario.main.scenario.offline",
                "transaction_id": "transaction-offline", "version": "1.0.0",
                "trace_parent": "00-0123456789abcdef0123456789abcdef-0123456789abcdef-01",
                "trace_state": "offline=trace", "attribution": "offline-test",
                "media_item_path": "photos /inspection.png"}
    arguments.update({name: value for name, value in optional.items() if name in signature.parameters})
    return arguments


def native_wire(resource, operation, arguments, request):
    assert request.method == native_field(resource, operation, "method", arguments)
    path = native_field(resource, operation, "resource_path", arguments)
    for key, value in native_field(resource, operation, "path_params", arguments).items():
        path = path.replace("{" + key + "}", quote(value, safe=""))
    assert request.url.raw_path.split(b"?", 1)[0] == ("/api" + path).encode()
    assert request.headers["Authorization"] == "Bearer offline-fixture-token"
    for key, value in native_field(resource, operation, "header_params", arguments).items():
        if value is None:
            assert key not in request.headers
        else:
            assert request.headers[key] == str(value)
    query = httpx.QueryParams({key: value for key, value in
                              native_field(resource, operation, "query_params", arguments).items()
                              if value is not None})
    assert sorted(request.url.params.multi_items()) == sorted(query.multi_items())
    body = native_field(resource, operation, "body", arguments)
    if isinstance(body, bytes):
        assert request.content == body
    elif body is None:
        assert request.content == b""
    else:
        assert json.loads(request.content) == TypeAdapter(type(body)).dump_python(
            body, mode="json", by_alias=True, exclude_none=True)
    assert request.extensions["timeout"] == dict.fromkeys(("connect", "read", "write", "pool"), 7)


@contextmanager
def native_client(resource, handler):
    module = importlib.import_module("foundry_sdk.v2.ontologies." + NATIVE_RESOURCES[resource])
    client_type = getattr(module, resource + "Client")
    with httpx.Client(transport=httpx.MockTransport(handler), timeout=30) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            client = client_type(auth=UserTokenAuth(token="offline-fixture-token"),
                                 hostname="offline.example.invalid",
                                 config=Config(timeout=30, max_retries=1,
                                               propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"))
        yield client


@asynccontextmanager
async def native_async_client(resource, handler):
    module = importlib.import_module("foundry_sdk.v2.ontologies." + NATIVE_RESOURCES[resource])
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler), timeout=30) as transport:
        with patch("foundry_sdk._core.api_client.AsyncHttpClient", return_value=transport):
            client = getattr(module, "Async" + resource + "Client")(
                auth=UserTokenAuth(token="offline-fixture-token"), hostname="offline.example.invalid",
                config=Config(timeout=30, max_retries=1,
                              propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"))
        yield client


def native_decode(resource, operation, data):
    response_type = native_field(resource, operation, "response_type")
    if data == b"" and type(None) in typing.get_args(response_type):
        return None
    return data if response_type is bytes else TypeAdapter(response_type).validate_json(data)


def native_execute(resource, operation, asynchronous, mode, handler, loop, arguments=None):
    arguments = native_inputs(resource, operation) if arguments is None else arguments

    def call(client):
        target = client if mode == "ordinary" else getattr(client, "with_" + mode + "_response")
        return getattr(target, operation)(**arguments)

    if asynchronous:
        async def exercise():
            async with native_async_client(resource, handler) as client:
                pending = call(client)
                if mode == "streaming":
                    assert not inspect.isawaitable(pending)
                    async with pending as response:
                        return native_decode(resource, operation, b"".join(
                            [chunk async for chunk in response.aiter_bytes()]))
                assert inspect.isawaitable(pending)
                result = await pending
                if mode == "raw":
                    assert not inspect.iscoroutinefunction(result.decode)
                    try:
                        return result.decode()
                    finally:
                        await result.aclose()
                assert not hasattr(result, "__aiter__")
                return result
        return loop.run_until_complete(exercise())
    with native_client(resource, handler) as client:
        result = call(client)
        if mode == "streaming":
            with result as response:
                return native_decode(resource, operation, b"".join(response.iter_bytes()))
        if mode == "raw":
            try:
                return result.decode()
            finally:
                result.close()
        assert not hasattr(result, "__next__")
        return result


def test_native_source_inventory_and_wrapper_assignments():
    assert importlib.metadata.version("foundry-platform-sdk") == "1.101.0"
    identities = sorted("v2.ontologies." + resource + "." + operation for resource, operation in NATIVE_IDS)
    assert len(identities) == 25
    assert hashlib.sha256("\n".join(identities).encode()).hexdigest() == (
        "710719af53721cbf4c1f37db6a3723ba5b5af3e405c99b572941599cd5ca2f80")
    assert len(NATIVE_FORMS) == 150
    assert sum(native_field(r, o, "response_type") is bytes for r, o in NATIVE_IDS) == 6
    assert sum(native_field(r, o, "response_type") is None for r, o in NATIVE_IDS) == 0
    for resource, operation in NATIVE_IDS:
        module, client, _, _ = native_contract(resource, operation)
        assert hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest() == NATIVE_SOURCE_HASHES[resource]
        assert native_field(resource, operation, "throwable_errors") == {}
        annotation = inspect.signature(getattr(getattr(module, "Async" + client.__name__), operation)).return_annotation
        assert "Awaitable" in str(annotation) and "Iterator" not in str(annotation)
        for prefix in ("_", "_Async"):
            for suffix in ("Raw", "Streaming"):
                wrapper = getattr(module, prefix + resource + "Client" + suffix)
                tree = ast.parse(textwrap.dedent(inspect.getsource(wrapper.__init__)))
                assignments = [target.attr for node in ast.walk(tree) if isinstance(node, ast.Assign)
                               for target in node.targets if isinstance(target, ast.Attribute)]
                assert operation in assignments


@pytest.mark.parametrize("resource,operation,asynchronous,mode", NATIVE_FORMS)
def test_native_all_forms_wire_and_typed_decode(resource, operation, asynchronous, mode, native_loop):
    arguments = native_inputs(resource, operation)
    payload = copy.deepcopy(example(resource, operation)["SUCCESS"])
    replies = []

    def handler(request):
        native_wire(resource, operation, arguments, request)
        reply = httpx.Response(200, content=payload) if isinstance(payload, bytes) else httpx.Response(200, json=payload)
        replies.append(reply)
        return reply

    result = native_execute(resource, operation, asynchronous, mode, handler, native_loop, arguments)
    expected_type = native_field(resource, operation, "response_type")
    expected = TypeAdapter(expected_type).validate_python(payload)
    assert result == expected
    assert type(result) is type(expected)
    assert len(replies) == 1 and replies[0].is_closed


@pytest.mark.parametrize("resource,operation,asynchronous,mode", NATIVE_FORMS)
@pytest.mark.parametrize("failure", ("permission", "timeout"))
def test_native_errors_preserve_denial_and_timeout(resource, operation, asynchronous, mode, failure, native_loop):
    arguments = native_inputs(resource, operation)
    requests = []

    def handler(request):
        native_wire(resource, operation, arguments, request)
        requests.append(request)
        if failure == "timeout":
            raise httpx.ReadTimeout("REST083 synthetic deadline", request=request)
        return httpx.Response(403, json={"errorName": "PermissionDenied", "errorCode": "PERMISSION_DENIED",
                              "errorInstanceId": "00000000-0000-0000-0000-000000000083",
                              "parameters": {"operation": operation}})

    with pytest.raises(PermissionDeniedError if failure == "permission" else ReadTimeout) as raised:
        native_execute(resource, operation, asynchronous, mode, handler, native_loop, arguments)
    assert len(requests) == 1
    if failure == "timeout":
        assert isinstance(raised.value.__cause__, httpx.ReadTimeout)
        assert "REST083 synthetic deadline" in str(raised.value)
    else:
        assert raised.value.name == "PermissionDenied"
        assert raised.value.parameters == {"operation": operation}


@pytest.mark.parametrize("resource,operation,asynchronous,mode", NATIVE_FORMS)
def test_native_missing_required_input_never_sends(resource, operation, asynchronous, mode, native_loop):
    arguments = native_inputs(resource, operation)
    signature = inspect.signature(native_contract(resource, operation)[2])
    required = next(name for name, item in signature.parameters.items()
                    if name != "self" and item.default is inspect.Parameter.empty)
    del arguments[required]
    requests = []

    def forbidden(request):
        requests.append(request)
        raise AssertionError("Invalid input reached HTTP")

    with pytest.raises(ValidationError):
        native_execute(resource, operation, asynchronous, mode, forbidden, native_loop, arguments)
    assert requests == []


class NativeStream(httpx.SyncByteStream):
    def __init__(self):
        self.chunks = (b"first", b"unread-second", b"unread-third")
        self.reads = 0
        self.closed = False

    def __iter__(self):
        for chunk in self.chunks:
            self.reads += 1
            yield chunk

    def close(self):
        self.closed = True


class NativeAsyncStream(httpx.AsyncByteStream):
    def __init__(self):
        self.state = NativeStream()

    async def __aiter__(self):
        for chunk in self.state:
            yield chunk

    async def aclose(self):
        self.state.close()


def assert_native_unbuffered(reply, state):
    assert not reply.is_closed and not reply.is_stream_consumed
    assert state.reads == 0 and not state.closed
    with pytest.raises(httpx.ResponseNotRead):
        _ = reply.content


@pytest.mark.parametrize("resource,operation", NATIVE_IDS)
@pytest.mark.parametrize("asynchronous", (False, True))
def test_native_unfinished_stream_closes_on_interrupt_or_cancel(resource, operation, asynchronous, native_loop):
    arguments = native_inputs(resource, operation)
    body = NativeAsyncStream() if asynchronous else NativeStream()
    state = body.state if asynchronous else body
    replies = []

    def handler(request):
        native_wire(resource, operation, arguments, request)
        reply = httpx.Response(200, stream=body)
        assert_native_unbuffered(reply, state)
        replies.append(reply)
        return reply

    if asynchronous:
        async def exercise():
            async with native_async_client(resource, handler) as client:
                async with getattr(client.with_streaming_response, operation)(**arguments) as response:
                    async for chunk in response.aiter_bytes():
                        assert chunk == state.chunks[0]
                        asyncio.current_task().cancel()
                        await asyncio.sleep(0)
                    raise AssertionError("Cancellation failed to interrupt stream")
        with pytest.raises(asyncio.CancelledError):
            native_loop.run_until_complete(exercise())
        native_loop.run_until_complete(native_loop.shutdown_asyncgens())
    else:
        with native_client(resource, handler) as client:
            with pytest.raises(RuntimeError, match="caller interrupted"):
                with getattr(client.with_streaming_response, operation)(**arguments) as response:
                    assert next(response.iter_bytes()) == state.chunks[0]
                    raise RuntimeError("caller interrupted")
    assert state.reads == 1 and state.closed
    assert len(replies) == 1 and replies[0].is_closed


def test_native_stream_guard_rejects_prebuffered_response():
    reply = httpx.Response(200, content=b"already read")
    with pytest.raises(AssertionError):
        assert_native_unbuffered(reply, NativeStream())


NULLABLE_IDS = [("TimeSeriesPropertyV2", "get_first_point"),
                ("TimeSeriesPropertyV2", "get_last_point"),
                ("TimeSeriesValueBankProperty", "get_latest_value")]


@pytest.mark.parametrize("resource,operation", NULLABLE_IDS)
@pytest.mark.parametrize("asynchronous", (False, True))
@pytest.mark.parametrize("mode", ("ordinary", "raw", "streaming"))
@pytest.mark.parametrize("data", (b"", b"null"))
def test_native_nullable_empty_body_and_json_null_differ(resource, operation, asynchronous, mode, data, native_loop):
    arguments = native_inputs(resource, operation)
    replies = []

    def handler(request):
        native_wire(resource, operation, arguments, request)
        reply = httpx.Response(200, content=data, headers={"Content-Type": "application/json"})
        replies.append(reply)
        return reply

    assert TypeAdapter(native_field(resource, operation, "response_type")).validate_python(None) is None
    # SDK101 treats an empty optional body as None; JSON null reaches model_validate.
    if data == b"null" and mode != "streaming":
        with pytest.raises(ValidationError):
            native_execute(resource, operation, asynchronous, mode, handler, native_loop, arguments)
    else:
        assert native_execute(resource, operation, asynchronous, mode, handler, native_loop, arguments) is None
    assert len(replies) == 1 and replies[0].is_closed


@pytest.mark.parametrize("asynchronous", (False, True))
@pytest.mark.parametrize("mode", ("ordinary", "raw", "streaming"))
def test_native_geotemporal_continuation_is_explicit_and_finite(asynchronous, mode, native_loop):
    resource, operation = "GeotemporalSeriesProperty", "load_geotemporal_series_entries"
    arguments = native_inputs(resource, operation)
    requests = []
    replies = []

    def handler(request):
        native_wire(resource, operation, arguments, request)
        token = json.loads(request.content).get("pageToken")
        assert token == (None if not requests else "next-page /token")
        requests.append(request)
        assert len(requests) <= 2
        reply = httpx.Response(200, json={"data": [{
            "time": "2026-01-01T00:00:00Z" if len(requests) == 1 else "2026-01-01T00:01:00Z",
            "position": {"type": "Point", "coordinates": [23.3, 42.7]}, "speed": 12.5,
        }], **({"nextPageToken": "next-page /token"} if len(requests) == 1 else {})})
        replies.append(reply)
        return reply

    pages = []
    for _ in range(2):
        page = native_execute(resource, operation, asynchronous, mode, handler, native_loop, arguments)
        assert isinstance(page, models.LoadGeotemporalSeriesResponse)
        pages.append(page)
        if page.next_page_token is None:
            break
        arguments["page_token"] = page.next_page_token
    assert len(requests) == len(pages) == 2
    assert pages[-1].next_page_token is None
    assert [entry["position"]["coordinates"] for page in pages for entry in page.data] == [[23.3, 42.7]] * 2
    assert all(reply.is_closed for reply in replies)


@pytest.mark.parametrize("resource,operation,asynchronous,mode", [
    form for form in NATIVE_FORMS if native_field(form[0], form[1], "response_type") is not bytes
])
def test_native_typed_decode_rejects_wrong_json_shape(resource, operation, asynchronous, mode, native_loop):
    arguments = native_inputs(resource, operation)
    replies = []

    def handler(request):
        native_wire(resource, operation, arguments, request)
        reply = httpx.Response(200, json=["wrong top-level response shape"])
        replies.append(reply)
        return reply

    with pytest.raises(ValidationError):
        native_execute(resource, operation, asynchronous, mode, handler, native_loop, arguments)
    assert len(replies) == 1 and replies[0].is_closed


@pytest.mark.parametrize("resource,operation,asynchronous,mode", [
    form for form in NATIVE_FORMS if native_field(form[0], form[1], "response_type") is bytes
])
def test_native_binary_download_keeps_non_utf8_bytes(resource, operation, asynchronous, mode, native_loop):
    arguments = native_inputs(resource, operation)
    payload = b"\x00\xff\xfe\x80\r\nREST083"
    replies = []

    def handler(request):
        native_wire(resource, operation, arguments, request)
        reply = httpx.Response(200, content=payload, headers={"Content-Type": "application/octet-stream"})
        replies.append(reply)
        return reply

    assert native_execute(resource, operation, asynchronous, mode, handler, native_loop, arguments) == payload
    assert len(replies) == 1 and replies[0].is_closed


@pytest.mark.parametrize("resource,operation", [("Attachment", "upload"),
                                                ("Attachment", "upload_with_rid"),
                                                ("MediaReferenceProperty", "upload")])
@pytest.mark.parametrize("asynchronous", (False, True))
@pytest.mark.parametrize("mode", ("ordinary", "raw", "streaming"))
def test_native_upload_is_raw_binary_not_multipart(resource, operation, asynchronous, mode, native_loop):
    arguments = native_inputs(resource, operation)
    arguments["body"] = b"\x00\xff\xfe\x80\r\nREST083 upload"
    if "content_length" in arguments:
        arguments["content_length"] = len(arguments["body"])
    payload = copy.deepcopy(example(resource, operation)["SUCCESS"])
    replies = []

    def handler(request):
        native_wire(resource, operation, arguments, request)
        assert request.content == arguments["body"]
        assert request.headers["Content-Type"] == "*/*"
        assert "boundary=" not in request.headers["Content-Type"]
        reply = httpx.Response(200, json=payload)
        replies.append(reply)
        return reply

    expected = TypeAdapter(native_field(resource, operation, "response_type")).validate_python(payload)
    assert native_execute(resource, operation, asynchronous, mode, handler, native_loop, arguments) == expected
    assert len(replies) == 1 and replies[0].is_closed
