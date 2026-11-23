"""Identity examples exercised through SDK 1.101.0 and synthetic HTTP responses.

SDK RequestInfo source supplies routes, models and declared exception classes.
Business assertions check the reader examples independently of their assertions.
The membership service below is a local model, not evidence of server behavior.
"""

import ast
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

import httpx
import pytest
from foundry_sdk import PalantirRPCException
from pydantic import TypeAdapter, ValidationError


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / ".agents/skills/pal-found-dev/examples/rest/071/v2/admin"
REGISTER = json.loads((ROOT / "maintainer/rest-domain-authoring-register.json").read_text())
ROWS = [row for row in REGISTER["operations"] if row["story"] == "DEV-STORY-071"]
ORACLE = json.loads((ROOT / "tests/fixtures/offline/rest-acceptance/source-oracle.json").read_text())
OPERATIONS = {
    "Group": ("create", "delete", "get", "get_batch", "list", "list_current", "replace", "search"),
    "GroupMember": ("add", "list", "remove"),
    "GroupMembership": ("list",),
    "GroupMembershipExpirationPolicy": ("get", "replace"),
    "GroupProviderInfo": ("get", "replace"),
    "User": ("delete", "get", "get_batch", "get_current", "get_markings", "list",
             "profile_picture", "revoke_all_tokens", "search"),
    "UserProviderInfo": ("get", "replace"),
}
CASES = [(resource, op) for resource, ops in OPERATIONS.items() for op in ops]
TARGET = "00000000-0000-0000-0000-000000000001"
MEMBER = "00000000-0000-0000-0000-000000000002"
OTHER = "00000000-0000-0000-0000-000000000003"


@pytest.fixture(autouse=True)
def deny_public_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("REST071 attempted public network access")

    for name in ("connect", "connect_ex"):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ("create_connection", "getaddrinfo", "gethostbyname", "gethostbyname_ex"):
        monkeypatch.setattr(socket, name, denied)
    monkeypatch.setattr(httpx.HTTPTransport, "handle_request", denied)
    monkeypatch.setattr(httpx.AsyncHTTPTransport, "handle_async_request", denied)


def example(resource, operation):
    return runpy.run_path(str(BASE / resource / f"{operation}.py"))["invoke"].__globals__


@lru_cache
def contract(resource, operation):
    snake = "".join(("_" if i else "") + c.lower() if c.isupper() else c
                    for i, c in enumerate(resource))
    module = importlib.import_module(f"foundry_sdk.v2.admin.{snake}")
    client = getattr(module, resource + "Client")
    tree = ast.parse(textwrap.dedent(inspect.getsource(getattr(client, operation))))
    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)
             and isinstance(node.func, ast.Attribute) and node.func.attr == "RequestInfo"]
    assert len(calls) == 1
    fields = {kw.arg: kw.value for kw in calls[0].keywords}

    def source_value(node):
        # These expressions are read from the installed frozen SDK, never fixtures.
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
    if isinstance(value, dict):
        return {key: normalized(child) for key, child in value.items()}
    if isinstance(value, (list, tuple)):
        return [normalized(child) for child in value]
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json", by_alias=True, exclude_none=True)
    return value


def response(payload):
    if payload is None:
        return httpx.Response(204)
    if isinstance(payload, bytes):
        return httpx.Response(200, content=payload)
    return httpx.Response(200, json=payload)


def execute(namespace, resource, handler):
    with namespace["mock_resource"](contract(resource, OPERATIONS[resource][0])["client"], handler) as client:
        raw = namespace["invoke"](client)
        try:
            return normalized(raw.decode())
        finally:
            raw.close()


def check_wire(resource, operation, request):
    source = contract(resource, operation)
    path = source["path"].replace("{groupId}", TARGET).replace("{userId}", TARGET)
    assert request.method == source["method"]
    assert request.url.path == "/api" + path
    assert request.headers["Authorization"] == "Bearer offline-fixture-token"
    for key, value in source["headers"].items():
        assert request.headers[key] == value


