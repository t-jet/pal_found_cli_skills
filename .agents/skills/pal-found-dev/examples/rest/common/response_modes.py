"""Run ordinary, raw, streaming and async-iterator handling without a network.

Inputs/results are synthetic. These assertions prove SDK invocation and
handling, not enrollment permission or server behavior.
"""

import asyncio
import inspect
import json
from functools import partial

import httpx
from foundry_sdk import AsyncResourceIterator, PalantirRPCException
from foundry_sdk.v2.filesystem.folder import AsyncFolderClient, FolderClient

from bounded_pages import fetch_pages, fetch_pages_async
from mock_transport import mock_async_resource, mock_resource

FOLDER_RID = "ri.compass.main.folder.00000000-0000-0000-0000-000000000001"
PARENT_RID = "ri.compass.main.folder.00000000-0000-0000-0000-000000000002"
SPACE_RID = "ri.compass.main.space.00000000-0000-0000-0000-000000000003"


def folder_payload():
    return {
        "rid": FOLDER_RID, "displayName": "Governance", "path": "/Governance",
        "type": "FOLDER", "createdBy": "00000000-0000-0000-0000-000000000005",
        "updatedBy": "00000000-0000-0000-0000-000000000005",
        "createdTime": "2026-10-06T00:00:00Z", "updatedTime": "2026-10-06T00:00:00Z",
        "trashStatus": "NOT_TRASHED", "parentFolderRid": PARENT_RID, "spaceRid": SPACE_RID,
    }


def resource_payload():
    return {**folder_payload(), "type": "COMPASS_FOLDER", "projectRid": PARENT_RID}


def handler(request):
    assert request.headers["Authorization"] == "Bearer offline-fixture-token"
    assert request.method == "GET"
    if request.url.path.endswith("/children"):
        if request.url.params.get("pageToken") is None:
            return httpx.Response(200, json={"data": [], "nextPageToken": "second-page"})
        assert request.url.params["pageToken"] == "second-page"
        return httpx.Response(200, json={"data": [resource_payload()]})
    assert request.url.path == f"/api/v2/filesystem/folders/{FOLDER_RID}"
    return httpx.Response(200, json=folder_payload())


def read_bytes(chunks, max_bytes=4096, max_chunks=100):
    accepted, total = [], 0
    for number, chunk in enumerate(chunks, start=1):
        total += len(chunk)
        if number > max_chunks or total > max_bytes:
            raise RuntimeError("Stream retrieval budget exhausted")
        accepted.append(chunk)
    return b"".join(accepted)


async def read_async_bytes(chunks, max_bytes=4096, max_chunks=100):
    accepted, total, number = [], 0, 0
    async for chunk in chunks:
        number += 1
        total += len(chunk)
        if number > max_chunks or total > max_bytes:
            raise RuntimeError("Stream retrieval budget exhausted")
        accepted.append(chunk)
    return b"".join(accepted)


def verify_sync():
    with mock_resource(FolderClient, handler) as folder:
        result = folder.get(FOLDER_RID, request_timeout=30)
        assert result.rid == FOLDER_RID and result.display_name == "Governance"
        raw = folder.with_raw_response.get(FOLDER_RID, request_timeout=30)
        try:
            assert raw.status_code == 200 and raw.decode().parent_folder_rid == PARENT_RID
        finally:
            raw.close()
        with folder.with_streaming_response.get(FOLDER_RID, request_timeout=30) as stream:
            payload = read_bytes(stream.iter_bytes())
            assert json.loads(payload)["rid"] == FOLDER_RID
        try:
            with folder.with_streaming_response.get(FOLDER_RID, request_timeout=30) as stream:
                read_bytes(stream.iter_bytes(), max_bytes=10)
        except RuntimeError as error:
            assert str(error) == "Stream retrieval budget exhausted"
            assert stream._response.is_closed
        else:
            raise AssertionError("Expected finite stream-budget rejection")
        page = partial(folder.with_raw_response.children, FOLDER_RID, page_size=100, request_timeout=30)
        result = fetch_pages(page, max_pages=3, max_items=10)
        assert result.complete and result.pages == 2 and result.items[0].rid == FOLDER_RID

    def missing(request):
        assert request.url.path.endswith(FOLDER_RID)
        return httpx.Response(404, json={
            "errorCode": "NOT_FOUND", "errorName": "FolderNotFound",
            "errorInstanceId": "00000000-0000-0000-0000-000000000004",
            "parameters": {"folderRid": FOLDER_RID},
        })

    with mock_resource(FolderClient, missing) as folder:
        try:
            folder.get(FOLDER_RID, request_timeout=30)
        except PalantirRPCException as error:
            assert error.name == "FolderNotFound" and error.parameters["folderRid"] == FOLDER_RID
        else:
            raise AssertionError("Expected the documented FolderNotFound fixture")


async def verify_async():
    async with mock_async_resource(AsyncFolderClient, handler) as folder:
        result = await folder.get(FOLDER_RID, request_timeout=30)
        assert result.rid == FOLDER_RID
        iterator = folder.children(FOLDER_RID, page_size=100, request_timeout=30)
        assert isinstance(iterator, AsyncResourceIterator) and not inspect.isawaitable(iterator)
        results = [item async for item in iterator]
        assert len(results) == 1 and results[0].rid == FOLDER_RID
        raw = await folder.with_raw_response.get(FOLDER_RID, request_timeout=30)
        try:
            assert raw.decode().display_name == "Governance"
        finally:
            await raw.aclose()
        async with folder.with_streaming_response.get(FOLDER_RID, request_timeout=30) as stream:
            payload = await read_async_bytes(stream.aiter_bytes())
            assert json.loads(payload)["rid"] == FOLDER_RID
        try:
            async with folder.with_streaming_response.get(FOLDER_RID, request_timeout=30) as stream:
                await read_async_bytes(stream.aiter_bytes(), max_bytes=10)
        except RuntimeError as error:
            assert str(error) == "Stream retrieval budget exhausted"
            assert stream._response.is_closed
        else:
            raise AssertionError("Expected finite async stream-budget rejection")
        page = partial(folder.with_raw_response.children, FOLDER_RID, page_size=100, request_timeout=30)
        result = await fetch_pages_async(page, max_pages=3, max_items=10)
        assert result.complete and result.pages == 2


if __name__ == "__main__":
    verify_sync()
    asyncio.run(verify_async())
    print("Synthetic SDK ordinary/raw/streaming/async-iterator fixtures passed")
