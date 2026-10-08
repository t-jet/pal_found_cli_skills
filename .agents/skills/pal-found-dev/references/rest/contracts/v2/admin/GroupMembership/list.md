# v2.admin.GroupMembership.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all Groups a given User is a member of.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
To get the next page, make the same request again, but set the value of the `pageToken` query parameter
to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
in the response, you are on the last page.

## SDK invocation contract

```python
def list(self, user_id: core_models.UserId, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, transitive: typing.Optional[bool]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[admin_models.GroupMembership]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| user_id | core_models.UserId | required | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| transitive | typing.Optional[bool] | None | When true, includes the transitive memberships of the Groups the User is a member of. For example, say the User is a member of Group A, and Group A is a member of Group B. If `transitive=false` only Group A will be returned, but if `transitive=true` then Groups A and B will be returned. This will recursively resolve Groups through all layers of nesting. Defaults to false. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |
| UserDeleted | The user is deleted. |
| UserNotFound | The given User could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/users/{userId}/groupMemberships'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token, 'transitive': transitive}
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
admin_models.ListGroupMembershipsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'InvalidPageSize': core_errors.InvalidPageSize, 'UserDeleted': admin_errors.UserDeleted, 'UserNotFound': admin_errors.UserNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[admin_models.GroupMembership]`. Ordinary async return: `core.AsyncResourceIterator[admin_models.GroupMembership]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[admin_models.GroupMembership] |
| sync_raw | ApiResponse[admin_models.ListGroupMembershipsResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListGroupMembershipsResponse] |
| async_ordinary | core.AsyncResourceIterator[admin_models.GroupMembership] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListGroupMembershipsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListGroupMembershipsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.UserDeleted](../../../../models/v2/admin/errors/UserDeleted.md)
- [foundry_sdk.v2.admin.errors.UserDeletedParameters](../../../../models/v2/admin/errors/UserDeletedParameters.md)
- [foundry_sdk.v2.admin.errors.UserNotFound](../../../../models/v2/admin/errors/UserNotFound.md)
- [foundry_sdk.v2.admin.errors.UserNotFoundParameters](../../../../models/v2/admin/errors/UserNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.GroupMembership](../../../../models/v2/admin/models/GroupMembership.md)
- [foundry_sdk.v2.admin.models.ListGroupMembershipsResponse](../../../../models/v2/admin/models/ListGroupMembershipsResponse.md)
- [foundry_sdk.v2.core.errors.InvalidPageSize](../../../../models/v2/core/errors/InvalidPageSize.md)
- [foundry_sdk.v2.core.errors.InvalidPageSizeParameters](../../../../models/v2/core/errors/InvalidPageSizeParameters.md)
- [foundry_sdk.v2.core.models.GroupId](../../../../models/v2/core/models/GroupId.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/GroupMembership.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
