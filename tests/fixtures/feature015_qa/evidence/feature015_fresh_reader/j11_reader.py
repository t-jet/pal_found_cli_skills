"""Source-blind J11 reader: public SDK routes against a denied-network fixture."""

import json
import socket
import sys
from functools import partial
from pathlib import Path
from unittest.mock import patch

import httpx
from foundry_sdk import Config, FoundryClient, PalantirRPCException, UserTokenAuth

SKILL = Path(__file__).parent / "skill"
sys.path.insert(0, str(SKILL / "examples/rest/common"))
from bounded_pages import fetch_pages  # noqa: E402

FOLDER = "ri.compass.main.folder.00000000-0000-0000-0000-000000000001"
PARENT = "ri.compass.main.folder.00000000-0000-0000-0000-000000000002"
SPACE = "ri.compass.main.space.00000000-0000-0000-0000-000000000003"
DATASET = "ri.foundry.main.dataset.00000000-0000-0000-0000-000000000004"
FILE = "reads/sample.bin"


def payload():
    return {
        "rid": FOLDER, "displayName": "Synthetic", "path": "/Synthetic",
        "type": "COMPASS_FOLDER", "createdBy": "00000000-0000-0000-0000-000000000005",
        "updatedBy": "00000000-0000-0000-0000-000000000005",
        "createdTime": "2026-10-06T00:00:00Z", "updatedTime": "2026-10-06T00:00:00Z",
        "trashStatus": "NOT_TRASHED", "parentFolderRid": PARENT,
        "spaceRid": SPACE, "projectRid": PARENT,
    }


def fail_network(*_args, **_kwargs):
    raise AssertionError("Public DNS/socket access attempted")


def make_client(handler):
    transport = httpx.Client(transport=httpx.MockTransport(handler), timeout=30)
    patcher = patch("foundry_sdk._core.api_client.HttpClient", return_value=transport)
    patcher.start()
    client = FoundryClient(
        auth=UserTokenAuth("offline-fixture-token"),
        hostname="https://offline.example.invalid",
        config=Config(timeout=30, max_retries=1,
                      propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
    )
    return client, transport, patcher


def main():
    calls = []
    mode = {"kind": "success", "page": "normal"}

    def handler(req):
        assert req.headers["Authorization"] == "Bearer offline-fixture-token"
        assert req.method == "GET" and req.content == b""
        path = req.url.path
        calls.append((req.method, path, dict(req.url.params)))
        if mode["kind"] == "error":
            code, name, category = mode["error"]
            parameters = {}
            if name == "GetFileContentPermissionDenied":
                parameters = {"datasetRid": DATASET, "filePath": FILE}
            elif name == "FileNotFoundOnBranch":
                parameters = {"datasetRid": DATASET, "branchName": "master", "path": FILE}
            return httpx.Response(code, json={"errorName": name, "errorCode": category,
                "errorInstanceId": "00000000-0000-0000-0000-000000000006",
                "parameters": parameters})
        if path == f"/api/v2/filesystem/folders/{FOLDER}/children":
            assert req.url.params["pageSize"] == "2"
            token = req.url.params.get("pageToken")
            if token is None:
                return httpx.Response(200, json={"data": [], "nextPageToken": "next"})
            assert token == "next"
            next_token = "next" if mode["page"] == "repeat" else None
            body = {"data": [payload()]}
            if next_token:
                body["nextPageToken"] = next_token
            return httpx.Response(200, json=body)
        if path == f"/api/v2/datasets/{DATASET}":
            return httpx.Response(200, json={"rid": DATASET, "name": "Synthetic",
                "parentFolderRid": PARENT, "createdBy": "00000000-0000-0000-0000-000000000005",
                "updatedBy": "00000000-0000-0000-0000-000000000005",
                "createdTime": "2026-10-06T00:00:00Z",
                "updatedTime": "2026-10-06T00:00:00Z", "trashStatus": "NOT_TRASHED"})
        if path == f"/api/v2/datasets/{DATASET}/files/{FILE}/content":
            assert req.url.params["branchName"] == "master"
            assert req.headers["Accept"] == "application/octet-stream"
            return httpx.Response(200, content=b"abcdef")
        raise AssertionError(f"Unexpected request: {path}")

    with patch.object(socket, "getaddrinfo", fail_network), patch.object(socket.socket, "connect", fail_network):
        client, transport, patcher = make_client(handler)
        try:
            result = fetch_pages(partial(client.filesystem.Folder.with_raw_response.children,
                                         FOLDER, page_size=2, request_timeout=30),
                                 max_pages=3, max_items=2)
            assert result.complete and result.pages == 2 and len(result.items) == 1
            assert result.items[0].rid == FOLDER
            dataset = client.datasets.Dataset.get(DATASET, request_timeout=30)
            assert dataset.rid == DATASET and dataset.parent_folder_rid == PARENT
            with client.datasets.Dataset.File.with_streaming_response.content(
                DATASET, FILE, branch_name="master", request_timeout=30,
            ) as response:
                chunks, total = [], 0
                for chunk in response.iter_bytes():
                    total += len(chunk)
                    assert total <= 8
                    chunks.append(chunk)
            assert b"".join(chunks) == b"abcdef"
            mode["page"] = "repeat"
            repeated = fetch_pages(partial(client.filesystem.Folder.with_raw_response.children,
                                           FOLDER, page_size=2, request_timeout=30),
                                   max_pages=4, max_items=2)
            assert not repeated.complete and repeated.reason == "repeated-token"
            assert repeated.pages == 2 and len(repeated.items) == 1
            mode["page"] = "normal"
            try:
                with client.datasets.Dataset.File.with_streaming_response.content(
                    DATASET, FILE, branch_name="master", request_timeout=30,
                ) as response:
                    total = 0
                    for chunk in response.iter_bytes():
                        total += len(chunk)
                        if total > 4:
                            raise ValueError("byte-budget")
            except ValueError as exc:
                assert str(exc) == "byte-budget"
            else:
                raise AssertionError("Expected bounded partial stream")
            for status, name, category in [
                (401, "Unauthorized", "UNAUTHORIZED"),
                (403, "GetFileContentPermissionDenied", "PERMISSION_DENIED"),
                (404, "FileNotFoundOnBranch", "NOT_FOUND"),
                (429, "TooManyRequests", "TOO_MANY_REQUESTS"),
                (503, "ServiceUnavailable", "SERVICE_UNAVAILABLE"),
            ]:
                mode["kind"] = "error"
                mode["error"] = (status, name, category)
                try:
                    client.datasets.Dataset.File.content(DATASET, FILE,
                        branch_name="master", request_timeout=30)
                except Exception as exc:
                    if status in (429, 503):
                        assert type(exc).__name__ in {"RateLimitError", "ServiceUnavailable"}, type(exc).__name__
                    else:
                        assert isinstance(exc, PalantirRPCException)
                        assert exc.name == name
                        assert type(exc).__name__ == ("UnauthorizedError" if status == 401 else name)
                else:
                    raise AssertionError(f"Expected HTTP {status}")
            mode["kind"] = "success"
            assert len(calls) == 12, calls
            print(json.dumps({"result": "PASS", "pages": result.pages,
                "repeated_token": repeated.reason, "binary_bytes": len(b"abcdef"),
                "named_errors": [401, 403, 404, 429, 503], "requests": calls}, indent=2))
        finally:
            patcher.stop()
            transport.close()


if __name__ == "__main__":
    main()
