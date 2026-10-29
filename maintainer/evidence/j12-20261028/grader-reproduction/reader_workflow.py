"""Independent J12 synthetic workflow. All artifacts stay beside this file."""

import hashlib
import json
import math
import os
from pathlib import Path
import socket
import time
from datetime import datetime, timezone
from importlib.metadata import version
from unittest.mock import patch

import httpx
from foundry_sdk import Config, FoundryClient, ReadTimeout, UserTokenAuth
from foundry_sdk.v2.orchestration.models import ManualTarget

ROOT = Path(__file__).resolve().parent
DS = "ri.reader.main.dataset.00000000-0000-0000-0000-000000000012"
TX = "ri.reader.main.transaction.00000000-0000-0000-0000-000000000012"
BASE = "ri.reader.main.transaction.00000000-0000-0000-0000-000000000011"
BUILD = "ri.reader.main.build.00000000-0000-0000-0000-000000000012"
BRANCH = "reader-j12"
FILE = "reader/batch.csv"
DATA = b"id,value\n12,accepted\n"
STAMP = "2026-10-28T12:00:00+00:00"


def utc():
    return datetime.now(timezone.utc).isoformat()


def digest(data):
    return hashlib.sha256(data).hexdigest()


class StopWorkflow(Exception):
    pass


class Journal:
    """Persist each decision before a mutation, then retain returned identities."""

    def __init__(self, path):
        self.path = path
        self.data = json.loads(path.read_text()) if path.exists() else {
            "dataset": DS, "branch": BRANCH, "path": FILE,
            "payload_sha256": digest(DATA), "events": [], "commit_attempts": 0,
        }
        assert (self.data["dataset"], self.data["branch"], self.data["path"],
                self.data["payload_sha256"]) == (DS, BRANCH, FILE, digest(DATA))

    def save(self, event, **fields):
        self.data.update(fields)
        self.data["events"].append({"at": utc(), "event": event, **fields})
        temporary = self.path.with_suffix(".writing")
        with temporary.open("w", encoding="utf-8") as out:
            json.dump(self.data, out, indent=2)
            out.flush()
            os.fsync(out.fileno())
        temporary.replace(self.path)


