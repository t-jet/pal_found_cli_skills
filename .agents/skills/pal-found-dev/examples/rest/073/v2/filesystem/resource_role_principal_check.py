"""Prove ResourceRole grant check matches principal and role across bounded pages."""

from unittest.mock import patch

import httpx
from foundry_sdk import Config, UserTokenAuth
from foundry_sdk.v2 import FoundryClient
from foundry_sdk.v2.filesystem.models import PrincipalIdOnly, ResourceRoleIdentifier


RID = "ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001"
PRINCIPAL = "00000000-0000-0000-0000-000000000001"
OTHER = "00000000-0000-0000-0000-000000000002"
ROLE = "synthetic-role"


def grant(principal):
    return {"resourceRolePrincipal": {"principalId": principal,
                                      "principalType": "USER",
                                      "type": "principalWithId"},
            "roleId": ROLE}


def verify(pages, expected_match, expected_calls):
    calls = []

    def handler(request):
        if request.method == "POST":
            assert request.url.path.endswith(f"/resources/{RID}/roles/add")
            body = request.content.decode()
            assert PRINCIPAL in body and ROLE in body
            return httpx.Response(204)
        assert request.method == "GET"
        assert request.url.path.endswith(f"/resources/{RID}/roles")
        assert request.url.params["includeInherited"] == "false"
        calls.append(request.url.params.get("pageToken"))
        assert len(calls) <= expected_calls
        return httpx.Response(200, json=pages[len(calls) - 1])

    with httpx.Client(transport=httpx.MockTransport(handler), timeout=30) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            client = FoundryClient(
                auth=UserTokenAuth("offline-fixture-token"),
                hostname="https://offline.example.invalid",
                config=Config(timeout=30, max_retries=1,
                              propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
            )
            role = ResourceRoleIdentifier(
                resource_role_principal=PrincipalIdOnly(principal_id=PRINCIPAL),
                role_id=ROLE,
            )
            client.filesystem.Resource.Role.add(RID, roles=[role], request_timeout=30)
            cursor = None
            seen = set()
            matched = None
            for _ in range(10):
                page = client.filesystem.Resource.Role.list(
                    RID, include_inherited=False, page_size=100,
                    page_token=cursor, request_timeout=30,
                )
                matched = next((item for item in page.data
                                if item.role_id == ROLE and
                                getattr(item.resource_role_principal, "principal_id", None)
                                == PRINCIPAL), None)
                if matched is not None:
                    break
                following = page.next_page_token
                if following is None:
                    break
                if following == cursor or following in seen:
                    assert not expected_match
                    break
                seen.add(following)
                cursor = following
            assert (matched is not None) is expected_match
    assert len(calls) == expected_calls


if __name__ == "__main__":
    verify([{"data": [grant(OTHER)], "nextPageToken": "A"},
            {"data": [], "nextPageToken": "B"},
            {"data": [grant(PRINCIPAL)]}], True, 3)
    verify([{"data": [grant(OTHER)], "nextPageToken": "A"},
            {"data": [], "nextPageToken": "A"}], False, 2)
    print("exact principal+role match, empty page and repeated cursor passed")
