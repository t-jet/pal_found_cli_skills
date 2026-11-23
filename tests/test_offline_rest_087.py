"""SDK bridge regressions and source-derived story087 fixture semantics."""

import ast
import asyncio
import hashlib
import importlib
import importlib.metadata
import importlib.util
import inspect
import json
import re
import socket
import textwrap
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote, unquote

import httpx
import pytest
from pydantic import TypeAdapter

FILE = Path(__file__).parents[1] / ".agents/skills/pal-found-dev/examples/rest/087/model_studio_config_version.py"
SPEC = importlib.util.spec_from_file_location("model_studio_bridge", FILE)
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)

ROOT = Path(__file__).parents[1]
OWNER = ROOT / ".agents/skills/pal-found-dev"
REGISTER = json.loads((ROOT / "maintainer/rest-domain-authoring-register.json").read_text())
ORACLE = json.loads((ROOT / "tests/fixtures/offline/rest-acceptance/source-oracle.json").read_text())
ROWS = {row["id"]: row for row in REGISTER["operations"] if row["story"] == "DEV-STORY-087"}
IDS = sorted(ROWS)


@pytest.fixture(scope="module")
def offline_event_loop():
    # Windows initializes its local socket pair before the network guard applies.
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def deny_public_network(monkeypatch, offline_event_loop):
    def denied(*args, **kwargs):
        raise AssertionError("Public network access forbidden in offline tests")

    for name in ("connect", "connect_ex"):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ("create_connection", "getaddrinfo", "gethostbyname", "gethostbyname_ex"):
        monkeypatch.setattr(socket, name, denied)


def test_native_sdk_failure_and_direct_rest_positive_named_generic_budget_cases():
    bridge.verify()


@pytest.mark.parametrize("body", [b"upstream unavailable", b'{"errorName": []}', b'{"parameters": []}'])
def test_malformed_http_errors_remain_http_errors_and_response_closes(body):
    responses = []
    def handler(request):
        response = httpx.Response(503, content=body)
        responses.append(response)
        return response
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        with pytest.raises(httpx.HTTPStatusError):
            bridge.get_config_version(client, hostname="offline.example.invalid", token="fixture",
                                      studio_rid=bridge.STUDIO, version=1)
    assert len(responses) == 1 and responses[0].is_closed


def test_direct_rest_rejects_string_version_and_preview_before_http():
    def unexpected(request):
        raise AssertionError("Invalid input must not send HTTP")
    with httpx.Client(transport=httpx.MockTransport(unexpected)) as client:
        with pytest.raises(TypeError, match="version must be an integer"):
            bridge.get_config_version(client, hostname="offline.example.invalid", token="fixture",
                                      studio_rid=bridge.STUDIO, version="1")
        with pytest.raises(TypeError, match="preview must be a boolean"):
            bridge.get_config_version(client, hostname="offline.example.invalid", token="fixture",
                                      studio_rid=bridge.STUDIO, version=1, preview="false")


@pytest.fixture
def promote_version_example():
    path = Path(__file__).parents[1] / (
        ".agents/skills/pal-found-dev/examples/rest/087/v2/models/Model/promote_version.py"
    )
    spec = importlib.util.spec_from_file_location("promote_version_example", path)
    example = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(example)
    return example


def test_promote_version_copies_to_new_version_rid(promote_version_example):
    example = promote_version_example
    target_model_rid = example.EXPECTED_PATH.split("/")[-2]
    assert len({target_model_rid, example.EXPECTED_BODY["sourceModelVersionRid"],
                example.SUCCESS["rid"]}) == 3
    example.verify()


def test_promote_version_rejects_reused_source_version_rid(promote_version_example, monkeypatch):
    example = promote_version_example
    monkeypatch.setitem(example.SUCCESS, "rid", example.EXPECTED_BODY["sourceModelVersionRid"])
    with pytest.raises(AssertionError, match="Promoted model version must have a new RID"):
        example.verify()