class Workflow:
    def __init__(self, client, journal):
        self.client, self.j = client, journal
        self.d = client.datasets.Dataset

    def transaction(self):
        return self.d.Transaction.get(DS, self.j.data["transaction_rid"], request_timeout=3)

    def branch(self):
        return self.d.Branch.get(DS, BRANCH, request_timeout=3)

    def verify_file(self, staged):
        tx = self.j.data["transaction_rid"]
        selector = ({"start_transaction_rid": tx, "end_transaction_rid": tx}
                    if staged else {"branch_name": BRANCH})
        metadata = self.d.File.get(DS, FILE, request_timeout=3, **selector)
        if metadata.path != FILE or metadata.transaction_rid != tx:
            raise StopWorkflow("file identity mismatch")
        if metadata.size_bytes is not None and metadata.size_bytes != len(DATA):
            raise StopWorkflow("file size mismatch")
        payload = bytearray()
        with self.d.File.with_streaming_response.content(
            DS, FILE, request_timeout=3, **selector
        ) as response:
            for chunk in response.iter_bytes():
                if len(payload) + len(chunk) > 1024:
                    raise StopWorkflow("file byte budget exceeded")
                payload.extend(chunk)
        if bytes(payload) != DATA:
            raise StopWorkflow("file content mismatch")
        self.j.save("staged_verified" if staged else "committed_file_verified")

    def abort_bad_staging(self, reason):
        if self.transaction().status == "OPEN":
            self.j.save("abort_intent", reason=reason)
            result = self.d.Transaction.abort(DS, self.j.data["transaction_rid"], request_timeout=3)
            assert result.status == "ABORTED" and self.transaction().status == "ABORTED"
            self.j.save("aborted")
        raise StopWorkflow(reason)

    def dataset_commit(self):
        tx = self.j.data.get("transaction_rid")
        if not tx:
            if self.j.data.get("create_intent"):
                raise StopWorkflow("create response unresolved; owner reconciliation required")
            before = self.branch().transaction_rid
            self.j.save("create_intent", create_intent=True, original_branch_rid=before)
            made = self.d.Transaction.create(DS, transaction_type="APPEND", branch_name=BRANCH,
                                             request_timeout=3)
            assert made.status == "OPEN"
            tx = made.rid
            self.j.save("transaction_known", transaction_rid=tx)
        state = self.transaction().status
        if state == "OPEN":
            if not self.j.data.get("upload_intent"):
                self.j.save("upload_intent", upload_intent=True)
                try:
                    uploaded = self.d.File.upload(DS, FILE, DATA, transaction_rid=tx, request_timeout=3)
                    assert uploaded.path == FILE and uploaded.transaction_rid == tx
                    self.j.save("upload_acknowledged")
                except ReadTimeout:
                    self.j.save("upload_response_lost")
            # Also executes on a new process resuming an uncertain upload.
            assert self.transaction().status == "OPEN"
            try:
                self.verify_file(staged=True)
            except (StopWorkflow, ReadTimeout) as exc:
                self.abort_bad_staging(str(exc))
            while self.j.data["commit_attempts"] < 2:
                # Reconcile both known transaction and branch before any commit attempt.
                state = self.transaction().status
                pointer = self.branch().transaction_rid
                self.j.save("commit_reconciled", transaction_status=state, branch_pointer=pointer)
                if state == "COMMITTED":
                    break
                if state != "OPEN" or pointer != self.j.data["original_branch_rid"]:
                    raise StopWorkflow("transaction or branch changed; commit withheld")
                self.verify_file(staged=True)
                self.j.save("commit_intent", commit_attempts=self.j.data["commit_attempts"] + 1)
                try:
                    committed = self.d.Transaction.commit(DS, tx, request_timeout=3)
                    assert committed.rid == tx and committed.status == "COMMITTED"
                    self.j.save("commit_acknowledged")
                    break
                except ReadTimeout:
                    self.j.save("commit_response_lost")
        elif state != "COMMITTED":
            raise StopWorkflow(f"transaction ended {state}")
        final, branch = self.transaction(), self.branch()
        if final.status != "COMMITTED" or branch.transaction_rid != tx:
            raise StopWorkflow("committed branch verification failed")
        self.j.save("committed_branch_verified")
        self.verify_file(staged=False)

    def build(self, max_polls=3, seconds=3):
        rid = self.j.data.get("build_rid")
        if not rid:
            if self.j.data.get("build_intent"):
                raise StopWorkflow("build submission unresolved; do not submit duplicate")
            self.j.save("build_intent", build_intent=True)
            submitted = self.client.orchestration.Build.create(
                target=ManualTarget(target_rids=[DS]), branch_name=BRANCH,
                fallback_branches=[BRANCH], retry_count=0, abort_on_failure=True,
                request_timeout=3,
            )
            assert submitted.branch_name == BRANCH
            rid = submitted.rid
            self.j.save("build_known", build_rid=rid, submission_status=submitted.status)
        deadline = time.monotonic() + seconds
        for poll in range(max_polls):
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                break
            observed = self.client.orchestration.Build.get(
                rid, request_timeout=min(3, max(1, math.ceil(remaining))))
            assert observed.rid == rid and observed.branch_name == BRANCH
            self.j.save("build_observed", build_status=observed.status, poll=poll + 1)
            if observed.status == "SUCCEEDED":
                self.j.save("build_complete", outcome="success")
                return "success"
            if observed.status in {"FAILED", "CANCELED"}:
                self.branch()
                self.j.save("build_complete", outcome="unsuccessful",
                            recovery="Inspect jobs and branch before correction or resubmission")
                return "unsuccessful"
            if poll + 1 < max_polls:
                time.sleep(min(0.3, max(0, deadline - time.monotonic())))
        self.j.save("build_pending", outcome="pending",
                    recovery="Resume reads of retained build RID; no duplicate create")
        return "pending"

    def run(self):
        self.dataset_commit()
        return self.build()


