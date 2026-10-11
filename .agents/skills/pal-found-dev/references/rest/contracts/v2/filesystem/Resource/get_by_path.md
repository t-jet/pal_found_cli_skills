# v2.filesystem.Resource.get_by_path


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get a resource by its absolute path.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Resource.get_by_path`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_by_path(self, *, path: filesystem_models.ResourcePath, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> filesystem_models.Resource: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| path | filesystem_models.ResourcePath | required | The path to the resource. The leading slash is optional. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetByPathPermissionDenied | Could not getByPath the Resource. |
| GetRootFolderNotSupported | Getting the root folder as a resource is not supported. |
| GetSpaceResourceNotSupported | Getting a space as a resource is not supported. |
| InvalidPath | The given path is invalid. A valid path has all components separated by a single `/`. |
| PathNotFound | The given path could not be found. |
| ResourceNotFound | The given Resource could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/filesystem/resources/getByPath'
```

**query_params**

```python
{'path': path}
```

**path_params**

```python
{}
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
filesystem_models.Resource
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetByPathPermissionDenied': filesystem_errors.GetByPathPermissionDenied, 'GetRootFolderNotSupported': filesystem_errors.GetRootFolderNotSupported, 'GetSpaceResourceNotSupported': filesystem_errors.GetSpaceResourceNotSupported, 'InvalidPath': filesystem_errors.InvalidPath, 'PathNotFound': filesystem_errors.PathNotFound, 'ResourceNotFound': filesystem_errors.ResourceNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `filesystem_models.Resource`. Ordinary async return: `typing.Awaitable[filesystem_models.Resource]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | filesystem_models.Resource |
| sync_raw | ApiResponse[filesystem_models.Resource] |
| sync_streaming | StreamingContextManager[filesystem_models.Resource] |
| async_ordinary | typing.Awaitable[filesystem_models.Resource] |
| async_raw | Awaitable[AsyncApiResponse[filesystem_models.Resource]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[filesystem_models.Resource]] |

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
- [foundry_sdk.v2.filesystem.errors.GetByPathPermissionDenied](../../../../models/v2/filesystem/errors/GetByPathPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.GetByPathPermissionDeniedParameters](../../../../models/v2/filesystem/errors/GetByPathPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.GetRootFolderNotSupported](../../../../models/v2/filesystem/errors/GetRootFolderNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.GetRootFolderNotSupportedParameters](../../../../models/v2/filesystem/errors/GetRootFolderNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.GetSpaceResourceNotSupported](../../../../models/v2/filesystem/errors/GetSpaceResourceNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.GetSpaceResourceNotSupportedParameters](../../../../models/v2/filesystem/errors/GetSpaceResourceNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidPath](../../../../models/v2/filesystem/errors/InvalidPath.md)
- [foundry_sdk.v2.filesystem.errors.InvalidPathParameters](../../../../models/v2/filesystem/errors/InvalidPathParameters.md)
- [foundry_sdk.v2.filesystem.errors.PathNotFound](../../../../models/v2/filesystem/errors/PathNotFound.md)
- [foundry_sdk.v2.filesystem.errors.PathNotFoundParameters](../../../../models/v2/filesystem/errors/PathNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFound](../../../../models/v2/filesystem/errors/ResourceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFoundParameters](../../../../models/v2/filesystem/errors/ResourceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.Resource](../../../../models/v2/filesystem/models/Resource.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](../../../../models/v2/filesystem/models/ResourcePath.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceType](../../../../models/v2/filesystem/models/ResourceType.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](../../../../models/v2/filesystem/models/SpaceRid.md)
- [foundry_sdk.v2.filesystem.models.TrashStatus](../../../../models/v2/filesystem/models/TrashStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Resource.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_by_path.md)
