# v2.datasets.View.create


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Create a new View.

## SDK invocation contract

```python
def create(self, *, backing_datasets: typing.List[datasets_models.ViewBackingDataset], parent_folder_rid: filesystem_models.FolderRid, view_name: datasets_models.DatasetName, branch: typing.Optional[core_models.BranchName]=None, primary_key: typing.Optional[datasets_models.ViewPrimaryKey]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.View: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| backing_datasets | typing.List[datasets_models.ViewBackingDataset] | required | Value shape and constraints are in its referenced local type definition. |
| parent_folder_rid | filesystem_models.FolderRid | required | Value shape and constraints are in its referenced local type definition. |
| view_name | datasets_models.DatasetName | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.BranchName] | None | The branch name of the View. If not specified, defaults to `master` for most enrollments. |
| primary_key | typing.Optional[datasets_models.ViewPrimaryKey] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateDatasetPermissionDenied | The provided token does not have permission to create a dataset in this folder. |
| CreateViewPermissionDenied | Could not create the View. |
| FolderNotFound | The given Folder could not be found. |
| InputBackingDatasetNotInOutputViewProject | One or more backing datasets do not live in the same project as the view. Add the missing datasets as project resource references to the view's project using the Filesystem API, or move them into the view's project, and then retry. |
| InvalidDisplayName | The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters. |
| InvalidViewBackingDataset | Either you do not have access to one or more of the backing datasets or it does not exist. |
| InvalidViewPrimaryKeyColumnType | The type of each referenced column in the primary key must be one of the following: BYTE, SHORT, DECIMAL, INTEGER, LONG, STRING, BOOLEAN, TIMESTAMP or DATE. |
| InvalidViewPrimaryKeyDeletionColumn | The deletion column must be a boolean. |
| NotAllColumnsInPrimaryKeyArePresent | Not all columns in the View's primary key are present in the dataset(s). |
| NotAuthorizedToDeclassifyMarkings | The caller does not have DECLASSIFY permission on these markings or the markings do not exist. |
| ResourceNameAlreadyExists | The provided resource name is already in use by another resource in the same folder. |
| ViewDatasetCleanupFailed | Failed to delete dataset following View creation failure. |
| ViewNotFound | The requested View could not be found. Either the view does not exist, the branch is not valid or the client token does not have access to it. |
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
'/v2/datasets/views'
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
datasets_models.CreateViewRequest(parent_folder_rid=parent_folder_rid, view_name=view_name, backing_datasets=backing_datasets, branch=branch, primary_key=primary_key)
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
{'CreateDatasetPermissionDenied': datasets_errors.CreateDatasetPermissionDenied, 'CreateViewPermissionDenied': datasets_errors.CreateViewPermissionDenied, 'FolderNotFound': filesystem_errors.FolderNotFound, 'InputBackingDatasetNotInOutputViewProject': datasets_errors.InputBackingDatasetNotInOutputViewProject, 'InvalidDisplayName': filesystem_errors.InvalidDisplayName, 'InvalidViewBackingDataset': datasets_errors.InvalidViewBackingDataset, 'InvalidViewPrimaryKeyColumnType': datasets_errors.InvalidViewPrimaryKeyColumnType, 'InvalidViewPrimaryKeyDeletionColumn': datasets_errors.InvalidViewPrimaryKeyDeletionColumn, 'NotAllColumnsInPrimaryKeyArePresent': datasets_errors.NotAllColumnsInPrimaryKeyArePresent, 'NotAuthorizedToDeclassifyMarkings': core_errors.NotAuthorizedToDeclassifyMarkings, 'ResourceNameAlreadyExists': filesystem_errors.ResourceNameAlreadyExists, 'ViewDatasetCleanupFailed': datasets_errors.ViewDatasetCleanupFailed, 'ViewNotFound': datasets_errors.ViewNotFound, 'ViewPrimaryKeyDeletionColumnNotInDatasetSchema': datasets_errors.ViewPrimaryKeyDeletionColumnNotInDatasetSchema, 'ViewPrimaryKeyMustContainAtLeastOneColumn': datasets_errors.ViewPrimaryKeyMustContainAtLeastOneColumn, 'ViewPrimaryKeyRequiresBackingDatasets': datasets_errors.ViewPrimaryKeyRequiresBackingDatasets}
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
- [foundry_sdk.v2.core.errors.NotAuthorizedToDeclassifyMarkings](../../../../models/v2/core/errors/NotAuthorizedToDeclassifyMarkings.md)
- [foundry_sdk.v2.core.errors.NotAuthorizedToDeclassifyMarkingsParameters](../../../../models/v2/core/errors/NotAuthorizedToDeclassifyMarkingsParameters.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.SchemaFieldType](../../../../models/v2/core/models/SchemaFieldType.md)
- [foundry_sdk.v2.datasets.errors.CreateDatasetPermissionDenied](../../../../models/v2/datasets/errors/CreateDatasetPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.CreateDatasetPermissionDeniedParameters](../../../../models/v2/datasets/errors/CreateDatasetPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.errors.CreateViewPermissionDenied](../../../../models/v2/datasets/errors/CreateViewPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.CreateViewPermissionDeniedParameters](../../../../models/v2/datasets/errors/CreateViewPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.errors.InputBackingDatasetNotInOutputViewProject](../../../../models/v2/datasets/errors/InputBackingDatasetNotInOutputViewProject.md)
- [foundry_sdk.v2.datasets.errors.InputBackingDatasetNotInOutputViewProjectParameters](../../../../models/v2/datasets/errors/InputBackingDatasetNotInOutputViewProjectParameters.md)
- [foundry_sdk.v2.datasets.errors.InvalidViewBackingDataset](../../../../models/v2/datasets/errors/InvalidViewBackingDataset.md)
- [foundry_sdk.v2.datasets.errors.InvalidViewBackingDatasetParameters](../../../../models/v2/datasets/errors/InvalidViewBackingDatasetParameters.md)
- [foundry_sdk.v2.datasets.errors.InvalidViewPrimaryKeyColumnType](../../../../models/v2/datasets/errors/InvalidViewPrimaryKeyColumnType.md)
- [foundry_sdk.v2.datasets.errors.InvalidViewPrimaryKeyColumnTypeParameters](../../../../models/v2/datasets/errors/InvalidViewPrimaryKeyColumnTypeParameters.md)
- [foundry_sdk.v2.datasets.errors.InvalidViewPrimaryKeyDeletionColumn](../../../../models/v2/datasets/errors/InvalidViewPrimaryKeyDeletionColumn.md)
- [foundry_sdk.v2.datasets.errors.InvalidViewPrimaryKeyDeletionColumnParameters](../../../../models/v2/datasets/errors/InvalidViewPrimaryKeyDeletionColumnParameters.md)
- [foundry_sdk.v2.datasets.errors.NotAllColumnsInPrimaryKeyArePresent](../../../../models/v2/datasets/errors/NotAllColumnsInPrimaryKeyArePresent.md)
- [foundry_sdk.v2.datasets.errors.NotAllColumnsInPrimaryKeyArePresentParameters](../../../../models/v2/datasets/errors/NotAllColumnsInPrimaryKeyArePresentParameters.md)
- [foundry_sdk.v2.datasets.errors.ViewDatasetCleanupFailed](../../../../models/v2/datasets/errors/ViewDatasetCleanupFailed.md)
- [foundry_sdk.v2.datasets.errors.ViewDatasetCleanupFailedParameters](../../../../models/v2/datasets/errors/ViewDatasetCleanupFailedParameters.md)
- [foundry_sdk.v2.datasets.errors.ViewNotFound](../../../../models/v2/datasets/errors/ViewNotFound.md)
- [foundry_sdk.v2.datasets.errors.ViewNotFoundParameters](../../../../models/v2/datasets/errors/ViewNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyDeletionColumnNotInDatasetSchema](../../../../models/v2/datasets/errors/ViewPrimaryKeyDeletionColumnNotInDatasetSchema.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyDeletionColumnNotInDatasetSchemaParameters](../../../../models/v2/datasets/errors/ViewPrimaryKeyDeletionColumnNotInDatasetSchemaParameters.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyMustContainAtLeastOneColumn](../../../../models/v2/datasets/errors/ViewPrimaryKeyMustContainAtLeastOneColumn.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyMustContainAtLeastOneColumnParameters](../../../../models/v2/datasets/errors/ViewPrimaryKeyMustContainAtLeastOneColumnParameters.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyRequiresBackingDatasets](../../../../models/v2/datasets/errors/ViewPrimaryKeyRequiresBackingDatasets.md)
- [foundry_sdk.v2.datasets.errors.ViewPrimaryKeyRequiresBackingDatasetsParameters](../../../../models/v2/datasets/errors/ViewPrimaryKeyRequiresBackingDatasetsParameters.md)
- [foundry_sdk.v2.datasets.models.CreateViewRequest](../../../../models/v2/datasets/models/CreateViewRequest.md)
- [foundry_sdk.v2.datasets.models.DatasetName](../../../../models/v2/datasets/models/DatasetName.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyLatestWinsResolutionStrategy](../../../../models/v2/datasets/models/PrimaryKeyLatestWinsResolutionStrategy.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyResolutionDuplicate](../../../../models/v2/datasets/models/PrimaryKeyResolutionDuplicate.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyResolutionStrategy](../../../../models/v2/datasets/models/PrimaryKeyResolutionStrategy.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyResolutionUnique](../../../../models/v2/datasets/models/PrimaryKeyResolutionUnique.md)
- [foundry_sdk.v2.datasets.models.View](../../../../models/v2/datasets/models/View.md)
- [foundry_sdk.v2.datasets.models.ViewBackingDataset](../../../../models/v2/datasets/models/ViewBackingDataset.md)
- [foundry_sdk.v2.datasets.models.ViewPrimaryKey](../../../../models/v2/datasets/models/ViewPrimaryKey.md)
- [foundry_sdk.v2.datasets.models.ViewPrimaryKeyResolution](../../../../models/v2/datasets/models/ViewPrimaryKeyResolution.md)
- [foundry_sdk.v2.filesystem.errors.FolderNotFound](../../../../models/v2/filesystem/errors/FolderNotFound.md)
- [foundry_sdk.v2.filesystem.errors.FolderNotFoundParameters](../../../../models/v2/filesystem/errors/FolderNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayName](../../../../models/v2/filesystem/errors/InvalidDisplayName.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayNameParameters](../../../../models/v2/filesystem/errors/InvalidDisplayNameParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExists](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExists.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExistsParameters](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/View.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
