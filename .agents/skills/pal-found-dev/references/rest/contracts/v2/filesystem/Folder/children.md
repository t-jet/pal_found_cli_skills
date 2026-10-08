# v2.filesystem.Folder.children


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List all child resources of the Folder.

This is a paged endpoint. The page size will be limited to 2,000 results per page. If no page size is
provided, this page size will also be used as the default.

## SDK invocation contract

```python
def children(self, folder_rid: filesystem_models.FolderRid, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[filesystem_models.Resource]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| folder_rid | filesystem_models.FolderRid | required | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| FolderNotFound | The given Folder could not be found. |
| GetRootFolderNotSupported | Getting the root folder as a resource is not supported. |
| GetSpaceResourceNotSupported | Getting a space as a resource is not supported. |
| InvalidFolder | The given resource is not a Folder. |
| ResourceNotFound | The given Resource could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/filesystem/folders/{folderRid}/children'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token}
```

**path_params**

```python
{'folderRid': folder_rid}
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
filesystem_models.ListChildrenOfFolderResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'FolderNotFound': filesystem_errors.FolderNotFound, 'GetRootFolderNotSupported': filesystem_errors.GetRootFolderNotSupported, 'GetSpaceResourceNotSupported': filesystem_errors.GetSpaceResourceNotSupported, 'InvalidFolder': filesystem_errors.InvalidFolder, 'ResourceNotFound': filesystem_errors.ResourceNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[filesystem_models.Resource]`. Ordinary async return: `core.AsyncResourceIterator[filesystem_models.Resource]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[filesystem_models.Resource] |
| sync_raw | ApiResponse[filesystem_models.ListChildrenOfFolderResponse] |
| sync_streaming | StreamingContextManager[filesystem_models.ListChildrenOfFolderResponse] |
| async_ordinary | core.AsyncResourceIterator[filesystem_models.Resource] |
| async_raw | Awaitable[AsyncApiResponse[filesystem_models.ListChildrenOfFolderResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[filesystem_models.ListChildrenOfFolderResponse]] |

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
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.UpdatedBy](../../../../models/v2/core/models/UpdatedBy.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../../../models/v2/core/models/UpdatedTime.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)
- [foundry_sdk.v2.filesystem.errors.FolderNotFound](../../../../models/v2/filesystem/errors/FolderNotFound.md)
- [foundry_sdk.v2.filesystem.errors.FolderNotFoundParameters](../../../../models/v2/filesystem/errors/FolderNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.GetRootFolderNotSupported](../../../../models/v2/filesystem/errors/GetRootFolderNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.GetRootFolderNotSupportedParameters](../../../../models/v2/filesystem/errors/GetRootFolderNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.GetSpaceResourceNotSupported](../../../../models/v2/filesystem/errors/GetSpaceResourceNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.GetSpaceResourceNotSupportedParameters](../../../../models/v2/filesystem/errors/GetSpaceResourceNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidFolder](../../../../models/v2/filesystem/errors/InvalidFolder.md)
- [foundry_sdk.v2.filesystem.errors.InvalidFolderParameters](../../../../models/v2/filesystem/errors/InvalidFolderParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFound](../../../../models/v2/filesystem/errors/ResourceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFoundParameters](../../../../models/v2/filesystem/errors/ResourceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)
- [foundry_sdk.v2.filesystem.models.ListChildrenOfFolderResponse](../../../../models/v2/filesystem/models/ListChildrenOfFolderResponse.md)
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

Read the [local resource guide](../../../../v2/filesystem/Folder.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](children.md)
