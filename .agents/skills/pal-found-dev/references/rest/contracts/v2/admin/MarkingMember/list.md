# v2.admin.MarkingMember.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all principals who can view resources protected by the given Marking. Ignores the `pageSize` parameter.
Requires `api:admin-write` because only marking administrators can view marking members.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Marking.MarkingMember.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, marking_id: core_models.MarkingId, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, transitive: typing.Optional[bool]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[admin_models.MarkingMember]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| marking_id | core_models.MarkingId | required | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| transitive | typing.Optional[bool] | None | When true, includes the transitive members of groups contained within groups that are members of this Marking. For example, say the Marking has member Group A, and Group A has member User B. If `transitive=false` only Group A will be returned, but if `transitive=true` then Group A and User B will be returned. This will recursively resolve Groups through all layers of nesting. Defaults to false. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetMarkingPermissionDenied | The provided token does not have permission to view the marking. |
| ListMarkingMembersPermissionDenied | The provided token does not have permission to list the members of this marking. |
| MarkingNotFound | The given Marking could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/markings/{markingId}/markingMembers'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token, 'transitive': transitive}
```

**path_params**

```python
{'markingId': marking_id}
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
admin_models.ListMarkingMembersResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetMarkingPermissionDenied': admin_errors.GetMarkingPermissionDenied, 'ListMarkingMembersPermissionDenied': admin_errors.ListMarkingMembersPermissionDenied, 'MarkingNotFound': admin_errors.MarkingNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[admin_models.MarkingMember]`. Ordinary async return: `core.AsyncResourceIterator[admin_models.MarkingMember]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[admin_models.MarkingMember] |
| sync_raw | ApiResponse[admin_models.ListMarkingMembersResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListMarkingMembersResponse] |
| async_ordinary | core.AsyncResourceIterator[admin_models.MarkingMember] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListMarkingMembersResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListMarkingMembersResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.GetMarkingPermissionDenied](../../../../models/v2/admin/errors/GetMarkingPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetMarkingPermissionDeniedParameters](../../../../models/v2/admin/errors/GetMarkingPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.ListMarkingMembersPermissionDenied](../../../../models/v2/admin/errors/ListMarkingMembersPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ListMarkingMembersPermissionDeniedParameters](../../../../models/v2/admin/errors/ListMarkingMembersPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingNotFound](../../../../models/v2/admin/errors/MarkingNotFound.md)
- [foundry_sdk.v2.admin.errors.MarkingNotFoundParameters](../../../../models/v2/admin/errors/MarkingNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.ListMarkingMembersResponse](../../../../models/v2/admin/models/ListMarkingMembersResponse.md)
- [foundry_sdk.v2.admin.models.MarkingMember](../../../../models/v2/admin/models/MarkingMember.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.PrincipalType](../../../../models/v2/core/models/PrincipalType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/MarkingMember.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
