# v1 datasets: File

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Dataset files have paths, binary contents and metadata within a branch or transaction
view. Default reads use the latest view of the default branch. Upload and deletion
normally create transactions; explicit transaction selection allows several file changes
to be staged together.

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

## Public v1 client route and bounded read

With a configured `foundry_sdk.v1.FoundryClient` named `client`, File methods
are under `client.datasets.Dataset.File`. SDK 1.101.0 has no
`client.datasets.File` resource. The v1 method for bytes is `read`, whereas
v2 calls it `content`. v1 selects `branch_id` rather than v2 `branch_name`.

```python
metadata = client.datasets.Dataset.File.get(
    dataset_rid, file_path, branch_id=branch_id, request_timeout=30,
)
assert metadata.path == file_path
limit = 8 * 1024 * 1024
payload = client.datasets.Dataset.File.read(
    dataset_rid, file_path, branch_id=branch_id, request_timeout=30,
)
if len(payload) > limit:
    raise ValueError("File exceeds application byte budget")
if metadata.size_bytes is not None:
    assert len(payload) == metadata.size_bytes
```

Use the streaming wrapper for files that could exceed memory; close its
response after consuming a bounded number of bytes. If metadata omits
`size_bytes`, the byte budget still applies. A changed file between metadata
and read makes the equality check uncertain; pin a transaction range when a
stable version matters. The [offline root-client regression](../../../../examples/rest/074/v2/datasets/file_client_route_regression.py)
checks v1/v2 composed routes, omitted size, bytes and a named missing-file
error without a tenant call.

### delete

Delete the intended path in the selected branch or explicit open transaction. Default
behavior creates a transaction on the default branch; historical views still retain the
file. Verify the resulting selected view.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/File/delete.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/File/delete.py):

```bash
python -B examples/rest/074/v1/datasets/File/delete.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AbortTransactionPermissionDenied | The provided token does not have permission to abort the given transaction on the given dataset. |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| CommitTransactionPermissionDenied | The provided token does not have permission to commit the given transaction on the given dataset. |
| CreateTransactionPermissionDenied | The provided token does not have permission to create a transaction on this dataset. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| FileNotFoundOnBranch | The requested file could not be found on the given branch, or the client token does not have access to it. |
| FileNotFoundOnTransactionRange | The requested file could not be found on the given transaction range, or the client token does not have access to it. |
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| InvalidTransactionType | The given transaction type is not valid. Valid transaction types are `SNAPSHOT`, `UPDATE`, `APPEND`, and `DELETE`. |
| OpenTransactionAlreadyExists | A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time. |
| PutSchemaPermissionDenied | Permission denied in a schema-related step of file deletion. Check access to this dataset and retain the error envelope; the SDK leaves the specific reason unspecified. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |
| TransactionNotOpen | The given transaction is not open. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Inspect file metadata at the selected branch or transaction view before consuming
content. The default uses the latest view of the default branch, which can differ from
an application's intended historical version.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/File/get.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/File/get.py):

```bash
python -B examples/rest/074/v1/datasets/File/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| FileNotFoundOnBranch | The requested file could not be found on the given branch, or the client token does not have access to it. |
| FileNotFoundOnTransactionRange | The requested file could not be found on the given transaction range, or the client token does not have access to it. |
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### list

Enumerate file metadata in the selected dataset view with finite continuation budgets.
Version-specific contracts distinguish branch and transaction selectors. Do not report a
bounded partial listing as a complete inventory.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/File/list.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/File/list.py):

```bash
python -B examples/rest/074/v1/datasets/File/list.py
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
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### read

Read file content as bytes from the intended view. Choose branch or transaction
selectors explicitly for historical reads and close raw/streaming responses; v1 views
are unsupported.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/File/read.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/File/read.py):

```bash
python -B examples/rest/074/v1/datasets/File/read.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| FileNotFoundOnBranch | The requested file could not be found on the given branch, or the client token does not have access to it. |
| FileNotFoundOnTransactionRange | The requested file could not be found on the given transaction range, or the client token does not have access to it. |
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### upload

Upload binary content with application/octet-stream. Default behavior creates a
transaction on the default branch; an existing path shows its most recent version in the
updated view. Use an explicit open transaction to stage coordinated file changes.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/File/upload.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/File/upload.py):

```bash
python -B examples/rest/074/v1/datasets/File/upload.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AbortTransactionPermissionDenied | The provided token does not have permission to abort the given transaction on the given dataset. |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| CommitTransactionPermissionDenied | The provided token does not have permission to commit the given transaction on the given dataset. |
| CreateTransactionPermissionDenied | The provided token does not have permission to create a transaction on this dataset. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| FileAlreadyExists | The given file path already exists in the dataset and transaction. |
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidFilePath | The provided file path is not valid. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| OpenTransactionAlreadyExists | A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |
| TransactionNotOpen | The given transaction is not open. |
| UploadFilePermissionDenied | The provided token does not have permission to upload the given file to the given dataset and transaction. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
