# v2.admin.User.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all Users.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.User.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, *, include: typing.Optional[core_models.UserStatus]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[admin_models.User]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| include | typing.Optional[core_models.UserStatus] | None | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |
| UserDeleted | The user is deleted. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/users'
```

**query_params**

```python
{'include': include, 'pageSize': page_size, 'pageToken': page_token}
```

**path_params**

```python
{}
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
admin_models.ListUsersResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'InvalidPageSize': core_errors.InvalidPageSize, 'UserDeleted': admin_errors.UserDeleted}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[admin_models.User]`. Ordinary async return: `core.AsyncResourceIterator[admin_models.User]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[admin_models.User] |
| sync_raw | ApiResponse[admin_models.ListUsersResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListUsersResponse] |
| async_ordinary | core.AsyncResourceIterator[admin_models.User] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListUsersResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListUsersResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.UserDeleted](../../../../models/v2/admin/errors/UserDeleted.md)
- [foundry_sdk.v2.admin.errors.UserDeletedParameters](../../../../models/v2/admin/errors/UserDeletedParameters.md)
- [foundry_sdk.v2.admin.models.AttributeName](../../../../models/v2/admin/models/AttributeName.md)
- [foundry_sdk.v2.admin.models.AttributeValue](../../../../models/v2/admin/models/AttributeValue.md)
- [foundry_sdk.v2.admin.models.AttributeValues](../../../../models/v2/admin/models/AttributeValues.md)
- [foundry_sdk.v2.admin.models.ListUsersResponse](../../../../models/v2/admin/models/ListUsersResponse.md)
- [foundry_sdk.v2.admin.models.User](../../../../models/v2/admin/models/User.md)
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

[Part 1](list.md)