CORRECTED_EXAMPLES = [
    "aip_agents/Agent/get", "aip_agents/Agent/all_sessions",
    "aip_agents/AgentVersion/get", "aip_agents/AgentVersion/list",
    "aip_agents/Session/blocking_continue", "aip_agents/Session/streaming_continue",
    "language_models/AnthropicModel/messages",
    "models/LiveDeployment/create", "models/LiveDeployment/replace",
]


def load_corrected_example(relative):
    path = Path(__file__).parents[1] / (
        ".agents/skills/pal-found-dev/examples/rest/087/v2/" + relative + ".py"
    )
    spec = importlib.util.spec_from_file_location("corrected_087_" + relative.replace("/", "_"), path)
    example = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(example)
    return example


def assert_source_semantics(relative, example):
    import re

    if "/AgentVersion/" in relative:
        rows = example.SUCCESS.get("data", [example.SUCCESS])
        for row in rows:
            assert row["string"] == f'{row["version"]["major"]}.{row["version"]["minor"]}'
    elif relative == "aip_agents/Agent/get":
        assert re.fullmatch(r"[0-9]+\.[0-9]+", example.SUCCESS["version"])
    elif relative == "aip_agents/Agent/all_sessions":
        for row in example.SUCCESS["data"]:
            assert re.fullmatch(r"[0-9]+\.[0-9]+", row["agentVersion"])
    for error in example.ERRORS:
        name, params = error["name"], error["parameters"]
        if name == "GpuTypeNotAvailable":
            assert params["requestedGpuType"] not in params["availableGpuTypes"]
        elif name == "InvalidGpuCount":
            assert not 1 <= params["providedGpuCount"] <= params["maxGpuCount"]
        elif name == "ThreadCountTooHigh":
            assert params["providedThreadCount"] > params["maxThreadCount"]
        elif name == "InvalidParameterType":
            assert params["expectedType"] != params["receivedType"]
        elif name == "MultipleSystemPromptsNotSupported":
            assert params["systemPromptSize"] > 1
        elif name == "MultipleToolResultContentsNotSupported":
            assert params["toolResultContentsSize"] > 1


@pytest.mark.parametrize("relative", CORRECTED_EXAMPLES)
def test_corrected_fixtures_match_source_semantics_and_real_sdk(relative):
    example = load_corrected_example(relative)
    assert_source_semantics(relative, example)
    example.verify()


@pytest.mark.parametrize("relative", CORRECTED_EXAMPLES[:4])
def test_rejects_agent_version_detail_mismatch_or_invalid_format(relative):
    example = load_corrected_example(relative)
    if "/AgentVersion/" in relative:
        example.SUCCESS.get("data", [example.SUCCESS])[0]["string"] = "1.2"
    elif relative.endswith("all_sessions"):
        example.SUCCESS["data"][0]["agentVersion"] = "invalid-version"
    else:
        example.SUCCESS["version"] = "invalid-version"
    with pytest.raises(AssertionError):
        assert_source_semantics(relative, example)


@pytest.mark.parametrize("relative,error_name,field,value", [
    (f"models/LiveDeployment/{method}", name, field, value)
    for method in ("create", "replace")
    for name, field, value in [
        ("GpuTypeNotAvailable", "availableGpuTypes", ["A100"]),
        ("InvalidGpuCount", "providedGpuCount", 1),
        ("ThreadCountTooHigh", "providedThreadCount", 1),
    ]
] + [
    ("language_models/AnthropicModel/messages", "MultipleSystemPromptsNotSupported", "systemPromptSize", 1),
    ("language_models/AnthropicModel/messages", "MultipleToolResultContentsNotSupported", "toolResultContentsSize", 1),
] + [
    (f"aip_agents/Session/{method}", "InvalidParameterType", "receivedType", "string")
    for method in ("blocking_continue", "streaming_continue")
])
def test_rejects_error_parameters_that_contradict_source(relative, error_name, field, value):
    example = load_corrected_example(relative)
    error = next(row for row in example.ERRORS if row["name"] == error_name)
    error["parameters"][field] = value
    with pytest.raises(AssertionError):
        assert_source_semantics(relative, example)


