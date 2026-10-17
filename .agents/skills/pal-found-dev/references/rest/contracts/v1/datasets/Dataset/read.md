# v1.datasets.Dataset.read


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets the content of a dataset as a table in the specified format.

This endpoint currently does not support views (virtual datasets composed of other datasets). For more information, refer to the [views documentation](../../../../v2/datasets/index.md).

## Public Python client route

With a configured `foundry_sdk.v1.FoundryClient` named `client`, call `client.datasets.Dataset.read`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def read(self, dataset_rid: datasets_models.DatasetRid, *, format: datasets_models.TableExportFormat, branch_id: typing.Optional[datasets_models.BranchId]=None, columns: typing.Optional[typing.List[str]]=None, end_transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, row_limit: typing.Optional[int]=None, start_transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> bytes: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | datasets_models.DatasetRid | required | The RID of the Dataset. |
| format | datasets_models.TableExportFormat | required | The export format. Must be `ARROW` or `CSV`. |
| branch_id | typing.Optional[datasets_models.BranchId] | None | The identifier (name) of the Branch. |
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
| ReadTablePermissionDenied | The provided token does not have permission to read the given dataset as a table. |
| SchemaNotFound | A schema could not be found for the given dataset and branch, or the client token does not have access to it. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v1/datasets/{datasetRid}/readTable'
```

**query_params**

```python
{'format': format, 'branchId': branch_id, 'columns': columns, 'endTransactionRid': end_transaction_rid, 'rowLimit': row_limit, 'startTransactionRid': start_transaction_rid}
```

**path_params**

```python
{'datasetRid': dataset_rid}
```

**header_params**

```python
{'Accept': '*/*'}
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
{'ColumnTypesNotSupported': datasets_errors.ColumnTypesNotSupported, 'DatasetReadNotSupported': datasets_errors.DatasetReadNotSupported, 'InvalidParameterCombination': core_errors.InvalidParameterCombination, 'ReadTablePermissionDenied': datasets_errors.ReadTablePermissionDenied, 'SchemaNotFound': datasets_errors.SchemaNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `bytes`. Ordinary async return: `typing.Awaitable[bytes]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | bytes |
| sync_raw | ApiResponse[bytes] |
| sync_streaming | StreamingContextManager[bytes] |
| async_ordinary | typing.Awaitable[bytes] |
| async_raw | Awaitable[AsyncApiResponse[bytes]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[bytes]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.errors.InvalidParameterCombination](../../../../models/v1/core/errors/InvalidParameterCombination.md)
- [foundry_sdk.v1.core.errors.InvalidParameterCombinationParameters](../../../../models/v1/core/errors/InvalidParameterCombinationParameters.md)
- [foundry_sdk.v1.datasets.errors.ColumnTypesNotSupported](../../../../models/v1/datasets/errors/ColumnTypesNotSupported.md)
- [foundry_sdk.v1.datasets.errors.ColumnTypesNotSupportedParameters](../../../../models/v1/datasets/errors/ColumnTypesNotSupportedParameters.md)
- [foundry_sdk.v1.datasets.errors.DatasetReadNotSupported](../../../../models/v1/datasets/errors/DatasetReadNotSupported.md)
- [foundry_sdk.v1.datasets.errors.DatasetReadNotSupportedParameters](../../../../models/v1/datasets/errors/DatasetReadNotSupportedParameters.md)
- [foundry_sdk.v1.datasets.errors.ReadTablePermissionDenied](../../../../models/v1/datasets/errors/ReadTablePermissionDenied.md)
- [foundry_sdk.v1.datasets.errors.ReadTablePermissionDeniedParameters](../../../../models/v1/datasets/errors/ReadTablePermissionDeniedParameters.md)
- [foundry_sdk.v1.datasets.errors.SchemaNotFound](../../../../models/v1/datasets/errors/SchemaNotFound.md)
- [foundry_sdk.v1.datasets.errors.SchemaNotFoundParameters](../../../../models/v1/datasets/errors/SchemaNotFoundParameters.md)
- [foundry_sdk.v1.datasets.models.BranchId](../../../../models/v1/datasets/models/BranchId.md)
- [foundry_sdk.v1.datasets.models.DatasetRid](../../../../models/v1/datasets/models/DatasetRid.md)
- [foundry_sdk.v1.datasets.models.TableExportFormat](../../../../models/v1/datasets/models/TableExportFormat.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](../../../../models/v1/datasets/models/TransactionRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/datasets/Dataset.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A View is a virtual dataset backed by other datasets. This read endpoint does not support Views; choose a supported backing dataset. [Local procedure](../../../../v2/datasets/index.md).

[Part 1](read.md)
