# v2.admin.GroupMember.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all members (which can be a User or a Group) of a given Group.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However,
it is guaranteed that if there are more results available, the `nextPageToken` field will be populated.
To get the next page, make the same request again, but set the value of the `pageToken` query parameter
to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field
in the response, you are on the last page.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Group.GroupMember.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, group_id: core_models.GroupId, *, include_expirations: typing.Optional[bool]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, transitive: typing.Optional[bool]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[admin_models.GroupMember]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| group_id | core_models.GroupId | required | Value shape and constraints are in its referenced local type definition. |
| include_expirations | typing.Optional[bool] | None | When true, includes the expiration time of any temporary members of this group. `includeExpirations` cannot be set to true if `transitive` is also set to true. Defaults to false. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| transitive | typing.Optional[bool] | None | When true, includes the transitive members of groups contained within this group. For example, say the Group has member Group A, and Group A has member User B. If `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B will be returned. This will recursively resolve Groups through all layers of nesting. If `transitive` is true, `includeExpirations` cannot also be set to true. Defaults to false. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ExpirationForTransitiveGroupMembersNotSupported | You cannot pass includeExpirations if transitive is true. |
| GroupNotFound | The given Group could not be found. |
| InvalidPageSize | The provided page size was zero or negative. Page sizes must be greater than zero. |
| ListGroupMembersPermissionDenied | The provided token does not have permission to view the members of the given group. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/groups/{groupId}/groupMembers'
```

**query_params**

```python
{'includeExpirations': include_expirations, 'pageSize': page_size, 'pageToken': page_token, 'transitive': transitive}
```

**path_params**

```python
{'groupId': group_id}
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
admin_models.ListGroupMembersResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ExpirationForTransitiveGroupMembersNotSupported': admin_errors.ExpirationForTransitiveGroupMembersNotSupported, 'GroupNotFound': admin_errors.GroupNotFound, 'InvalidPageSize': core_errors.InvalidPageSize, 'ListGroupMembersPermissionDenied': admin_errors.ListGroupMembersPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[admin_models.GroupMember]`. Ordinary async return: `core.AsyncResourceIterator[admin_models.GroupMember]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[admin_models.GroupMember] |
| sync_raw | ApiResponse[admin_models.ListGroupMembersResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListGroupMembersResponse] |
| async_ordinary | core.AsyncResourceIterator[admin_models.GroupMember] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListGroupMembersResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListGroupMembersResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.ExpirationForTransitiveGroupMembersNotSupported](../../../../models/v2/admin/errors/ExpirationForTransitiveGroupMembersNotSupported.md)
- [foundry_sdk.v2.admin.errors.ExpirationForTransitiveGroupMembersNotSupportedParameters](../../../../models/v2/admin/errors/ExpirationForTransitiveGroupMembersNotSupportedParameters.md)
- [foundry_sdk.v2.admin.errors.GroupNotFound](../../../../models/v2/admin/errors/GroupNotFound.md)
- [foundry_sdk.v2.admin.errors.GroupNotFoundParameters](../../../../models/v2/admin/errors/GroupNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.ListGroupMembersPermissionDenied](../../../../models/v2/admin/errors/ListGroupMembersPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ListGroupMembersPermissionDeniedParameters](../../../../models/v2/admin/errors/ListGroupMembersPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.GroupMember](../../../../models/v2/admin/models/GroupMember.md)
- [foundry_sdk.v2.admin.models.GroupMembershipExpiration](../../../../models/v2/admin/models/GroupMembershipExpiration.md)
- [foundry_sdk.v2.admin.models.ListGroupMembersResponse](../../../../models/v2/admin/models/ListGroupMembersResponse.md)
- [foundry_sdk.v2.core.errors.InvalidPageSize](../../../../models/v2/core/errors/InvalidPageSize.md)
- [foundry_sdk.v2.core.errors.InvalidPageSizeParameters](../../../../models/v2/core/errors/InvalidPageSizeParameters.md)
- [foundry_sdk.v2.core.models.GroupId](../../../../models/v2/core/models/GroupId.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.PrincipalType](../../../../models/v2/core/models/PrincipalType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/GroupMember.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
