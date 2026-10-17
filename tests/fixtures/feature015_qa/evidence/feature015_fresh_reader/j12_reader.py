"""Source-blind J12 transaction and build workflow through public SDK routes."""

import json
import socket
import time
from unittest.mock import patch

import httpx
from foundry_sdk import Config, FoundryClient, ReadTimeout, UserTokenAuth

DATASET = "ri.synthetic.main.dataset.00000000-0000-0000-0000-000000000001"
TX = "ri.synthetic.main.transaction.00000000-0000-0000-0000-000000000001"
BUILD = "ri.synthetic.main.build.00000000-0000-0000-0000-000000000001"
BRANCH = "feature-offline"
FILE = "inspections/status.csv"
PAYLOAD = b"id,status\n1,ready\n"
TIME = "2026-10-07T00:00:00+00:00"


def deny(*_args, **_kwargs):
    raise AssertionError("Public DNS/socket access attempted")


def exercise(terminal, timeout_at=None, abort=False):
    state = {"tx": "ABSENT", "file": False, "build_reads": 0, "calls": [], "mutations": []}
    root = f"/api/v2/datasets/{DATASET}"

    def transaction():
        return {"rid": TX, "transactionType": "APPEND", "status": state["tx"],
                "createdTime": TIME}

    def file():
        return {"path": FILE, "transactionRid": TX,
                "sizeBytes": len(PAYLOAD), "updatedTime": TIME}

    def handler(request):
        method, path, params = request.method, request.url.path, request.url.params
        assert request.headers["Authorization"] == "Bearer offline-fixture-token"
        state["calls"].append((method, path, dict(params)))
        if method == "POST" and path == f"{root}/transactions":
            assert state["tx"] == "ABSENT" and params["branchName"] == BRANCH
            assert json.loads(request.content) == {"transactionType": "APPEND"}
            state["tx"] = "OPEN"
            state["mutations"].append("create")
            return httpx.Response(200, json=transaction())
        if method == "POST" and path == f"{root}/files/{FILE}/upload":
            assert state["tx"] == "OPEN" and params["transactionRid"] == TX
            assert request.headers["Content-Type"] == "application/octet-stream"
            assert request.content == PAYLOAD
            state["file"] = True
            state["mutations"].append("upload")
            if timeout_at == "upload":
                raise httpx.ReadTimeout("synthetic lost upload reply")
            return httpx.Response(200, json=file())
        if method == "GET" and path == f"{root}/transactions/{TX}":
            assert state["tx"] != "ABSENT"
            return httpx.Response(200, json=transaction())
        if method == "GET" and path in {f"{root}/files/{FILE}",
                                           f"{root}/files/{FILE}/content"}:
            assert state["file"]
            if state["tx"] == "OPEN":
                assert params["startTransactionRid"] == TX
                assert params["endTransactionRid"] == TX
                assert "branchName" not in params
            else:
                assert params["branchName"] == BRANCH
            return httpx.Response(200, content=PAYLOAD) if path.endswith("/content") else httpx.Response(200, json=file())
        if method == "POST" and path == f"{root}/transactions/{TX}/abort":
            assert state["tx"] == "OPEN"
            state["tx"] = "ABORTED"
            state["mutations"].append("abort")
            return httpx.Response(200, json=transaction())
        if method == "POST" and path == f"{root}/transactions/{TX}/commit":
            assert state["tx"] == "OPEN" and state["file"]
            state["tx"] = "COMMITTED"
            state["mutations"].append("commit")
            if timeout_at == "commit":
                raise httpx.ReadTimeout("synthetic lost commit reply")
            return httpx.Response(200, json=transaction())
        if method == "GET" and path == f"{root}/branches/{BRANCH}":
            assert state["tx"] == "COMMITTED"
            return httpx.Response(200, json={"name": BRANCH, "transactionRid": TX})
        if method == "GET" and path == f"/api/v2/orchestration/builds/{BUILD}":
            state["build_reads"] += 1
            status = "RUNNING" if state["build_reads"] == 1 else terminal
            return httpx.Response(200, json={"rid": BUILD, "branchName": BRANCH,
                "createdTime": TIME, "createdBy": "00000000-0000-0000-0000-000000000001",
                "fallbackBranches": [BRANCH], "jobRids": [], "retryCount": 0,
                "retryBackoffDuration": {"value": 1, "unit": "MILLISECONDS"},
                "abortOnFailure": True, "status": status})
        raise AssertionError(f"Unexpected request: {method} {path}")

    with patch.object(socket, "getaddrinfo", deny), patch.object(socket.socket, "connect", deny):
        with httpx.Client(transport=httpx.MockTransport(handler), timeout=30) as transport:
            with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
                client = FoundryClient(
                    auth=UserTokenAuth("offline-fixture-token"),
                    hostname="https://offline.example.invalid",
                    config=Config(timeout=30, max_retries=1,
                                  propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
                )
                dataset = client.datasets.Dataset
                tx = dataset.Transaction.create(DATASET, transaction_type="APPEND",
                    branch_name=BRANCH, request_timeout=30)
                assert tx.rid == TX and tx.status == "OPEN"
                try:
                    uploaded = dataset.File.upload(DATASET, FILE, PAYLOAD,
                        transaction_rid=tx.rid, request_timeout=30)
                    assert uploaded.path == FILE and uploaded.transaction_rid == TX
                except ReadTimeout:
                    assert timeout_at == "upload"
                    assert dataset.Transaction.get(DATASET, TX, request_timeout=30).status == "OPEN"
                    # Read the same known transaction's staged view; never replay upload.
                    assert dataset.File.get(DATASET, FILE,
                        start_transaction_rid=TX, end_transaction_rid=TX,
                        request_timeout=30).size_bytes == len(PAYLOAD)
                staged = {"start_transaction_rid": TX, "end_transaction_rid": TX,
                          "request_timeout": 30}
                assert dataset.File.get(DATASET, FILE, **staged).transaction_rid == TX
                assert dataset.File.content(DATASET, FILE, **staged) == PAYLOAD
                if abort:
                    assert dataset.Transaction.get(DATASET, TX, request_timeout=30).status == "OPEN"
                    assert dataset.Transaction.abort(DATASET, TX, request_timeout=30).status == "ABORTED"
                    assert dataset.Transaction.get(DATASET, TX, request_timeout=30).status == "ABORTED"
                    assert state["mutations"] == ["create", "upload", "abort"]
                    return {"case": "abort", "status": "ABORTED", "calls": len(state["calls"])}
                try:
                    committed = dataset.Transaction.commit(DATASET, TX, request_timeout=30)
                    assert committed.status == "COMMITTED"
                except ReadTimeout:
                    assert timeout_at == "commit"
                    # Known transaction RID and branch pointer settle the lost reply.
                    assert dataset.Transaction.get(DATASET, TX, request_timeout=30).status == "COMMITTED"
                assert dataset.Transaction.get(DATASET, TX, request_timeout=30).status == "COMMITTED"
                assert dataset.Branch.get(DATASET, BRANCH, request_timeout=30).transaction_rid == TX
                assert dataset.File.get(DATASET, FILE, branch_name=BRANCH,
                    request_timeout=30).transaction_rid == TX
                assert dataset.File.content(DATASET, FILE, branch_name=BRANCH,
                    request_timeout=30) == PAYLOAD
                # BUILD is a separately recorded submitted RID; commit alone did not create it.
                statuses = []
                for _ in range(2):
                    if statuses:
                        time.sleep(0.25)  # Build.get allows at most four requests/second.
                    build = client.orchestration.Build.get(BUILD, request_timeout=30)
                    statuses.append(build.status)
                    if build.status in {"SUCCEEDED", "FAILED", "CANCELED"}:
                        break
                assert statuses == ["RUNNING", terminal]
                outcome = "pending-budget" if terminal == "RUNNING" else terminal
                assert state["mutations"] == ["create", "upload", "commit"]
                return {"case": timeout_at or terminal, "status": outcome,
                        "build_reads": state["build_reads"], "calls": len(state["calls"]),
                        "mutations": state["mutations"]}


if __name__ == "__main__":
    results = [exercise("SUCCEEDED"), exercise("FAILED"), exercise("CANCELED"),
               exercise("RUNNING"), exercise("SUCCEEDED", timeout_at="upload"),
               exercise("SUCCEEDED", timeout_at="commit"), exercise("RUNNING", abort=True)]
    print(json.dumps({"result": "PASS", "cases": results}, indent=2))