@lru_cache
def source_contract(identity):
    """Read wire and response definitions from the installed frozen SDK."""
    version, service, resource, operation = identity.split(".")
    snake = re.sub(r"(?<!^)(?=[A-Z])", "_", resource).lower()
    module = importlib.import_module(f"foundry_sdk.{version}.{service}.{snake}")
    client = getattr(module, resource + "Client")
    method = getattr(client, operation)
    tree = ast.parse(textwrap.dedent(inspect.getsource(method)))
    request = next(node for node in ast.walk(tree) if isinstance(node, ast.Call)
                   and isinstance(node.func, ast.Attribute) and node.func.attr == "RequestInfo")
    fields = {item.arg: item.value for item in request.keywords}
    return module, client, method, fields


def source_value(module, expression, arguments=None):
    return eval(compile(ast.Expression(expression), "<frozen SDK contract>", "eval"),
                vars(module), arguments or {})


def load_owned(identity):
    path = OWNER / ROWS[identity]["example"]
    spec = importlib.util.spec_from_file_location("owned_087_" + identity.replace(".", "_"), path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def operation_inputs(identity, example):
    """Example literals are inputs; installed source defines expected wire values."""
    operation = identity.rsplit(".", 1)[1]
    if identity == "v2.models.ModelStudioConfigVersion.get":
        return {"model_studio_rid": example.STUDIO, "model_studio_config_version_version": 1,
                "preview": True, "request_timeout": 30}
    if identity in {f"v2.aip_agents.Session.{name}" for name in ("create", "get", "list")}:
        arguments = {"agent_rid": example.AGENT, "preview": True, "request_timeout": 30}
        arguments.update({"create": {"agent_version": "1.0"},
                          "get": {"session_rid": example.SESSION},
                          "list": {"page_size": 10}}[operation])
        return arguments
    tree = ast.parse(textwrap.dedent(inspect.getsource(example.invoke)))
    call = next(node for node in ast.walk(tree) if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute) and node.func.attr == operation)
    return {item.arg: ast.literal_eval(item.value) for item in call.keywords}


def bound_inputs(identity, example):
    _, _, method, _ = source_contract(identity)
    bound = inspect.signature(method).bind_partial(None, **operation_inputs(identity, example))
    bound.apply_defaults()
    return bound.arguments


def check_source_request(identity, example, request):
    module, _, _, fields = source_contract(identity)
    arguments = bound_inputs(identity, example)

    def expected(name):
        return source_value(module, fields[name], arguments)

    assert request.method == expected("method")
    path = expected("resource_path")
    for key, value in expected("path_params").items():
        path = path.replace("{" + key + "}", quote(str(value), safe=""))
    assert unquote(request.url.path) == "/api" + unquote(path)
    assert request.headers["Authorization"] == "Bearer offline-fixture-token"
    for key, value in expected("header_params").items():
        if value is None:
            assert key not in request.headers
        else:
            assert request.headers[key] == str(value)
    query = httpx.QueryParams({key: value for key, value in expected("query_params").items()
                              if value is not None})
    assert sorted(request.url.params.multi_items()) == sorted(query.multi_items())
    body = expected("body")
    if body is not None:
        payload = TypeAdapter(type(body)).dump_python(body, mode="json", by_alias=True,
                                                     exclude_none=True)
        assert json.loads(request.content) == payload
    assert request.extensions["timeout"]["read"] == 30


def success_payload(identity, example):
    if hasattr(example, "SUCCESS"):
        return example.SUCCESS
    value = example.payload()
    return {"data": [value]} if identity.endswith(".list") else value


def invoke_owned(identity, example, handler):
    _, client_type, _, _ = source_contract(identity)
    if identity == "v2.models.ModelStudioConfigVersion.get":
        with httpx.Client(transport=httpx.MockTransport(handler)) as client:
            return example.get_config_version(client, hostname="offline.example.invalid",
                                              token="offline-fixture-token", studio_rid=example.STUDIO,
                                              version=1, preview=True, timeout=30)
    with example.mock_resource(client_type, handler) as client:
        raw = getattr(client.with_raw_response, identity.rsplit(".", 1)[1])(
            **operation_inputs(identity, example))
        try:
            return raw.decode()
        finally:
            raw.close()


