# v2.datasets.File.delete


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Deletes a File from a Dataset. By default the file is deleted in a new transaction on the default
branch - `master` for most enrollments. The file will still be visible on historical views.
#### Advanced Usage
See [Datasets Core Concepts](../../../../../pipelines/transactions.md) for details on using branches and transactions.
To **delete a File from a specific Branch** specify the Branch's name as `branchName`. A new delete Transaction
will be created and committed on this branch.
To **delete a File using a manually opened Transaction**, specify the Transaction's resource identifier
as `transactionRid`. The transaction must be of type `DELETE`. This is useful for deleting multiple files in a
single transaction. See [createTransaction](../../../../catalog.md) to
open a transaction.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.Dataset.File.delete`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def delete(self, dataset_rid: core_models.DatasetRid, file_path: core_models.FilePath, *, branch_name: typing.Optional[core_models.BranchName]=None, transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| file_path | core_models.FilePath | required | Value shape and constraints are in its referenced local type definition. |
| branch_name | typing.Optional[core_models.BranchName] | None | The name of the Branch on which to delete the File. Defaults to `master` for most enrollments. |
| transaction_rid | typing.Optional[datasets_models.TransactionRid] | None | The Resource Identifier (RID) of the open delete Transaction on which to delete the File. |
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
| DeleteFilePermissionDenied | Could not delete the File. |
| FileNotFoundOnBranch | The requested file could not be found on the given branch, or the client token does not have access to it. |
| FileNotFoundOnTransactionRange | The requested file could not be found on the given transaction range, or the client token does not have access to it. |
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| InvalidTransactionType | The given transaction type is not valid. Valid transaction types are `SNAPSHOT`, `UPDATE`, `APPEND`, and `DELETE`. |
| OpenTransactionAlreadyExists | A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |
| TransactionNotOpen | The given transaction is not open. |

## Wire request

**method**

```python
'DELETE'
```

**resource_path**

```python
'/v2/datasets/{datasetRid}/files/{filePath}'
```

**query_params**

```python
{'branchName': branch_name, 'transactionRid': transaction_rid}
```

**path_params**

```python
{'datasetRid': dataset_rid, 'filePath': file_path}
```

**header_params**

```python
{}
```

**body**

```python
None
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
{'AbortTransactionPermissionDenied': datasets_errors.AbortTransactionPermissionDenied, 'BranchNotFound': datasets_errors.BranchNotFound, 'CommitTransactionPermissionDenied': datasets_errors.CommitTransactionPermissionDenied, 'CreateTransactionPermissionDenied': datasets_errors.CreateTransactionPermissionDenied, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'DeleteFilePermissionDenied': datasets_errors.DeleteFilePermissionDenied, 'FileNotFoundOnBranch': datasets_errors.FileNotFoundOnBranch, 'FileNotFoundOnTransactionRange': datasets_errors.FileNotFoundOnTransactionRange, 'InvalidBranchName': datasets_errors.InvalidBranchName, 'InvalidParameterCombination': core_errors.InvalidParameterCombination, 'InvalidTransactionType': datasets_errors.InvalidTransactionType, 'OpenTransactionAlreadyExists': datasets_errors.OpenTransactionAlreadyExists, 'TransactionNotFound': datasets_errors.TransactionNotFound, 'TransactionNotOpen': datasets_errors.TransactionNotOpen}
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
- [foundry_sdk.v2.core.errors.InvalidParameterCombination](../../../../models/v2/core/errors/InvalidParameterCombination.md)
- [foundry_sdk.v2.core.errors.InvalidParameterCombinationParameters](../../../../models/v2/core/errors/InvalidParameterCombinationParameters.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.FilePath](../../../../models/v2/core/models/FilePath.md)
- [foundry_sdk.v2.datasets.errors.AbortTransactionPermissionDenied](../../../../models/v2/datasets/errors/AbortTransactionPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.AbortTransactionPermissionDeniedParameters](../../../../models/v2/datasets/errors/AbortTransactionPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFound](../../../../models/v2/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFoundParameters](../../../../models/v2/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.CommitTransactionPermissionDenied](../../../../models/v2/datasets/errors/CommitTransactionPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.CommitTransactionPermissionDeniedParameters](../../../../models/v2/datasets/errors/CommitTransactionPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.errors.CreateTransactionPermissionDenied](../../../../models/v2/datasets/errors/CreateTransactionPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.CreateTransactionPermissionDeniedParameters](../../../../models/v2/datasets/errors/CreateTransactionPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFound](../../../../models/v2/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFoundParameters](../../../../models/v2/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.DeleteFilePermissionDenied](../../../../models/v2/datasets/errors/DeleteFilePermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.DeleteFilePermissionDeniedParameters](../../../../models/v2/datasets/errors/DeleteFilePermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.errors.FileNotFoundOnBranch](../../../../models/v2/datasets/errors/FileNotFoundOnBranch.md)
- [foundry_sdk.v2.datasets.errors.FileNotFoundOnBranchParameters](../../../../models/v2/datasets/errors/FileNotFoundOnBranchParameters.md)
- [foundry_sdk.v2.datasets.errors.FileNotFoundOnTransactionRange](../../../../models/v2/datasets/errors/FileNotFoundOnTransactionRange.md)
- [foundry_sdk.v2.datasets.errors.FileNotFoundOnTransactionRangeParameters](../../../../models/v2/datasets/errors/FileNotFoundOnTransactionRangeParameters.md)
- [foundry_sdk.v2.datasets.errors.InvalidBranchName](../../../../models/v2/datasets/errors/InvalidBranchName.md)
- [foundry_sdk.v2.datasets.errors.InvalidBranchNameParameters](../../../../models/v2/datasets/errors/InvalidBranchNameParameters.md)
- [foundry_sdk.v2.datasets.errors.InvalidTransactionType](../../../../models/v2/datasets/errors/InvalidTransactionType.md)
- [foundry_sdk.v2.datasets.errors.InvalidTransactionTypeParameters](../../../../models/v2/datasets/errors/InvalidTransactionTypeParameters.md)
- [foundry_sdk.v2.datasets.errors.OpenTransactionAlreadyExists](../../../../models/v2/datasets/errors/OpenTransactionAlreadyExists.md)
- [foundry_sdk.v2.datasets.errors.OpenTransactionAlreadyExistsParameters](../../../../models/v2/datasets/errors/OpenTransactionAlreadyExistsParameters.md)
- [foundry_sdk.v2.datasets.errors.TransactionNotFound](../../../../models/v2/datasets/errors/TransactionNotFound.md)
- [foundry_sdk.v2.datasets.errors.TransactionNotFoundParameters](../../../../models/v2/datasets/errors/TransactionNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.TransactionNotOpen](../../../../models/v2/datasets/errors/TransactionNotOpen.md)
- [foundry_sdk.v2.datasets.errors.TransactionNotOpenParameters](../../../../models/v2/datasets/errors/TransactionNotOpenParameters.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../../../../models/v2/datasets/models/TransactionRid.md)
- [foundry_sdk.v2.datasets.models.TransactionStatus](../../../../models/v2/datasets/models/TransactionStatus.md)
- [foundry_sdk.v2.datasets.models.TransactionType](../../../../models/v2/datasets/models/TransactionType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/File.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A dataset branch selects a lineage. A transaction stages writes on that lineage until it is committed or aborted. [Local procedure](../../../../../pipelines/transactions.md).
- Open a transaction on the intended dataset and branch before staging writes; commit it only after validating the staged changes. [Local procedure](../../../../catalog.md).

[Part 1](delete.md)
