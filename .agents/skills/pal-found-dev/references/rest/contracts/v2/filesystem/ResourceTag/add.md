# v2.filesystem.ResourceTag.add


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Apply tags to a resource.

## SDK invocation contract

```python
def add(self, resource_rid: filesystem_models.ResourceRid, *, tag_rids: typing.List[filesystem_models.TagRid], preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| resource_rid | filesystem_models.ResourceRid | required | Value shape and constraints are in its referenced local type definition. |
| tag_rids | typing.List[filesystem_models.TagRid] | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AddResourceTagsPermissionDenied | Could not add the ResourceTag. |
| ForbiddenOperationOnAutosavedResource | Performing this operation on an autosaved resource is not supported. |
| ForbiddenOperationOnHiddenResource | Performing this operation on a hidden resource is not supported. |
| ResourceNotFound | The given Resource could not be found. |
| TagNotFound | At least one of the provided tag RIDs could not be found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/filesystem/resources/{resourceRid}/tags/add'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'resourceRid': resource_rid}
```

**header_params**

```python
{'Content-Type': 'application/json'}
```

**body**

```python
filesystem_models.AddResourceTagsRequest(tag_rids=tag_rids)
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
{'AddResourceTagsPermissionDenied': filesystem_errors.AddResourceTagsPermissionDenied, 'ForbiddenOperationOnAutosavedResource': filesystem_errors.ForbiddenOperationOnAutosavedResource, 'ForbiddenOperationOnHiddenResource': filesystem_errors.ForbiddenOperationOnHiddenResource, 'ResourceNotFound': filesystem_errors.ResourceNotFound, 'TagNotFound': filesystem_errors.TagNotFound}
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
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.filesystem.errors.AddResourceTagsPermissionDenied](../../../../models/v2/filesystem/errors/AddResourceTagsPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.AddResourceTagsPermissionDeniedParameters](../../../../models/v2/filesystem/errors/AddResourceTagsPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.ForbiddenOperationOnAutosavedResource](../../../../models/v2/filesystem/errors/ForbiddenOperationOnAutosavedResource.md)
- [foundry_sdk.v2.filesystem.errors.ForbiddenOperationOnAutosavedResourceParameters](../../../../models/v2/filesystem/errors/ForbiddenOperationOnAutosavedResourceParameters.md)
- [foundry_sdk.v2.filesystem.errors.ForbiddenOperationOnHiddenResource](../../../../models/v2/filesystem/errors/ForbiddenOperationOnHiddenResource.md)
- [foundry_sdk.v2.filesystem.errors.ForbiddenOperationOnHiddenResourceParameters](../../../../models/v2/filesystem/errors/ForbiddenOperationOnHiddenResourceParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFound](../../../../models/v2/filesystem/errors/ResourceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFoundParameters](../../../../models/v2/filesystem/errors/ResourceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.TagNotFound](../../../../models/v2/filesystem/errors/TagNotFound.md)
- [foundry_sdk.v2.filesystem.errors.TagNotFoundParameters](../../../../models/v2/filesystem/errors/TagNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.AddResourceTagsRequest](../../../../models/v2/filesystem/models/AddResourceTagsRequest.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)
- [foundry_sdk.v2.filesystem.models.TagRid](../../../../models/v2/filesystem/models/TagRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/ResourceTag.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](add.md)
