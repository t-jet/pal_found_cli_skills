"""Bound public audit LogFile pagination across empty and repeated pages."""

import socket
from datetime import date
from importlib.metadata import version
from time import monotonic
from unittest.mock import patch

import httpx
from foundry_sdk import Config, PalantirRPCException, TimeoutError as FoundryTimeoutError, UserTokenAuth
from foundry_sdk.v2 import FoundryClient


ORG = "ri.synthetic.main.organization.00000000-0000-0000-0000-000000000001"
START = date(2026, 10, 1)
END = date(2026, 10, 7)


def enumerate_files(client, max_pages, max_items=500, seconds=30, clock=monotonic):
    deadline = clock() + seconds
    cursor = None
    seen = set()
    files = []
    for _ in range(max_pages):
        remaining = deadline - clock()
        timeout_seconds = min(5, int(remaining))
        if timeout_seconds <= 0:
            return [item.id for item in files], False, "time_budget", cursor
        try:
            page = client.audit.Organization.LogFile.list(
                ORG, start_date=START, end_date=END, page_size=100,
                page_token=cursor, request_timeout=timeout_seconds,
            )
        except FoundryTimeoutError:
            # The requested page is unconfirmed. Do not advance its cursor.
            return [item.id for item in files], False, "lost_response", cursor
        if len(files) + len(page.data) > max_items:
            files.extend(page.data[:max_items - len(files)])
            return [item.id for item in files], False, "item_budget", cursor
        files.extend(page.data)  # one fetched page, no SDK iterator iteration
        if clock() >= deadline:
            return [item.id for item in files], False, "time_budget", cursor
        following = page.next_page_token
        if following is None:
            return [item.id for item in files], True, None, None
        if following == cursor or following in seen:
            return [item.id for item in files], False, "repeated_token", following
        seen.add(following)
        cursor = following
    return [item.id for item in files], False, "page_budget", cursor


def scenario(pages, max_pages, expected, **limits):
    requested = []

    def handler(request):
        assert request.method == "GET"
        assert request.url.path == f"/api/v2/audit/organizations/{ORG}/logFiles"
        assert request.url.params["startDate"] == START.isoformat()
        assert request.url.params["endDate"] == END.isoformat()
        assert request.url.params["pageSize"] == "100"
        cursor = request.url.params.get("pageToken")
        requested.append(cursor)
        assert len(requested) <= len(pages)
        return httpx.Response(200, json=pages[len(requested) - 1])

    with httpx.Client(transport=httpx.MockTransport(handler), timeout=10) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            client = FoundryClient(
                auth=UserTokenAuth("offline-fixture-token"),
                hostname="https://offline.example.invalid",
                config=Config(timeout=10, max_retries=1,
                              propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
            )
            actual = enumerate_files(client, max_pages, **limits)
            assert actual == expected, (actual, expected)
    return requested


def missing_start_date():
    """Confirm the documented named server error on the public root client."""
    calls = []

    def handler(request):
        assert request.url.path == f"/api/v2/audit/organizations/{ORG}/logFiles"
        assert "startDate" not in request.url.params
        calls.append(request)
        return httpx.Response(400, json={
            "errorName": "MissingStartDate", "errorCode": "INVALID_ARGUMENT",
            "parameters": {},
            "errorInstanceId": "00000000-0000-0000-0000-000000000004",
        })

    with httpx.Client(transport=httpx.MockTransport(handler), timeout=10) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            client = FoundryClient(
                auth=UserTokenAuth("offline-fixture-token"),
                hostname="https://offline.example.invalid",
                config=Config(timeout=10, max_retries=1,
                              propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
            )
            try:
                client.audit.Organization.LogFile.list(ORG)
            except PalantirRPCException as error:
                assert error.name == "MissingStartDate"
                assert type(error).__name__ == "MissingStartDate"
            else:
                raise AssertionError("MissingStartDate was not raised")
    assert len(calls) == 1


def lost_response():
    """Check SDK timeout conversion and preserve the unconfirmed read cursor."""
    for completed_first_page, expected in (
        (False, ([], False, "lost_response", None)),
        (True, (["log-1"], False, "lost_response", "A")),
    ):
        calls = []

        def handler(request):
            calls.append(request)
            assert request.url.path == f"/api/v2/audit/organizations/{ORG}/logFiles"
            assert request.url.params["startDate"] == START.isoformat()
            if completed_first_page and len(calls) == 1:
                assert request.url.params.get("pageToken") is None
                return httpx.Response(200, json={
                    "data": [{"id": "log-1"}], "nextPageToken": "A",
                })
            assert request.url.params.get("pageToken") == ("A" if completed_first_page else None)
            raise httpx.ReadTimeout("synthetic lost audit response")

        with httpx.Client(transport=httpx.MockTransport(handler), timeout=10) as transport:
            with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
                client = FoundryClient(
                    auth=UserTokenAuth("offline-fixture-token"),
                    hostname="https://offline.example.invalid",
                    config=Config(timeout=10, max_retries=1,
                                  propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
                )
                assert enumerate_files(client, 5) == expected
        assert len(calls) == (2 if completed_first_page else 1)


def deny_network(*args, **kwargs):
    raise RuntimeError("public network denied")


if __name__ == "__main__":
    assert version("foundry-platform-sdk") == "1.101.0"
    with patch.object(socket, "getaddrinfo", side_effect=deny_network), \
         patch.object(socket.socket, "connect", side_effect=deny_network), \
         patch.object(socket.socket, "connect_ex", side_effect=deny_network), \
         patch.object(socket, "create_connection", side_effect=deny_network):
        try:
            socket.getaddrinfo("www.palantir.com", 443)
        except RuntimeError as error:
            assert str(error) == "public network denied"
        else:
            raise AssertionError("public DNS was available")

        pages = [
            {"data": [{"id": "log-1"}], "nextPageToken": "A"},
            {"data": [], "nextPageToken": "B"},
            {"data": [{"id": "log-2"}]},
        ]
        assert scenario(pages, 5, (["log-1", "log-2"], True, None, None)) == [None, "A", "B"]
        assert scenario(pages[:2], 2, (["log-1"], False, "page_budget", "B")) == [None, "A"]
        assert scenario([{"data": [{"id": "log-1"}, {"id": "log-2"}], "nextPageToken": "A"}],
                        5, (["log-1"], False, "item_budget", None), max_items=1) == [None]
        assert scenario([pages[0], {"data": [], "nextPageToken": "A"}],
                        5, (["log-1"], False, "repeated_token", "A")) == [None, "A"]
        ticks = iter([0, 31])
        assert scenario([], 5, ([], False, "time_budget", None),
                        clock=lambda: next(ticks)) == []
        short_ticks = iter([0, 0])
        assert scenario([], 5, ([], False, "time_budget", None), seconds=0.01,
                        clock=lambda: next(short_ticks)) == []
        overrun_ticks = iter([0, 0, 1.2])
        assert scenario([{"data": [{"id": "log-1"}]}], 5,
                        (["log-1"], False, "time_budget", None), seconds=1.01,
                        clock=lambda: next(overrun_ticks)) == [None]
        missing_start_date()
        lost_response()
    print("audit pagination, named errors, lost response and denied network passed")