def check_business(resource, operation, request, result):
    body = json.loads(request.content) if request.content else None
    if operation == "get_batch":
        key = "groupId" if resource == "Group" else "userId"
        requested = {element[key] for element in body}
        assert requested and requested == {TARGET}
        # These fixtures demonstrate complete success; live batches may omit IDs.
        assert set(result["data"]) == requested
        assert all(value["id"] == key for key, value in result["data"].items())
    if resource in ("Group", "User") and operation in ("get", "replace"):
        assert result["id"] == request.url.path.rsplit("/", 1)[1]
    if resource == "Group" and operation in ("create", "replace"):
        for field in ("name", "organizations", "attributes"):
            assert result[field] == body[field]
        assert body["organizations"]
    if operation == "replace" and resource.endswith("ProviderInfo"):
        assert result == body
    if resource == "GroupMembershipExpirationPolicy" and operation == "replace":
        # Both fields are optional in the SDK; this reader example must set a policy.
        assert any(body.get(field) is not None for field in ("maximumDuration", "maximumValue"))
        policy = TypeAdapter(contract(resource, operation)["response"]).validate_python(body)
        assert result == normalized(policy)
    if resource == "GroupMember" and operation == "list":
        assert not (request.url.params.get("includeExpirations") == "true"
                    and request.url.params.get("transitive") == "true")
    if resource == "GroupMember" and operation in ("add", "remove"):
        assert body["principalIds"] == [MEMBER]
        assert MEMBER != TARGET
        assert result is None
    if resource == "User" and operation in ("delete", "revoke_all_tokens"):
        assert result is None
    if resource == "User" and operation == "get":
        assert result["status"] == request.url.params.get("status", "ACTIVE")
    if operation in ("list", "list_current", "search"):
        assert isinstance(result["data"], list) and result["data"]
    if resource == "User" and operation == "profile_picture":
        assert isinstance(result, bytes) and result


def successful_example(resource, operation):
    namespace = example(resource, operation)
    requests = []

    def handler(request):
        requests.append(request)
        if resource == "Group" and operation == "replace" and request.method == "GET":
            return response(namespace["EXISTING"])
        return response(namespace["SUCCESS"])

    result = execute(namespace, resource, handler)
    assert len(requests) == (2 if resource == "Group" and operation == "replace" else 1)
    return namespace, requests[-1], result


def test_owned_operations_match_frozen_sdk_and_source_register():
    assert importlib.metadata.version("foundry-platform-sdk") == "1.101.0"
    assert {row["id"] for row in ROWS} == {f"v2.admin.{r}.{op}" for r, op in CASES}
    for row in ROWS:
        resource, operation = row["id"].split(".")[-2:]
        source = contract(resource, operation)
        frozen = ORACLE["operations"][row["id"]]
        assert source["source_hash"] == row["source_sha256"] == frozen["source_sha256"]
        assert source["method"] == frozen["documentation"]["method"]
        assert source["path"] == frozen["documentation"]["resource_path"]



@pytest.mark.parametrize("resource,operation", CASES)
def test_every_reader_operation_has_sdk_wire_and_business_correspondence(resource, operation):
    _, request, result = successful_example(resource, operation)
    check_wire(resource, operation, request)
    check_business(resource, operation, request, result)
    model = contract(resource, operation)["response"]
    if model not in (None, bytes):
        TypeAdapter(model).validate_python(result)


@pytest.mark.parametrize("resource,operation", CASES)
def test_declared_errors_keep_typed_identity_and_target_parameters(resource, operation):
    namespace = example(resource, operation)
    declared = contract(resource, operation)["errors"]
    cases = {error["name"]: error for error in namespace["ERRORS"]}
    assert cases.keys() == declared.keys()
    for name, error_type in declared.items():
        case = cases[name]
        for key in ("groupId", "userId", "principalId"):
            if key in case["parameters"]:
                assert case["parameters"][key] == (MEMBER if name == "PrincipalNotFound" else TARGET)

        def failure(request):
            if resource == "Group" and operation == "replace" and request.method == "GET":
                return response(namespace["EXISTING"])
            check_wire(resource, operation, request)
            return httpx.Response(case["status"], json={
                "errorName": name, "errorCode": case["code"], "parameters": case["parameters"],
                "errorInstanceId": OTHER,
            })

        with pytest.raises(error_type) as raised:
            execute(namespace, resource, failure)
        error = raised.value
        assert isinstance(error, PalantirRPCException)
        assert error.name == name and normalized(error.parameters) == case["parameters"]
        assert error.error_instance_id == OTHER


