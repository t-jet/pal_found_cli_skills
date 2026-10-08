# v2.admin.User.search


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Perform a case-insensitive prefix search for active users based on username, given name and family name.
Deleted users are not included in results. To list deleted users, use the `list` endpoint with `include=DELETED`.

## SDK invocation contract

```python
def search(self, *, where: admin_models.UserSearchFilter, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.SearchUsersResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| where | admin_models.UserSearchFilter | required | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | Value shape and constraints are in its referenced local type definition. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |
| SearchUsersPermissionDenied | Could not search the User. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/users/search'
```

**query_params**

```python
{}
```

**path_params**

```python
{}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
admin_models.SearchUsersRequest(where=where, page_size=page_size, page_token=page_token)
```

**response_type**

```python
admin_models.SearchUsersResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'InvalidPageSize': core_errors.InvalidPageSize, 'SearchUsersPermissionDenied': admin_errors.SearchUsersPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.SearchUsersResponse`. Ordinary async return: `typing.Awaitable[admin_models.SearchUsersResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.SearchUsersResponse |
| sync_raw | ApiResponse[admin_models.SearchUsersResponse] |
| sync_streaming | StreamingContextManager[admin_models.SearchUsersResponse] |
| async_ordinary | typing.Awaitable[admin_models.SearchUsersResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.SearchUsersResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.SearchUsersResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.SearchUsersPermissionDenied](../../../../models/v2/admin/errors/SearchUsersPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.SearchUsersPermissionDeniedParameters](../../../../models/v2/admin/errors/SearchUsersPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.AttributeName](../../../../models/v2/admin/models/AttributeName.md)
- [foundry_sdk.v2.admin.models.AttributeValue](../../../../models/v2/admin/models/AttributeValue.md)
- [foundry_sdk.v2.admin.models.AttributeValues](../../../../models/v2/admin/models/AttributeValues.md)
- [foundry_sdk.v2.admin.models.PrincipalFilterType](../../../../models/v2/admin/models/PrincipalFilterType.md)
- [foundry_sdk.v2.admin.models.SearchUsersRequest](../../../../models/v2/admin/models/SearchUsersRequest.md)
- [foundry_sdk.v2.admin.models.SearchUsersResponse](../../../../models/v2/admin/models/SearchUsersResponse.md)
- [foundry_sdk.v2.admin.models.User](../../../../models/v2/admin/models/User.md)
- [foundry_sdk.v2.admin.models.UserSearchFilter](../../../../models/v2/admin/models/UserSearchFilter.md)
- [foundry_sdk.v2.admin.models.UserUsername](../../../../models/v2/admin/models/UserUsername.md)
- [foundry_sdk.v2.core.errors.InvalidPageSize](../../../../models/v2/core/errors/InvalidPageSize.md)
- [foundry_sdk.v2.core.errors.InvalidPageSizeParameters](../../../../models/v2/core/errors/InvalidPageSizeParameters.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.Realm](../../../../models/v2/core/models/Realm.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)
- [foundry_sdk.v2.core.models.UserStatus](../../../../models/v2/core/models/UserStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/User.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](search.md)
