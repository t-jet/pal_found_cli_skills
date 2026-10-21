"""Source-blind, offline exercise of v2 Audit LogFile discovery."""

from __future__ import annotations

import json
import sys
from datetime import date
from importlib.metadata import version
from pathlib import Path
from time import monotonic
from unittest.mock import patch

import httpx
from foundry_sdk import Config, PalantirRPCException, UserTokenAuth
from foundry_sdk.v2 import FoundryClient


ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / ".ept" / "tmp"))
from feature015_final_reader_deny_public import deny_public_network  # noqa: E402


ORG = "ri.synthetic.main.organization.00000000-0000-0000-0000-000000000001"
START = date(2026, 10, 1)
END = date(2026, 10, 7)


def discover(client, *, max_pages=5, max_items=500, seconds=30, clock=monotonic):
    """Return only fetched IDs; preserve the next request cursor on partials.

    For an oversized page, discard that page so resuming at its request cursor
    cannot silently lose unreturned IDs.
    """
    deadline = clock() + seconds
    cursor = None
    seen = set()
    ids = []
    for _ in range(max_pages):
        remaining = deadline - clock()
        if remaining <= 0:
            return dict(ids=ids, complete=False, reason="time_budget", cursor=cursor)
        try:
            page = client.audit.Organization.LogFile.list(
                ORG,
                start_date=START,
                end_date=END,
                page_size=100,
                page_token=cursor,
                request_timeout=min(5, max(1, int(remaining))),
            )
        except httpx.TimeoutException:
            return dict(ids=ids, complete=False, reason="lost_response", cursor=cursor)
        except PalantirRPCException as error:
            return dict(ids=ids, complete=False, reason=error.name or "rpc_error", cursor=cursor)
        batch = page.data  # Do not iterate the ResourceIterator.
        if len(ids) + len(batch) > max_items:
            return dict(ids=ids, complete=False, reason="item_budget", cursor=cursor)
        ids.extend(item.id for item in batch)
        following = page.next_page_token
        if following is None:
            return dict(ids=ids, complete=True, reason=None, cursor=None)
        if following == cursor or following in seen:
            return dict(ids=ids, complete=False, reason="repeated_token", cursor=following)
        seen.add(following)
        cursor = following
    return dict(ids=ids, complete=False, reason="page_budget", cursor=cursor)


def run_case(name, responses, expected, *, max_pages=5, max_items=500, clock=monotonic):
    requests = []

    def handle(request):
        assert request.method == "GET"
        assert request.url.path == f"/api/v2/audit/organizations/{ORG}/logFiles"
        assert request.url.params["startDate"] == START.isoformat()
        assert request.url.params["endDate"] == END.isoformat()
        assert request.url.params["pageSize"] == "100"
        cursor = request.url.params.get("pageToken")
        requests.append(cursor)
        assert len(requests) <= len(responses), "Unexpected extra request"
        response = responses[len(requests) - 1]
        if isinstance(response, Exception):
            raise response
        return httpx.Response(response[0], json=response[1])

    with httpx.Client(transport=httpx.MockTransport(handle), timeout=10) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            client = FoundryClient(
                auth=UserTokenAuth("offline-fixture-token"),
                hostname="https://offline.example.invalid",
                config=Config(timeout=10, max_retries=1,
                              propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
            )
            actual = discover(client, max_pages=max_pages, max_items=max_items, clock=clock)
    assert actual == expected, f"{name}: {actual!r} != {expected!r}"
    print(json.dumps({"case": name, "result": actual, "request_cursors": requests}))


def main():
    assert version("foundry-platform-sdk") == "1.101.0"
    with deny_public_network():
        print("PUBLIC_NETWORK_DENIED probe: PASS")
        first = (200, {"data": [{"id": "log-1"}], "nextPageToken": "A"})
        empty = (200, {"data": [], "nextPageToken": "B"})
        last = (200, {"data": [{"id": "log-2"}]})
        run_case("prepared", [first, empty, last],
                 dict(ids=["log-1", "log-2"], complete=True, reason=None, cursor=None))
        run_case("page_budget", [first, empty],
                 dict(ids=["log-1"], complete=False, reason="page_budget", cursor="B"), max_pages=2)
        run_case("repeated_token", [first, (200, {"data": [], "nextPageToken": "A"})],
                 dict(ids=["log-1"], complete=False, reason="repeated_token", cursor="A"))
        run_case("item_budget", [(200, {"data": [{"id": "log-1"}, {"id": "log-2"}], "nextPageToken": "A"})],
                 dict(ids=[], complete=False, reason="item_budget", cursor=None), max_items=1)
        ticks = iter([0, 31])
        run_case("time_budget", [],
                 dict(ids=[], complete=False, reason="time_budget", cursor=None), clock=lambda: next(ticks))
        timeout = httpx.ReadTimeout("synthetic lost response")
        run_case("lost_response", [first, timeout],
                 dict(ids=["log-1"], complete=False, reason="lost_response", cursor="A"))
        permission = (403, {"errorName": "ListLogFilesPermissionDenied", "errorCode": "PERMISSION_DENIED",
                            "parameters": {}, "errorInstanceId": "00000000-0000-0000-0000-000000000003"})
        run_case("permission", [permission],
                 dict(ids=[], complete=False, reason="ListLogFilesPermissionDenied", cursor=None))
        missing = (400, {"errorName": "MissingStartDate", "errorCode": "INVALID_ARGUMENT",
                         "parameters": {}, "errorInstanceId": "00000000-0000-0000-0000-000000000004"})
        run_case("named_missing_start", [missing],
                 dict(ids=[], complete=False, reason="MissingStartDate", cursor=None))
    print("8/8 fixture cases passed; no tenant request")


if __name__ == "__main__":
    main()
