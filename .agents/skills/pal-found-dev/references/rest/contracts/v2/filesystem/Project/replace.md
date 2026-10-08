# v2.filesystem.Project.replace


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Replace the Project with the specified rid.

## SDK invocation contract

```python
def replace(self, project_rid: filesystem_models.ProjectRid, *, display_name: filesystem_models.ResourceDisplayName, description: typing.Optional[str]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> filesystem_models.Project: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| project_rid | filesystem_models.ProjectRid | required | Value shape and constraints are in its referenced local type definition. |
| display_name | filesystem_models.ResourceDisplayName | required | The display name of the Project. Must be unique and cannot contain a / |
| description | typing.Optional[str] | None | The description associated with the Project. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| InvalidDisplayName | The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters. |
| ProjectNameAlreadyExists | The requested display name for the created project is already being used in the space. |
| ProjectNotFound | The given Project could not be found. |
| ReplaceProjectPermissionDenied | Could not replace the Project. |

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/filesystem/projects/{projectRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'projectRid': project_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
filesystem_models.ReplaceProjectRequest(display_name=display_name, description=description)
```

**response_type**

```python
filesystem_models.Project
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'InvalidDisplayName': filesystem_errors.InvalidDisplayName, 'ProjectNameAlreadyExists': filesystem_errors.ProjectNameAlreadyExists, 'ProjectNotFound': filesystem_errors.ProjectNotFound, 'ReplaceProjectPermissionDenied': filesystem_errors.ReplaceProjectPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `filesystem_models.Project`. Ordinary async return: `typing.Awaitable[filesystem_models.Project]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | filesystem_models.Project |
| sync_raw | ApiResponse[filesystem_models.Project] |
| sync_streaming | StreamingContextManager[filesystem_models.Project] |
| async_ordinary | typing.Awaitable[filesystem_models.Project] |
| async_raw | Awaitable[AsyncApiResponse[filesystem_models.Project]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[filesystem_models.Project]] |

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
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayName](../../../../models/v2/filesystem/errors/InvalidDisplayName.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayNameParameters](../../../../models/v2/filesystem/errors/InvalidDisplayNameParameters.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNameAlreadyExists](../../../../models/v2/filesystem/errors/ProjectNameAlreadyExists.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNameAlreadyExistsParameters](../../../../models/v2/filesystem/errors/ProjectNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFound](../../../../models/v2/filesystem/errors/ProjectNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFoundParameters](../../../../models/v2/filesystem/errors/ProjectNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.ReplaceProjectPermissionDenied](../../../../models/v2/filesystem/errors/ReplaceProjectPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.ReplaceProjectPermissionDeniedParameters](../../../../models/v2/filesystem/errors/ReplaceProjectPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.models.Project](../../../../models/v2/filesystem/models/Project.md)
- [foundry_sdk.v2.filesystem.models.ProjectResourceLevelRoleGrantsAllowed](../../../../models/v2/filesystem/models/ProjectResourceLevelRoleGrantsAllowed.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.ReplaceProjectRequest](../../../../models/v2/filesystem/models/ReplaceProjectRequest.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](../../../../models/v2/filesystem/models/ResourcePath.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](../../../../models/v2/filesystem/models/SpaceRid.md)
- [foundry_sdk.v2.filesystem.models.TrashStatus](../../../../models/v2/filesystem/models/TrashStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Project.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](replace.md)
