"""SDK-backed examples for identity, policy, datasets, execution and v1 Ontology.

These author unit checks complement independent semantic review and acceptance.
Operation and error identities come from the installed frozen SDK source, not
the catalog generator. MockTransport remains available; real I/O is prohibited.
"""

import ast
import asyncio
import importlib
import importlib.metadata
import inspect
import json
import runpy
import socket
import subprocess
import urllib.request
import urllib.parse
from functools import lru_cache
from pathlib import Path
from types import SimpleNamespace

import httpx
import pytest
import requests
from foundry_sdk import AsyncResourceIterator, ResourceIterator

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/pal-found-dev"
MANIFEST = json.loads((ROOT / "maintainer/offline-rest-wave1.json").read_text())
ROWS = MANIFEST["operations"]

# Explicit resource ownership keeps a missing manifest resource detectable.
RESOURCES = (
    "v2.admin.Group", "v2.admin.GroupMember", "v2.admin.GroupMembership",
    "v2.admin.GroupMembershipExpirationPolicy", "v2.admin.GroupProviderInfo",
    "v2.admin.User", "v2.admin.UserProviderInfo", "v2.admin.AuthenticationProvider",
    "v2.admin.CbacBanner", "v2.admin.CbacMarkingRestrictions", "v2.admin.Enrollment",
    "v2.admin.EnrollmentRoleAssignment", "v2.admin.Host", "v2.admin.Marking",
    "v2.admin.MarkingCategory", "v2.admin.MarkingMember", "v2.admin.MarkingRoleAssignment",
    "v2.admin.Organization", "v2.admin.OrganizationGuestMember",
    "v2.admin.OrganizationRoleAssignment", "v2.admin.Role",
    "v1.datasets.Branch", "v1.datasets.Dataset", "v1.datasets.File", "v1.datasets.Transaction",
    "v2.datasets.Branch", "v2.datasets.Dataset", "v2.datasets.File", "v2.datasets.Transaction",
    "v2.datasets.View", "v2.checkpoints.Record", "v2.data_health.Check",
    "v2.data_health.CheckReport", "v2.orchestration.Build", "v2.orchestration.Job",
    "v2.orchestration.Schedule", "v2.orchestration.ScheduleVersion",
    "v1.ontologies.Action", "v1.ontologies.ActionType", "v1.ontologies.Attachment",
    "v1.ontologies.ObjectType", "v1.ontologies.Ontology", "v1.ontologies.OntologyObject",
    "v1.ontologies.Query", "v1.ontologies.QueryType",
)


