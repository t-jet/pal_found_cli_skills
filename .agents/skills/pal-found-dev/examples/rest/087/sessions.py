"""AIP session create/get/list with real SDK and synthetic HTTP responses."""

import json
import sys
from functools import partial
from pathlib import Path

import httpx
from foundry_sdk import PalantirRPCException
from foundry_sdk.v2.aip_agents.session import SessionClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from bounded_pages import fetch_pages
from mock_transport import mock_resource

AGENT = "ri.aip-agents.main.agent.00000000-0000-0000-0000-000000000001"
SESSION = "ri.aip-agents.main.session.00000000-0000-0000-0000-000000000002"


def payload():
    return {"rid": SESSION, "agentRid": AGENT, "agentVersion": "1.0",
            "metadata": {"title": "Governance review", "messageCount": 0,
                         "createdTime": "2026-10-06T00:00:00Z",
                         "updatedTime": "2026-10-06T00:00:00Z",
                         "estimatedExpiresTime": "2026-10-07T00:00:00Z"}}


def verify():
    seen = []
    def handler(request):
        assert request.headers["Authorization"] == "Bearer offline-fixture-token"
        assert request.url.params["preview"] == "true"
        assert request.url.path.startswith(f"/api/v2/aipAgents/agents/{AGENT}/sessions")
        seen.append(request.method)
        if request.method == "POST":
            assert json.loads(request.content) == {"agentVersion": "1.0"}
            return httpx.Response(200, json=payload())
        if request.url.path.endswith(SESSION):
            return httpx.Response(200, json=payload())
        assert request.url.params["pageSize"] == "10"
        return httpx.Response(200, json={"data": [payload()]})

    with mock_resource(SessionClient, handler) as sessions:
        created = sessions.create(AGENT, agent_version="1.0", preview=True, request_timeout=30)
        assert created.rid == SESSION and created.agent_version == "1.0"
        fetched = sessions.get(AGENT, created.rid, preview=True, request_timeout=30)
        assert fetched.metadata.message_count == 0
        result = fetch_pages(partial(sessions.with_raw_response.list, AGENT,
                                     preview=True, page_size=10, request_timeout=30),
                             max_pages=2, max_items=10)
        assert result.complete and result.items[0].rid == SESSION
    assert seen == ["POST", "GET", "GET"]

    cases = [
        ("CreateSessionPermissionDenied", "PERMISSION_DENIED", {"agentRid": AGENT},
         lambda c: c.create(AGENT, agent_version="1.0", preview=True)),
        ("SessionNotFound", "NOT_FOUND", {"agentRid": AGENT, "sessionRid": SESSION},
         lambda c: c.get(AGENT, SESSION, preview=True)),
        ("AgentNotFound", "NOT_FOUND", {"agentRid": AGENT},
         lambda c: list(c.list(AGENT, preview=True))),
    ]
    for name, code, parameters, invoke in cases:
        def denied(request):
            return httpx.Response(403 if code == "PERMISSION_DENIED" else 404, json={
                "errorName": name, "errorCode": code, "parameters": parameters,
                "errorInstanceId": "00000000-0000-0000-0000-000000000004",
            })
        with mock_resource(SessionClient, denied) as sessions:
            try:
                invoke(sessions)
            except PalantirRPCException as error:
                assert error.name == name and error.parameters == parameters
                assert type(error).__name__ == name
            else:
                raise AssertionError(f"Missing {name} error")


if __name__ == "__main__":
    verify()
    print("Session create/get/list request, result and error fixtures passed")