def test_owned_partition_equals_the_three_frozen_sdk_namespaces():
    frozen = {identity for identity in ORACLE["operations"] if identity.startswith(
        ("v2.aip_agents.", "v2.language_models.", "v2.models."))}
    assert set(IDS) == frozen


@pytest.mark.parametrize("identity", IDS)
def test_every_owned_operation_matches_frozen_source_wire_and_typed_result(identity):
    assert importlib.metadata.version("foundry-platform-sdk") == "1.101.0"
    module, _, _, fields = source_contract(identity)
    digest = hashlib.sha256(Path(module.__file__).read_bytes()).hexdigest()
    assert digest == ROWS[identity]["source_sha256"] == ORACLE["operations"][identity]["source_sha256"]
    example = load_owned(identity)
    payload = success_payload(identity, example)
    response_type = source_value(module, fields["response_type"])
    typed = TypeAdapter(response_type).validate_python(payload)
    requests, responses = [], []

    def handler(request):
        check_source_request(identity, example, request)
        requests.append(request)
        if isinstance(payload, bytes):
            response = httpx.Response(200, content=payload)
        elif payload is None:
            response = httpx.Response(204)
        else:
            response = httpx.Response(200, json=payload)
        responses.append(response)
        return response

    actual = invoke_owned(identity, example, handler)
    assert actual == typed
    assert len(requests) == 1 and responses[0].is_closed


def synthetic_error_parameters(schema, definitions=None):
    """Build small typed error inputs for the three composed Session examples."""
    definitions = schema.get("$defs", {}) if definitions is None else definitions
    if "$ref" in schema:
        return synthetic_error_parameters(definitions[schema["$ref"].split("/")[-1]], definitions)
    if "enum" in schema:
        return schema["enum"][0]
    if "const" in schema:
        return schema["const"]
    if "anyOf" in schema:
        return synthetic_error_parameters(schema["anyOf"][0], definitions)
    if schema.get("type") == "object":
        return {key: synthetic_error_parameters(value, definitions)
                for key, value in schema.get("properties", {}).items()
                if key in schema.get("required", [])}
    if schema.get("type") == "array":
        return [synthetic_error_parameters(schema["items"], definitions)]
    if schema.get("type") == "integer":
        return 1
    return "ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001"


@pytest.mark.parametrize("identity", IDS)
def test_every_declared_error_decodes_as_its_source_exception(identity):
    module, _, _, fields = source_contract(identity)
    errors = source_value(module, fields["throwable_errors"])
    example = load_owned(identity)
    fixtures = {row["name"]: row for row in getattr(example, "ERRORS", [])}
    if fixtures:
        assert fixtures.keys() == errors.keys()
    for name, error_type in errors.items():
        parameters_type = error_type.__annotations__["parameters"]
        adapter = TypeAdapter(parameters_type)
        parameters = fixtures[name]["parameters"] if fixtures else synthetic_error_parameters(adapter.json_schema())
        adapter.validate_python(parameters)
        code = error_type.__mro__[1].__name__.removesuffix("Error")
        code = re.sub(r"(?<!^)(?=[A-Z])", "_", code).upper()
        if code == "BAD_REQUEST":
            code = "INVALID_ARGUMENT"
        elif code == "INTERNAL_SERVER":
            code = "INTERNAL"
        status = {"NOT_FOUND": 404, "PERMISSION_DENIED": 403, "INVALID_ARGUMENT": 400,
                  "CONFLICT": 409, "FAILED_PRECONDITION": 400, "INTERNAL": 500}[code]
        responses = []

        def denied(request):
            check_source_request(identity, example, request)
            response = httpx.Response(status, json={"errorName": name, "errorCode": code,
                "parameters": parameters, "errorInstanceId": "00000000-0000-0000-0000-000000000004"})
            responses.append(response)
            return response

        with pytest.raises(error_type) as raised:
            invoke_owned(identity, example, denied)
        assert raised.value.name == name
        assert adapter.dump_python(adapter.validate_python(raised.value.parameters),
                                   mode="json", by_alias=True, exclude_none=True) == adapter.dump_python(
            adapter.validate_python(parameters), mode="json", by_alias=True, exclude_none=True)
        assert len(responses) == 1 and responses[0].is_closed


