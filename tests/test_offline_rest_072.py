"""Regressions for Admin marking inputs, result identity and role restrictions.

The assertions inspect requests produced by reader examples through the real SDK.
They supplement the full operation/error coverage in test_offline_rest_wave1.py.
"""

import json
import runpy
import socket
from pathlib import Path

import httpx
import pytest


BASE = Path(__file__).resolve().parents[1] / ".agents/skills/pal-found-dev/examples/rest/072/v2/admin"


@pytest.fixture(autouse=True)
def deny_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("REST072 tests attempted network access")

    monkeypatch.setattr(socket.socket, "connect", denied)
    monkeypatch.setattr(socket.socket, "connect_ex", denied)
    monkeypatch.setattr(socket, "create_connection", denied)
    monkeypatch.setattr(socket, "getaddrinfo", denied)


def example(resource, operation):
    return runpy.run_path(str(BASE / resource / f"{operation}.py"))


def invoke_example(namespace, resource):
    requests = []

    def respond(request):
        requests.append(request)
        return httpx.Response(200, json=namespace["SUCCESS"])

    with namespace["mock_resource"](namespace[resource + "Client"], respond) as client:
        raw = namespace["invoke"](client)
        try:
            outcome = raw.decode().model_dump(mode="json", by_alias=True, exclude_none=True)
        finally:
            raw.close()
    assert len(requests) == 1
    return requests[0], outcome


@pytest.mark.parametrize("resource,request_key", [("Marking", "markingId"), ("Role", "roleId")])
def test_batch_examples_correlate_requested_ids_with_map_keys_and_models(resource, request_key):
    request, outcome = invoke_example(example(resource, "get_batch"), resource)
    requested = {item[request_key] for item in json.loads(request.content)}
    assert requested
    # These reader fixtures represent complete success, although live batches can omit IDs.
    assert set(outcome["data"]) == requested
    assert {value["id"] for value in outcome["data"].values()} == requested


@pytest.mark.parametrize("resource", ["CbacBanner", "CbacMarkingRestrictions"])
def test_cbac_examples_send_marking_ids_before_claiming_specific_results(resource):
    namespace = example(resource, "get")
    request, outcome = invoke_example(namespace, resource)
    requested = request.url.params.get_list("markingIds")
    assert requested and all(requested)
    assert request.url.params["preview"] == "true"
    if resource == "CbacBanner":
        assert outcome["markings"] == requested
    else:
        assert outcome["disallowedMarkings"]
        assert outcome["requiredMarkings"]
    permission = next(error for error in namespace["ERRORS"] if error["code"] == "PERMISSION_DENIED")
    assert permission["parameters"]["markingIds"] == requested


def test_classification_example_accounts_for_success_and_invalid_input_separately():
    request, outcome = invoke_example(example("Marking", "parse_classifications"), "Marking")
    requested = set(json.loads(request.content)["classificationStrings"])
    parsed, errors = set(outcome["parsed"]), set(outcome["errors"])
    assert parsed and errors
    assert parsed.isdisjoint(errors)
    assert parsed | errors == requested
    assert outcome["parsed"]["MTS//MNF"] == ["MNF", "MTS"]
    assert "INVALID_MARKING" in outcome["errors"]


@pytest.mark.parametrize("operation", ["add", "remove"])
def test_role_examples_distinguish_organization_administer_and_last_admin(operation, monkeypatch):
    namespace = example("MarkingRoleAssignment", operation)
    original = namespace["mock_resource"]
    observed = []

    def capture(client_type, handler):
        def checked(request):
            response = handler(request)
            observed.append((request, response))
            return response

        return original(client_type, checked)

    monkeypatch.setitem(namespace["verify"].__globals__, "mock_resource", capture)
    namespace["verify"]()
    assert observed
    success = json.loads(observed[0][0].content)["roleAssignments"]
    assert {assignment["role"] for assignment in success} <= {"USE", "DECLASSIFY"}
    errors = {response.json()["errorName"]: request for request, response in observed[1:]}
    organization_request = errors["OrganizationMarkingAdministerRoleNotSupported"]
    assert "synthetic-organization-marking" in organization_request.url.path
    assert json.loads(organization_request.content)["roleAssignments"][0]["role"] == "ADMINISTER"
    if operation == "remove":
        last_admin = errors["RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed"]
        assert "synthetic-organization-marking" not in last_admin.url.path
        assert json.loads(last_admin.content)["roleAssignments"][0]["role"] == "ADMINISTER"
