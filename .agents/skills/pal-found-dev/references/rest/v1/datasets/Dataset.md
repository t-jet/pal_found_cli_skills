# v1 datasets: Dataset

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Datasets contain tabular or file data with branches, transactions and schemas. Metadata,
exported data, health checks and execution history have different contracts. Views are
virtual datasets with separate APIs. Choose a branch and version intentionally when
reading data.

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

Create the dataset in its intended parent location and retain the returned RID. A
default branch is created, usually master; inspect the returned configuration rather
than assuming that name.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/Dataset/create.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/Dataset/create.py):

```bash
python -B examples/rest/074/v1/datasets/Dataset/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchAlreadyExists | The branch cannot be created because a branch with that name already exists. |
| CreateBranchPermissionDenied | The provided token does not have permission to create a branch of this dataset. |
| CreateDatasetPermissionDenied | The provided token does not have permission to create a dataset in this folder. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| FolderNotFound | The requested folder could not be found, or the client token does not have access to it. |
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| ResourceNameAlreadyExists | The provided resource name is already in use by another resource in the same folder. |
| TransactionNotCommitted | The given transaction has not been committed. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### delete_schema

Delete schema for the intended dataset and branch only after confirming why removal is
required. Verify subsequent schema reads and preserve branch identity when interpreting
failure.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/Dataset/delete_schema.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/Dataset/delete_schema.py):

```bash
python -B examples/rest/074/v1/datasets/Dataset/delete_schema.py
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
| DeleteSchemaPermissionDenied | todo |
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| SchemaNotFound | A schema could not be found for the given dataset and branch, or the client token does not have access to it. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Read dataset metadata by RID before resolving its branch, files or schema. Metadata
success does not prove that table export or file reads are permitted.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/Dataset/get.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/Dataset/get.py):

```bash
python -B examples/rest/074/v1/datasets/Dataset/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_schema

Read schema for the selected dataset version. In v2 omission of endTransactionRid
selects the latest committed version. Check column types before parsing exports or
authoring schema-dependent code.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/Dataset/get_schema.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/Dataset/get_schema.py):

```bash
python -B examples/rest/074/v1/datasets/Dataset/get_schema.py
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
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### read

Export dataset content as CSV or ARROW with explicit row/column bounds. Views are
unsupported. Parse the chosen encoding and validate expected fields; row order is
nondeterministic.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/Dataset/read.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/Dataset/read.py):

```bash
python -B examples/rest/074/v1/datasets/Dataset/read.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ColumnTypesNotSupported | The dataset contains column types that are not supported. |
| DatasetReadNotSupported | The dataset does not support being read. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| ReadTablePermissionDenied | The provided token does not have permission to read the given dataset as a table. |
| SchemaNotFound | A schema could not be found for the given dataset and branch, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace_schema

Replace schema on the intended dataset branch with a complete source-compatible schema.
Re-read the schema and compare fields before treating the branch as ready for consumers.

[Exact parameters, request, result and error models](../../contracts/v1/datasets/Dataset/replace_schema.md).

[Executable SDK example](../../../../examples/rest/074/v1/datasets/Dataset/replace_schema.py):

```bash
python -B examples/rest/074/v1/datasets/Dataset/replace_schema.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| AbortTransactionPermissionDenied | The provided token does not have permission to abort the given transaction on the given dataset. |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| CommitTransactionPermissionDenied | The provided token does not have permission to commit the given transaction on the given dataset. |
| CreateTransactionPermissionDenied | The provided token does not have permission to create a transaction on this dataset. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| FileNotFoundOnTransactionRange | The requested file could not be found on the given transaction range, or the client token does not have access to it. |
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidTransactionType | The given transaction type is not valid. Valid transaction types are `SNAPSHOT`, `UPDATE`, `APPEND`, and `DELETE`. |
| OpenTransactionAlreadyExists | A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time. |
| PutSchemaPermissionDenied | todo |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |
| TransactionNotOpen | The given transaction is not open. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
