# v2 datasets: Transaction

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A transaction stages dataset changes on a branch. An open transaction can be committed
or aborted. Commit preserves modifications and advances the branch; abort discards those
modifications and leaves the branch unchanged. A transaction can lack a build or job
association.

## Prepare the application

Use prepared SDK 1.101.0 and an authorized identity for the intended enrollment. Resolve
the resource identities and complete request models linked below before calling a
method. Offline fixtures use synthetic identities and an actual SDK HTTP transport; they
need prepared Python, SDK and httpx and contact no enrollment.

Verify the application grants, resource permissions and capability enablement in the
tenant. SDK source does not enumerate a universal role or scope for every operation;
operation-specific documented requirements below take precedence. Source does not
provide a universal idempotency guarantee. For uncertain writes, retain request identity
and reconcile through authorized reads before repeating.

## Operations and outcome checks

## Stage a file, commit, and verify the branch

Use the public v2 route `client.datasets.Dataset.Transaction` together with
`client.datasets.Dataset.File` and `client.datasets.Dataset.Branch`. Resolve
`dataset_rid`, `branch_name` and `file_path` from an authorized dataset first.
This example stages a small file in one explicit transaction and checks the
staged view before committing. A read by `end_transaction_rid` selects the
transaction view; do not substitute a branch read before commit. Set both
transaction-range bounds to the same RID for this single staged transaction.

```python
tx = client.datasets.Dataset.Transaction.create(
    dataset_rid, transaction_type="APPEND", branch_name=branch_name,
    request_timeout=30,
)
assert tx.status == "OPEN"
payload = b"id,status\n1,ready\n"
uploaded = client.datasets.Dataset.File.upload(
    dataset_rid, file_path, payload, transaction_rid=tx.rid,
    request_timeout=30,
)
assert uploaded.transaction_rid == tx.rid and uploaded.path == file_path
staged = client.datasets.Dataset.File.get(
    dataset_rid, file_path, start_transaction_rid=tx.rid,
    end_transaction_rid=tx.rid, request_timeout=30,
)
assert staged.transaction_rid == tx.rid
staged_bytes = client.datasets.Dataset.File.content(
    dataset_rid, file_path, start_transaction_rid=tx.rid,
    end_transaction_rid=tx.rid, request_timeout=30,
)
assert staged_bytes == payload
committed = client.datasets.Dataset.Transaction.commit(
    dataset_rid, tx.rid, request_timeout=30,
)
assert committed.rid == tx.rid and committed.status == "COMMITTED"
branch = client.datasets.Dataset.Branch.get(
    dataset_rid, branch_name, request_timeout=30,
)
assert branch.transaction_rid == tx.rid
visible = client.datasets.Dataset.File.get(
    dataset_rid, file_path, branch_name=branch_name, request_timeout=30,
)
assert visible.transaction_rid == tx.rid
assert client.datasets.Dataset.File.content(
    dataset_rid, file_path, branch_name=branch_name, request_timeout=30,
) == payload
```

Limit payload size in the application before calling the ordinary `content`
method; use the [bounded streaming read](File.md) for larger files. If staging
fails, inspect transaction state and abort only an OPEN transaction. If commit
times out, call `Transaction.get` and `Branch.get` before deciding whether to
retry; a committed transaction or branch pointer can outlive the lost reply.
The post-commit file check must use the same branch. A different branch or
default selector can show another version. The [offline staged-commit fixture](../../../../examples/rest/074/v2/datasets/staged_commit_journey.py)
checks these transitions with SDK transport and synthetic identities.

### abort

Abort the confirmed open transaction. Its modifications are discarded and the branch
remains unchanged. Check transaction state after an uncertain response before attempting
another lifecycle operation.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Transaction/abort.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Transaction/abort.py):

```bash
python -B examples/rest/074/v2/datasets/Transaction/abort.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AbortTransactionPermissionDenied | The provided token does not have permission to abort the given transaction on the given dataset. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |
| TransactionNotOpen | The given transaction is not open. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### build

Read the build associated with the transaction when one exists. User-uploaded data can
have no associated build; absence is not proof that transaction creation failed.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Transaction/build.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Transaction/build.py):

```bash
python -B examples/rest/074/v2/datasets/Transaction/build.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BuildTransactionPermissionDenied | Could not build the Transaction. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### commit

Commit the confirmed open transaction. Its modifications are preserved and the branch
points to it. Read transaction and branch state after submission; do not blindly repeat
after a lost response.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Transaction/commit.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Transaction/commit.py):

```bash
python -B examples/rest/074/v2/datasets/Transaction/commit.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CommitTransactionPermissionDenied | The provided token does not have permission to commit the given transaction on the given dataset. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |
| TransactionNotOpen | The given transaction is not open. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### create

Open a transaction on the intended dataset branch using the selected transaction type.
Retain its RID for staged file/schema work and ensure the application eventually commits
or aborts it.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Transaction/create.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Transaction/create.py):

```bash
python -B examples/rest/074/v2/datasets/Transaction/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| CreateTransactionPermissionDenied | The provided token does not have permission to create a transaction on this dataset. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| OpenTransactionAlreadyExists | A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Read transaction state and identity before committing, aborting or interpreting its
contents. Confirm that it belongs to the intended dataset and branch workflow.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Transaction/get.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Transaction/get.py):

```bash
python -B examples/rest/074/v2/datasets/Transaction/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### job

Read the job associated with the transaction when one exists. User-uploaded data can
have no associated job; inspect transaction state independently.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Transaction/job.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Transaction/job.py):

```bash
python -B examples/rest/074/v2/datasets/Transaction/job.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| JobTransactionPermissionDenied | Could not job the Transaction. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
