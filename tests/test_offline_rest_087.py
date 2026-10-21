"""Narrow SDK integer-path bridge regressions; other47-op tests follow authoring."""

import importlib.util
from pathlib import Path

import httpx
import pytest

FILE = Path(__file__).parents[1] / ".agents/skills/pal-found-dev/examples/rest/087/model_studio_config_version.py"
SPEC = importlib.util.spec_from_file_location("model_studio_bridge", FILE)
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)


def test_native_sdk_failure_and_direct_rest_positive_named_generic_budget_cases():
    bridge.verify()


@pytest.mark.parametrize("body", [b"upstream unavailable", b'{"errorName": []}', b'{"parameters": []}'])
def test_malformed_http_errors_remain_http_errors_and_response_closes(body):
    responses = []
    def handler(request):
        response = httpx.Response(503, content=body)
        responses.append(response)
        return response
    with httpx.Client(transport=httpx.MockTransport(handler)) as client:
        with pytest.raises(httpx.HTTPStatusError):
            bridge.get_config_version(client, hostname="offline.example.invalid", token="fixture",
                                      studio_rid=bridge.STUDIO, version=1)
    assert len(responses) == 1 and responses[0].is_closed


def test_direct_rest_rejects_string_version_and_preview_before_http():
    def unexpected(request):
        raise AssertionError("Invalid input must not send HTTP")
    with httpx.Client(transport=httpx.MockTransport(unexpected)) as client:
        with pytest.raises(TypeError, match="version must be an integer"):
            bridge.get_config_version(client, hostname="offline.example.invalid", token="fixture",
                                      studio_rid=bridge.STUDIO, version="1")
        with pytest.raises(TypeError, match="preview must be a boolean"):
            bridge.get_config_version(client, hostname="offline.example.invalid", token="fixture",
                                      studio_rid=bridge.STUDIO, version=1, preview="false")
