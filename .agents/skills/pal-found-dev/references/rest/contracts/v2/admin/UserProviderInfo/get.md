# v2.admin.UserProviderInfo.get


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the UserProviderInfo.

## SDK invocation contract

```python
def get(self, user_id: core_models.UserId, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.UserProviderInfo: ...
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
| GetUserProviderInfoPermissionDenied | The provided token does not have permission to view the provider information for the given user. |
| UserDeleted | The user is deleted. |
| UserNotFound | The given User could not be found. |
| UserProviderInfoNotFound | The given UserProviderInfo could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/users/{userId}/providerInfo'
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
admin_models.UserProviderInfo
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetUserProviderInfoPermissionDenied': admin_errors.GetUserProviderInfoPermissionDenied, 'UserDeleted': admin_errors.UserDeleted, 'UserNotFound': admin_errors.UserNotFound, 'UserProviderInfoNotFound': admin_errors.UserProviderInfoNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.UserProviderInfo`. Ordinary async return: `typing.Awaitable[admin_models.UserProviderInfo]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.UserProviderInfo |
| sync_raw | ApiResponse[admin_models.UserProviderInfo] |
| sync_streaming | StreamingContextManager[admin_models.UserProviderInfo] |
| async_ordinary | typing.Awaitable[admin_models.UserProviderInfo] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.UserProviderInfo]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.UserProviderInfo]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.GetUserProviderInfoPermissionDenied](../../../../models/v2/admin/errors/GetUserProviderInfoPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetUserProviderInfoPermissionDeniedParameters](../../../../models/v2/admin/errors/GetUserProviderInfoPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.UserDeleted](../../../../models/v2/admin/errors/UserDeleted.md)
- [foundry_sdk.v2.admin.errors.UserDeletedParameters](../../../../models/v2/admin/errors/UserDeletedParameters.md)
- [foundry_sdk.v2.admin.errors.UserNotFound](../../../../models/v2/admin/errors/UserNotFound.md)
- [foundry_sdk.v2.admin.errors.UserNotFoundParameters](../../../../models/v2/admin/errors/UserNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.UserProviderInfoNotFound](../../../../models/v2/admin/errors/UserProviderInfoNotFound.md)
- [foundry_sdk.v2.admin.errors.UserProviderInfoNotFoundParameters](../../../../models/v2/admin/errors/UserProviderInfoNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.ProviderId](../../../../models/v2/admin/models/ProviderId.md)
- [foundry_sdk.v2.admin.models.UserProviderInfo](../../../../models/v2/admin/models/UserProviderInfo.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/UserProviderInfo.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
