# v1.datasets.Dataset.create


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new Dataset. A default branch - `master` for most enrollments - will be created on the Dataset.

## Public Python client route

With a configured `foundry_sdk.v1.FoundryClient` named `client`, call `client.datasets.Dataset.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, *, name: datasets_models.DatasetName, parent_folder_rid: core_models.FolderRid, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.Dataset: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| name | datasets_models.DatasetName | required | Value shape and constraints are in its referenced local type definition. |
| parent_folder_rid | core_models.FolderRid | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

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

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v1/datasets'
```

**query_params**

```python
{}
```

**path_params**

```python
{}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
datasets_models.CreateDatasetRequest(name=name, parent_folder_rid=parent_folder_rid)
```

**response_type**

```python
datasets_models.Dataset
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'BranchAlreadyExists': datasets_errors.BranchAlreadyExists, 'CreateBranchPermissionDenied': datasets_errors.CreateBranchPermissionDenied, 'CreateDatasetPermissionDenied': datasets_errors.CreateDatasetPermissionDenied, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'FolderNotFound': core_errors.FolderNotFound, 'InvalidBranchId': datasets_errors.InvalidBranchId, 'ResourceNameAlreadyExists': core_errors.ResourceNameAlreadyExists, 'TransactionNotCommitted': datasets_errors.TransactionNotCommitted, 'TransactionNotFound': datasets_errors.TransactionNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `datasets_models.Dataset`. Ordinary async return: `typing.Awaitable[datasets_models.Dataset]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | datasets_models.Dataset |
| sync_raw | ApiResponse[datasets_models.Dataset] |
| sync_streaming | StreamingContextManager[datasets_models.Dataset] |
| async_ordinary | typing.Awaitable[datasets_models.Dataset] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.Dataset]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.Dataset]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.errors.FolderNotFound](../../../../models/v1/core/errors/FolderNotFound.md)
- [foundry_sdk.v1.core.errors.FolderNotFoundParameters](../../../../models/v1/core/errors/FolderNotFoundParameters.md)
- [foundry_sdk.v1.core.errors.ResourceNameAlreadyExists](../../../../models/v1/core/errors/ResourceNameAlreadyExists.md)
- [foundry_sdk.v1.core.errors.ResourceNameAlreadyExistsParameters](../../../../models/v1/core/errors/ResourceNameAlreadyExistsParameters.md)
- [foundry_sdk.v1.core.models.FolderRid](../../../../models/v1/core/models/FolderRid.md)
- [foundry_sdk.v1.datasets.errors.BranchAlreadyExists](../../../../models/v1/datasets/errors/BranchAlreadyExists.md)
- [foundry_sdk.v1.datasets.errors.BranchAlreadyExistsParameters](../../../../models/v1/datasets/errors/BranchAlreadyExistsParameters.md)
- [foundry_sdk.v1.datasets.errors.CreateBranchPermissionDenied](../../../../models/v1/datasets/errors/CreateBranchPermissionDenied.md)
- [foundry_sdk.v1.datasets.errors.CreateBranchPermissionDeniedParameters](../../../../models/v1/datasets/errors/CreateBranchPermissionDeniedParameters.md)
- [foundry_sdk.v1.datasets.errors.CreateDatasetPermissionDenied](../../../../models/v1/datasets/errors/CreateDatasetPermissionDenied.md)
- [foundry_sdk.v1.datasets.errors.CreateDatasetPermissionDeniedParameters](../../../../models/v1/datasets/errors/CreateDatasetPermissionDeniedParameters.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFound](../../../../models/v1/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFoundParameters](../../../../models/v1/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.InvalidBranchId](../../../../models/v1/datasets/errors/InvalidBranchId.md)
- [foundry_sdk.v1.datasets.errors.InvalidBranchIdParameters](../../../../models/v1/datasets/errors/InvalidBranchIdParameters.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotCommitted](../../../../models/v1/datasets/errors/TransactionNotCommitted.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotCommittedParameters](../../../../models/v1/datasets/errors/TransactionNotCommittedParameters.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotFound](../../../../models/v1/datasets/errors/TransactionNotFound.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotFoundParameters](../../../../models/v1/datasets/errors/TransactionNotFoundParameters.md)
- [foundry_sdk.v1.datasets.models.BranchId](../../../../models/v1/datasets/models/BranchId.md)
- [foundry_sdk.v1.datasets.models.CreateDatasetRequest](../../../../models/v1/datasets/models/CreateDatasetRequest.md)
- [foundry_sdk.v1.datasets.models.Dataset](../../../../models/v1/datasets/models/Dataset.md)
- [foundry_sdk.v1.datasets.models.DatasetName](../../../../models/v1/datasets/models/DatasetName.md)
- [foundry_sdk.v1.datasets.models.DatasetRid](../../../../models/v1/datasets/models/DatasetRid.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](../../../../models/v1/datasets/models/TransactionRid.md)
- [foundry_sdk.v1.datasets.models.TransactionStatus](../../../../models/v1/datasets/models/TransactionStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/datasets/Dataset.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
