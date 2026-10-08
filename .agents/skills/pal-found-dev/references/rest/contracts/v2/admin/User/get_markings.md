# v2.admin.User.get_markings


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Retrieve Markings that the user is currently a member of.

## SDK invocation contract

```python
def get_markings(self, user_id: core_models.UserId, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.GetUserMarkingsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| user_id | core_models.UserId | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetMarkingsUserPermissionDenied | Could not getMarkings the User. |
| UserDeleted | The user is deleted. |
| UserNotFound | The given User could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/users/{userId}/getMarkings'
```

**query_params**

```python
{}
```

**path_params**

```python
{'userId': user_id}
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
admin_models.GetUserMarkingsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetMarkingsUserPermissionDenied': admin_errors.GetMarkingsUserPermissionDenied, 'UserDeleted': admin_errors.UserDeleted, 'UserNotFound': admin_errors.UserNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.GetUserMarkingsResponse`. Ordinary async return: `typing.Awaitable[admin_models.GetUserMarkingsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.GetUserMarkingsResponse |
| sync_raw | ApiResponse[admin_models.GetUserMarkingsResponse] |
| sync_streaming | StreamingContextManager[admin_models.GetUserMarkingsResponse] |
| async_ordinary | typing.Awaitable[admin_models.GetUserMarkingsResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.GetUserMarkingsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.GetUserMarkingsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.GetMarkingsUserPermissionDenied](../../../../models/v2/admin/errors/GetMarkingsUserPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetMarkingsUserPermissionDeniedParameters](../../../../models/v2/admin/errors/GetMarkingsUserPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.UserDeleted](../../../../models/v2/admin/errors/UserDeleted.md)
- [foundry_sdk.v2.admin.errors.UserDeletedParameters](../../../../models/v2/admin/errors/UserDeletedParameters.md)
- [foundry_sdk.v2.admin.errors.UserNotFound](../../../../models/v2/admin/errors/UserNotFound.md)
- [foundry_sdk.v2.admin.errors.UserNotFoundParameters](../../../../models/v2/admin/errors/UserNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.GetUserMarkingsResponse](../../../../models/v2/admin/models/GetUserMarkingsResponse.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/User.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_markings.md)
