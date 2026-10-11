# v2.admin.MarkingRoleAssignment.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List all principals who are assigned a role for the given Marking. Ignores the `pageSize` parameter.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Marking.MarkingRoleAssignment.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, marking_id: core_models.MarkingId, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[admin_models.MarkingRoleAssignment]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| marking_id | core_models.MarkingId | required | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ListMarkingRoleAssignmentsPermissionDenied | The provided token does not have permission to list assigned roles for this marking. |
| MarkingNotFound | The given Marking could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/markings/{markingId}/roleAssignments'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token}
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
admin_models.ListMarkingRoleAssignmentsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ListMarkingRoleAssignmentsPermissionDenied': admin_errors.ListMarkingRoleAssignmentsPermissionDenied, 'MarkingNotFound': admin_errors.MarkingNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[admin_models.MarkingRoleAssignment]`. Ordinary async return: `core.AsyncResourceIterator[admin_models.MarkingRoleAssignment]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[admin_models.MarkingRoleAssignment] |
| sync_raw | ApiResponse[admin_models.ListMarkingRoleAssignmentsResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListMarkingRoleAssignmentsResponse] |
| async_ordinary | core.AsyncResourceIterator[admin_models.MarkingRoleAssignment] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListMarkingRoleAssignmentsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListMarkingRoleAssignmentsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.ListMarkingRoleAssignmentsPermissionDenied](../../../../models/v2/admin/errors/ListMarkingRoleAssignmentsPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ListMarkingRoleAssignmentsPermissionDeniedParameters](../../../../models/v2/admin/errors/ListMarkingRoleAssignmentsPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingNotFound](../../../../models/v2/admin/errors/MarkingNotFound.md)
- [foundry_sdk.v2.admin.errors.MarkingNotFoundParameters](../../../../models/v2/admin/errors/MarkingNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.ListMarkingRoleAssignmentsResponse](../../../../models/v2/admin/models/ListMarkingRoleAssignmentsResponse.md)
- [foundry_sdk.v2.admin.models.MarkingRole](../../../../models/v2/admin/models/MarkingRole.md)
- [foundry_sdk.v2.admin.models.MarkingRoleAssignment](../../../../models/v2/admin/models/MarkingRoleAssignment.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.PrincipalType](../../../../models/v2/core/models/PrincipalType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/MarkingRoleAssignment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