@pytest.mark.parametrize("resource", ("Group", "User"))
@pytest.mark.parametrize("fault", ("wrong_map_key", "wrong_model_id", "missing_requested_result"))
def test_batch_business_oracle_rejects_uncorrelated_success(resource, fault):
    _, request, result = successful_example(resource, "get_batch")
    damaged = copy.deepcopy(result)
    if fault == "wrong_map_key":
        damaged["data"][OTHER] = damaged["data"].pop(TARGET)
    elif fault == "wrong_model_id":
        damaged["data"][TARGET]["id"] = OTHER
    else:
        damaged["data"].clear()
    with pytest.raises(AssertionError):
        check_business(resource, "get_batch", request, damaged)


@pytest.mark.parametrize("resource", ("Group", "User"))
def test_batch_missing_request_id_fails_sdk_validation_before_http(resource):
    namespace = example(resource, "get_batch")

    def unexpected(request):
        raise AssertionError("Invalid batch reached HTTP transport")

    with namespace["mock_resource"](contract(resource, "get_batch")["client"], unexpected) as client:
        with pytest.raises(ValidationError):
            client.with_raw_response.get_batch(body=[{}])


@pytest.mark.parametrize("resource,operation", [("Group", "get"), ("User", "get"),
                                               ("Group", "replace")])
def test_business_oracle_rejects_valid_model_for_wrong_target(resource, operation):
    _, request, result = successful_example(resource, operation)
    result["id"] = OTHER
    TypeAdapter(contract(resource, operation)["response"]).validate_python(result)
    with pytest.raises(AssertionError):
        check_business(resource, operation, request, result)


def test_group_replace_preserves_reserved_attributes_from_actual_preflight():
    namespace = example("Group", "replace")
    existing = copy.deepcopy(namespace["EXISTING"])
    existing["attributes"]["multipass:new-reserved"] = ["must-survive"]
    existing["attributes"]["unrelated"] = ["preserve"]
    requests = []

    def handler(request):
        requests.append(request)
        if request.method == "GET":
            return response(existing)
        body = json.loads(request.content)
        assert body["organizations"] == existing["organizations"]
        for key, value in existing["attributes"].items():
            if key != "team":
                assert body["attributes"][key] == value
        return response({**existing, **body})

    result = execute(namespace, "Group", handler)
    assert [request.method for request in requests] == ["GET", "PUT"]
    assert result["attributes"]["team"] == ["analytics"]


def test_membership_examples_target_requested_principal_and_preserve_other_members():
    namespace = example("GroupMember", "add")
    members = {OTHER}
    observed = []

    def service(request):
        observed.append(request)
        assert request.url.path.startswith(f"/api/v2/admin/groups/{TARGET}/groupMembers")
        if request.method == "GET":
            return response({"data": [{"principalId": principal, "principalType": "USER"}
                                      for principal in sorted(members)]})
        requested = set(json.loads(request.content)["principalIds"])
        assert requested == {MEMBER}
        if request.url.path.endswith("/add"):
            members.update(requested)
        else:
            assert request.url.path.endswith("/remove")
            members.difference_update(requested)
        return response(None)

    client_type = contract("GroupMember", "add")["client"]
    with namespace["mock_resource"](client_type, service) as client:
        for operation, expected in (("add", {OTHER, MEMBER}), ("remove", {OTHER})):
            raw = example("GroupMember", operation)["invoke"](client)
            try:
                assert raw.decode() is None
            finally:
                raw.close()
            listed = list(client.list(group_id=TARGET))
            assert {member.principal_id for member in listed} == expected
    assert [request.method for request in observed] == ["POST", "GET", "POST", "GET"]


@pytest.mark.parametrize("fault", ("empty_request", "empty_response", "changed_duration"))
def test_policy_example_rejects_empty_or_different_replacement(fault):
    _, request, result = successful_example("GroupMembershipExpirationPolicy", "replace")
    if fault == "empty_request":
        request = httpx.Request(request.method, request.url, content=b"{}")
        result = {}
    elif fault == "empty_response":
        result = {}
    else:
        result["maximumDuration"] = "7200"
    with pytest.raises(AssertionError):
        check_business("GroupMembershipExpirationPolicy", "replace", request, result)


def test_membership_example_rejects_transitive_expiration_combination():
    _, request, result = successful_example("GroupMember", "list")
    invalid = httpx.Request(request.method, request.url.copy_merge_params({
        "includeExpirations": "true", "transitive": "true",
    }))
    with pytest.raises(AssertionError):
        check_business("GroupMember", "list", invalid, result)