class Service:
    """Stateful synthetic service, independent of the workflow's journal."""

    def __init__(self, status="SUCCEEDED", fault=None):
        self.status, self.fault = status, fault
        self.tx = "ABSENT"
        self.uploaded = False
        self.build_created = False
        self.polls = 0
        self.requests = []
        self.mutations = []
        self.attempts = {"upload": 0, "commit": 0}

    def tx_body(self):
        return {"rid": TX, "transactionType": "APPEND", "status": self.tx, "createdTime": STAMP}

    def build_body(self, status):
        return {"rid": BUILD, "branchName": BRANCH, "createdTime": STAMP,
                "createdBy": "00000000-0000-0000-0000-000000000012", "fallbackBranches": [BRANCH],
                "jobRids": [], "retryCount": 0,
                "retryBackoffDuration": {"value": 1, "unit": "MILLISECONDS"},
                "abortOnFailure": True, "status": status}

    def handle(self, request):
        entry = {"at": utc(), "method": request.method, "path": request.url.path,
                 "query": list(request.url.params.multi_items()),
                 "headers": {k: v for k, v in request.headers.items() if k.lower() != "authorization"},
                 "body": request.content.decode(), "timeout": request.extensions.get("timeout")}
        self.requests.append(entry)
        assert request.url.host == "reader.invalid"
        assert request.headers["authorization"] == "Bearer synthetic-j12"
        assert 0 < request.extensions["timeout"]["read"] <= 3
        try:
            result = self.dispatch(request)
            entry["http_status"] = result.status_code
            entry["response"] = result.content.decode()
            return result
        except httpx.ReadTimeout as exc:
            entry["transport_exception"] = str(exc)
            raise

    def dispatch(self, request):
        method, path, query = request.method, request.url.path, dict(request.url.params)
        root = f"/api/v2/datasets/{DS}"
        if path == f"{root}/branches/{BRANCH}" and method == "GET":
            pointer = TX if self.tx == "COMMITTED" else BASE
            if self.fault == "wrong_branch" and self.tx == "COMMITTED":
                pointer = BASE
            return httpx.Response(200, json={"name": BRANCH, "transactionRid": pointer})
        if path == f"{root}/transactions" and method == "POST":
            assert self.tx == "ABSENT" and query == {"branchName": BRANCH}
            assert json.loads(request.content) == {"transactionType": "APPEND"}
            self.tx = "OPEN"
            self.mutations.append("create")
            return httpx.Response(200, json=self.tx_body())
        if path == f"{root}/transactions/{TX}" and method == "GET":
            assert self.tx != "ABSENT" and not query
            return httpx.Response(200, json=self.tx_body())
        if path == f"{root}/files/{FILE}/upload" and method == "POST":
            self.attempts["upload"] += 1
            assert self.tx == "OPEN" and not self.uploaded
            assert query == {"transactionRid": TX} and request.content == DATA
            assert request.headers["content-type"] == "application/octet-stream"
            self.uploaded = True
            self.mutations.append("upload")
            if self.fault == "upload_lost":
                raise httpx.ReadTimeout("synthetic lost upload reply", request=request)
            return httpx.Response(200, json={"path": FILE, "transactionRid": TX,
                "sizeBytes": len(DATA), "updatedTime": STAMP})
        if path in {f"{root}/files/{FILE}", f"{root}/files/{FILE}/content"} and method == "GET":
            assert self.uploaded
            staged = "startTransactionRid" in query
            assert query == ({"startTransactionRid": TX, "endTransactionRid": TX}
                             if staged else {"branchName": BRANCH})
            assert self.tx == ("OPEN" if staged else "COMMITTED")
            if path.endswith("/content"):
                if staged and self.fault == "reconcile_unavailable":
                    raise httpx.ReadTimeout("synthetic read unavailable", request=request)
                corrupt = (staged and self.fault == "bad_staged") or (
                    not staged and self.fault == "bad_visible")
                return httpx.Response(200, content=b"corrupt" if corrupt else DATA)
            return httpx.Response(200, json={"path": FILE, "transactionRid": TX,
                "sizeBytes": len(DATA), "updatedTime": STAMP})
        if path == f"{root}/transactions/{TX}/commit" and method == "POST":
            assert self.tx == "OPEN" and self.uploaded and not query
            self.attempts["commit"] += 1
            if self.fault == "commit_before_effect" and self.attempts["commit"] == 1:
                raise httpx.ReadTimeout("synthetic commit not applied", request=request)
            self.tx = "COMMITTED"
            self.mutations.append("commit")
            if self.fault == "commit_lost":
                raise httpx.ReadTimeout("synthetic lost commit reply", request=request)
            return httpx.Response(200, json=self.tx_body())
        if path == f"{root}/transactions/{TX}/abort" and method == "POST":
            assert self.tx == "OPEN"
            self.tx = "ABORTED"
            self.mutations.append("abort")
            return httpx.Response(200, json=self.tx_body())
        if path == "/api/v2/orchestration/builds/create" and method == "POST":
            assert self.tx == "COMMITTED" and not self.build_created
            assert json.loads(request.content) == {"target": {"type": "manual", "targetRids": [DS]},
                "branchName": BRANCH, "fallbackBranches": [BRANCH], "retryCount": 0,
                "abortOnFailure": True}
            self.build_created = True
            self.mutations.append("build_create")
            return httpx.Response(200, json=self.build_body("RUNNING"))
        if path == f"/api/v2/orchestration/builds/{BUILD}" and method == "GET":
            assert self.build_created
            self.polls += 1
            return httpx.Response(200, json=self.build_body("RUNNING" if self.polls == 1 else self.status))
        raise AssertionError(f"Unexpected request: {method} {request.url}")


