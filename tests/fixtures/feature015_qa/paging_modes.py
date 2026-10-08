"""Compare one paged and one nonpaged SDK operation against local HTTP fixtures."""

from unittest.mock import patch

import httpx
from foundry_sdk import Config, ResourceIterator, UserTokenAuth
from foundry_sdk.v2.datasets.dataset import DatasetClient
from foundry_sdk.v2.filesystem.folder import FolderClient


FOLDER = "ri.compass.main.folder.00000000-0000-0000-0000-000000000001"
DATASET = "ri.foundry.main.dataset.00000000-0000-0000-0000-000000000002"


def run() -> None:
    requests = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append((request.url.path, request.url.params.get("pageToken")))
        if request.url.path.endswith("/children"):
            if request.url.params.get("pageToken") is None:
                return httpx.Response(200, json={"data": [], "nextPageToken": "next"})
            assert request.url.params["pageToken"] == "next"
            return httpx.Response(200, json={"data": [{
                "rid": FOLDER,
                "displayName": "Child",
                "path": "/Parent/Child",
                "type": "COMPASS_FOLDER",
                "createdBy": "00000000-0000-0000-0000-000000000005",
                "updatedBy": "00000000-0000-0000-0000-000000000005",
                "createdTime": "2026-10-06T00:00:00Z",
                "updatedTime": "2026-10-06T00:00:00Z",
                "trashStatus": "NOT_TRASHED",
                "parentFolderRid": FOLDER,
                "spaceRid": "ri.compass.main.space.00000000-0000-0000-0000-000000000003",
                "projectRid": FOLDER,
            }]})
        assert request.url.path == f"/api/v2/datasets/{DATASET}"
        assert not request.url.params
        return httpx.Response(200, json={
            "rid": DATASET, "name": "orders", "parentFolderRid": FOLDER,
        })

    with httpx.Client(transport=httpx.MockTransport(respond), timeout=10) as http:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=http):
            options = {
                "auth": UserTokenAuth(token="fixture-only"),
                "hostname": "offline.example.invalid",
                "config": Config(timeout=10, max_retries=1,
                                 propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
            }
            folders = FolderClient(**options)
            datasets = DatasetClient(**options)
        children = folders.children(FOLDER)
        assert isinstance(children, ResourceIterator)
        assert [item.display_name for item in children] == ["Child"]
        dataset = datasets.get(DATASET)
        assert dataset.name == "orders" and dataset.rid == DATASET
        assert not isinstance(dataset, ResourceIterator)

    assert requests == [
        (f"/api/v2/filesystem/folders/{FOLDER}/children", None),
        (f"/api/v2/filesystem/folders/{FOLDER}/children", "next"),
        (f"/api/v2/datasets/{DATASET}", None),
    ]
    print("PASS: paged children continued after empty page; Dataset.get returned one model")


if __name__ == "__main__":
    run()
