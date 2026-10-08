# v2.filesystem.Space.delete


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Delete the space. This will only work if the Space is empty, meaning any Projects or resources have been deleted first.

## SDK invocation contract

```python
def delete(self, space_rid: filesystem_models.SpaceRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| space_rid | filesystem_models.SpaceRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| DeleteSpacePermissionDenied | Could not delete the Space. |
| SpaceNotEmpty | The space cannot be deleted because it contains resources. |
| SpaceNotFound | The given Space could not be found. |

## Wire request

**method**

```python
'DELETE'
```

**resource_path**

```python
'/v2/filesystem/spaces/{spaceRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'spaceRid': space_rid}
```

**header_params**

```python
{}
```

**body**

```python
None
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
{'DeleteSpacePermissionDenied': filesystem_errors.DeleteSpacePermissionDenied, 'SpaceNotEmpty': filesystem_errors.SpaceNotEmpty, 'SpaceNotFound': filesystem_errors.SpaceNotFound}
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
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.filesystem.errors.DeleteSpacePermissionDenied](../../../../models/v2/filesystem/errors/DeleteSpacePermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.DeleteSpacePermissionDeniedParameters](../../../../models/v2/filesystem/errors/DeleteSpacePermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNotEmpty](../../../../models/v2/filesystem/errors/SpaceNotEmpty.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNotEmptyParameters](../../../../models/v2/filesystem/errors/SpaceNotEmptyParameters.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNotFound](../../../../models/v2/filesystem/errors/SpaceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNotFoundParameters](../../../../models/v2/filesystem/errors/SpaceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](../../../../models/v2/filesystem/models/SpaceRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Space.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](delete.md)
