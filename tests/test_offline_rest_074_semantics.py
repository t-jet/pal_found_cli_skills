"""REST-074 success fixtures must agree with serialized SDK requests."""

import copy
import json
import runpy
import socket
from pathlib import Path

import httpx
import pytest


BASE = Path(__file__).parents[1] / ".agents/skills/pal-found-dev/examples/rest/074"
FILES = tuple(f"{version}/datasets/File/{operation}.py"
              for version in ("v1", "v2") for operation in ("get", "upload"))
SCHEMAS = tuple(f"v2/datasets/Dataset/{operation}.py"
                for operation in ("get_schema", "put_schema"))
REMOVE = "v2/datasets/View/remove_backing_datasets.py"
ADD_KEY = "v2/datasets/View/add_primary_key.py"
CORRECTED = (*FILES, *SCHEMAS, REMOVE, ADD_KEY)


@pytest.fixture(autouse=True)
def deny_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("External network denied in REST-074 tests")

    for name in ("connect", "connect_ex"):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ("create_connection", "getaddrinfo"):
        monkeypatch.setattr(socket, name, denied)


def load_example(relative_path):
    return runpy.run_path(str(BASE / relative_path))["verify"].__globals__


def capture_success_request(example, monkeypatch):
    requests = []
    check_result = example["check_result"]

    def checked(result, request):
        requests.append(request)
        check_result(result, request)

    monkeypatch.setitem(example, "check_result", checked)
    example["verify"]()
    assert len(requests) == 1
    return requests[0], check_result


@pytest.mark.parametrize("path", sorted(BASE.glob("v*/datasets/*/*.py")), ids=lambda p: p.relative_to(BASE).as_posix())
def test_all_rest074_examples_pass_without_network(path):
    runpy.run_path(str(path))["verify"]()


@pytest.mark.parametrize("relative_path", (*FILES, *SCHEMAS))
def test_examples_reject_wrong_returned_identity(relative_path):
    example = load_example(relative_path)
    key = "path" if relative_path in FILES else "branchName"
    example["SUCCESS"][key] = "different-resource"
    with pytest.raises(AssertionError, match="differs from request"):
        example["verify"]()


@pytest.mark.parametrize("fault", ("missing", "columns", "resolution"))
def test_add_primary_key_rejects_missing_or_different_key(fault):
    example = load_example(ADD_KEY)
    if fault == "missing":
        example["SUCCESS"].pop("primaryKey")
    elif fault == "columns":
        example["SUCCESS"]["primaryKey"]["columns"] = ["other-column"]
    else:
        example["SUCCESS"]["primaryKey"]["resolution"] = {"type": "duplicate", "resolutionStrategy": {"type": "latestWins", "columns": ["updated"]}}
    with pytest.raises(AssertionError, match="Returned primary key differs from request"):
        example["verify"]()


@pytest.mark.parametrize("branch", (None, "master"))
def test_remove_rejects_removed_pair_with_implicit_or_explicit_branch(branch):
    example = load_example(REMOVE)
    backing = copy.deepcopy(example["EXPECTED_BODY"]["backingDatasets"][0])
    if branch is not None:
        backing["branch"] = branch
    example["SUCCESS"]["backingDatasets"] = [backing]
    with pytest.raises(AssertionError, match="Removed backing dataset remains in result"):
        example["verify"]()


@pytest.mark.parametrize("relative_path", CORRECTED)
def test_result_guards_use_actual_serialized_request(relative_path, monkeypatch):
    example = load_example(relative_path)
    request, check_result = capture_success_request(example, monkeypatch)
    result = copy.deepcopy(example["SUCCESS"])
    if relative_path == "v1/datasets/File/upload.py":
        changed = httpx.Request(request.method, request.url.copy_set_param("filePath", "other/file.csv"))
        replacement = ("path", "other/file.csv")
    elif relative_path in FILES:
        url = request.url.copy_with(path=request.url.path.replace("inspections/status.csv", "other/file.csv"))
        changed = httpx.Request(request.method, url)
        replacement = ("path", "other/file.csv")
    elif relative_path.endswith("get_schema.py"):
        changed = httpx.Request(request.method, request.url.copy_set_param("branchName", "feature"))
        replacement = ("branchName", "feature")
    else:
        body = json.loads(request.content)
        if relative_path.endswith("put_schema.py"):
            body["branchName"] = "feature"
            replacement = ("branchName", "feature")
        elif relative_path == ADD_KEY:
            body["primaryKey"]["columns"] = ["other-column"]
            replacement = ("primaryKey", body["primaryKey"])
        else:
            survivor = copy.deepcopy(body["backingDatasets"][0])
            survivor["branch"] = "feature"
            result["backingDatasets"] = [survivor]
            check_result(result, request)
            body["branch"] = "feature"
            replacement = ("backingDatasets", [])
        changed = httpx.Request(request.method, request.url, json=body)

    with pytest.raises(AssertionError):
        check_result(result, changed)
    result[replacement[0]] = replacement[1]
    check_result(result, changed)


def test_put_schema_rejects_different_returned_schema():
    example = load_example("v2/datasets/Dataset/put_schema.py")
    example["SUCCESS"]["schema"]["fieldSchemaList"][0]["name"] = "other-column"
    with pytest.raises(AssertionError, match="Returned schema differs from request"):
        example["verify"]()
