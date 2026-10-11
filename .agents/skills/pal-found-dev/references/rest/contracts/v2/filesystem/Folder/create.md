# v2.filesystem.Folder.create


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new Folder.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Folder.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, *, display_name: filesystem_models.ResourceDisplayName, parent_folder_rid: filesystem_models.FolderRid, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> filesystem_models.Folder: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| display_name | filesystem_models.ResourceDisplayName | required | Value shape and constraints are in its referenced local type definition. |
| parent_folder_rid | filesystem_models.FolderRid | required | The parent folder Resource Identifier (RID). For Projects, this will be the Space RID and for Spaces, this value will be the root folder (`ri.compass.main.folder.0`). |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateFolderOutsideProjectNotSupported | The given resource is not a folder. |
| CreateFolderPermissionDenied | Could not create the Folder. |
| FolderNotFound | The given Folder could not be found. |
| GetRootFolderNotSupported | Getting the root folder as a resource is not supported. |
| InvalidDisplayName | The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters. |
| InvalidFolder | The given resource is not a Folder. |
| MissingDisplayName | A Display Name must be provided. |
| ResourceNameAlreadyExists | The provided resource name is already in use by another resource in the same folder. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/filesystem/folders'
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
filesystem_models.CreateFolderRequest(parent_folder_rid=parent_folder_rid, display_name=display_name)
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
{'CreateFolderOutsideProjectNotSupported': filesystem_errors.CreateFolderOutsideProjectNotSupported, 'CreateFolderPermissionDenied': filesystem_errors.CreateFolderPermissionDenied, 'FolderNotFound': filesystem_errors.FolderNotFound, 'GetRootFolderNotSupported': filesystem_errors.GetRootFolderNotSupported, 'InvalidDisplayName': filesystem_errors.InvalidDisplayName, 'InvalidFolder': filesystem_errors.InvalidFolder, 'MissingDisplayName': filesystem_errors.MissingDisplayName, 'ResourceNameAlreadyExists': filesystem_errors.ResourceNameAlreadyExists}
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
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.UpdatedBy](../../../../models/v2/core/models/UpdatedBy.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../../../models/v2/core/models/UpdatedTime.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)
- [foundry_sdk.v2.filesystem.errors.CreateFolderOutsideProjectNotSupported](../../../../models/v2/filesystem/errors/CreateFolderOutsideProjectNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.CreateFolderOutsideProjectNotSupportedParameters](../../../../models/v2/filesystem/errors/CreateFolderOutsideProjectNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.CreateFolderPermissionDenied](../../../../models/v2/filesystem/errors/CreateFolderPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.CreateFolderPermissionDeniedParameters](../../../../models/v2/filesystem/errors/CreateFolderPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.FolderNotFound](../../../../models/v2/filesystem/errors/FolderNotFound.md)
- [foundry_sdk.v2.filesystem.errors.FolderNotFoundParameters](../../../../models/v2/filesystem/errors/FolderNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.GetRootFolderNotSupported](../../../../models/v2/filesystem/errors/GetRootFolderNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.GetRootFolderNotSupportedParameters](../../../../models/v2/filesystem/errors/GetRootFolderNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayName](../../../../models/v2/filesystem/errors/InvalidDisplayName.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayNameParameters](../../../../models/v2/filesystem/errors/InvalidDisplayNameParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidFolder](../../../../models/v2/filesystem/errors/InvalidFolder.md)
- [foundry_sdk.v2.filesystem.errors.InvalidFolderParameters](../../../../models/v2/filesystem/errors/InvalidFolderParameters.md)
- [foundry_sdk.v2.filesystem.errors.MissingDisplayName](../../../../models/v2/filesystem/errors/MissingDisplayName.md)
- [foundry_sdk.v2.filesystem.errors.MissingDisplayNameParameters](../../../../models/v2/filesystem/errors/MissingDisplayNameParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExists](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExists.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExistsParameters](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.filesystem.models.CreateFolderRequest](../../../../models/v2/filesystem/models/CreateFolderRequest.md)
- [foundry_sdk.v2.filesystem.models.Folder](../../../../models/v2/filesystem/models/Folder.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)
- [foundry_sdk.v2.filesystem.models.FolderType](../../../../models/v2/filesystem/models/FolderType.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](../../../../models/v2/filesystem/models/ResourcePath.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](../../../../models/v2/filesystem/models/SpaceRid.md)
- [foundry_sdk.v2.filesystem.models.TrashStatus](../../../../models/v2/filesystem/models/TrashStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Folder.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
