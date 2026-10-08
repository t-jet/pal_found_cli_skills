# v2.filesystem.Resource.restore


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Restore the given resource and any directly trashed ancestors from the trash. If the resource is not
trashed, this operation will be ignored.

## SDK invocation contract

```python
def restore(self, resource_rid: filesystem_models.ResourceRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| resource_rid | filesystem_models.ResourceRid | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ResourceNotDirectlyTrashed | The resource is not directly trashed. |
| ResourceNotFound | The given Resource could not be found. |
| RestoreResourcePermissionDenied | Could not restore the Resource. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/filesystem/resources/{resourceRid}/restore'
```

**query_params**

```python
{}
```

**path_params**

```python
{'resourceRid': resource_rid}
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
{'ResourceNotDirectlyTrashed': filesystem_errors.ResourceNotDirectlyTrashed, 'ResourceNotFound': filesystem_errors.ResourceNotFound, 'RestoreResourcePermissionDenied': filesystem_errors.RestoreResourcePermissionDenied}
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
- [foundry_sdk.v2.filesystem.errors.ResourceNotDirectlyTrashed](../../../../models/v2/filesystem/errors/ResourceNotDirectlyTrashed.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotDirectlyTrashedParameters](../../../../models/v2/filesystem/errors/ResourceNotDirectlyTrashedParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFound](../../../../models/v2/filesystem/errors/ResourceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFoundParameters](../../../../models/v2/filesystem/errors/ResourceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.RestoreResourcePermissionDenied](../../../../models/v2/filesystem/errors/RestoreResourcePermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.RestoreResourcePermissionDeniedParameters](../../../../models/v2/filesystem/errors/RestoreResourcePermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Resource.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](restore.md)
