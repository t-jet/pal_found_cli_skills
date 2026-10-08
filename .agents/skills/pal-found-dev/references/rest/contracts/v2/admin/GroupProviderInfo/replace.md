# v2.admin.GroupProviderInfo.replace


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Replace the GroupProviderInfo.

## SDK invocation contract

```python
def replace(self, group_id: core_models.GroupId, *, provider_id: admin_models.ProviderId, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.GroupProviderInfo: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| group_id | core_models.GroupId | required | Value shape and constraints are in its referenced local type definition. |
| provider_id | admin_models.ProviderId | required | The ID of the Group in the external authentication provider. This value is determined by the authentication provider. At most one Group can have a given provider ID in a given Realm. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CannotReplaceProviderInfoForPrincipalInProtectedRealm | Provider information for Principals in this Realm cannot be replaced. |
| GetGroupProviderInfoPermissionDenied | The provided token does not have permission to view the provider information for the given group. |
| GroupNotFound | The given Group could not be found. |
| GroupProviderInfoNotFound | The given GroupProviderInfo could not be found. |
| ReplaceGroupProviderInfoPermissionDenied | Could not replace the GroupProviderInfo. |

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/admin/groups/{groupId}/providerInfo'
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
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
admin_models.ReplaceGroupProviderInfoRequest(provider_id=provider_id)
```

**response_type**

```python
admin_models.GroupProviderInfo
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CannotReplaceProviderInfoForPrincipalInProtectedRealm': admin_errors.CannotReplaceProviderInfoForPrincipalInProtectedRealm, 'GetGroupProviderInfoPermissionDenied': admin_errors.GetGroupProviderInfoPermissionDenied, 'GroupNotFound': admin_errors.GroupNotFound, 'GroupProviderInfoNotFound': admin_errors.GroupProviderInfoNotFound, 'ReplaceGroupProviderInfoPermissionDenied': admin_errors.ReplaceGroupProviderInfoPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.GroupProviderInfo`. Ordinary async return: `typing.Awaitable[admin_models.GroupProviderInfo]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.GroupProviderInfo |
| sync_raw | ApiResponse[admin_models.GroupProviderInfo] |
| sync_streaming | StreamingContextManager[admin_models.GroupProviderInfo] |
| async_ordinary | typing.Awaitable[admin_models.GroupProviderInfo] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.GroupProviderInfo]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.GroupProviderInfo]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.CannotReplaceProviderInfoForPrincipalInProtectedRealm](../../../../models/v2/admin/errors/CannotReplaceProviderInfoForPrincipalInProtectedRealm.md)
- [foundry_sdk.v2.admin.errors.CannotReplaceProviderInfoForPrincipalInProtectedRealmParameters](../../../../models/v2/admin/errors/CannotReplaceProviderInfoForPrincipalInProtectedRealmParameters.md)
- [foundry_sdk.v2.admin.errors.GetGroupProviderInfoPermissionDenied](../../../../models/v2/admin/errors/GetGroupProviderInfoPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetGroupProviderInfoPermissionDeniedParameters](../../../../models/v2/admin/errors/GetGroupProviderInfoPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.GroupNotFound](../../../../models/v2/admin/errors/GroupNotFound.md)
- [foundry_sdk.v2.admin.errors.GroupNotFoundParameters](../../../../models/v2/admin/errors/GroupNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.GroupProviderInfoNotFound](../../../../models/v2/admin/errors/GroupProviderInfoNotFound.md)
- [foundry_sdk.v2.admin.errors.GroupProviderInfoNotFoundParameters](../../../../models/v2/admin/errors/GroupProviderInfoNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.ReplaceGroupProviderInfoPermissionDenied](../../../../models/v2/admin/errors/ReplaceGroupProviderInfoPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ReplaceGroupProviderInfoPermissionDeniedParameters](../../../../models/v2/admin/errors/ReplaceGroupProviderInfoPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.GroupProviderInfo](../../../../models/v2/admin/models/GroupProviderInfo.md)
- [foundry_sdk.v2.admin.models.ProviderId](../../../../models/v2/admin/models/ProviderId.md)
- [foundry_sdk.v2.admin.models.ReplaceGroupProviderInfoRequest](../../../../models/v2/admin/models/ReplaceGroupProviderInfoRequest.md)
- [foundry_sdk.v2.core.models.GroupId](../../../../models/v2/core/models/GroupId.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.Realm](../../../../models/v2/core/models/Realm.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/GroupProviderInfo.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](replace.md)
