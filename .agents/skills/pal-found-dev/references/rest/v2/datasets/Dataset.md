# v2 datasets: Dataset

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

[Detailed worked procedure](Dataset-worked.md).

## Operations and outcome checks

### create

Create the dataset in its intended parent location and retain the returned RID. A
default branch is created, usually master; inspect the returned configuration rather
than assuming that name.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/create.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/create.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchAlreadyExists | The branch cannot be created because a branch with that name already exists. |
| CreateBranchPermissionDenied | The provided token does not have permission to create a branch of this dataset. |
| CreateDatasetPermissionDenied | The provided token does not have permission to create a dataset in this folder. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| FolderNotFound | The given Folder could not be found. |
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidDisplayName | The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters. |
| ResourceNameAlreadyExists | The provided resource name is already in use by another resource in the same folder. |
| TransactionNotCommitted | The given transaction has not been committed. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Read dataset metadata by RID before resolving its branch, files or schema. Metadata
success does not prove that table export or file reads are permitted.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/get.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/get.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| ResourceNameAlreadyExists | The provided resource name is already in use by another resource in the same folder. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_health_check_reports

Read the latest report for each configured check to inspect current dataset health. One
report per check is returned; this is not each check's full report history.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/get_health_check_reports.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/get_health_check_reports.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/get_health_check_reports.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| CheckTypeNotSupported | The type of the requested check is not yet supported in the Platform API. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| GetDatasetHealthCheckReportsPermissionDenied | Could not getHealthCheckReports the Dataset. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_health_checks

Read configured health-check RIDs, then inspect Check and CheckReport resources for
configuration and outcomes. A check RID alone does not describe a passing evaluation.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/get_health_checks.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/get_health_checks.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/get_health_checks.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| GetDatasetHealthChecksPermissionDenied | Could not getHealthChecks the Dataset. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_schedules

Discover schedules targeting the dataset. Recent changes can take up to one hour to
appear, especially Marketplace-managed schedules; do not use this response as immediate
write confirmation.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/get_schedules.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/get_schedules.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/get_schedules.py
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
| GetDatasetSchedulesPermissionDenied | Could not getSchedules the Dataset. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_schema

Read schema for the selected dataset version. In v2 omission of endTransactionRid
selects the latest committed version. Check column types before parsing exports or
authoring schema-dependent code.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/get_schema.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/get_schema.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/get_schema.py
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
| GetDatasetSchemaPermissionDenied | Could not getSchema the Dataset. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| SchemaNotFound | A schema could not be found for the given dataset and branch, or the client token does not have access to it. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get_schema_batch

Retrieve schemas for up to 1000 datasets per batch. Missing or inaccessible datasets are
omitted, so reconcile every requested dataset against returned identities and report
omissions.

[Exact parameters, request, result and error models](../../contracts/v2/datasets/Dataset/get_schema_batch.md).

[Executable SDK example](../../../../examples/rest/074/v2/datasets/Dataset/get_schema_batch.py):

```bash
python -B examples/rest/074/v2/datasets/Dataset/get_schema_batch.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

## More operations

- [Part 2](Dataset-2.md)
