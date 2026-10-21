"""Independent offline reader exercise for the public Audit LogFile route."""

import json
import socket
from datetime import date
from importlib.metadata import version
from time import monotonic
from unittest.mock import patch

import httpx
from foundry_sdk import Config, PalantirRPCException, UserTokenAuth
from foundry_sdk.v2 import FoundryClient


ORG = "ri.synthetic.main.organization.00000000-0000-0000-0000-000000000001"
START = date(2026, 10, 1)
END = date(2026, 10, 7)
PATH = f"/api/v2/audit/organizations/{ORG}/logFiles"


def read_window(client, *, max_pages=5, max_items=500, seconds=30, clock=monotonic):
    """Return the retrieved prefix and a reason when finite discovery stops."""
    deadline = clock() + seconds
    cursor = None
    seen = set()
    files = []
    pages = 0
    while pages < max_pages:
        remaining = deadline - clock()
        if remaining <= 0:
            return {"ids": files, "complete": False, "reason": "time_budget", "cursor": cursor, "pages": pages}
        page = client.audit.Organization.LogFile.list(
            ORG,
            start_date=START,
            end_date=END,
            page_size=100,
            page_token=cursor,
            request_timeout=min(5, max(1, int(remaining))),
        )
        pages += 1
        page_ids = [item.id for item in page.data]
        if len(files) + len(page_ids) > max_items:
            files.extend(page_ids[: max_items - len(files)])
            return {"ids": files, "complete": False, "reason": "item_budget", "cursor": cursor, "pages": pages}
        files.extend(page_ids)
        following = page.next_page_token
        if following is None:
            return {"ids": files, "complete": True, "reason": None, "cursor": None, "pages": pages}
        if following == cursor or following in seen:
            return {"ids": files, "complete": False, "reason": "repeated_token", "cursor": following, "pages": pages}
        seen.add(following)
        cursor = following
    return {"ids": files, "complete": False, "reason": "page_budget", "cursor": cursor, "pages": pages}


def client_with_transport(handler):
    transport = httpx.Client(transport=httpx.MockTransport(handler), timeout=10)
    return transport, patch("foundry_sdk._core.api_client.HttpClient", return_value=transport)


def make_client():
    return FoundryClient(
        auth=UserTokenAuth("offline-fixture-token"),
        hostname="https://offline.example.invalid",
        config=Config(timeout=10, max_retries=1, propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
    )


def pages_case(name, payloads, expected_cursors, expected, **limits):
    observed = []

    def handler(request):
        assert request.method == "GET" and request.url.path == PATH
        assert request.headers["Authorization"] == "Bearer offline-fixture-token"
        assert request.url.params["startDate"] == START.isoformat()
        assert request.url.params["endDate"] == END.isoformat()
        assert request.url.params["pageSize"] == "100"
        observed.append(request.url.params.get("pageToken"))
        assert len(observed) <= len(payloads), "unexpected SDK request"
        return httpx.Response(200, json=payloads[len(observed) - 1])

    transport, mock = client_with_transport(handler)
    with transport, mock:
        actual = read_window(make_client(), **limits)
    assert observed == expected_cursors, (name, observed, expected_cursors)
    assert actual == expected, (name, actual, expected)
    return {"case": name, "status": "PASS", "requests": observed, "result": actual}


def named_error_case(name, status, code, *, missing_date=False):
    observed = []

    def handler(request):
        assert request.method == "GET" and request.url.path == PATH
        observed.append(dict(request.url.params))
        if missing_date:
            assert "startDate" not in request.url.params
        else:
            assert request.url.params["startDate"] == START.isoformat()
        return httpx.Response(status, json={
            "errorName": name,
            "errorCode": code,
            "parameters": {},
            "errorInstanceId": "00000000-0000-0000-0000-000000000004",
        })

    transport, mock = client_with_transport(handler)
    with transport, mock:
        try:
            client = make_client()
            if missing_date:
                client.audit.Organization.LogFile.list(ORG)
            else:
                client.audit.Organization.LogFile.list(ORG, start_date=START)
        except PalantirRPCException as error:
            assert error.name == name and type(error).__name__ == name
            actual = {"name": error.name, "type": type(error).__name__}
        else:
            raise AssertionError(f"Expected {name}")
    assert len(observed) == 1
    return {"case": name, "status": "PASS", "requests": observed, "result": actual}


def deny_network(*args, **kwargs):
    raise RuntimeError("public network denied by Audit reader fixture")


def run():
    assert version("foundry-platform-sdk") == "1.101.0"
    results = []
    with patch.object(socket, "getaddrinfo", side_effect=deny_network), \
         patch.object(socket.socket, "connect", side_effect=deny_network), \
         patch.object(socket.socket, "connect_ex", side_effect=deny_network), \
         patch.object(socket, "create_connection", side_effect=deny_network):
        try:
            socket.getaddrinfo("www.palantir.com", 443)
        except RuntimeError as error:
            assert "denied" in str(error)
            results.append({"case": "public_network_probe", "status": "PASS", "result": str(error)})
        else:
            raise AssertionError("public DNS was reachable")

        results.append(pages_case(
            "three_pages_with_empty_middle",
            [{"data": [{"id": "log-1"}], "nextPageToken": "A"},
             {"data": [], "nextPageToken": "B"},
             {"data": [{"id": "log-2"}]}],
            [None, "A", "B"],
            {"ids": ["log-1", "log-2"], "complete": True, "reason": None, "cursor": None, "pages": 3},
        ))
        results.append(pages_case(
            "page_budget_partial",
            [{"data": [{"id": "log-1"}], "nextPageToken": "A"},
             {"data": [], "nextPageToken": "B"}],
            [None, "A"],
            {"ids": ["log-1"], "complete": False, "reason": "page_budget", "cursor": "B", "pages": 2},
            max_pages=2,
        ))
        results.append(pages_case(
            "item_budget_partial",
            [{"data": [{"id": "log-1"}, {"id": "log-2"}], "nextPageToken": "A"}],
            [None],
            {"ids": ["log-1"], "complete": False, "reason": "item_budget", "cursor": None, "pages": 1},
            max_items=1,
        ))
        results.append(pages_case(
            "repeated_token_partial",
            [{"data": [{"id": "log-1"}], "nextPageToken": "A"},
             {"data": [], "nextPageToken": "A"}],
            [None, "A"],
            {"ids": ["log-1"], "complete": False, "reason": "repeated_token", "cursor": "A", "pages": 2},
        ))
        ticks = iter([0, 31])
        results.append(pages_case(
            "time_budget_before_request",
            [], [],
            {"ids": [], "complete": False, "reason": "time_budget", "cursor": None, "pages": 0},
            clock=lambda: next(ticks),
        ))
        results.append(named_error_case("MissingStartDate", 400, "INVALID_ARGUMENT", missing_date=True))
        results.append(named_error_case("ListLogFilesPermissionDenied", 403, "PERMISSION_DENIED"))
    return {"sdk": "1.101.0", "source": "standalone pal-found-dev skill", "live_tenant_tested": False, "cases": results}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
