# v2 datasets: File

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

## Client route and bounded content read

With a configured `FoundryClient` named `client`, File operations are under
`client.datasets.Dataset.File`. `client.datasets.File` is not an SDK 1.101.0
resource. Select the dataset RID, file path and branch or transaction view from
authorized dataset metadata before reading. The following call reads one known
file and closes the streaming response:

```python
metadata = client.datasets.Dataset.File.get(
    dataset_rid, file_path, branch_name=branch_name, request_timeout=30
)
assert metadata.path == file_path
limit = 8 * 1024 * 1024  # application byte budget
payload = bytearray()
with client.datasets.Dataset.File.with_streaming_response.content(
    dataset_rid, file_path, branch_name=branch_name, request_timeout=30
) as response:
    for chunk in response.iter_bytes():
        if len(payload) + len(chunk) > limit:
            raise ValueError("File exceeds application byte budget")
        payload.extend(chunk)
if metadata.size_bytes is not None:
    assert len(payload) == metadata.size_bytes
```

The size check applies when the response provides a size and the file has not
changed between metadata and content reads. An omitted size is valid; enforce
the byte budget regardless. Pin a transaction view when repeatable content matters, and
handle a changed size as an uncertain read to reconcile rather than accepting
partial bytes. A denied or missing result calls for checking the exact dataset,
view and path. The [offline content fixture](../../../../examples/rest/074/v2/datasets/File/content.py)
checks SDK request and bytes with synthetic input; it makes no tenant call.
The [root-client regression](../../../../examples/rest/074/v2/datasets/file_client_route_regression.py)
also checks v1/v2 route names, an omitted size and a named missing-file error.

## Operations and outcome checks

For a write spanning several files, open one explicit transaction, upload with
its `transaction_rid`, read staged metadata/content with matching
`start_transaction_rid` and `end_transaction_rid`, then commit and verify the
named branch and file. Follow
the [typed staged-commit procedure](Transaction.md) and its offline fixture.
`File.get` and `File.content` can select a transaction view or a branch view;
keep those selectors explicit throughout the check.

### content

Read file content as bytes from the intended view. Choose branch or transaction
selectors explicitly for historical reads and close raw/streaming responses.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/File/content.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/File/content.py):

```bash
python -B examples/rest/074/v2/datasets/File/content.py
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
| FileSizeLimitExceeded | The requested file is larger than the configured maximum download size. Contact Palantir Support to discuss limit increases. |
| GetFileContentPermissionDenied | Could not content the File. |
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### delete

Delete the intended path in the selected branch or explicit open transaction. Default
behavior creates a transaction on the default branch; historical views still retain the
file. Verify the resulting selected view.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/File/delete.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/File/delete.py):

```bash
python -B examples/rest/074/v2/datasets/File/delete.py
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
| DeleteFilePermissionDenied | Could not delete the File. |
| FileNotFoundOnBranch | The requested file could not be found on the given branch, or the client token does not have access to it. |
| FileNotFoundOnTransactionRange | The requested file could not be found on the given transaction range, or the client token does not have access to it. |
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| InvalidTransactionType | The given transaction type is not valid. Valid transaction types are `SNAPSHOT`, `UPDATE`, `APPEND`, and `DELETE`. |
| OpenTransactionAlreadyExists | A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time. |
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

[Exact parameters, request, result and error models](../../contracts/v2/datasets/File/get.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/File/get.py):

```bash
python -B examples/rest/074/v2/datasets/File/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| FileNotFound | The given File could not be found. |
| FileNotFoundOnBranch | The requested file could not be found on the given branch, or the client token does not have access to it. |
| FileNotFoundOnTransactionRange | The requested file could not be found on the given transaction range, or the client token does not have access to it. |
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
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

[Exact parameters, request, result and error models](../../contracts/v2/datasets/File/list.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/File/list.py):

```bash
python -B examples/rest/074/v2/datasets/File/list.py
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
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidFilePath | The provided file path is invalid. Check that the path does not start with a leading slash. |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |
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

[Exact parameters, request, result and error models](../../contracts/v2/datasets/File/upload.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/File/upload.py):

```bash
python -B examples/rest/074/v2/datasets/File/upload.py
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
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidFilePath | The provided file path is invalid. Check that the path does not start with a leading slash. |
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