def test_async_agent_iterator_and_streaming_session_bytes_are_distinct_modes(offline_event_loop):
    from foundry_sdk.v2.aip_agents.agent import AsyncAgentClient
    from foundry_sdk.v2.aip_agents.session import AsyncSessionClient

    # Both adapters use the distributed fake transport and real asynchronous SDK.
    helper = load_owned("v2.aip_agents.Session.create")
    mock_async = importlib.import_module("mock_transport").mock_async_resource
    session = helper.payload()
    seen = []

    async def exercise():
        def page(request):
            seen.append(request.url.params.get("pageToken"))
            assert len(seen) <= 2, "Iterator must stop at the finite final page"
            assert seen == [None] if len(seen) == 1 else seen == [None, "next-fixture"]
            return httpx.Response(200, json={"data": [session], "nextPageToken": "next-fixture"}
                                  if len(seen) == 1 else {"data": []})
        async with mock_async(AsyncAgentClient, page) as agents:
            iterator = agents.all_sessions(preview=True, request_timeout=30)
            assert hasattr(iterator, "__aiter__") and not inspect.isawaitable(iterator)
            rows = [row async for row in iterator]
            assert [row.rid for row in rows] == [helper.SESSION]
        assert len(seen) == 2
        responses = []

        def stream(request):
            response = httpx.Response(200, content=b"bounded synthetic bytes")
            responses.append(response)
            return response
        async with mock_async(AsyncSessionClient, stream) as sessions:
            pending = sessions.streaming_continue(helper.AGENT, helper.SESSION,
                parameter_inputs={}, user_input={"text": "Hello"}, request_timeout=30)
            assert inspect.isawaitable(pending) and not hasattr(pending, "__aiter__")
            assert await pending == b"bounded synthetic bytes"
        assert len(responses) == 1 and responses[0].is_closed

    offline_event_loop.run_until_complete(exercise())


@pytest.mark.parametrize("identity", [
    "v2.aip_agents.Session.streaming_continue",
    "v2.models.ExperimentArtifactTable.json", "v2.models.ExperimentArtifactTable.parquet",
    "v2.models.ExperimentSeries.json", "v2.models.ExperimentSeries.parquet",
])
def test_sdk_stream_context_closes_after_caller_budget_interrupts(identity):
    example = load_owned(identity)
    _, client_type, _, _ = source_contract(identity)
    responses = []

    def handler(request):
        check_source_request(identity, example, request)
        response = httpx.Response(200, content=b"bounded synthetic bytes")
        responses.append(response)
        return response

    with example.mock_resource(client_type, handler) as client:
        with pytest.raises(RuntimeError, match="Caller byte budget exhausted"):
            with getattr(client.with_streaming_response, identity.rsplit(".", 1)[1])(
                    **operation_inputs(identity, example)) as response:
                total = 0
                for chunk in response.iter_bytes(chunk_size=4):
                    total += len(chunk)
                    if total > 4:
                        raise RuntimeError("Caller byte budget exhausted")
    assert len(responses) == 1 and responses[0].is_closed


def test_public_socket_and_dns_guard_is_active():
    with pytest.raises(AssertionError, match="Public network access forbidden"):
        socket.create_connection(("public.example.invalid", 443))
    with pytest.raises(AssertionError, match="Public network access forbidden"):
        socket.getaddrinfo("public.example.invalid", 443)


@pytest.mark.parametrize("fault", ("method", "path", "body"))
def test_source_wire_oracle_rejects_mutated_request(fault):
    identity = "v2.models.Model.create"
    example = load_owned(identity)
    requests = []

    def handler(request):
        requests.append(request)
        return httpx.Response(200, json=example.SUCCESS)

    invoke_owned(identity, example, handler)
    original = requests[0]
    body = json.loads(original.content)
    if fault == "body":
        body["name"] = "changed-name"
    damaged = httpx.Request("DELETE" if fault == "method" else original.method,
        str(original.url) + ("/wrong" if fault == "path" else ""),
        headers=original.headers, json=body, extensions=original.extensions)
    with pytest.raises(AssertionError):
        check_source_request(identity, example, damaged)
