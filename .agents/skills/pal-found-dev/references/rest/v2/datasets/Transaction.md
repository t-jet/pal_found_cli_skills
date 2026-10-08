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
