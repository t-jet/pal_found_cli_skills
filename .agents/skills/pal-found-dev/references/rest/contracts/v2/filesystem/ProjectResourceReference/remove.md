# v2.filesystem.ProjectResourceReference.remove


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Remove references from the given project

## SDK invocation contract

```python
def remove(self, project_rid: filesystem_models.ProjectRid, *, resources: typing.List[core.RID], request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| project_rid | filesystem_models.ProjectRid | required | Value shape and constraints are in its referenced local type definition. |
| resources | typing.List[core.RID] | required | The resource identifiers to remove as references. These may be either filesystem or external resource identifiers. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| InvalidProject | The provided resource identifier does not refer to a valid project. |
| InvalidResourceReference | The resource reference is invalid. This can occur when the resource identifier is malformed, the resource type does not match the reference type, or the resource cannot be added as a reference. |
| ProjectNotFound | The given Project could not be found. |
| RemoveProjectResourceReferencesPermissionDenied | Could not remove the ProjectResourceReference. |
| ResourceNotFound | The given Resource could not be found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/filesystem/projects/{projectRid}/references/remove'
```

**query_params**

```python
{}
```

**path_params**

```python
{'projectRid': project_rid}
```

**header_params**

```python
{'Content-Type': 'application/json'}
```

**body**

```python
filesystem_models.RemoveProjectResourceReferencesRequest(resources=resources)
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
{'InvalidProject': filesystem_errors.InvalidProject, 'InvalidResourceReference': filesystem_errors.InvalidResourceReference, 'ProjectNotFound': filesystem_errors.ProjectNotFound, 'RemoveProjectResourceReferencesPermissionDenied': filesystem_errors.RemoveProjectResourceReferencesPermissionDenied, 'ResourceNotFound': filesystem_errors.ResourceNotFound}
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
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.filesystem.errors.InvalidProject](../../../../models/v2/filesystem/errors/InvalidProject.md)
- [foundry_sdk.v2.filesystem.errors.InvalidProjectParameters](../../../../models/v2/filesystem/errors/InvalidProjectParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidResourceReference](../../../../models/v2/filesystem/errors/InvalidResourceReference.md)
- [foundry_sdk.v2.filesystem.errors.InvalidResourceReferenceParameters](../../../../models/v2/filesystem/errors/InvalidResourceReferenceParameters.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFound](../../../../models/v2/filesystem/errors/ProjectNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFoundParameters](../../../../models/v2/filesystem/errors/ProjectNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.RemoveProjectResourceReferencesPermissionDenied](../../../../models/v2/filesystem/errors/RemoveProjectResourceReferencesPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.RemoveProjectResourceReferencesPermissionDeniedParameters](../../../../models/v2/filesystem/errors/RemoveProjectResourceReferencesPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFound](../../../../models/v2/filesystem/errors/ResourceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFoundParameters](../../../../models/v2/filesystem/errors/ResourceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.RemoveProjectResourceReferencesRequest](../../../../models/v2/filesystem/models/RemoveProjectResourceReferencesRequest.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/ProjectResourceReference.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](remove.md)
