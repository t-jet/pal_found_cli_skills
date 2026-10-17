"""Folder create/get/children: real SDK calls against synthetic HTTP fixtures."""

import json
import sys
from functools import partial
from pathlib import Path

import httpx
from foundry_sdk import PalantirRPCException
from foundry_sdk.v2.filesystem.folder import FolderClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from bounded_pages import fetch_pages
from mock_transport import mock_resource
from response_modes import FOLDER_RID, PARENT_RID, folder_payload, resource_payload


def verify():
    seen = []

    def handler(request):
        assert request.headers["Authorization"] == "Bearer offline-fixture-token"
        seen.append((request.method, request.url.path))
        if request.method == "POST":
            assert request.url.path == "/api/v2/filesystem/folders"
            assert json.loads(request.content) == {
                "displayName": "Governance", "parentFolderRid": PARENT_RID,
            }
            return httpx.Response(200, json=folder_payload())
        if request.url.path.endswith("/children"):
            assert request.url.params["pageSize"] == "100"
            if not request.url.params.get("pageToken"):
                return httpx.Response(200, json={"data": [], "nextPageToken": "next"})
            assert request.url.params["pageToken"] == "next"
            return httpx.Response(200, json={"data": [resource_payload()]})
        assert request.url.path.endswith(FOLDER_RID)
        return httpx.Response(200, json=folder_payload())

    with mock_resource(FolderClient, handler) as folders:
        created = folders.create(display_name="Governance", parent_folder_rid=PARENT_RID,
                                 request_timeout=30)
        assert created.rid == FOLDER_RID and created.parent_folder_rid == PARENT_RID
        fetched = folders.get(created.rid, request_timeout=30)
        assert fetched.display_name == "Governance"
        result = fetch_pages(partial(folders.with_raw_response.children, FOLDER_RID,
                                     page_size=100, request_timeout=30),
                             max_pages=3, max_items=10)
        assert result.complete and result.pages == 2 and result.items[0].rid == FOLDER_RID
    assert len(seen) == 4

    # Every operation has a distinct source-declared error fixture.
    cases = [
        ("create", "CreateFolderPermissionDenied", "PERMISSION_DENIED", {},
         lambda c: c.create(display_name="Governance", parent_folder_rid=PARENT_RID)),
        ("get", "FolderNotFound", "NOT_FOUND", {"folderRid": FOLDER_RID},
         lambda c: c.get(FOLDER_RID)),
        ("children", "FolderNotFound", "NOT_FOUND", {"folderRid": FOLDER_RID},
         lambda c: list(c.children(FOLDER_RID))),
    ]
    for operation, name, code, parameters, invoke in cases:
        def denied(request):
            return httpx.Response(403 if code == "PERMISSION_DENIED" else 404, json={
                "errorName": name, "errorCode": code, "parameters": parameters,
                "errorInstanceId": "00000000-0000-0000-0000-000000000004",
            })
        with mock_resource(FolderClient, denied) as folders:
            try:
                invoke(folders)
            except PalantirRPCException as error:
                assert error.name == name and error.parameters == parameters, operation
                assert type(error).__name__ == name
            else:
                raise AssertionError(f"Missing {operation} error")


if __name__ == "__main__":
    verify()
    print("Folder create/get/children request, result and error fixtures passed")
