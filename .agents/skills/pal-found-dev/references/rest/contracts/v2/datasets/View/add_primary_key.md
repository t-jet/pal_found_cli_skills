# v2.datasets.View.add_primary_key


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Adds a primary key to a View that does not already have one. Primary keys are treated as
guarantees provided by the creator of the dataset.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.View.add_primary_key`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def add_primary_key(self, view_dataset_rid: core_models.DatasetRid, *, primary_key: datasets_models.ViewPrimaryKey, branch: typing.Optional[core_models.BranchName]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.View: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| view_dataset_rid | core_models.DatasetRid | required | The rid of the View. |
| primary_key | datasets_models.ViewPrimaryKey | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.BranchName] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AddPrimaryKeyPermissionDenied | Could not addPrimaryKey the View. |
| InvalidViewPrimaryKeyColumnType | The type of each referenced column in the primary key must be one of the following: BYTE, SHORT, DECIMAL, INTEGER, LONG, STRING, BOOLEAN, TIMESTAMP or DATE. |
| InvalidViewPrimaryKeyDeletionColumn | The deletion column must be a boolean. |
| NotAllColumnsInPrimaryKeyArePresent | Not all columns in the View's primary key are present in the dataset(s). |
| ViewNotFound | The requested View could not be found. Either the view does not exist, the branch is not valid or the client token does not have access to it. |
| ViewPrimaryKeyCannotBeModified | A primary key already exits. |
| ViewPrimaryKeyDeletionColumnNotInDatasetSchema | The deletion column is not present in the dataset. |
| ViewPrimaryKeyMustContainAtLeastOneColumn | No columns were provided as part of the primary key |
| ViewPrimaryKeyRequiresBackingDatasets | Cannot add a primary key to a View that does not have any backing datasets. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/datasets/views/{viewDatasetRid}/addPrimaryKey'
```

**query_params**

```python
{}
```

**path_params**

```python
{'viewDatasetRid': view_dataset_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
datasets_models.AddPrimaryKeyRequest(branch=branch, primary_key=primary_key)
```

**response_type**

