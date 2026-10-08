# v2 datasets: Branch

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Branches name dataset version histories. A branch may initially point to a committed
transaction. Choose branch identity explicitly before reading or mutating data; the
enrollment default is often master but is not universal. Branch deletion differs from
deleting dataset files.

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

### create

Create a named branch on an existing dataset. If selecting an initial transaction, use a
committed transaction and compare the resulting branch pointer with the intended
version.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Branch/create.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Branch/create.py):

```bash
python -B examples/rest/074/v2/datasets/Branch/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchAlreadyExists | The branch cannot be created because a branch with that name already exists. |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| CreateBranchPermissionDenied | The provided token does not have permission to create a branch of this dataset. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| TransactionNotCommitted | The given transaction has not been committed. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### delete

Confirm dataset and branch identity before deleting the branch. Preserve intended
downstream dependencies for review; branch deletion is distinct from deleting historical
file content.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Branch/delete.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Branch/delete.py):

```bash
python -B examples/rest/074/v2/datasets/Branch/delete.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| DeleteBranchPermissionDenied | The provided token does not have permission to delete the given branch from this dataset. |
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Inspect the selected dataset branch and its transaction reference before reading or
writing data. Treat an absent branch as an identity problem rather than silently using
the default.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Branch/get.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Branch/get.py):

```bash
python -B examples/rest/074/v2/datasets/Branch/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

List branches for the selected dataset and choose the intended branch by its returned
identity. Bound enumeration when the version contract exposes pages.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Branch/list.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Branch/list.py):

```bash
python -B examples/rest/074/v2/datasets/Branch/list.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### transactions

Read transaction history for the selected branch. Requests for all transactions return
reverse chronological order; preserve finite paging and use transaction IDs for follow-
up.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Branch/transactions.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Branch/transactions.py):

```bash
python -B examples/rest/074/v2/datasets/Branch/transactions.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| GetBranchTransactionHistoryPermissionDenied | Could not transactions the Branch. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
