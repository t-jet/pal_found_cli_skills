# v1.datasets.File.get


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets metadata about a File contained in a Dataset. By default this retrieves the file's metadata from the latest
view of the default branch - `master` for most enrollments.

#### Advanced Usage

See [Datasets Core Concepts](../../../../../pipelines/transactions.md) for details on using branches and transactions.

To **get a file's metadata from a specific Branch** specify the Branch's identifier as `branchId`. This will
retrieve metadata for the most recent version of the file since the latest snapshot transaction, or the earliest
ancestor transaction of the branch if there are no snapshot transactions.

To **get a file's metadata from the resolved view of a transaction** specify the Transaction's resource identifier
as `endTransactionRid`. This will retrieve metadata for the most recent version of the file since the latest snapshot
transaction, or the earliest ancestor transaction if there are no snapshot transactions.

To **get a file's metadata from the resolved view of a range of transactions** specify the the start transaction's
resource identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`.
This will retrieve metadata for the most recent version of the file since the `startTransactionRid` up to the
`endTransactionRid`. Behavior is undefined when the start and end transactions do not belong to the same root-to-leaf path.

To **get a file's metadata from a specific transaction** specify the Transaction's resource identifier as both the
`startTransactionRid` and `endTransactionRid`.

## Public Python client route

With a configured `foundry_sdk.v1.FoundryClient` named `client`, call `client.datasets.Dataset.File.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, dataset_rid: datasets_models.DatasetRid, file_path: core_models.FilePath, *, branch_id: typing.Optional[datasets_models.BranchId]=None, end_transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, start_transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.File: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | datasets_models.DatasetRid | required | The Resource Identifier (RID) of the Dataset that contains the File. |
| file_path | core_models.FilePath | required | The File's path within the Dataset. |
| branch_id | typing.Optional[datasets_models.BranchId] | None | The identifier (name) of the Branch that contains the File. Defaults to `master` for most enrollments. |
| end_transaction_rid | typing.Optional[datasets_models.TransactionRid] | None | The Resource Identifier (RID) of the end Transaction. |
| start_transaction_rid | typing.Optional[datasets_models.TransactionRid] | None | The Resource Identifier (RID) of the start Transaction. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| FileNotFoundOnBranch | The requested file could not be found on the given branch, or the client token does not have access to it. |
| FileNotFoundOnTransactionRange | The requested file could not be found on the given transaction range, or the client token does not have access to it. |
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v1/datasets/{datasetRid}/files/{filePath}'
```

**query_params**

```python
{'branchId': branch_id, 'endTransactionRid': end_transaction_rid, 'startTransactionRid': start_transaction_rid}
```

**path_params**

```python
{'datasetRid': dataset_rid, 'filePath': file_path}
```

**header_params**

```python
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
datasets_models.File
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'BranchNotFound': datasets_errors.BranchNotFound, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'FileNotFoundOnBranch': datasets_errors.FileNotFoundOnBranch, 'FileNotFoundOnTransactionRange': datasets_errors.FileNotFoundOnTransactionRange, 'InvalidBranchId': datasets_errors.InvalidBranchId, 'InvalidParameterCombination': core_errors.InvalidParameterCombination, 'TransactionNotFound': datasets_errors.TransactionNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `datasets_models.File`. Ordinary async return: `typing.Awaitable[datasets_models.File]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | datasets_models.File |
| sync_raw | ApiResponse[datasets_models.File] |
| sync_streaming | StreamingContextManager[datasets_models.File] |
| async_ordinary | typing.Awaitable[datasets_models.File] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.File]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.File]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.errors.InvalidParameterCombination](../../../../models/v1/core/errors/InvalidParameterCombination.md)
- [foundry_sdk.v1.core.errors.InvalidParameterCombinationParameters](../../../../models/v1/core/errors/InvalidParameterCombinationParameters.md)
- [foundry_sdk.v1.core.models.FilePath](../../../../models/v1/core/models/FilePath.md)
- [foundry_sdk.v1.datasets.errors.BranchNotFound](../../../../models/v1/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v1.datasets.errors.BranchNotFoundParameters](../../../../models/v1/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFound](../../../../models/v1/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFoundParameters](../../../../models/v1/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.FileNotFoundOnBranch](../../../../models/v1/datasets/errors/FileNotFoundOnBranch.md)
- [foundry_sdk.v1.datasets.errors.FileNotFoundOnBranchParameters](../../../../models/v1/datasets/errors/FileNotFoundOnBranchParameters.md)
- [foundry_sdk.v1.datasets.errors.FileNotFoundOnTransactionRange](../../../../models/v1/datasets/errors/FileNotFoundOnTransactionRange.md)
- [foundry_sdk.v1.datasets.errors.FileNotFoundOnTransactionRangeParameters](../../../../models/v1/datasets/errors/FileNotFoundOnTransactionRangeParameters.md)
- [foundry_sdk.v1.datasets.errors.InvalidBranchId](../../../../models/v1/datasets/errors/InvalidBranchId.md)
- [foundry_sdk.v1.datasets.errors.InvalidBranchIdParameters](../../../../models/v1/datasets/errors/InvalidBranchIdParameters.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotFound](../../../../models/v1/datasets/errors/TransactionNotFound.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotFoundParameters](../../../../models/v1/datasets/errors/TransactionNotFoundParameters.md)
- [foundry_sdk.v1.datasets.models.BranchId](../../../../models/v1/datasets/models/BranchId.md)
- [foundry_sdk.v1.datasets.models.DatasetRid](../../../../models/v1/datasets/models/DatasetRid.md)
- [foundry_sdk.v1.datasets.models.File](../../../../models/v1/datasets/models/File.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](../../../../models/v1/datasets/models/TransactionRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/datasets/File.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A dataset branch selects a lineage. A transaction stages writes on that lineage until it is committed or aborted. [Local procedure](../../../../../pipelines/transactions.md).

[Part 1](get.md)
