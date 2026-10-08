# v2.datasets.Dataset.read_table


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets the content of a dataset as a table in the specified format.

This endpoint currently does not support views (virtual datasets composed of other datasets).

## SDK invocation contract

```python
def read_table(self, dataset_rid: core_models.DatasetRid, *, format: datasets_models.TableExportFormat, branch_name: typing.Optional[core_models.BranchName]=None, columns: typing.Optional[typing.List[str]]=None, end_transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, row_limit: typing.Optional[int]=None, start_transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.TableResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| format | datasets_models.TableExportFormat | required | The export format. Must be `ARROW` or `CSV`. |
| branch_name | typing.Optional[core_models.BranchName] | None | The name of the Branch. |
| columns | typing.Optional[typing.List[str]] | None | A subset of the dataset columns to include in the result. Defaults to all columns. |
| end_transaction_rid | typing.Optional[datasets_models.TransactionRid] | None | The Resource Identifier (RID) of the end Transaction. |
| row_limit | typing.Optional[int] | None | A limit on the number of rows to return. Note that row ordering is non-deterministic. |
| start_transaction_rid | typing.Optional[datasets_models.TransactionRid] | None | The Resource Identifier (RID) of the start Transaction. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

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

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/datasets/{datasetRid}/readTable'
```

**query_params**

```python
{'format': format, 'branchName': branch_name, 'columns': columns, 'endTransactionRid': end_transaction_rid, 'rowLimit': row_limit, 'startTransactionRid': start_transaction_rid}
```

**path_params**

```python
{'datasetRid': dataset_rid}
```

**header_params**

```python
{'Accept': 'application/octet-stream'}
```

**body**

```python
None
```

**response_type**

```python
bytes
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ColumnTypesNotSupported': datasets_errors.ColumnTypesNotSupported, 'DatasetReadNotSupported': datasets_errors.DatasetReadNotSupported, 'InvalidParameterCombination': core_errors.InvalidParameterCombination, 'ReadTableDatasetPermissionDenied': datasets_errors.ReadTableDatasetPermissionDenied, 'ReadTableError': datasets_errors.ReadTableError, 'ReadTableRowLimitExceeded': datasets_errors.ReadTableRowLimitExceeded, 'ReadTableTimeout': datasets_errors.ReadTableTimeout, 'SchemaNotFound': datasets_errors.SchemaNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ARROW_TABLE')
```

## Response modes

Ordinary sync return: `core.TableResponse`. Ordinary async return: `typing.Awaitable[core.TableResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.TableResponse |
| sync_raw | ApiResponse[bytes] |
| sync_streaming | StreamingContextManager[bytes] |
| async_ordinary | typing.Awaitable[core.TableResponse] |
| async_raw | Awaitable[AsyncApiResponse[bytes]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[bytes]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.errors.InvalidParameterCombination](../../../../models/v2/core/errors/InvalidParameterCombination.md)
- [foundry_sdk.v2.core.errors.InvalidParameterCombinationParameters](../../../../models/v2/core/errors/InvalidParameterCombinationParameters.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.datasets.errors.ColumnTypesNotSupported](../../../../models/v2/datasets/errors/ColumnTypesNotSupported.md)
- [foundry_sdk.v2.datasets.errors.ColumnTypesNotSupportedParameters](../../../../models/v2/datasets/errors/ColumnTypesNotSupportedParameters.md)
- [foundry_sdk.v2.datasets.errors.DatasetReadNotSupported](../../../../models/v2/datasets/errors/DatasetReadNotSupported.md)
- [foundry_sdk.v2.datasets.errors.DatasetReadNotSupportedParameters](../../../../models/v2/datasets/errors/DatasetReadNotSupportedParameters.md)
- [foundry_sdk.v2.datasets.errors.ReadTableDatasetPermissionDenied](../../../../models/v2/datasets/errors/ReadTableDatasetPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.ReadTableDatasetPermissionDeniedParameters](../../../../models/v2/datasets/errors/ReadTableDatasetPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.errors.ReadTableError](../../../../models/v2/datasets/errors/ReadTableError.md)
- [foundry_sdk.v2.datasets.errors.ReadTableErrorParameters](../../../../models/v2/datasets/errors/ReadTableErrorParameters.md)
- [foundry_sdk.v2.datasets.errors.ReadTableRowLimitExceeded](../../../../models/v2/datasets/errors/ReadTableRowLimitExceeded.md)
- [foundry_sdk.v2.datasets.errors.ReadTableRowLimitExceededParameters](../../../../models/v2/datasets/errors/ReadTableRowLimitExceededParameters.md)
- [foundry_sdk.v2.datasets.errors.ReadTableTimeout](../../../../models/v2/datasets/errors/ReadTableTimeout.md)
- [foundry_sdk.v2.datasets.errors.ReadTableTimeoutParameters](../../../../models/v2/datasets/errors/ReadTableTimeoutParameters.md)
- [foundry_sdk.v2.datasets.errors.SchemaNotFound](../../../../models/v2/datasets/errors/SchemaNotFound.md)
- [foundry_sdk.v2.datasets.errors.SchemaNotFoundParameters](../../../../models/v2/datasets/errors/SchemaNotFoundParameters.md)
- [foundry_sdk.v2.datasets.models.TableExportFormat](../../../../models/v2/datasets/models/TableExportFormat.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../../../../models/v2/datasets/models/TransactionRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/Dataset.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](read_table.md)
