# v2.datasets.File.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists Files contained in a Dataset. By default files are listed on the latest view of the default
branch - `master` for most enrollments.
#### Advanced Usage
See [Datasets Core Concepts](../../../../../pipelines/transactions.md) for details on using branches and transactions.
To **list files on a specific Branch** specify the Branch's name as `branchName`. This will include the most
recent version of all files since the latest snapshot transaction, or the earliest ancestor transaction of the
branch if there are no snapshot transactions.
To **list files on the resolved view of a transaction** specify the Transaction's resource identifier
as `endTransactionRid`. This will include the most recent version of all files since the latest snapshot
transaction, or the earliest ancestor transaction if there are no snapshot transactions.
To **list files on the resolved view of a range of transactions** specify the the start transaction's resource
identifier as `startTransactionRid` and the end transaction's resource identifier as `endTransactionRid`. This
will include the most recent version of all files since the `startTransactionRid` up to the `endTransactionRid`.
Note that an intermediate snapshot transaction will remove all files from the view. Behavior is undefined when
the start and end transactions do not belong to the same root-to-leaf path.
To **list files on a specific transaction** specify the Transaction's resource identifier as both the
`startTransactionRid` and `endTransactionRid`. This will include only files that were modified as part of that
Transaction.

## SDK invocation contract

```python
def list(self, dataset_rid: core_models.DatasetRid, *, branch_name: typing.Optional[core_models.BranchName]=None, end_transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, path_prefix: typing.Optional[core_models.FilePath]=None, start_transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[datasets_models.File]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| branch_name | typing.Optional[core_models.BranchName] | None | The name of the Branch on which to list Files. Defaults to `master` for most enrollments. |
| end_transaction_rid | typing.Optional[datasets_models.TransactionRid] | None | The Resource Identifier (RID) of the end Transaction. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| path_prefix | typing.Optional[core_models.FilePath] | None | When present returns only files in the dataset whose path starts with this value. If pathPrefix matches a file exactly, returns just that file. |
| start_transaction_rid | typing.Optional[datasets_models.TransactionRid] | None | The Resource Identifier (RID) of the start Transaction. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| InvalidBranchName | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidFilePath | The provided file path is invalid. Check that the path does not start with a leading slash. |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/datasets/{datasetRid}/files'
```

**query_params**

```python
{'branchName': branch_name, 'endTransactionRid': end_transaction_rid, 'pageSize': page_size, 'pageToken': page_token, 'pathPrefix': path_prefix, 'startTransactionRid': start_transaction_rid}
```

**path_params**

```python
{'datasetRid': dataset_rid}
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
datasets_models.ListFilesResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'BranchNotFound': datasets_errors.BranchNotFound, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'InvalidBranchName': datasets_errors.InvalidBranchName, 'InvalidFilePath': core_errors.InvalidFilePath, 'InvalidPageSize': core_errors.InvalidPageSize, 'InvalidParameterCombination': core_errors.InvalidParameterCombination, 'TransactionNotFound': datasets_errors.TransactionNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[datasets_models.File]`. Ordinary async return: `core.AsyncResourceIterator[datasets_models.File]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[datasets_models.File] |
| sync_raw | ApiResponse[datasets_models.ListFilesResponse] |
| sync_streaming | StreamingContextManager[datasets_models.ListFilesResponse] |
| async_ordinary | core.AsyncResourceIterator[datasets_models.File] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.ListFilesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.ListFilesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.errors.InvalidFilePath](../../../../models/v2/core/errors/InvalidFilePath.md)
- [foundry_sdk.v2.core.errors.InvalidFilePathParameters](../../../../models/v2/core/errors/InvalidFilePathParameters.md)
- [foundry_sdk.v2.core.errors.InvalidPageSize](../../../../models/v2/core/errors/InvalidPageSize.md)
- [foundry_sdk.v2.core.errors.InvalidPageSizeParameters](../../../../models/v2/core/errors/InvalidPageSizeParameters.md)
- [foundry_sdk.v2.core.errors.InvalidParameterCombination](../../../../models/v2/core/errors/InvalidParameterCombination.md)
- [foundry_sdk.v2.core.errors.InvalidParameterCombinationParameters](../../../../models/v2/core/errors/InvalidParameterCombinationParameters.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.FilePath](../../../../models/v2/core/models/FilePath.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFound](../../../../models/v2/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFoundParameters](../../../../models/v2/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFound](../../../../models/v2/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFoundParameters](../../../../models/v2/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.InvalidBranchName](../../../../models/v2/datasets/errors/InvalidBranchName.md)
- [foundry_sdk.v2.datasets.errors.InvalidBranchNameParameters](../../../../models/v2/datasets/errors/InvalidBranchNameParameters.md)
- [foundry_sdk.v2.datasets.errors.TransactionNotFound](../../../../models/v2/datasets/errors/TransactionNotFound.md)
- [foundry_sdk.v2.datasets.errors.TransactionNotFoundParameters](../../../../models/v2/datasets/errors/TransactionNotFoundParameters.md)
- [foundry_sdk.v2.datasets.models.File](../../../../models/v2/datasets/models/File.md)
- [foundry_sdk.v2.datasets.models.FileUpdatedTime](../../../../models/v2/datasets/models/FileUpdatedTime.md)
- [foundry_sdk.v2.datasets.models.ListFilesResponse](../../../../models/v2/datasets/models/ListFilesResponse.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../../../../models/v2/datasets/models/TransactionRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/File.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A dataset branch selects a lineage. A transaction stages writes on that lineage until it is committed or aborted. [Local procedure](../../../../../pipelines/transactions.md).

[Part 1](list.md)
