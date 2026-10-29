# J12: dataset file transaction and finite build inspection

## Prerequisites and boundaries

Use installed `foundry-platform-sdk==1.101.0`, `httpx`, a configured `foundry_sdk.v2.FoundryClient`, an authorized token, enrollment hostname, known dataset RID, branch, safe relative file path, payload, and a separately supplied build RID. The root v2 client is the public composed route. A generated Ontology SDK or v1 client has a different contract. Confirm the acting identity can create, upload, read, commit, and, if needed, abort a transaction on the chosen dataset and branch. Confirm build read permission separately. The SDK source states no universal scope or idempotency guarantee. Synthetic IDs in the fixture imply no tenant access.

Consulted local headings: `references/rest-api.md` **Discover and author any frozen SDK REST operation / Prerequisites / Procedure / Failures and recovery / Access boundary**; `references/rest/client-behavior.md` **Client and API version / Response modes / Timeouts, throttling and uncertain writes / Errors and cleanup**; `references/rest/v2/datasets/Transaction.md` **Capability and lifecycle / Stage a file, commit, and verify the branch**; `references/rest/v2/orchestration/Build.md` **Capability and lifecycle / Wait for a submitted build**. Exact method and model headings: `contracts/v2/datasets/Transaction/{create,get,commit,abort}.md`, `contracts/v2/datasets/File/{upload,get,content}.md`, `contracts/v2/datasets/Branch/get.md`, `contracts/v2/orchestration/Build/get.md`, `models/v2/datasets/models/{Transaction,TransactionStatus,File}.md`, and `models/v2/orchestration/models/{Build,BuildStatus}.md`.

## Ordered workflow

1. Set `Config(timeout=30, max_retries=1, propagate_qos="PROPAGATE_429_AND_503_TO_CALLER")`; give each request `request_timeout=30`. Use a separate monotonic total deadline and finite poll count. `max_retries=1` means one synchronous attempt in this SDK. A zero value falls back to its default, so avoid zero. Choose `APPEND`, `UPDATE`, `SNAPSHOT`, or `DELETE` from intended branch effect; this example uses `APPEND` and a new file path.
2. Call `client.datasets.Dataset.Transaction.create(dataset_rid, transaction_type="APPEND", branch_name=branch_name, request_timeout=30)`. Save returned `tx.rid` and verify `OPEN`. If creation response is lost, do not create another transaction blindly: inspect the known branch's open transaction through an authorized lookup or involve the owner if identity cannot be established.
3. Call `client.datasets.Dataset.File.upload(dataset_rid, file_path, payload_bytes, transaction_rid=tx.rid, request_timeout=30)`. It sends `application/octet-stream`. Assert returned `path` and `transaction_rid`. Before commit, inspect `File.get` and `File.content` using **both** `start_transaction_rid=tx.rid` and `end_transaction_rid=tx.rid`; this selects the staged view. Keep payload size bounded before an ordinary `content` read. On lost upload response, get the known transaction and inspect the staged file/content once under a fixed read budget. Do not replay upload until its effect is known.
4. Call `Transaction.commit(dataset_rid, tx.rid, request_timeout=30)` once. Verify `COMMITTED` via `Transaction.get`; verify `Branch.get(dataset_rid, branch_name).transaction_rid == tx.rid`; then read file metadata/content on **that branch**. On lost commit response, reconcile transaction and branch first. If the transaction remains `OPEN` and staging is verified, the owner may decide whether a controlled commit attempt is safe. If staging fails and the transaction is confirmed `OPEN`, `Transaction.abort(dataset_rid, tx.rid)` discards it. Read state again after an uncertain abort. A committed transaction cannot be treated as aborted.
5. A transaction commit does not submit a build. For a separately submitted build, retain its returned RID and call `client.orchestration.Build.get(build_rid, request_timeout=...)` at no more than four requests per second, with at most one concurrent poll here. Accept `SUCCEEDED` as terminal success; `FAILED` and `CANCELED` are terminal unsuccessful results. Inspect jobs and branch state before any resubmission. If `RUNNING` at poll or deadline limit, report **pending**, save the same build RID, and resume inspection later. A build read does not itself prove downstream data correctness.

Suggested live poll bound: at most 20 `Build.get` calls, at least 0.25 seconds apart, per-call timeout at most 10 seconds, and a 120-second monotonic deadline. The application checks remaining time before each call and records `RUNNING` when a limit expires. Positive integer SDK request timeouts can make the final call extend slightly beyond an application deadline. No page traversal is needed for `Build.get`; optional job diagnostics need a separate five-page, 500-job bound and repeated-token check from **Wait for a submitted build**. Limit upload payload to 1 MiB in this example and give stage reconciliation at most two reads (`Transaction.get`, then `File.get`/`content` if needed). These are application budgets, not claimed SDK maxima.

## Runnable synthetic fixture and observed result

The [fixture](j12_fixture.py) uses the installed SDK's composed v2 client and `httpx.MockTransport`. It asserts wire paths, payload, selector parameters, transaction/branch/file checks, exactly one create/upload/commit submission, and two build polls separated by 0.26 seconds. Scenarios: prepared `SUCCEEDED`; a lost upload reply with staged read reconciliation; a lost commit reply with transaction/branch reconciliation; and `RUNNING` after two polls. The fixture accepts an externally known synthetic build RID; it does not claim to create a build or use a real enrollment.

```powershell
python -B pal_found_cli_skills/tests/fixtures/feature015_qa/evidence/final_reader_j12/j12_fixture.py
```

Observed exit code: `0`.

```text
network probe: PUBLIC_NETWORK_DENIED (cooperative socket guard)
prepared: SUCCEEDED; writes=create,upload,commit exactly once
lost-upload: SUCCEEDED; writes=create,upload,commit exactly once
lost-commit: SUCCEEDED; writes=create,upload,commit exactly once
pending-budget: RUNNING; writes=create,upload,commit exactly once
```

The supplied guard patches Python socket DNS/connect/send methods and proves its own `www.palantir.com` lookup raises `PUBLIC_NETWORK_DENIED` before the MockTransport calls. This is cooperative in-process denial. It does not establish an operating-system firewall, cover subprocesses or native transports, or prove live Foundry permissions, committed tenant state, or a production build outcome.
