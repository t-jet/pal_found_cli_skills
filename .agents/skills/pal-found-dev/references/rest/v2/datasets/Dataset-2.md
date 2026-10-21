# v2 datasets: Dataset, continued

[Resource overview](Dataset.md) | [Client behavior](../../client-behavior.md)

### jobs

Read job RIDs for the dataset; default order is descending job start time. Inspect Job
records to establish outcomes instead of treating a returned RID as execution success.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/jobs.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/jobs.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/jobs.py
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
| GetDatasetJobsPermissionDenied | Could not jobs the Dataset. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### put_schema

Write a schema on the selected existing dataset with PUT, then read it back and compare
intended columns/types. Confirm branch and transaction selection from the contract
before submission.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/put_schema.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/put_schema.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/put_schema.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| DatasetViewNotFound | The requested dataset view could not be found. A dataset view represents the effective file contents of a dataset for a branch at a point in time, calculated from transactions (SNAPSHOT, APPEND, UPDATE, DELETE). The view may not exist if the dataset has no transactions, contains no files, the branch is not valid, or the client token does not have access to it. |
| InvalidSchema | The schema failed validations |
| PutDatasetSchemaPermissionDenied | Could not putSchema the Dataset. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### read_table

Export dataset content as CSV or ARROW with explicit row/column bounds. Views are
unsupported. Parse the chosen encoding and validate expected fields; row order is
nondeterministic.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/read_table.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/read_table.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/read_table.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| ColumnTypesNotSupported | The dataset contains column types that are not supported. |
| DatasetReadNotSupported | The dataset does not support being read. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| ReadTableDatasetPermissionDenied | The provided token does not have permission to read the given dataset as a table. |
| ReadTableError | An error occurred while reading the table. Refer to the message for more details. |
| ReadTableRowLimitExceeded | The request to read the table generates a result that exceeds the allowed number of rows. For datasets not stored as Parquet there is a limit of 1 million rows. For datasets stored as Parquet there is no limit. |
| ReadTableTimeout | The request to read the table timed out. |
| SchemaNotFound | A schema could not be found for the given dataset and branch, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### transactions

Read dataset transaction history with bounded paging. When requesting all transactions,
order is reverse chronological; retain transaction IDs and incomplete continuation
state.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/transactions.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/transactions.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/transactions.py
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

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
