# v1.datasets.Dataset.replace_schema


API v1; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Puts a Schema on an existing Dataset and Branch.

## SDK invocation contract

```python
def replace_schema(self, dataset_rid: datasets_models.DatasetRid, body: typing.Any, *, branch_id: typing.Optional[datasets_models.BranchId]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | datasets_models.DatasetRid | required | The RID of the Dataset on which to put the Schema. |
| body | typing.Any | required | Body of the request |
| branch_id | typing.Optional[datasets_models.BranchId] | None | The ID of the Branch on which to put the Schema. |
| preview | typing.Optional[core_models.PreviewMode] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

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

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v1/datasets/{datasetRid}/schema'
```

**query_params**

```python
{'branchId': branch_id, 'preview': preview}
```

**path_params**

```python
{'datasetRid': dataset_rid}
```

**header_params**

```python
{'Content-Type': 'application/json'}
```

**body**

```python
body
```

**response_type**

```python
None
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AbortTransactionPermissionDenied': datasets_errors.AbortTransactionPermissionDenied, 'BranchNotFound': datasets_errors.BranchNotFound, 'CommitTransactionPermissionDenied': datasets_errors.CommitTransactionPermissionDenied, 'CreateTransactionPermissionDenied': datasets_errors.CreateTransactionPermissionDenied, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'FileNotFoundOnTransactionRange': datasets_errors.FileNotFoundOnTransactionRange, 'InvalidBranchId': datasets_errors.InvalidBranchId, 'InvalidTransactionType': datasets_errors.InvalidTransactionType, 'OpenTransactionAlreadyExists': datasets_errors.OpenTransactionAlreadyExists, 'PutSchemaPermissionDenied': datasets_errors.PutSchemaPermissionDenied, 'TransactionNotFound': datasets_errors.TransactionNotFound, 'TransactionNotOpen': datasets_errors.TransactionNotOpen}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `None`. Ordinary async return: `typing.Awaitable[None]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | None |
| sync_raw | ApiResponse[None] |
| sync_streaming | Not exposed |
| async_ordinary | typing.Awaitable[None] |
| async_raw | Awaitable[AsyncApiResponse[None]] |
| async_streaming | Not exposed |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.models.FilePath](../../../../models/v1/core/models/FilePath.md)
- [foundry_sdk.v1.core.models.PreviewMode](../../../../models/v1/core/models/PreviewMode.md)
- [foundry_sdk.v1.datasets.errors.AbortTransactionPermissionDenied](../../../../models/v1/datasets/errors/AbortTransactionPermissionDenied.md)
- [foundry_sdk.v1.datasets.errors.AbortTransactionPermissionDeniedParameters](../../../../models/v1/datasets/errors/AbortTransactionPermissionDeniedParameters.md)
- [foundry_sdk.v1.datasets.errors.BranchNotFound](../../../../models/v1/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v1.datasets.errors.BranchNotFoundParameters](../../../../models/v1/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.CommitTransactionPermissionDenied](../../../../models/v1/datasets/errors/CommitTransactionPermissionDenied.md)
- [foundry_sdk.v1.datasets.errors.CommitTransactionPermissionDeniedParameters](../../../../models/v1/datasets/errors/CommitTransactionPermissionDeniedParameters.md)
- [foundry_sdk.v1.datasets.errors.CreateTransactionPermissionDenied](../../../../models/v1/datasets/errors/CreateTransactionPermissionDenied.md)
- [foundry_sdk.v1.datasets.errors.CreateTransactionPermissionDeniedParameters](../../../../models/v1/datasets/errors/CreateTransactionPermissionDeniedParameters.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFound](../../../../models/v1/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFoundParameters](../../../../models/v1/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.FileNotFoundOnTransactionRange](../../../../models/v1/datasets/errors/FileNotFoundOnTransactionRange.md)
- [foundry_sdk.v1.datasets.errors.FileNotFoundOnTransactionRangeParameters](../../../../models/v1/datasets/errors/FileNotFoundOnTransactionRangeParameters.md)
- [foundry_sdk.v1.datasets.errors.InvalidBranchId](../../../../models/v1/datasets/errors/InvalidBranchId.md)
- [foundry_sdk.v1.datasets.errors.InvalidBranchIdParameters](../../../../models/v1/datasets/errors/InvalidBranchIdParameters.md)
- [foundry_sdk.v1.datasets.errors.InvalidTransactionType](../../../../models/v1/datasets/errors/InvalidTransactionType.md)
- [foundry_sdk.v1.datasets.errors.InvalidTransactionTypeParameters](../../../../models/v1/datasets/errors/InvalidTransactionTypeParameters.md)
- [foundry_sdk.v1.datasets.errors.OpenTransactionAlreadyExists](../../../../models/v1/datasets/errors/OpenTransactionAlreadyExists.md)
- [foundry_sdk.v1.datasets.errors.OpenTransactionAlreadyExistsParameters](../../../../models/v1/datasets/errors/OpenTransactionAlreadyExistsParameters.md)
- [foundry_sdk.v1.datasets.errors.PutSchemaPermissionDenied](../../../../models/v1/datasets/errors/PutSchemaPermissionDenied.md)
- [foundry_sdk.v1.datasets.errors.PutSchemaPermissionDeniedParameters](../../../../models/v1/datasets/errors/PutSchemaPermissionDeniedParameters.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotFound](../../../../models/v1/datasets/errors/TransactionNotFound.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotFoundParameters](../../../../models/v1/datasets/errors/TransactionNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotOpen](../../../../models/v1/datasets/errors/TransactionNotOpen.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotOpenParameters](../../../../models/v1/datasets/errors/TransactionNotOpenParameters.md)
- [foundry_sdk.v1.datasets.models.BranchId](../../../../models/v1/datasets/models/BranchId.md)
- [foundry_sdk.v1.datasets.models.DatasetRid](../../../../models/v1/datasets/models/DatasetRid.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](../../../../models/v1/datasets/models/TransactionRid.md)
- [foundry_sdk.v1.datasets.models.TransactionStatus](../../../../models/v1/datasets/models/TransactionStatus.md)
- [foundry_sdk.v1.datasets.models.TransactionType](../../../../models/v1/datasets/models/TransactionType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/datasets/Dataset.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](replace_schema.md)