```python
datasets_models.View
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AddPrimaryKeyPermissionDenied': datasets_errors.AddPrimaryKeyPermissionDenied, 'InvalidViewPrimaryKeyColumnType': datasets_errors.InvalidViewPrimaryKeyColumnType, 'InvalidViewPrimaryKeyDeletionColumn': datasets_errors.InvalidViewPrimaryKeyDeletionColumn, 'NotAllColumnsInPrimaryKeyArePresent': datasets_errors.NotAllColumnsInPrimaryKeyArePresent, 'ViewNotFound': datasets_errors.ViewNotFound, 'ViewPrimaryKeyCannotBeModified': datasets_errors.ViewPrimaryKeyCannotBeModified, 'ViewPrimaryKeyDeletionColumnNotInDatasetSchema': datasets_errors.ViewPrimaryKeyDeletionColumnNotInDatasetSchema, 'ViewPrimaryKeyMustContainAtLeastOneColumn': datasets_errors.ViewPrimaryKeyMustContainAtLeastOneColumn, 'ViewPrimaryKeyRequiresBackingDatasets': datasets_errors.ViewPrimaryKeyRequiresBackingDatasets}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `datasets_models.View`. Ordinary async return: `typing.Awaitable[datasets_models.View]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | datasets_models.View |
| sync_raw | ApiResponse[datasets_models.View] |
| sync_streaming | StreamingContextManager[datasets_models.View] |
| async_ordinary | typing.Awaitable[datasets_models.View] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.View]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.View]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.SchemaFieldType](../../../../models/v2/core/models/SchemaFieldType.md)
- [foundry_sdk.v2.datasets.errors.AddPrimaryKeyPermissionDenied](../../../../models/v2/datasets/errors/AddPrimaryKeyPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.AddPrimaryKeyPermissionDeniedParameters](../../../../models/v2/datasets/errors/AddPrimaryKeyPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.errors.InvalidViewPrimaryKeyColumnType](../../../../models/v2/datasets/errors/InvalidViewPrimaryKeyColumnType.md)
- [foundry_sdk.v2.datasets.errors.InvalidViewPrimaryKeyColumnTypeParameters](../../../../models/v2/datasets/errors/InvalidViewPrimaryKeyColumnTypeParameters.md)
- [foundry_sdk.v2.datasets.errors.InvalidViewPrimaryKeyDeletionColumn](../../../../models/v2/datasets/errors/InvalidViewPrimaryKeyDeletionColumn.md)
- [foundry_sdk.v2.datasets.errors.InvalidViewPrimaryKeyDeletionColumnParameters](../../../../models/v2/datasets/errors/InvalidViewPrimaryKeyDeletionColumnParameters.md)
- [foundry_sdk.v2.datasets.errors.NotAllColumnsInPrimaryKeyArePresent](../../../../models/v2/datasets/errors/NotAllColumnsInPrimaryKeyArePresent.md)
- [foundry_sdk.v2.datasets.errors.NotAllColumnsInPrimaryKeyArePresentParameters](../../../../models/v2/datasets/errors/NotAllColumnsInPrimaryKeyArePresentParameters.md)
- [foundry_sdk.v2.datasets.errors.ViewNotFound](../../../../models/v2/datasets/errors/ViewNotFound.md)
- [foundry_sdk.v2.datasets.errors.ViewNotFoundParameters](../../../../models/v2/datasets/errors/ViewNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyCannotBeModified](../../../../models/v2/datasets/errors/ViewPrimaryKeyCannotBeModified.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyCannotBeModifiedParameters](../../../../models/v2/datasets/errors/ViewPrimaryKeyCannotBeModifiedParameters.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyDeletionColumnNotInDatasetSchema](../../../../models/v2/datasets/errors/ViewPrimaryKeyDeletionColumnNotInDatasetSchema.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyDeletionColumnNotInDatasetSchemaParameters](../../../../models/v2/datasets/errors/ViewPrimaryKeyDeletionColumnNotInDatasetSchemaParameters.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyMustContainAtLeastOneColumn](../../../../models/v2/datasets/errors/ViewPrimaryKeyMustContainAtLeastOneColumn.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyMustContainAtLeastOneColumnParameters](../../../../models/v2/datasets/errors/ViewPrimaryKeyMustContainAtLeastOneColumnParameters.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyRequiresBackingDatasets](../../../../models/v2/datasets/errors/ViewPrimaryKeyRequiresBackingDatasets.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyRequiresBackingDatasetsParameters](../../../../models/v2/datasets/errors/ViewPrimaryKeyRequiresBackingDatasetsParameters.md)
- [foundry_sdk.v2.datasets.models.AddPrimaryKeyRequest](../../../../models/v2/datasets/models/AddPrimaryKeyRequest.md)
- [foundry_sdk.v2.datasets.models.DatasetName](../../../../models/v2/datasets/models/DatasetName.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyLatestWinsResolutionStrategy](../../../../models/v2/datasets/models/PrimaryKeyLatestWinsResolutionStrategy.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyResolutionDuplicate](../../../../models/v2/datasets/models/PrimaryKeyResolutionDuplicate.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyResolutionStrategy](../../../../models/v2/datasets/models/PrimaryKeyResolutionStrategy.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyResolutionUnique](../../../../models/v2/datasets/models/PrimaryKeyResolutionUnique.md)
- [foundry_sdk.v2.datasets.models.View](../../../../models/v2/datasets/models/View.md)
- [foundry_sdk.v2.datasets.models.ViewBackingDataset](../../../../models/v2/datasets/models/ViewBackingDataset.md)
- [foundry_sdk.v2.datasets.models.ViewPrimaryKey](../../../../models/v2/datasets/models/ViewPrimaryKey.md)
- [foundry_sdk.v2.datasets.models.ViewPrimaryKeyResolution](../../../../models/v2/datasets/models/ViewPrimaryKeyResolution.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/View.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](add_primary_key.md)
