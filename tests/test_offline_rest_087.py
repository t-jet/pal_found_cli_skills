"""SDK bridge regressions and source-derived story087 fixture semantics."""

import importlib.util
import socket
from pathlib import Path

import httpx
import pytest

FILE = Path(__file__).parents[1] / ".agents/skills/pal-found-dev/examples/rest/087/model_studio_config_version.py"
SPEC = importlib.util.spec_from_file_location("model_studio_bridge", FILE)
bridge = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(bridge)


@pytest.fixture(autouse=True)
def deny_public_network(monkeypatch):
    def denied(*args, **kwargs):
        raise AssertionError("Public network access forbidden in offline tests")

    for name in ("connect", "connect_ex"):
        monkeypatch.setattr(socket.socket, name, denied)
    for name in ("create_connection", "getaddrinfo", "gethostbyname", "gethostbyname_ex"):
        monkeypatch.setattr(socket, name, denied)


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


@pytest.fixture
def promote_version_example():
    path = Path(__file__).parents[1] / (
        ".agents/skills/pal-found-dev/examples/rest/087/v2/models/Model/promote_version.py"
    )
    spec = importlib.util.spec_from_file_location("promote_version_example", path)
    example = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(example)
    return example


def test_promote_version_copies_to_new_version_rid(promote_version_example):
    example = promote_version_example
    target_model_rid = example.EXPECTED_PATH.split("/")[-2]
    assert len({target_model_rid, example.EXPECTED_BODY["sourceModelVersionRid"],
                example.SUCCESS["rid"]}) == 3
    example.verify()


def test_promote_version_rejects_reused_source_version_rid(promote_version_example, monkeypatch):
    example = promote_version_example
    monkeypatch.setitem(example.SUCCESS, "rid", example.EXPECTED_BODY["sourceModelVersionRid"])
    with pytest.raises(AssertionError, match="Promoted model version must have a new RID"):
        example.verify()


CORRECTED_EXAMPLES = [
    "aip_agents/Agent/get", "aip_agents/Agent/all_sessions",
    "aip_agents/AgentVersion/get", "aip_agents/AgentVersion/list",
    "aip_agents/Session/blocking_continue", "aip_agents/Session/streaming_continue",
    "language_models/AnthropicModel/messages",
    "models/LiveDeployment/create", "models/LiveDeployment/replace",
]


def load_corrected_example(relative):
    path = Path(__file__).parents[1] / (
        ".agents/skills/pal-found-dev/examples/rest/087/v2/" + relative + ".py"
    )
    spec = importlib.util.spec_from_file_location("corrected_087_" + relative.replace("/", "_"), path)
    example = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(example)
    return example


def assert_source_semantics(relative, example):
    import re

    if "/AgentVersion/" in relative:
        rows = example.SUCCESS.get("data", [example.SUCCESS])
        for row in rows:
            assert row["string"] == f'{row["version"]["major"]}.{row["version"]["minor"]}'
    elif relative == "aip_agents/Agent/get":
        assert re.fullmatch(r"[0-9]+\.[0-9]+", example.SUCCESS["version"])
    elif relative == "aip_agents/Agent/all_sessions":
        for row in example.SUCCESS["data"]:
            assert re.fullmatch(r"[0-9]+\.[0-9]+", row["agentVersion"])
    for error in example.ERRORS:
        name, params = error["name"], error["parameters"]
        if name == "GpuTypeNotAvailable":
            assert params["requestedGpuType"] not in params["availableGpuTypes"]
        elif name == "InvalidGpuCount":
            assert not 1 <= params["providedGpuCount"] <= params["maxGpuCount"]
        elif name == "ThreadCountTooHigh":
            assert params["providedThreadCount"] > params["maxThreadCount"]
        elif name == "InvalidParameterType":
            assert params["expectedType"] != params["receivedType"]
        elif name == "MultipleSystemPromptsNotSupported":
            assert params["systemPromptSize"] > 1
        elif name == "MultipleToolResultContentsNotSupported":
            assert params["toolResultContentsSize"] > 1


@pytest.mark.parametrize("relative", CORRECTED_EXAMPLES)
def test_corrected_fixtures_match_source_semantics_and_real_sdk(relative):
    example = load_corrected_example(relative)
    assert_source_semantics(relative, example)
    example.verify()


@pytest.mark.parametrize("relative", CORRECTED_EXAMPLES[:4])
def test_rejects_agent_version_detail_mismatch_or_invalid_format(relative):
    example = load_corrected_example(relative)
    if "/AgentVersion/" in relative:
        example.SUCCESS.get("data", [example.SUCCESS])[0]["string"] = "1.2"
    elif relative.endswith("all_sessions"):
        example.SUCCESS["data"][0]["agentVersion"] = "invalid-version"
    else:
        example.SUCCESS["version"] = "invalid-version"
    with pytest.raises(AssertionError):
        assert_source_semantics(relative, example)


@pytest.mark.parametrize("relative,error_name,field,value", [
    (f"models/LiveDeployment/{method}", name, field, value)
    for method in ("create", "replace")
    for name, field, value in [
        ("GpuTypeNotAvailable", "availableGpuTypes", ["A100"]),
        ("InvalidGpuCount", "providedGpuCount", 1),
        ("ThreadCountTooHigh", "providedThreadCount", 1),
    ]
] + [
    ("language_models/AnthropicModel/messages", "MultipleSystemPromptsNotSupported", "systemPromptSize", 1),
    ("language_models/AnthropicModel/messages", "MultipleToolResultContentsNotSupported", "toolResultContentsSize", 1),
] + [
    (f"aip_agents/Session/{method}", "InvalidParameterType", "receivedType", "string")
    for method in ("blocking_continue", "streaming_continue")
])
def test_rejects_error_parameters_that_contradict_source(relative, error_name, field, value):
    example = load_corrected_example(relative)
    error = next(row for row in example.ERRORS if row["name"] == error_name)
    error["parameters"][field] = value
    with pytest.raises(AssertionError):
        assert_source_semantics(relative, example)
