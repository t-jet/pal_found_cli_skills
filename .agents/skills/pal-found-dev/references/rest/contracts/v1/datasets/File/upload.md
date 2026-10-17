# v1.datasets.File.upload


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Uploads a File to an existing Dataset.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.

By default the file is uploaded to a new transaction on the default branch - `master` for most enrollments.
If the file already exists only the most recent version will be visible in the updated view.

#### Advanced Usage

See [Datasets Core Concepts](../../../../../pipelines/transactions.md) for details on using branches and transactions.

To **upload a file to a specific Branch** specify the Branch's identifier as `branchId`. A new transaction will
be created and committed on this branch. By default the TransactionType will be `UPDATE`, to override this
default specify `transactionType` in addition to `branchId`.
See [createBranch](../../../../catalog.md) to create a custom branch.

To **upload a file on a manually opened transaction** specify the Transaction's resource identifier as
`transactionRid`. This is useful for uploading multiple files in a single transaction.
See [createTransaction](../../../../catalog.md) to open a transaction.

## Public Python client route

With a configured `foundry_sdk.v1.FoundryClient` named `client`, call `client.datasets.Dataset.File.upload`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def upload(self, dataset_rid: datasets_models.DatasetRid, body: bytes, *, file_path: core_models.FilePath, branch_id: typing.Optional[datasets_models.BranchId]=None, transaction_rid: typing.Optional[datasets_models.TransactionRid]=None, transaction_type: typing.Optional[datasets_models.TransactionType]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.File: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | datasets_models.DatasetRid | required | The Resource Identifier (RID) of the Dataset on which to upload the File. |
| body | bytes | required | Body of the request |
| file_path | core_models.FilePath | required | The File's path within the Dataset. |
| branch_id | typing.Optional[datasets_models.BranchId] | None | The identifier (name) of the Branch on which to upload the File. Defaults to `master` for most enrollments. |
| transaction_rid | typing.Optional[datasets_models.TransactionRid] | None | The Resource Identifier (RID) of the open Transaction on which to upload the File. |
| transaction_type | typing.Optional[datasets_models.TransactionType] | None | The type of the Transaction to create when using branchId. Defaults to `UPDATE`. |
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
| FileAlreadyExists | The given file path already exists in the dataset and transaction. |
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| InvalidFilePath | The provided file path is not valid. |
| InvalidParameterCombination | The given parameters are individually valid but cannot be used in the given combination. |
| OpenTransactionAlreadyExists | A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |
| TransactionNotOpen | The given transaction is not open. |
| UploadFilePermissionDenied | The provided token does not have permission to upload the given file to the given dataset and transaction. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v1/datasets/{datasetRid}/files:upload'
```

**query_params**

```python
{'filePath': file_path, 'branchId': branch_id, 'transactionRid': transaction_rid, 'transactionType': transaction_type}
```

**path_params**

```python
{'datasetRid': dataset_rid}
```

**header_params**

```python
{'Content-Type': '*/*', 'Accept': 'application/json'}
```

**body**

```python
body
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
{'AbortTransactionPermissionDenied': datasets_errors.AbortTransactionPermissionDenied, 'BranchNotFound': datasets_errors.BranchNotFound, 'CommitTransactionPermissionDenied': datasets_errors.CommitTransactionPermissionDenied, 'CreateTransactionPermissionDenied': datasets_errors.CreateTransactionPermissionDenied, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'FileAlreadyExists': datasets_errors.FileAlreadyExists, 'InvalidBranchId': datasets_errors.InvalidBranchId, 'InvalidFilePath': core_errors.InvalidFilePath, 'InvalidParameterCombination': core_errors.InvalidParameterCombination, 'OpenTransactionAlreadyExists': datasets_errors.OpenTransactionAlreadyExists, 'TransactionNotFound': datasets_errors.TransactionNotFound, 'TransactionNotOpen': datasets_errors.TransactionNotOpen, 'UploadFilePermissionDenied': datasets_errors.UploadFilePermissionDenied}
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
- [foundry_sdk.v1.core.errors.InvalidFilePath](../../../../models/v1/core/errors/InvalidFilePath.md)
- [foundry_sdk.v1.core.errors.InvalidFilePathParameters](../../../../models/v1/core/errors/InvalidFilePathParameters.md)
- [foundry_sdk.v1.core.errors.InvalidParameterCombination](../../../../models/v1/core/errors/InvalidParameterCombination.md)
- [foundry_sdk.v1.core.errors.InvalidParameterCombinationParameters](../../../../models/v1/core/errors/InvalidParameterCombinationParameters.md)
- [foundry_sdk.v1.core.models.FilePath](../../../../models/v1/core/models/FilePath.md)
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
- [foundry_sdk.v1.datasets.errors.FileAlreadyExists](../../../../models/v1/datasets/errors/FileAlreadyExists.md)
- [foundry_sdk.v1.datasets.errors.FileAlreadyExistsParameters](../../../../models/v1/datasets/errors/FileAlreadyExistsParameters.md)
- [foundry_sdk.v1.datasets.errors.InvalidBranchId](../../../../models/v1/datasets/errors/InvalidBranchId.md)
- [foundry_sdk.v1.datasets.errors.InvalidBranchIdParameters](../../../../models/v1/datasets/errors/InvalidBranchIdParameters.md)
- [foundry_sdk.v1.datasets.errors.OpenTransactionAlreadyExists](../../../../models/v1/datasets/errors/OpenTransactionAlreadyExists.md)
- [foundry_sdk.v1.datasets.errors.OpenTransactionAlreadyExistsParameters](../../../../models/v1/datasets/errors/OpenTransactionAlreadyExistsParameters.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotFound](../../../../models/v1/datasets/errors/TransactionNotFound.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotFoundParameters](../../../../models/v1/datasets/errors/TransactionNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotOpen](../../../../models/v1/datasets/errors/TransactionNotOpen.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotOpenParameters](../../../../models/v1/datasets/errors/TransactionNotOpenParameters.md)
- [foundry_sdk.v1.datasets.errors.UploadFilePermissionDenied](../../../../models/v1/datasets/errors/UploadFilePermissionDenied.md)
- [foundry_sdk.v1.datasets.errors.UploadFilePermissionDeniedParameters](../../../../models/v1/datasets/errors/UploadFilePermissionDeniedParameters.md)
- [foundry_sdk.v1.datasets.models.BranchId](../../../../models/v1/datasets/models/BranchId.md)
- [foundry_sdk.v1.datasets.models.DatasetRid](../../../../models/v1/datasets/models/DatasetRid.md)
- [foundry_sdk.v1.datasets.models.File](../../../../models/v1/datasets/models/File.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](../../../../models/v1/datasets/models/TransactionRid.md)
- [foundry_sdk.v1.datasets.models.TransactionStatus](../../../../models/v1/datasets/models/TransactionStatus.md)
- [foundry_sdk.v1.datasets.models.TransactionType](../../../../models/v1/datasets/models/TransactionType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/datasets/File.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A dataset branch selects a lineage. A transaction stages writes on that lineage until it is committed or aborted. [Local procedure](../../../../../pipelines/transactions.md).
- Create a branch on the intended dataset before writing to a non-default branch; use the matching version's Branch.create contract. [Local procedure](../../../../catalog.md).

[Part 1](upload.md)
