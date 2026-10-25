"""Verify one staged file, committed branch, and Build terminal result offline.

Uses SDK 1.101.0 request serialization with a stateful synthetic HTTP transport.
No network connection or tenant mutation occurs.
"""

import socket
from time import sleep
from typing import Any
from unittest.mock import patch

import httpx
from foundry_sdk import Config, ReadTimeout, UserTokenAuth
from foundry_sdk.v2 import FoundryClient


DATASET = "ri.synthetic.main.dataset.00000000-0000-0000-0000-000000000001"
TRANSACTION = "ri.synthetic.main.transaction.00000000-0000-0000-0000-000000000001"
BUILD = "ri.synthetic.main.build.00000000-0000-0000-0000-000000000001"
BRANCH = "feature-offline"
FILE = "inspections/status.csv"
PAYLOAD = b"id,status\n1,ready\n"
TIME = "2026-10-07T00:00:00+00:00"


def deny_network(*_args, **_kwargs):
    """Fail if a fixture accidentally attempts a public network connection."""
    raise AssertionError("Public DNS or socket access attempted")


def exercise(build_terminal: str, *, timeout_at: str | None = None,
             abort: bool = False, fault_at: str | None = None,
             trace: dict[str, Any] | None = None) -> dict[str, object]:
    """Exercise one transaction and its separately submitted Build RID."""
    state: dict[str, Any] = trace if trace is not None else {}
    state.update({"transaction": "ABSENT", "build_reads": 0, "file_uploaded": False,
                  "mutations": [], "staged_reads": 0, "visible_reads": 0})

    def handler(request):
        path = request.url.path
        params = request.url.params
        dataset_root = f"/api/v2/datasets/{DATASET}"
        assert request.headers["Authorization"] == "Bearer offline-fixture-token"
        if request.method == "POST" and path == f"{dataset_root}/transactions":
            assert state["transaction"] == "ABSENT"
            assert params["branchName"] == BRANCH
            assert request.content and b"APPEND" in request.content
            state["transaction"] = "OPEN"
            return httpx.Response(200, json={"rid": TRANSACTION, "transactionType": "APPEND",
                                            "status": "OPEN", "createdTime": TIME})
        if request.method == "POST" and path == f"{dataset_root}/files/{FILE}/upload":
            assert state["transaction"] == "OPEN"
            assert params["transactionRid"] == TRANSACTION
            assert request.content == PAYLOAD
            state["file_uploaded"] = True
            state["mutations"].append("upload")
            if timeout_at == "upload":
                raise httpx.ReadTimeout("synthetic lost upload reply")
            return httpx.Response(200, json={"path": FILE, "transactionRid": TRANSACTION,
                                            "sizeBytes": len(PAYLOAD), "updatedTime": TIME})
        if request.method == "GET" and path in {f"{dataset_root}/files/{FILE}",
                                                 f"{dataset_root}/files/{FILE}/content"}:
            assert state["file_uploaded"] and state["transaction"] != "ABORTED"
            if state["transaction"] == "OPEN":
                assert params["startTransactionRid"] == TRANSACTION
                assert params["endTransactionRid"] == TRANSACTION
                assert "branchName" not in params
                state["staged_reads"] += 1
            else:
                assert state["transaction"] == "COMMITTED"
                assert params["branchName"] == BRANCH
                assert "startTransactionRid" not in params
                state["visible_reads"] += 1
            if path.endswith("/content"):
                view = "staged-content" if state["transaction"] == "OPEN" else "visible-content"
                content = b"unexpected-content" if fault_at == view else PAYLOAD
                return httpx.Response(200, content=content)
            return httpx.Response(200, json={"path": FILE, "transactionRid": TRANSACTION,
                                            "sizeBytes": len(PAYLOAD), "updatedTime": TIME})
        if request.method == "POST" and path == f"{dataset_root}/transactions/{TRANSACTION}/commit":
            assert state["transaction"] == "OPEN"
            state["transaction"] = "COMMITTED"
            state["mutations"].append("commit")
            if timeout_at == "commit":
                raise httpx.ReadTimeout("synthetic lost commit reply")
            return httpx.Response(200, json={"rid": TRANSACTION, "transactionType": "APPEND",
                                            "status": "COMMITTED", "createdTime": TIME})
        if request.method == "POST" and path == f"{dataset_root}/transactions/{TRANSACTION}/abort":
            assert state["transaction"] == "OPEN"
            state["transaction"] = "ABORTED"
            state["mutations"].append("abort")
            return httpx.Response(200, json={"rid": TRANSACTION, "transactionType": "APPEND",
                                            "status": "ABORTED", "createdTime": TIME})
        if request.method == "GET" and path == f"{dataset_root}/transactions/{TRANSACTION}":
            assert state["transaction"] != "ABSENT"
            return httpx.Response(200, json={"rid": TRANSACTION, "transactionType": "APPEND",
                                            "status": state["transaction"], "createdTime": TIME})
        if request.method == "GET" and path == f"{dataset_root}/branches/{BRANCH}":
            assert state["transaction"] == "COMMITTED"
            branch_transaction = ("ri.synthetic.main.transaction.00000000-0000-0000-0000-000000000002"
                                  if fault_at == "branch-pointer" else TRANSACTION)
            return httpx.Response(200, json={"name": BRANCH,
                                            "transactionRid": branch_transaction})
        if request.method == "GET" and path == f"/api/v2/orchestration/builds/{BUILD}":
            assert state["transaction"] == "COMMITTED"
            state["build_reads"] += 1
            status = "RUNNING" if state["build_reads"] == 1 else build_terminal
            return httpx.Response(200, json={
                "rid": BUILD, "branchName": BRANCH, "createdTime": TIME,
                "createdBy": "00000000-0000-0000-0000-000000000001",
                "fallbackBranches": [BRANCH], "jobRids": [], "retryCount": 0,
                "retryBackoffDuration": {"value": 1, "unit": "MILLISECONDS"},
                "abortOnFailure": True, "status": status,
            })
        raise AssertionError(f"Unexpected request: {request.method} {request.url}")

    with patch.object(socket, "getaddrinfo", deny_network), patch.object(socket.socket, "connect", deny_network), httpx.Client(transport=httpx.MockTransport(handler), timeout=30) as transport:
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
            assert tx.rid == TRANSACTION and tx.status == "OPEN"
            state["mutations"].append("create")
            try:
                uploaded = dataset.File.upload(DATASET, FILE, PAYLOAD,
                                               transaction_rid=tx.rid, request_timeout=30)
                assert uploaded.transaction_rid == tx.rid and uploaded.path == FILE
            except ReadTimeout:
                assert timeout_at == "upload"
                assert dataset.Transaction.get(DATASET, tx.rid,
                                               request_timeout=30).status == "OPEN"
                # Read the known transaction view; never replay an uncertain upload.
                assert dataset.File.get(DATASET, FILE,
                                        start_transaction_rid=tx.rid,
                                        end_transaction_rid=tx.rid,
                                        request_timeout=30).size_bytes == len(PAYLOAD)
            staged_args = {"start_transaction_rid": tx.rid,
                           "end_transaction_rid": tx.rid, "request_timeout": 30}
            assert dataset.File.get(DATASET, FILE, **staged_args).transaction_rid == tx.rid
            assert dataset.File.content(DATASET, FILE, **staged_args) == PAYLOAD
            if abort:
                assert dataset.Transaction.get(DATASET, tx.rid,
                                               request_timeout=30).status == "OPEN"
                assert dataset.Transaction.abort(DATASET, tx.rid,
                                                 request_timeout=30).status == "ABORTED"
                assert dataset.Transaction.get(DATASET, tx.rid,
                                               request_timeout=30).status == "ABORTED"
                assert state["mutations"] == ["create", "upload", "abort"]
                assert state["staged_reads"] >= 2 and state["visible_reads"] == 0
                return {"case": "abort", "outcome": "ABORTED"}
            try:
                committed = dataset.Transaction.commit(DATASET, tx.rid,
                                                       request_timeout=30)
                assert committed.status == "COMMITTED"
            except ReadTimeout:
                assert timeout_at == "commit"
                # A lost reply is not proof of failure; reconcile the known RID.
                assert dataset.Transaction.get(DATASET, tx.rid,
                                               request_timeout=30).status == "COMMITTED"
            # This read also reconciles a lost commit reply before any retry.
            assert dataset.Transaction.get(DATASET, tx.rid, request_timeout=30).status == "COMMITTED"
            assert dataset.Branch.get(DATASET, BRANCH, request_timeout=30).transaction_rid == tx.rid
            assert dataset.File.get(DATASET, FILE, branch_name=BRANCH,
                                    request_timeout=30).transaction_rid == tx.rid
            assert dataset.File.content(DATASET, FILE, branch_name=BRANCH,
                                        request_timeout=30) == PAYLOAD
            assert client.orchestration.Build.get(BUILD, request_timeout=30).status == "RUNNING"
            sleep(0.25)  # The documented Build.get limit is four requests per second.
            final = client.orchestration.Build.get(BUILD, request_timeout=30)
            assert final.status == build_terminal
            outcome = ("success" if final.status == "SUCCEEDED" else
                       "unsuccessful" if final.status in {"FAILED", "CANCELED"} else
                       "unknown-after-budget")
            assert state["mutations"] == ["create", "upload", "commit"]
            assert state["staged_reads"] >= 2 and state["visible_reads"] == 2
            assert state["build_reads"] == 2
            return {"case": timeout_at or build_terminal,
                    "build_status": final.status, "outcome": outcome,
                    "build_rid": BUILD}


if __name__ == "__main__":
    for terminal in ("SUCCEEDED", "FAILED", "CANCELED", "RUNNING"):
        result = exercise(terminal)
        assert result["build_status"] == terminal
        assert result["outcome"] == ("success" if terminal == "SUCCEEDED" else
                                     "unknown-after-budget" if terminal == "RUNNING" else
                                     "unsuccessful")
    for uncertain_step in ("upload", "commit"):
        assert exercise("SUCCEEDED", timeout_at=uncertain_step)["outcome"] == "success"
    assert exercise("RUNNING", abort=True) == {"case": "abort", "outcome": "ABORTED"}
    print("seven staged transaction and Build outcomes passed with public network denied")
