"""Offline J12 check against the installed Foundry Platform SDK 1.101.0."""

import importlib.util
import json
from pathlib import Path
from time import sleep
from unittest.mock import patch

import httpx
from foundry_sdk import Config, ReadTimeout, UserTokenAuth
from foundry_sdk.v2 import FoundryClient


ROOT = Path(__file__).resolve().parents[6]
GUARD = ROOT / ".ept/tmp/feature015_final_reader_deny_public.py"
spec = importlib.util.spec_from_file_location("deny_public", GUARD)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)

DATASET = "ri.synthetic.main.dataset.00000000-0000-0000-0000-000000000012"
TX = "ri.synthetic.main.transaction.00000000-0000-0000-0000-000000000012"
BUILD = "ri.synthetic.main.build.00000000-0000-0000-0000-000000000012"
BRANCH = "j12-review"
PATH = "inbox/j12.csv"
BODY = b"id,value\n1,ok\n"
STAMP = "2026-10-11T00:00:00Z"


def run_case(lost_reply=None, final="SUCCEEDED"):
    state = {"tx": None, "uploaded": False, "writes": [], "build_reads": 0}
    base = f"/api/v2/datasets/{DATASET}"

    def tx_json():
        return {"rid": TX, "transactionType": "APPEND", "status": state["tx"],
                "createdTime": STAMP}

    def file_json():
        return {"path": PATH, "transactionRid": TX, "sizeBytes": len(BODY),
                "updatedTime": STAMP}

    def handler(req):
        p, q = req.url.path, req.url.params
        assert req.headers["Authorization"] == "Bearer synthetic-token"
        if req.method == "POST" and p == base + "/transactions":
            assert q["branchName"] == BRANCH
            assert json.loads(req.content) == {"transactionType": "APPEND"}
            assert state["tx"] is None
            state["tx"] = "OPEN"
            state["writes"].append("create")
            return httpx.Response(200, json=tx_json())
        if req.method == "POST" and p == base + f"/files/{PATH}/upload":
            assert q["transactionRid"] == TX and req.content == BODY
            assert req.headers["Content-Type"] == "application/octet-stream"
            assert state["tx"] == "OPEN" and not state["uploaded"]
            state["uploaded"] = True
            state["writes"].append("upload")
            if lost_reply == "upload":
                raise httpx.ReadTimeout("synthetic upload response lost")
            return httpx.Response(200, json=file_json())
        if req.method == "GET" and p == base + f"/transactions/{TX}":
            return httpx.Response(200, json=tx_json())
        if req.method == "GET" and p == base + f"/files/{PATH}":
            assert state["uploaded"]
            if state["tx"] == "OPEN":
                assert q["startTransactionRid"] == TX and q["endTransactionRid"] == TX
            else:
                assert q["branchName"] == BRANCH
            return httpx.Response(200, json=file_json())
        if req.method == "GET" and p == base + f"/files/{PATH}/content":
            assert state["uploaded"]
            return httpx.Response(200, content=BODY)
        if req.method == "POST" and p == base + f"/transactions/{TX}/commit":
            assert state["tx"] == "OPEN" and state["uploaded"]
            state["tx"] = "COMMITTED"
            state["writes"].append("commit")
            if lost_reply == "commit":
                raise httpx.ReadTimeout("synthetic commit response lost")
            return httpx.Response(200, json=tx_json())
        if req.method == "GET" and p == base + f"/branches/{BRANCH}":
            assert state["tx"] == "COMMITTED"
            return httpx.Response(200, json={"name": BRANCH, "transactionRid": TX})
        if req.method == "GET" and p == f"/api/v2/orchestration/builds/{BUILD}":
            state["build_reads"] += 1
            status = final if state["build_reads"] == 2 else "RUNNING"
            return httpx.Response(200, json={"rid": BUILD, "branchName": BRANCH,
                "createdTime": STAMP, "createdBy": "00000000-0000-0000-0000-000000000012",
                "fallbackBranches": [BRANCH], "jobRids": [], "retryCount": 0,
                "retryBackoffDuration": {"value": 1, "unit": "MILLISECONDS"},
                "abortOnFailure": True, "status": status})
        raise AssertionError(f"unexpected {req.method} {req.url}")

    with guard.deny_public_network():
        with httpx.Client(transport=httpx.MockTransport(handler), timeout=3) as transport:
            with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
                client = FoundryClient(
                    hostname="https://synthetic.invalid", auth=UserTokenAuth("synthetic-token"),
                    config=Config(timeout=3, max_retries=1,
                                  propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
                )
                ds = client.datasets.Dataset
                tx = ds.Transaction.create(DATASET, transaction_type="APPEND",
                                           branch_name=BRANCH, request_timeout=3)
                assert tx.rid == TX and tx.status == "OPEN"
                try:
                    upload = ds.File.upload(DATASET, PATH, BODY, transaction_rid=TX,
                                            request_timeout=3)
                    assert upload.transaction_rid == TX
                except ReadTimeout:
                    assert lost_reply == "upload"
                    assert ds.Transaction.get(DATASET, TX, request_timeout=3).status == "OPEN"
                    assert ds.File.get(DATASET, PATH, start_transaction_rid=TX,
                                       end_transaction_rid=TX, request_timeout=3).size_bytes == len(BODY)
                assert ds.File.content(DATASET, PATH, start_transaction_rid=TX,
                                       end_transaction_rid=TX, request_timeout=3) == BODY
                try:
                    assert ds.Transaction.commit(DATASET, TX, request_timeout=3).status == "COMMITTED"
                except ReadTimeout:
                    assert lost_reply == "commit"
                assert ds.Transaction.get(DATASET, TX, request_timeout=3).status == "COMMITTED"
                assert ds.Branch.get(DATASET, BRANCH, request_timeout=3).transaction_rid == TX
                assert ds.File.get(DATASET, PATH, branch_name=BRANCH,
                                   request_timeout=3).transaction_rid == TX
                assert ds.File.content(DATASET, PATH, branch_name=BRANCH,
                                       request_timeout=3) == BODY
                status = "RUNNING"
                for attempt in range(2):
                    if attempt:
                        sleep(0.26)  # Build.get allows at most four requests/second.
                    status = client.orchestration.Build.get(BUILD, request_timeout=3).status
                    if status in {"SUCCEEDED", "FAILED", "CANCELED"}:
                        break
                assert state["writes"] == ["create", "upload", "commit"]
                assert state["build_reads"] == 2
                return status


if __name__ == "__main__":
    import foundry_sdk

    assert foundry_sdk.__version__ == "1.101.0"
    print("network probe: PUBLIC_NETWORK_DENIED (cooperative socket guard)")
    for label, lost, terminal in [
        ("prepared", None, "SUCCEEDED"),
        ("lost-upload", "upload", "SUCCEEDED"),
        ("lost-commit", "commit", "SUCCEEDED"),
        ("pending-budget", None, "RUNNING"),
    ]:
        print(f"{label}: {run_case(lost, terminal)}; writes=create,upload,commit exactly once")
