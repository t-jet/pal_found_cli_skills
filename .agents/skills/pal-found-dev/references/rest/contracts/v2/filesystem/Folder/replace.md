# v2.filesystem.Folder.replace


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Replace the Folder with the specified rid.

## SDK invocation contract

```python
def replace(self, folder_rid: filesystem_models.FolderRid, *, display_name: filesystem_models.ResourceDisplayName, parent_folder_rid: filesystem_models.FolderRid, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> filesystem_models.Folder: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| folder_rid | filesystem_models.FolderRid | required | Value shape and constraints are in its referenced local type definition. |
| display_name | filesystem_models.ResourceDisplayName | required | Value shape and constraints are in its referenced local type definition. |
| parent_folder_rid | filesystem_models.FolderRid | required | The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`). |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CircularDependency | The requested operation would result in a circular dependency in the folder hierarchy. For example, moving a folder into one of its descendants. |
| FolderNotFound | The given Folder could not be found. |
| GetRootFolderNotSupported | Getting the root folder as a resource is not supported. |
| InvalidDisplayName | The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters. |
| InvalidFolder | The given resource is not a Folder. |
| InvalidParentFolder | The specified parent folder is not a valid destination for the resource. For example, a project cannot be moved under a regular folder, a folder cannot be moved to a Space, etc. |
| MissingDisplayName | A Display Name must be provided. |
| ReplaceFolderPermissionDenied | Could not replace the Folder. |
| ResourceNameAlreadyExists | The provided resource name is already in use by another resource in the same folder. |

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/filesystem/folders/{folderRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'folderRid': folder_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
filesystem_models.ReplaceFolderRequest(parent_folder_rid=parent_folder_rid, display_name=display_name)
```

**response_type**

```python
filesystem_models.Folder
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CircularDependency': filesystem_errors.CircularDependency, 'FolderNotFound': filesystem_errors.FolderNotFound, 'GetRootFolderNotSupported': filesystem_errors.GetRootFolderNotSupported, 'InvalidDisplayName': filesystem_errors.InvalidDisplayName, 'InvalidFolder': filesystem_errors.InvalidFolder, 'InvalidParentFolder': filesystem_errors.InvalidParentFolder, 'MissingDisplayName': filesystem_errors.MissingDisplayName, 'ReplaceFolderPermissionDenied': filesystem_errors.ReplaceFolderPermissionDenied, 'ResourceNameAlreadyExists': filesystem_errors.ResourceNameAlreadyExists}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `filesystem_models.Folder`. Ordinary async return: `typing.Awaitable[filesystem_models.Folder]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | filesystem_models.Folder |
| sync_raw | ApiResponse[filesystem_models.Folder] |
| sync_streaming | StreamingContextManager[filesystem_models.Folder] |
| async_ordinary | typing.Awaitable[filesystem_models.Folder] |
| async_raw | Awaitable[AsyncApiResponse[filesystem_models.Folder]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[filesystem_models.Folder]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.UpdatedBy](../../../../models/v2/core/models/UpdatedBy.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../../../models/v2/core/models/UpdatedTime.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)
- [foundry_sdk.v2.filesystem.errors.CircularDependency](../../../../models/v2/filesystem/errors/CircularDependency.md)
- [foundry_sdk.v2.filesystem.errors.CircularDependencyParameters](../../../../models/v2/filesystem/errors/CircularDependencyParameters.md)
- [foundry_sdk.v2.filesystem.errors.FolderNotFound](../../../../models/v2/filesystem/errors/FolderNotFound.md)
- [foundry_sdk.v2.filesystem.errors.FolderNotFoundParameters](../../../../models/v2/filesystem/errors/FolderNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.GetRootFolderNotSupported](../../../../models/v2/filesystem/errors/GetRootFolderNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.GetRootFolderNotSupportedParameters](../../../../models/v2/filesystem/errors/GetRootFolderNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayName](../../../../models/v2/filesystem/errors/InvalidDisplayName.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayNameParameters](../../../../models/v2/filesystem/errors/InvalidDisplayNameParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidFolder](../../../../models/v2/filesystem/errors/InvalidFolder.md)
- [foundry_sdk.v2.filesystem.errors.InvalidFolderParameters](../../../../models/v2/filesystem/errors/InvalidFolderParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidParentFolder](../../../../models/v2/filesystem/errors/InvalidParentFolder.md)
- [foundry_sdk.v2.filesystem.errors.InvalidParentFolderParameters](../../../../models/v2/filesystem/errors/InvalidParentFolderParameters.md)
- [foundry_sdk.v2.filesystem.errors.MissingDisplayName](../../../../models/v2/filesystem/errors/MissingDisplayName.md)
- [foundry_sdk.v2.filesystem.errors.MissingDisplayNameParameters](../../../../models/v2/filesystem/errors/MissingDisplayNameParameters.md)
- [foundry_sdk.v2.filesystem.errors.ReplaceFolderPermissionDenied](../../../../models/v2/filesystem/errors/ReplaceFolderPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.ReplaceFolderPermissionDeniedParameters](../../../../models/v2/filesystem/errors/ReplaceFolderPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExists](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExists.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExistsParameters](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.filesystem.models.Folder](../../../../models/v2/filesystem/models/Folder.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)
- [foundry_sdk.v2.filesystem.models.FolderType](../../../../models/v2/filesystem/models/FolderType.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.ReplaceFolderRequest](../../../../models/v2/filesystem/models/ReplaceFolderRequest.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](../../../../models/v2/filesystem/models/ResourcePath.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](../../../../models/v2/filesystem/models/SpaceRid.md)
- [foundry_sdk.v2.filesystem.models.TrashStatus](../../../../models/v2/filesystem/models/TrashStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Folder.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](replace.md)
