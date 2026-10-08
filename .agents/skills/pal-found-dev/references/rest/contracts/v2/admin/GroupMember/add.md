# v2.admin.GroupMember.add


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning



## SDK invocation contract

```python
def add(self, group_id: core_models.GroupId, *, principal_ids: typing.List[core_models.PrincipalId], expiration: typing.Optional[admin_models.GroupMembershipExpiration]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| group_id | core_models.GroupId | required | Value shape and constraints are in its referenced local type definition. |
| principal_ids | typing.List[core_models.PrincipalId] | required | Value shape and constraints are in its referenced local type definition. |
| expiration | typing.Optional[admin_models.GroupMembershipExpiration] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AddGroupMembersPermissionDenied | Could not add the GroupMember. |
| GroupNotFound | The given Group could not be found. |
| InvalidGroupMembershipExpiration | The member expiration you provided does not conform to the Group's requirements for member expirations. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/groups/{groupId}/groupMembers/add'
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
{'Content-Type': 'application/json'}
```

**body**

```python
admin_models.AddGroupMembersRequest(principal_ids=principal_ids, expiration=expiration)
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
{'AddGroupMembersPermissionDenied': admin_errors.AddGroupMembersPermissionDenied, 'GroupNotFound': admin_errors.GroupNotFound, 'InvalidGroupMembershipExpiration': admin_errors.InvalidGroupMembershipExpiration, 'PrincipalNotFound': admin_errors.PrincipalNotFound}
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
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.AddGroupMembersPermissionDenied](../../../../models/v2/admin/errors/AddGroupMembersPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.AddGroupMembersPermissionDeniedParameters](../../../../models/v2/admin/errors/AddGroupMembersPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.GroupNotFound](../../../../models/v2/admin/errors/GroupNotFound.md)
- [foundry_sdk.v2.admin.errors.GroupNotFoundParameters](../../../../models/v2/admin/errors/GroupNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.InvalidGroupMembershipExpiration](../../../../models/v2/admin/errors/InvalidGroupMembershipExpiration.md)
- [foundry_sdk.v2.admin.errors.InvalidGroupMembershipExpirationParameters](../../../../models/v2/admin/errors/InvalidGroupMembershipExpirationParameters.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFound](../../../../models/v2/admin/errors/PrincipalNotFound.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFoundParameters](../../../../models/v2/admin/errors/PrincipalNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.AddGroupMembersRequest](../../../../models/v2/admin/models/AddGroupMembersRequest.md)
- [foundry_sdk.v2.admin.models.GroupMembershipExpiration](../../../../models/v2/admin/models/GroupMembershipExpiration.md)
- [foundry_sdk.v2.core.models.DurationSeconds](../../../../models/v2/core/models/DurationSeconds.md)
- [foundry_sdk.v2.core.models.GroupId](../../../../models/v2/core/models/GroupId.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/GroupMember.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](add.md)
