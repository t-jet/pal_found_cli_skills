# v2.filesystem.Resource.delete


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Move the given resource to the trash. Following this operation, the resource can be restored, using the
`restore` operation, or permanently deleted using the `permanentlyDelete` operation.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Resource.delete`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def delete(self, resource_rid: filesystem_models.ResourceRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
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
| DeleteResourcePermissionDenied | Could not delete the Resource. |
| ResourceNotFound | The given Resource could not be found. |
| TrashingAutosavedResourcesNotSupported | Auto-saved resources cannot be trashed. |
| TrashingHiddenResourcesNotSupported | Hidden resources cannot be trashed. |
| TrashingSpaceNotSupported | Spaces cannot be trashed. |

## Wire request

**method**

```python
'DELETE'
```

**resource_path**

```python
'/v2/filesystem/resources/{resourceRid}'
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
{'DeleteResourcePermissionDenied': filesystem_errors.DeleteResourcePermissionDenied, 'ResourceNotFound': filesystem_errors.ResourceNotFound, 'TrashingAutosavedResourcesNotSupported': filesystem_errors.TrashingAutosavedResourcesNotSupported, 'TrashingHiddenResourcesNotSupported': filesystem_errors.TrashingHiddenResourcesNotSupported, 'TrashingSpaceNotSupported': filesystem_errors.TrashingSpaceNotSupported}
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
- [foundry_sdk.v2.filesystem.errors.DeleteResourcePermissionDenied](../../../../models/v2/filesystem/errors/DeleteResourcePermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.DeleteResourcePermissionDeniedParameters](../../../../models/v2/filesystem/errors/DeleteResourcePermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFound](../../../../models/v2/filesystem/errors/ResourceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFoundParameters](../../../../models/v2/filesystem/errors/ResourceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.TrashingAutosavedResourcesNotSupported](../../../../models/v2/filesystem/errors/TrashingAutosavedResourcesNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.TrashingAutosavedResourcesNotSupportedParameters](../../../../models/v2/filesystem/errors/TrashingAutosavedResourcesNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.TrashingHiddenResourcesNotSupported](../../../../models/v2/filesystem/errors/TrashingHiddenResourcesNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.TrashingHiddenResourcesNotSupportedParameters](../../../../models/v2/filesystem/errors/TrashingHiddenResourcesNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.TrashingSpaceNotSupported](../../../../models/v2/filesystem/errors/TrashingSpaceNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.TrashingSpaceNotSupportedParameters](../../../../models/v2/filesystem/errors/TrashingSpaceNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Resource.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](delete.md)
