# J12 offline reader result

Input: J12 prompt and synthetic records from `reader_prompts.json`. I read only the copied `pal-found-dev` folder and used prepared SDK 1.101.0 with local synthetic examples. Public sources, expected-answer files and a Foundry tenant were unavailable. The copy was staged at `.ept/tmp/feature015-j12-reader/pal-found-dev`. Public-network denial was instructed but not instrumented for this reader process.

## Capability and lifecycle

Use v2 `datasets.Dataset.Transaction` to open, inspect, commit or abort a dataset transaction; use `datasets.Dataset.File.upload` with its explicit `transaction_rid` to stage the file in that open transaction. A default file upload creates and commits its own transaction, so it cannot serve this multi-step workflow. A commit updates the selected branch; an abort discards staged changes. A transaction need not have a build. For an independently known build RID, `orchestration.Build.get` reports `RUNNING`, `SUCCEEDED`, `FAILED` or `CANCELED`; submission and completion differ. Local headings: `references/rest/v2/datasets/Transaction.md#capability-and-lifecycle`, `references/rest/v2/datasets/File.md#capability-and-lifecycle`, `references/rest/v2/orchestration/Build.md#capability-and-lifecycle`, and `references/rest/models/v2/orchestration/models/BuildStatus.md#exact-sdk-definition`.

## Prerequisites and access

Use prepared `foundry_sdk==1.101.0`, `httpx`, a selected dataset RID, branch name, relative file path, bytes, an authorized identity and a finite request/poll budget. Local fixtures use synthetic IDs and fake HTTP transport. Live create, upload, commit, build lookup and permission checks require enrollment connectivity plus dataset/branch access. The SDK does not declare one universal role or scope; verify each operation and its resource policy. Do not put tokens in fixture output. Local headings: `references/rest-api.md#prerequisites`, `references/rest/v2/datasets/Transaction.md#prepare-the-application`, `references/rest/authentication.md`, `references/rest/client-behavior.md#timeouts-throttling-and-uncertain-writes`.

## Ordered procedure and adaptable code

1. Select the dataset and branch; choose `APPEND`, `UPDATE`, `SNAPSHOT` or `DELETE` according to the intended change. A branch can have only one open transaction at once.
2. Create the transaction and retain its RID; confirm status `OPEN` and intended dataset/branch context before staging.
3. Upload bytes to a relative path with `transaction_rid`, `Content-Type: application/octet-stream`, and no conflicting branch selector. Read transaction state after upload. Use `File.get` or `File.list` with the intended transaction/branch selector when available to inspect the staged view.
4. Commit only after staged content is verified. Re-read transaction status and branch/file view; `COMMITTED` and the expected visible file establish the transaction result. Abort a confirmed still-open transaction when abandoning the staged change; do not abort a committed one.
5. If a build RID is provided or returned by a separate build request, poll `Build.get` at no more than four calls per second and 25 concurrent calls. Stop on a terminal status, deadline or attempt cap. `RUNNING` when the budget expires is pending, not success.

The following is an adaptation skeleton using the prepared v2 client. Replace values with authorized enrollment values for live use; keep the uncertain-write branches described below around `upload` and `commit`.

```python
from foundry_sdk import Config, FoundryClient, UserTokenAuth

client = FoundryClient(
    hostname="example.palantirfoundry.com",
    auth=UserTokenAuth(token="<authorized-token>"),
    config=Config(timeout=30, max_retries=1,
                  propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
)
dataset = "ri.synthetic.main.dataset.00000000-0000-0000-0000-000000000001"
branch = "master"
path = "inspections/status.csv"
payload = b"asset_id,status\nA-1,ready\n"

transactions = client.datasets.Dataset.Transaction
files = client.datasets.Dataset.File
created = transactions.create(dataset, transaction_type="APPEND",
                              branch_name=branch, request_timeout=30)
transaction_rid = created.rid
assert created.status == "OPEN"
staged = files.upload(dataset, path, payload,
                      transaction_rid=transaction_rid, request_timeout=30)
assert transactions.get(dataset, transaction_rid,
                        request_timeout=30).status == "OPEN"
# Verify the staged file view and intended content before this mutation.
committed = transactions.commit(dataset, transaction_rid, request_timeout=30)
assert committed.status == "COMMITTED"
assert transactions.get(dataset, transaction_rid,
                        request_timeout=30).status == "COMMITTED"

# For a separately known build RID, use bounded polling below four calls/second.
import time
build_rid = "<known-build-rid>"
for attempt in range(8):
    build = client.orchestration.Build.get(build_rid, request_timeout=30)
    if build.status in {"SUCCEEDED", "FAILED", "CANCELED"}:
        break
    if attempt < 7:
        time.sleep(0.5)
else:
    build = None  # pending: preserve build_rid and last RUNNING observation
```

The example uses `APPEND` only because the synthetic input is a new file. For a replacement path choose the intended transaction type after checking the branch and local transaction type contract. Local headings: `references/rest/contracts/v2/datasets/Transaction/create.md#sdk-invocation-contract`, `File/upload.md#sdk-invocation-contract`, `Transaction/commit.md#sdk-invocation-contract`, `Transaction/get.md#sdk-invocation-contract`, `references/rest/contracts/v2/orchestration/Build/get.md#sdk-invocation-contract`.

## Observable checks and local execution

I ran these six independent synthetic SDK transport examples from the copied skill root, each exit 0:

| Command suffix under `examples/rest/` | Observed result |
| --- | --- |
| `074/v2/datasets/Transaction/create.py` | Request/result and 5 named errors passed |
| `074/v2/datasets/File/upload.py` | Request/result and 13 named errors passed |
| `074/v2/datasets/Transaction/commit.py` | Request/result and 4 named errors passed |
| `074/v2/datasets/Transaction/get.py` | Request/result and 2 named errors passed |
| `074/v2/datasets/Transaction/abort.py` | Request/result and 4 named errors passed |
| `075/v2/orchestration/Build/get.py` | Request/result and 1 named error passed |

These checks validate serialization, model decoding and named error handling independently. I did not execute the combined skeleton, a real tenant write, a real build or a network-denial probe. Local headings: each operation page `#operations-and-outcome-checks` and its linked `#sdk-invocation-contract`.

## Failures and bounded recovery

On upload timeout, retain dataset, branch, transaction RID, path and payload digest; read the transaction and staged file view with the authorized identity. The upload may have applied. Do not send another upload until the staged view proves it absent or the owner resolves an unknown state. On commit timeout, read transaction status: `COMMITTED` means verify branch/file visibility; `OPEN` means inspect the staged file and decide whether one commit attempt is appropriate; `ABORTED` means do not claim success. If status is inaccessible, report uncertainty and stop. A request ID alone is not an idempotency key. `OpenTransactionAlreadyExists`, `TransactionNotOpen`, permission denial and missing resource names require distinct diagnosis. A build still `RUNNING` at poll budget is pending; keep its RID and last state. `FAILED` or `CANCELED` is terminal but unsuccessful. Local headings: `references/rest/client-behavior.md#timeouts-throttling-and-uncertain-writes`, `references/rest/v2/datasets/Transaction.md#operations-and-outcome-checks`, `references/rest/v2/orchestration/Build.md#operations-and-outcome-checks`.
