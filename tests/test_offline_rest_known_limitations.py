"""Independent SDK defect evidence and bounded public REST fallback checks."""

from pathlib import Path
import runpy
from unittest.mock import patch

import httpx
import pytest
from foundry_sdk import Config, UserTokenAuth
from foundry_sdk.v2.models.errors import ModelStudioNotFound
from foundry_sdk.v2.models.model_studio_config_version import ModelStudioConfigVersionClient

from test_offline_rest_acceptance import denied_public_network


STUDIO = "ri.synthetic.main.resource.11111111-1111-1111-1111-111111111111"
INSTANCE = "11111111-1111-1111-1111-111111111112"
EXAMPLE = Path(__file__).parents[1] / ".agents/skills/pal-found-dev/examples/rest/087/model_studio_config_version.py"


def load_adapter():
    return runpy.run_path(str(EXAMPLE))["get_config_version"]


def test_native_integer_path_fails_before_actual_http_transport():
    """Use SDK URL construction, without replacing call_api or _create_url."""
    touched = []
    with denied_public_network(), httpx.Client(
        transport=httpx.MockTransport(lambda request: touched.append(request))
    ) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            resource = ModelStudioConfigVersionClient(
                auth=UserTokenAuth(token="fixture"), hostname="qa.invalid",
                config=Config(max_retries=1),
            )
        with pytest.raises(Exception, match=r"quote_from_bytes\(\) expected bytes"):
            resource.get(STUDIO, 7, preview=True)
    assert touched == []


class ChunkStream(httpx.SyncByteStream):
    """Observable lifetime; independent chunks exceed either selected budget."""
    closed = False

    def __iter__(self):
        yield b"{"
        yield b'"tooLong":'
        yield b"1}"

    def close(self):
        self.closed = True


@pytest.mark.parametrize("budget", [{"max_bytes": 1}, {"max_chunks": 2}])
def test_direct_bridge_closes_on_independently_seeded_budget_exhaustion(budget):
    stream = ChunkStream()
    adapter = load_adapter()
    with denied_public_network(), httpx.Client(
        transport=httpx.MockTransport(lambda request: httpx.Response(200, stream=stream))
    ) as transport:
        with pytest.raises(RuntimeError, match="response budget exhausted"):
            adapter(transport, hostname="qa.invalid", token="fixture",
                    studio_rid=STUDIO, version=7, **budget)
    assert stream.closed


def test_direct_bridge_omits_preview_and_preserves_named_error_identity():
    """Independent input differs from the authored example's positive fixture."""
    requests = []

    def missing(request):
        requests.append(request)
        assert request.method == "GET"
        assert request.url.path == f"/api/v2/models/modelStudios/{STUDIO}/configVersions/7"
        assert "preview" not in request.url.params
        assert request.headers["Authorization"] == "Bearer fixture"
        return httpx.Response(404, json={
            "errorName": "ModelStudioNotFound", "errorCode": "NOT_FOUND",
            "errorInstanceId": INSTANCE, "parameters": {"studioRid": STUDIO},
        })

    adapter = load_adapter()
    with denied_public_network(), httpx.Client(transport=httpx.MockTransport(missing)) as transport:
        with pytest.raises(ModelStudioNotFound) as caught:
            adapter(transport, hostname="qa.invalid", token="fixture", studio_rid=STUDIO, version=7)
    assert len(requests) == 1
    assert caught.value.parameters == {"studioRid": STUDIO}
    assert caught.value.error_instance_id == INSTANCE