@lru_cache
def source_operations(qualified):
    version, service, resource = qualified.split(".")
    snake = "".join("_" + char.lower() if char.isupper() and index else char.lower()
                    for index, char in enumerate(resource))
    module = importlib.import_module(f"foundry_sdk.{version}.{service}.{snake}")
    source = ast.parse(inspect.getsource(getattr(module, resource + "Client")))
    operations = {}
    for method in source.body[0].body:
        if not isinstance(method, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if method.name.startswith("_"):
            continue
        requests_info = [node for node in ast.walk(method)
                         if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                         and node.func.attr == "RequestInfo"]
        if not requests_info:
            continue  # Cached nested-client properties are navigation, not operations.
        assert len(requests_info) == 1, qualified + "." + method.name
        fields = {keyword.arg: keyword.value for keyword in requests_info[0].keywords}
        errors = fields.get("throwable_errors")
        assert isinstance(errors, ast.Dict), qualified + "." + method.name
        operations[qualified + "." + method.name] = {ast.literal_eval(key) for key in errors.keys}
    return operations


@pytest.fixture
def deny_external_io(monkeypatch, local_event_loop):
    def denied(*args, **kwargs):
        raise AssertionError("Offline SDK example attempted external I/O")

    for name in ("create_connection", "getaddrinfo", "gethostbyname", "gethostbyname_ex"):
        monkeypatch.setattr(socket, name, denied)
    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(httpx.HTTPTransport, "handle_request", denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, "handle_async_request", denied)
    monkeypatch.setattr(requests.sessions.Session, "request", denied)
    monkeypatch.setattr(urllib.request, "urlopen", denied)
    monkeypatch.setattr(urllib.request.OpenerDirector, "open", denied)
    monkeypatch.setattr(subprocess, "run", denied)
    monkeypatch.setattr(subprocess, "Popen", denied)


@pytest.fixture(scope="session")
def local_event_loop():
    # Windows creates an internal wakeup socket when constructing its event loop.
    # Create test infrastructure before denying I/O in all example execution.
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


def test_manifest_exactly_covers_owned_sdk_operations():
    assert importlib.metadata.version("foundry-platform-sdk") == MANIFEST["sdk_version"] == "1.101.0"
    assert set(MANIFEST["resources"]) == set(RESOURCES)
    expected = {operation for resource in RESOURCES for operation in source_operations(resource)}
    actual = [row["id"] for row in ROWS]
    assert len(actual) == len(set(actual)), "Duplicate example identity"
    assert set(actual) == expected
    for row in ROWS:
        for key in ("behavior", "example"):
            path = (SKILL / row[key]).resolve()
            assert path.is_relative_to(SKILL.resolve())
            assert path.is_file(), (row["id"], key)


@pytest.mark.parametrize("row", ROWS, ids=lambda row: row["id"])
def test_actual_sdk_request_result_and_every_named_error_offline(row, deny_external_io):
    namespace = runpy.run_path(str(SKILL / row["example"]))
    resource, method = row["id"].rsplit(".", 1)
    expected_errors = source_operations(resource)[row["id"]]
    fixture_errors = [error["name"] for error in namespace["ERRORS"]]
    assert len(fixture_errors) == len(set(fixture_errors)), "Duplicate named-error fixture"
    assert set(fixture_errors) == expected_errors
    assert method in namespace["invoke"].__code__.co_names
    namespace["verify"]()


def success_transport(namespace, responses):
    def handler(request):
        namespace["check_request"](request)
        if len(responses) >= 8:
            raise AssertionError("Fixture exceeded its finite request budget")
        success = (namespace["EXISTING"] if request.method == "GET" and "EXISTING" in namespace
                   else namespace["SUCCESS"])
        if isinstance(success, bytes):
            response = httpx.Response(200, content=success)
        elif success is None:
            response = httpx.Response(204)
        else:
            response = httpx.Response(200, json=success)
        responses.append(response)
        return response
    return handler


def sync_invoke_client(namespace, client, response_mode):
    if "EXISTING" in namespace:
        return SimpleNamespace(get=client.get, with_raw_response=response_mode)
    return SimpleNamespace(with_raw_response=response_mode)


async def async_invoke_client(namespace, client, response_mode):
    if "EXISTING" in namespace:
        current = await client.get(group_id=namespace["EXISTING"]["id"], request_timeout=30)
        return SimpleNamespace(get=lambda **kwargs: current, with_raw_response=response_mode)
    return client if response_mode is client.with_raw_response else SimpleNamespace(
        with_raw_response=response_mode
    )


def check_stream_bytes(namespace, content):
    expected = namespace["SUCCESS"]
    if isinstance(expected, bytes):
        assert content == expected
    elif expected is None:
        assert content == b""
    else:
        assert json.loads(content) == expected


def schema_call_args(namespace):
    return {
        "dataset_rid": namespace["EXPECTED_PATH"].split("/")[4],
        "branch_id": namespace["EXPECTED_QUERY"]["branchId"],
        "request_timeout": 30,
    }


def assert_public_schema_signature(client):
    # Dataset.get_schema is public through FoundryClient.datasets.Dataset.
    signature = inspect.signature(client.datasets.Dataset.get_schema)
    assert signature.parameters["dataset_rid"].default is inspect.Parameter.empty
    assert {"branch_id", "preview", "request_timeout"} <= signature.parameters.keys()


def schema_preview_transport(namespace, responses):
    """Check method-level preview=true without changing default omission fixtures."""

    def handler(request):
        assert request.method == namespace["EXPECTED_METHOD"]
        assert urllib.parse.unquote(request.url.path) == namespace["EXPECTED_PATH"]
        assert request.headers["Authorization"] == "Bearer offline-fixture-token"
        for key, value in namespace["EXPECTED_HEADERS"].items():
            if value is None:
                assert key not in request.headers
            else:
                assert request.headers[key] == str(value)
        expected_query = {key: value for key, value in namespace["EXPECTED_QUERY"].items()
                          if value is not None}
        expected_query["preview"] = "true"
        assert sorted(request.url.params.multi_items()) == sorted(
            httpx.QueryParams(expected_query).multi_items()
        )
        assert request.content == b""
        assert len(responses) < 4, "Preview fixture exceeded finite request budget"
        response = httpx.Response(200, json=namespace["SUCCESS"])
        responses.append(response)
        return response

    return handler


def verify_composed_schema_sync(namespace):
    responses = []
    with namespace["mock_composed_client"](success_transport(namespace, responses)) as client:
        assert_public_schema_signature(client)
        raw = namespace["invoke"](client)
        try:
            assert namespace["normalized"](raw.decode()) == namespace["SUCCESS"]
        finally:
            raw.close()
        with client.datasets.Dataset.with_streaming_response.get_schema(
            **schema_call_args(namespace)
        ) as stream:
            chunks = []
            for count, chunk in enumerate(stream.iter_bytes(), 1):
                assert count <= 100 and sum(map(len, chunks)) + len(chunk) <= 100_000
                chunks.append(chunk)
            check_stream_bytes(namespace, b"".join(chunks))
    assert len(responses) == 2
    assert all(response.is_closed for response in responses)
    preview_responses = []
    with namespace["mock_composed_client"](
        schema_preview_transport(namespace, preview_responses)
    ) as client:
        assert namespace["normalized"](client.datasets.Dataset.get_schema(
            **schema_call_args(namespace), preview=True
        )) == namespace["SUCCESS"]
        with client.datasets.Dataset.with_streaming_response.get_schema(
            **schema_call_args(namespace), preview=True
        ) as stream:
            check_stream_bytes(namespace, b"".join(stream.iter_bytes()))
    assert len(preview_responses) == 2
    assert all(response.is_closed for response in preview_responses)


def verify_composed_schema_async(namespace, local_event_loop):
    from foundry_sdk import Config, UserTokenAuth
    from foundry_sdk.v1 import AsyncFoundryClient
    from unittest.mock import patch

    responses = []

    async def execute():
        async with httpx.AsyncClient(
            transport=httpx.MockTransport(success_transport(namespace, responses)), timeout=30
        ) as transport:
            with patch("foundry_sdk._core.api_client.AsyncHttpClient", return_value=transport):
                client = AsyncFoundryClient(
                    auth=UserTokenAuth("offline-fixture-token"),
                    hostname="https://offline.example.invalid",
                    config=Config(timeout=30, max_retries=1,
                                  propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
                    preview=True,
                )
                assert_public_schema_signature(client)
                decoded = await client.datasets.Dataset.get_schema(**schema_call_args(namespace))
                assert namespace["normalized"](decoded) == namespace["SUCCESS"]
                raw = await namespace["invoke"](client)
                try:
                    assert namespace["normalized"](raw.decode()) == namespace["SUCCESS"]
                finally:
                    await raw.aclose()
                async with client.datasets.Dataset.with_streaming_response.get_schema(
                    **schema_call_args(namespace)
                ) as stream:
                    chunks = []
                    async for chunk in stream.aiter_bytes():
                        assert len(chunks) < 100 and sum(map(len, chunks)) + len(chunk) <= 100_000
                        chunks.append(chunk)
                    check_stream_bytes(namespace, b"".join(chunks))
        assert len(responses) == 3
        assert all(response.is_closed for response in responses)

    local_event_loop.run_until_complete(execute())

    preview_responses = []

    async def execute_preview():
        async with httpx.AsyncClient(
            transport=httpx.MockTransport(schema_preview_transport(namespace, preview_responses)),
            timeout=30,
        ) as transport:
            with patch("foundry_sdk._core.api_client.AsyncHttpClient", return_value=transport):
                client = AsyncFoundryClient(
                    auth=UserTokenAuth("offline-fixture-token"),
                    hostname="https://offline.example.invalid",
                    config=Config(timeout=30, max_retries=1,
                                  propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
                    preview=True,
                )
                assert namespace["normalized"](await client.datasets.Dataset.get_schema(
                    **schema_call_args(namespace), preview=True
                )) == namespace["SUCCESS"]
                async with client.datasets.Dataset.with_streaming_response.get_schema(
                    **schema_call_args(namespace), preview=True
                ) as stream:
                    chunks = []
                    async for chunk in stream.aiter_bytes():
                        assert len(chunks) < 100 and sum(map(len, chunks)) + len(chunk) <= 100_000
                        chunks.append(chunk)
                    check_stream_bytes(namespace, b"".join(chunks))
        assert len(preview_responses) == 2
        assert all(response.is_closed for response in preview_responses)

    local_event_loop.run_until_complete(execute_preview())


@pytest.mark.parametrize("row", ROWS, ids=lambda row: row["id"])
def test_sync_ordinary_and_streaming_modes_close_with_finite_work(row, deny_external_io):
    namespace = runpy.run_path(str(SKILL / row["example"]))
    if row["id"] == "v1.datasets.Dataset.get_schema":
        verify_composed_schema_sync(namespace)
        return
    resource = row["id"].split(".")[2]
    method = row["id"].split(".")[3]
    client_type = namespace[resource + "Client"]
    responses = []
    with namespace["mock_resource"](client_type, success_transport(namespace, responses)) as client:
        ordinary = namespace["invoke"](sync_invoke_client(namespace, client, client))
        if isinstance(ordinary, ResourceIterator):
            items = []
            for item in ordinary:
                assert len(items) < 10, "Finite object budget exhausted"
                items.append(namespace["normalized"](item))
            assert items == namespace["SUCCESS"]["data"]
        else:
            assert namespace["normalized"](ordinary) == namespace["SUCCESS"]
        streaming_supported = hasattr(client.with_streaming_response, method)
        if streaming_supported:
            with namespace["invoke"](sync_invoke_client(
                namespace, client, client.with_streaming_response
            )) as stream:
                chunks, size = [], 0
                for number, chunk in enumerate(stream.iter_bytes(), 1):
                    size += len(chunk)
                    assert number <= 100 and size <= 100_000, "Finite stream budget exhausted"
                    chunks.append(chunk)
                check_stream_bytes(namespace, b"".join(chunks))
    assert len(responses) == (1 + streaming_supported) * (2 if "EXISTING" in namespace else 1)
    assert all(response.is_closed for response in responses)


@pytest.mark.parametrize("row", ROWS, ids=lambda row: row["id"])
def test_actual_async_iterator_raw_and_stream_modes_close_offline(row, deny_external_io, local_event_loop):
    namespace = runpy.run_path(str(SKILL / row["example"]))
    if row["id"] == "v1.datasets.Dataset.get_schema":
        verify_composed_schema_async(namespace, local_event_loop)
        return
    resource = row["id"].split(".")[2]
    method = row["id"].split(".")[3]
    module = importlib.import_module(namespace[resource + "Client"].__module__)
    async_type = getattr(module, "Async" + resource + "Client")
    # The example loaded the standalone common helper without a source checkout.
    mock_async_resource = importlib.import_module("mock_transport").mock_async_resource
    responses = []

    async def execute():
        async with mock_async_resource(async_type, success_transport(namespace, responses)) as client:
            result = namespace["invoke"](await async_invoke_client(
                namespace, client, client
            ))
            if isinstance(result, AsyncResourceIterator):
                assert not inspect.isawaitable(result)
                items = []
                async for item in result:
                    assert len(items) < 10, "Finite object budget exhausted"
                    items.append(namespace["normalized"](item))
                assert items == namespace["SUCCESS"]["data"]
            else:
                assert inspect.isawaitable(result)
                assert namespace["normalized"](await result) == namespace["SUCCESS"]
            raw = await namespace["invoke"](await async_invoke_client(
                namespace, client, client.with_raw_response
            ))
            try:
                assert namespace["normalized"](raw.decode()) == namespace["SUCCESS"]
            finally:
                await raw.aclose()
            streaming_supported = hasattr(client.with_streaming_response, method)
            if streaming_supported:
                async with namespace["invoke"](await async_invoke_client(
                    namespace, client, client.with_streaming_response
                )) as stream:
                    chunks, size, count = [], 0, 0
                    async for chunk in stream.aiter_bytes():
                        size += len(chunk)
                        count += 1
                        assert count <= 100 and size <= 100_000, "Finite stream budget exhausted"
                        chunks.append(chunk)
                    check_stream_bytes(namespace, b"".join(chunks))
        assert len(responses) == (2 + streaming_supported) * (2 if "EXISTING" in namespace else 1)
        assert all(response.is_closed for response in responses)

    local_event_loop.run_until_complete(execute())


@pytest.mark.parametrize("boundary", ["socket", "httpx", "urllib", "subprocess"])
def test_external_io_guards_reject_live_dispatch(boundary, deny_external_io):
    with pytest.raises(AssertionError, match="attempted external I/O"):
        if boundary == "socket":
            socket.create_connection(("offline.example.invalid", 443))
        elif boundary == "httpx":
            with httpx.Client(trust_env=False) as client:
                client.get("https://offline.example.invalid/")
        elif boundary == "urllib":
            urllib.request.urlopen("https://offline.example.invalid/")
        else:
            subprocess.run(["unexpected-offline-child"])
