# v2.admin.MarkingMember.remove


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning



## SDK invocation contract

```python
def remove(self, marking_id: core_models.MarkingId, *, principal_ids: typing.List[core_models.PrincipalId], request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| marking_id | core_models.MarkingId | required | Value shape and constraints are in its referenced local type definition. |
| principal_ids | typing.List[core_models.PrincipalId] | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetMarkingPermissionDenied | The provided token does not have permission to view the marking. |
| MarkingNotFound | The given Marking could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| RemoveMarkingMembersPermissionDenied | Could not remove the MarkingMember. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/markings/{markingId}/markingMembers/remove'
```

**query_params**

```python
{}
```

**path_params**

```python
{'markingId': marking_id}
```

**header_params**

```python
{'Content-Type': 'application/json'}
```

**body**

```python
admin_models.RemoveMarkingMembersRequest(principal_ids=principal_ids)
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
{'GetMarkingPermissionDenied': admin_errors.GetMarkingPermissionDenied, 'MarkingNotFound': admin_errors.MarkingNotFound, 'PrincipalNotFound': admin_errors.PrincipalNotFound, 'RemoveMarkingMembersPermissionDenied': admin_errors.RemoveMarkingMembersPermissionDenied}
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
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.GetMarkingPermissionDenied](../../../../models/v2/admin/errors/GetMarkingPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetMarkingPermissionDeniedParameters](../../../../models/v2/admin/errors/GetMarkingPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingNotFound](../../../../models/v2/admin/errors/MarkingNotFound.md)
- [foundry_sdk.v2.admin.errors.MarkingNotFoundParameters](../../../../models/v2/admin/errors/MarkingNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFound](../../../../models/v2/admin/errors/PrincipalNotFound.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFoundParameters](../../../../models/v2/admin/errors/PrincipalNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.RemoveMarkingMembersPermissionDenied](../../../../models/v2/admin/errors/RemoveMarkingMembersPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.RemoveMarkingMembersPermissionDeniedParameters](../../../../models/v2/admin/errors/RemoveMarkingMembersPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.RemoveMarkingMembersRequest](../../../../models/v2/admin/models/RemoveMarkingMembersRequest.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/MarkingMember.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](remove.md)
