"""Check public v1/v2 File routes, omitted size and named error offline."""

from unittest.mock import patch

import httpx
from foundry_sdk import Config, PalantirRPCException, UserTokenAuth
from foundry_sdk.v1 import FoundryClient as V1Client
from foundry_sdk.v2 import FoundryClient as V2Client


DATASET = "ri.synthetic.main.dataset.00000000-0000-0000-0000-000000000001"
FILE = "inspections/status.csv"
BRANCH = "master"
PAYLOAD = b"id,status\n1,ready\n"


def exercise(version, client_type, read_name, selector):
    calls = []

    def handler(request):
        path = request.url.path
        calls.append((request.method, path))
        assert path.startswith(f"/api/{version}/datasets/{DATASET}/files/")
        assert request.url.params[selector] == BRANCH
        if path.endswith("missing.csv"):
            return httpx.Response(404, json={
                "errorName": "FileNotFoundOnBranch", "errorCode": "NOT_FOUND",
                "parameters": {"datasetRid": DATASET, selector: BRANCH,
                               "path": "missing.csv"},
                "errorInstanceId": "00000000-0000-0000-0000-000000000004",
            })
        assert path in {f"/api/{version}/datasets/{DATASET}/files/{FILE}",
                        f"/api/{version}/datasets/{DATASET}/files/{FILE}/content"}
        if path.endswith("/content") or (version == "v1" and request.headers.get("Accept") == "application/octet-stream"):
            return httpx.Response(200, content=PAYLOAD)
        return httpx.Response(200, json={"path": FILE,
                                        "transactionRid": DATASET,
                                        "updatedTime": "2026-10-07T00:00:00+00:00"})

    with httpx.Client(transport=httpx.MockTransport(handler), timeout=30) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            client = client_type(
                auth=UserTokenAuth("offline-fixture-token"),
                hostname="https://offline.example.invalid",
                config=Config(timeout=30, max_retries=1,
                              propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
            )
            assert not hasattr(client.datasets, "File")
            resource = client.datasets.Dataset.File
            selector_args = {selector.replace("Id", "_id").replace("Name", "_name"): BRANCH}
            metadata = resource.get(DATASET, FILE, **selector_args, request_timeout=30)
            assert metadata.path == FILE and metadata.size_bytes is None
            payload = getattr(resource, read_name)(DATASET, FILE, **selector_args,
                                                   request_timeout=30)
            assert payload == PAYLOAD
            # An omitted size does not reject valid bytes; the byte budget still applies.
            assert len(payload) <= 8 * 1024 * 1024
            try:
                resource.get(DATASET, "missing.csv", **selector_args, request_timeout=30)
            except PalantirRPCException as error:
                assert error.name == "FileNotFoundOnBranch"
            else:
                raise AssertionError("Expected named missing-file error")
    assert len(calls) == 3


if __name__ == "__main__":
    exercise("v1", V1Client, "read", "branchId")
    exercise("v2", V2Client, "content", "branchName")
    print("v1/v2 composed File routes, omitted size, bytes and named error passed")
