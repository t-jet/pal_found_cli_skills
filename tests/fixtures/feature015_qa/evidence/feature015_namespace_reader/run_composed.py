"""Run staged SDK examples through public composed FoundryClient routes."""

from __future__ import annotations

import contextlib
import importlib
import json
import re
import runpy
import socket
import traceback
from pathlib import Path
from unittest.mock import patch

import httpx
from foundry_sdk import Config, UserTokenAuth


OUT = Path(__file__).resolve().parent
SKILL = OUT / "isolated-pal-found-dev"
BASE = json.loads((OUT / "case_results.json").read_text(encoding="utf-8"))["outcomes"]
CASES = [(item["namespace"], item["example"]) for item in BASE] + [
    ("v1.datasets.File.get", "examples/rest/074/v1/datasets/File/get.py"),
    ("v2.datasets.File.get", "examples/rest/074/v2/datasets/File/get.py"),
    ("v2.datasets.File.content", "examples/rest/074/v2/datasets/File/content.py"),
]


def denied(*_args: object, **_kwargs: object) -> None:
    raise RuntimeError("PUBLIC_NETWORK_DENIED")


def contract_for(example: str) -> Path:
    parts = Path(example).parts
    version, service, resource = parts[3:6]
    operation = parts[6].removesuffix(".py").removeprefix("invoke_")
    return SKILL / "references/rest/contracts" / version / service / resource / f"{operation}.md"


def resolve_route(client: object, contract: Path) -> tuple[object, str]:
    match = re.search(r"call `client\.([^`]+)`", contract.read_text(encoding="utf-8"))
    if match is None:
        raise AssertionError(f"no composed route in {contract}")
    route = match.group(1)
    resource_path = route.rsplit(".", 1)[0]
    resource = client
    for part in resource_path.split("."):
        resource = getattr(resource, part)
    return resource, route


def run_case(namespace: str, example: str) -> dict[str, object]:
    module = runpy.run_path(str(SKILL / example))
    contract = contract_for(example)
    client_type = importlib.import_module("foundry_sdk.v1" if "/v1/" in example else "foundry_sdk").FoundryClient
    calls = []

    def handler(request: httpx.Request, success: bool, error_case: dict | None = None) -> httpx.Response:
        module["check_request"](request)
        calls.append(str(request.url))
        if not success:
            assert error_case is not None
            return httpx.Response(error_case["status"], json={
                "errorName": error_case["name"],
                "errorCode": error_case["code"],
                "parameters": error_case["parameters"],
                "errorInstanceId": "00000000-0000-0000-0000-000000000004",
            })
        payload = module["SUCCESS"]
        if isinstance(payload, bytes):
            return httpx.Response(200, content=payload)
        if payload is None:
            return httpx.Response(204)
        return httpx.Response(200, json=payload)

    def with_client(callback):
        with httpx.Client(transport=httpx.MockTransport(callback), timeout=30) as transport:
            with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
                client = client_type(
                    auth=UserTokenAuth(token="offline-fixture-token"),
                    hostname="offline.example.invalid",
                    config=Config(timeout=30, max_retries=1,
                                  propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
                )
                resource, route = resolve_route(client, contract)
                yield resource, route

    from foundry_sdk import PalantirRPCException

    route = ""
    for resource, route in with_client(lambda request: handler(request, True)):
        raw = module["invoke"](resource)
        try:
            assert module["normalized"](raw.decode()) == module["SUCCESS"]
        finally:
            raw.close()
    for error_case in module["ERRORS"]:
        for resource, route in with_client(lambda request, item=error_case: handler(request, False, item)):
            try:
                raw = module["invoke"](resource)
                raw.close()
            except PalantirRPCException as error:
                assert error.name == error_case["name"]
                assert type(error).__name__ == error_case["name"]
                assert module["normalized"](error.parameters) == error_case["parameters"]
            else:
                raise AssertionError(f"Expected {error_case['name']}")
    assert len(calls) == 1 + len(module["ERRORS"])
    return {
        "namespace": namespace,
        "example": example,
        "contract": contract.relative_to(SKILL).as_posix(),
        "route": f"client.{route}",
        "method": module["EXPECTED_METHOD"],
        "path": module["EXPECTED_PATH"],
        "named_errors": [item["name"] for item in module["ERRORS"]],
        "calls": len(calls),
        "passed": True,
    }


def main() -> None:
    socket.socket.connect = denied  # type: ignore[method-assign]
    socket.socket.connect_ex = denied  # type: ignore[method-assign]
    socket.create_connection = denied  # type: ignore[assignment]
    socket.getaddrinfo = denied  # type: ignore[assignment]
    try:
        socket.getaddrinfo("example.com", 443)
    except RuntimeError as error:
        assert str(error) == "PUBLIC_NETWORK_DENIED"
    else:
        raise AssertionError("DNS denial failed")

    outcomes = []
    for namespace, example in CASES:
        try:
            result = run_case(namespace, example)
        except Exception:
            result = {"namespace": namespace, "example": example, "passed": False,
                      "error": traceback.format_exc()}
        outcomes.append(result)
        print(f"{namespace}: {'PASS' if result['passed'] else 'FAIL'} {result.get('route', '')}")
        if not result["passed"]:
            print(result["error"])
    (OUT / "composed_results.json").write_text(json.dumps({
        "network_probe": "PUBLIC_NETWORK_DENIED", "isolated_skill": str(SKILL),
        "files_read": sorted({path for item in outcomes for path in
                              (item.get("example"), item.get("contract")) if path}),
        "localhost_socket_exception": "none; httpx.MockTransport is in-process",
        "outcomes": outcomes,
    }, indent=2), encoding="utf-8")
    print(f"passed={sum(bool(x['passed']) for x in outcomes)}/{len(outcomes)}")


if __name__ == "__main__":
    main()
