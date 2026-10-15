"""Offline audit LogFile discovery through the public composed SDK client."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import date
from importlib.metadata import version
from pathlib import Path
from time import monotonic
from unittest.mock import patch

import httpx
from foundry_sdk import Config, PalantirRPCException, ReadTimeout, UserTokenAuth
from foundry_sdk.v2 import FoundryClient


ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / ".ept" / "tmp"))
from feature015_final_reader_deny_public import deny_public_network  # noqa: E402


ORG = "ri.synthetic.main.organization.00000000-0000-0000-0000-000000000001"
START = date(2026, 10, 1)
END = date(2026, 10, 7)


@dataclass
class Discovery:
    ids: list[str]
    complete: bool
    reason: str
    cursor: str | None
    pages: int
    remaining_on_page: list[str]


def discover(client, *, max_pages=5, max_items=500, seconds=30, clock=monotonic):
    """Return complete only after a final fixed-window page has no token."""
    if max_pages < 1 or max_items < 1 or seconds <= 0:
        raise ValueError("Budgets must be positive")
    deadline = clock() + seconds
    ids, seen, cursor = [], set(), None
    for page_number in range(1, max_pages + 1):
        remaining_seconds = deadline - clock()
        timeout = min(5, int(remaining_seconds))
        if timeout < 1:
            return Discovery(ids, False, "time_budget", cursor, page_number - 1, [])
        requested_cursor = cursor
        try:
            raw = client.audit.Organization.LogFile.with_raw_response.list(
                ORG, start_date=START, end_date=END, page_size=100,
                page_token=requested_cursor, request_timeout=timeout,
            )
            try:
                page = raw.decode()
            finally:
                raw.close()
        except (ReadTimeout, httpx.TimeoutException):
            return Discovery(ids, False, "lost_response", requested_cursor, page_number - 1, [])
        except PalantirRPCException as error:
            if error.name == "ListLogFilesPermissionDenied":
                return Discovery(ids, False, "permission_denied", requested_cursor, page_number - 1, [])
            raise

        batch = [entry.id for entry in page.data]
        room = max_items - len(ids)
        ids.extend(batch[:room])
        if len(batch) > room:
            return Discovery(ids, False, "item_budget", page.next_page_token,
                             page_number, batch[room:])
        if clock() >= deadline:
            return Discovery(ids, False, "time_budget", requested_cursor,
                             page_number, [])
        following = page.next_page_token
        if following is None:
            return Discovery(ids, True, "complete", None, page_number, [])
        if following == requested_cursor or following in seen:
            return Discovery(ids, False, "repeated_token", following,
                             page_number, [])
        seen.add(following)
        cursor = following
        if len(ids) >= max_items:
            return Discovery(ids, False, "item_budget", cursor, page_number, [])
    return Discovery(ids, False, "page_budget", cursor, max_pages, [])


def run_case(name, responses, expected, *, max_pages=5, max_items=500,
             seconds=30, clock=monotonic):
    calls = []

    def handler(request):
        assert request.method == "GET"
        assert request.url.path == f"/api/v2/audit/organizations/{ORG}/logFiles"
        assert request.headers["Authorization"] == "Bearer offline-fixture-token"
        assert request.url.params["startDate"] == START.isoformat()
        assert request.url.params["endDate"] == END.isoformat()
        assert request.url.params["pageSize"] == "100"
        assert len(calls) < len(responses), "Unexpected extra page request"
        wanted_cursor, answer = responses[len(calls)]
        actual_cursor = request.url.params.get("pageToken")
        assert actual_cursor == wanted_cursor, (actual_cursor, wanted_cursor)
        calls.append(actual_cursor)
        if isinstance(answer, Exception):
            raise answer
        if isinstance(answer, tuple):
            return httpx.Response(answer[0], json=answer[1])
        return httpx.Response(200, json=answer)

    with httpx.Client(transport=httpx.MockTransport(handler), timeout=10) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            client = FoundryClient(
                hostname="https://offline.example.invalid",
                auth=UserTokenAuth("offline-fixture-token"),
                config=Config(timeout=10, max_retries=1,
                              propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
            )
            result = discover(client, max_pages=max_pages, max_items=max_items,
                              seconds=seconds, clock=clock)
    assert result == expected, (name, result, expected)
    print(json.dumps({"scenario": name, "status": "PASS", "requests": calls,
                      "ids": result.ids, "complete": result.complete,
                      "reason": result.reason, "cursor": result.cursor,
                      "pages": result.pages,
                      "remaining_on_page": result.remaining_on_page}))


def named_missing_start_date():
    def handler(request):
        assert "startDate" not in request.url.params
        return httpx.Response(400, json={
            "errorName": "MissingStartDate", "errorCode": "INVALID_ARGUMENT",
            "parameters": {},
            "errorInstanceId": "00000000-0000-0000-0000-000000000004",
        })

    with httpx.Client(transport=httpx.MockTransport(handler), timeout=10) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            client = FoundryClient(
                hostname="https://offline.example.invalid",
                auth=UserTokenAuth("offline-fixture-token"),
                config=Config(timeout=10, max_retries=1),
            )
            try:
                client.audit.Organization.LogFile.list(ORG)
            except PalantirRPCException as error:
                assert error.name == "MissingStartDate"
                assert type(error).__name__ == "MissingStartDate"
            else:
                raise AssertionError("Expected MissingStartDate")
    print(json.dumps({"scenario": "missing_start_date", "status": "PASS",
                      "error": "MissingStartDate"}))


def main():
    assert version("foundry-platform-sdk") == "1.101.0"
    first = {"data": [{"id": "log-1"}], "nextPageToken": "A"}
    empty = {"data": [], "nextPageToken": "B"}
    final = {"data": [{"id": "log-2"}]}
    with deny_public_network():
        print(json.dumps({"scenario": "public_network_guard", "status": "PASS",
                          "probe": "PUBLIC_NETWORK_DENIED"}))
        run_case("complete_empty_middle", [(None, first), ("A", empty), ("B", final)],
                 Discovery(["log-1", "log-2"], True, "complete", None, 3, []))
        run_case("page_budget", [(None, first), ("A", empty)],
                 Discovery(["log-1"], False, "page_budget", "B", 2, []), max_pages=2)
        run_case("item_budget_mid_page", [(None, {"data": [
                 {"id": "log-1"}, {"id": "log-2"}], "nextPageToken": "A"})],
                 Discovery(["log-1"], False, "item_budget", "A", 1, ["log-2"]),
                 max_items=1)
        run_case("repeated_token", [(None, first), ("A", {"data": [],
                 "nextPageToken": "A"})],
                 Discovery(["log-1"], False, "repeated_token", "A", 2, []))
        ticks = iter([0, 31])
        run_case("time_budget_before_request", [],
                 Discovery([], False, "time_budget", None, 0, []),
                 clock=lambda: next(ticks))
        ticks = iter([0, 0, 2])
        run_case("time_budget_after_response", [(None, final)],
                 Discovery(["log-2"], False, "time_budget", None, 1, []),
                 seconds=1.5, clock=lambda: next(ticks))
        run_case("lost_response", [(None, httpx.ReadTimeout("lost"))],
                 Discovery([], False, "lost_response", None, 0, []))
        denial = {"errorName": "ListLogFilesPermissionDenied",
                  "errorCode": "PERMISSION_DENIED", "parameters": {},
                  "errorInstanceId": "00000000-0000-0000-0000-000000000004"}
        run_case("permission_denied", [(None, (403, denial))],
                 Discovery([], False, "permission_denied", None, 0, []))
        named_missing_start_date()


if __name__ == "__main__":
    main()
