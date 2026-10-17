# v2.admin.Group.delete


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Delete the Group with the specified id.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Group.delete`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def delete(self, group_id: core_models.GroupId, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| group_id | core_models.GroupId | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| DeleteGroupPermissionDenied | Could not delete the Group. |
| GroupNotFound | The given Group could not be found. |

## Wire request

**method**

```python
'DELETE'
```

**resource_path**

```python
'/v2/admin/groups/{groupId}'
```

**query_params**

```python
{}
```

**path_params**

```python
{'groupId': group_id}
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
{'DeleteGroupPermissionDenied': admin_errors.DeleteGroupPermissionDenied, 'GroupNotFound': admin_errors.GroupNotFound}
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
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.DeleteGroupPermissionDenied](../../../../models/v2/admin/errors/DeleteGroupPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.DeleteGroupPermissionDeniedParameters](../../../../models/v2/admin/errors/DeleteGroupPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.GroupNotFound](../../../../models/v2/admin/errors/GroupNotFound.md)
- [foundry_sdk.v2.admin.errors.GroupNotFoundParameters](../../../../models/v2/admin/errors/GroupNotFoundParameters.md)
- [foundry_sdk.v2.core.models.GroupId](../../../../models/v2/core/models/GroupId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Group.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](delete.md)
