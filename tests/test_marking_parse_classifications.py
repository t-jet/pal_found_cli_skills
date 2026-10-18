"""Check the SDK transport boundary for classification batch sizes."""

import json
from unittest.mock import patch

import httpx
import pytest
from foundry_sdk import Config, UserTokenAuth
from foundry_sdk.v2.admin.marking import MarkingClient


@pytest.mark.parametrize("count", [0, 1001])
def test_sdk_forwards_out_of_range_classification_batches(count):
    submitted = ["duplicate"] * count
    requests = []

    def handle(request):
        requests.append(request)
        return httpx.Response(200, json={"parsed": {}, "errors": {}})

    with httpx.Client(transport=httpx.MockTransport(handle), timeout=30) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            client = MarkingClient(
                auth=UserTokenAuth(token="offline-fixture-token"),
                hostname="offline.example.invalid",
                config=Config(timeout=30, max_retries=1),
            )
        client.parse_classifications(classification_strings=submitted, preview=True)

    assert len(requests) == 1
    assert requests[0].url.path == "/api/v2/admin/markings/parseClassifications"
    assert json.loads(requests[0].content)["classificationStrings"] == submitted