def deny(*args, **kwargs):
    raise AssertionError("public network denied by J12 reader")


def execute(name, status="SUCCEEDED", fault=None, resume=False):
    service = Service(status, fault)
    journal_path = ROOT / f"journal_{name}.json"
    assert not journal_path.exists(), "Keep original evidence; use a fresh output directory"
    started = utc()
    with patch.object(socket, "getaddrinfo", deny), patch.object(socket.socket, "connect", deny), \
         patch.object(socket.socket, "connect_ex", deny), \
         httpx.Client(transport=httpx.MockTransport(service.handle), timeout=3) as transport:
        denial = []
        for probe in (lambda: socket.getaddrinfo("www.palantir.com", 443),
                      lambda: socket.socket().connect(("1.1.1.1", 443))):
            try:
                probe()
            except AssertionError as exc:
                denial.append(str(exc))
        assert len(denial) == 2
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            client = FoundryClient(hostname="https://reader.invalid", auth=UserTokenAuth("synthetic-j12"),
                config=Config(timeout=3, max_retries=1,
                              propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"))
            workflow = Workflow(client, Journal(journal_path))
            try:
                outcome = workflow.run()
                if resume:
                    before = list(service.mutations)
                    assert outcome == "pending"
                    service.status = "SUCCEEDED"
                    outcome = Workflow(client, Journal(journal_path)).run()
                    assert service.mutations == before
            except StopWorkflow as exc:
                outcome = "stopped"
                workflow.j.save("stopped", reason=str(exc), outcome=outcome)
    result = {"name": name, "started": started, "finished": utc(), "outcome": outcome,
              "status_requested": status, "fault": fault, "denial_probes": denial,
              "mutations": service.mutations, "mutation_attempts": service.attempts,
              "build_reads": service.polls, "journal": journal_path.name,
              "requests": service.requests}
    (ROOT / f"trace_{name}.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    expected = "stopped" if fault in {"bad_staged", "bad_visible", "wrong_branch", "reconcile_unavailable"} else (
        "success" if status == "SUCCEEDED" or resume else "pending" if status == "RUNNING" else "unsuccessful")
    assert outcome == expected, (name, expected, outcome)
    if outcome == "stopped":
        assert not service.build_created
        if fault in {"bad_staged", "reconcile_unavailable"}:
            assert service.mutations == ["create", "upload", "abort"]
    else:
        assert service.mutations == ["create", "upload", "commit", "build_create"]
    assert service.attempts["upload"] == 1
    assert service.attempts["commit"] <= (2 if fault == "commit_before_effect" else 1)
    if status == "RUNNING" and not resume:
        assert service.polls == 3
    print(json.dumps({k: v for k, v in result.items() if k != "requests"}))
    return {k: v for k, v in result.items() if k != "requests"}


def main():
    assert version("foundry-platform-sdk") == "1.101.0"
    runtime = {"sdk": version("foundry-platform-sdk"), "httpx": version("httpx"),
               "python": __import__("sys").version, "executable": __import__("sys").executable}
    cases = [execute("success"), execute("failed", "FAILED"), execute("canceled", "CANCELED"),
             execute("pending", "RUNNING"), execute("upload_recovery", fault="upload_lost"),
             execute("commit_recovery", fault="commit_lost"),
             execute("commit_safe_retry", fault="commit_before_effect"),
             execute("pending_resume", "RUNNING", resume=True),
             execute("staging_corruption", fault="bad_staged"),
             execute("visible_corruption", fault="bad_visible"),
             execute("branch_mismatch", fault="wrong_branch"),
             execute("reconciliation_unavailable", fault="reconcile_unavailable")]
    (ROOT / "execution_results.json").write_text(json.dumps({"runtime": runtime, "cases": cases}, indent=2))
    print(f"Independent reader: {len(cases)} scenarios matched expected outcomes; synthetic transport only")


if __name__ == "__main__":
    main()
