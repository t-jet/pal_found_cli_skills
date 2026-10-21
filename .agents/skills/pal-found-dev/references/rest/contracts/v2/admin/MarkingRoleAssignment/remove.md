# v2.admin.MarkingRoleAssignment.remove


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Removes role assignments for the given Marking. For Organization markings, only the USE and DECLASSIFY
roles are supported; the ADMINISTER role must be managed via the Organization Role Assignment endpoints.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Marking.MarkingRoleAssignment.remove`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def remove(self, marking_id: core_models.MarkingId, *, role_assignments: typing.List[admin_models.MarkingRoleUpdate], request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| marking_id | core_models.MarkingId | required | Value shape and constraints are in its referenced local type definition. |
| role_assignments | typing.List[admin_models.MarkingRoleUpdate] | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetMarkingPermissionDenied | The provided token does not have permission to view the marking. |
| ListMarkingRoleAssignmentsPermissionDenied | The provided token does not have permission to list assigned roles for this marking. |
| MarkingNotFound | The given Marking could not be found. |
| OrganizationMarkingAdministerRoleNotSupported | The ADMINISTER role on Organization markings cannot be managed through the Marking Role Assignments endpoints. To manage administrator roles for an Organization, use the Organization Role Assignment endpoints instead. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| RemoveMarkingMembersPermissionDenied | Could not remove the MarkingMember. |
| RemoveMarkingRoleAssignmentsPermissionDenied | Could not remove the MarkingRoleAssignment. |
| RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed | You cannot remove all administrators from a marking. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/markings/{markingId}/roleAssignments/remove'
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
admin_models.RemoveMarkingRoleAssignmentsRequest(role_assignments=role_assignments)
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
{'GetMarkingPermissionDenied': admin_errors.GetMarkingPermissionDenied, 'ListMarkingRoleAssignmentsPermissionDenied': admin_errors.ListMarkingRoleAssignmentsPermissionDenied, 'MarkingNotFound': admin_errors.MarkingNotFound, 'OrganizationMarkingAdministerRoleNotSupported': admin_errors.OrganizationMarkingAdministerRoleNotSupported, 'PrincipalNotFound': admin_errors.PrincipalNotFound, 'RemoveMarkingMembersPermissionDenied': admin_errors.RemoveMarkingMembersPermissionDenied, 'RemoveMarkingRoleAssignmentsPermissionDenied': admin_errors.RemoveMarkingRoleAssignmentsPermissionDenied, 'RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed': admin_errors.RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed}
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
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.GetMarkingPermissionDenied](../../../../models/v2/admin/errors/GetMarkingPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetMarkingPermissionDeniedParameters](../../../../models/v2/admin/errors/GetMarkingPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.ListMarkingRoleAssignmentsPermissionDenied](../../../../models/v2/admin/errors/ListMarkingRoleAssignmentsPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ListMarkingRoleAssignmentsPermissionDeniedParameters](../../../../models/v2/admin/errors/ListMarkingRoleAssignmentsPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingNotFound](../../../../models/v2/admin/errors/MarkingNotFound.md)
- [foundry_sdk.v2.admin.errors.MarkingNotFoundParameters](../../../../models/v2/admin/errors/MarkingNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.OrganizationMarkingAdministerRoleNotSupported](../../../../models/v2/admin/errors/OrganizationMarkingAdministerRoleNotSupported.md)
- [foundry_sdk.v2.admin.errors.OrganizationMarkingAdministerRoleNotSupportedParameters](../../../../models/v2/admin/errors/OrganizationMarkingAdministerRoleNotSupportedParameters.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFound](../../../../models/v2/admin/errors/PrincipalNotFound.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFoundParameters](../../../../models/v2/admin/errors/PrincipalNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.RemoveMarkingMembersPermissionDenied](../../../../models/v2/admin/errors/RemoveMarkingMembersPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.RemoveMarkingMembersPermissionDeniedParameters](../../../../models/v2/admin/errors/RemoveMarkingMembersPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.RemoveMarkingRoleAssignmentsPermissionDenied](../../../../models/v2/admin/errors/RemoveMarkingRoleAssignmentsPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.RemoveMarkingRoleAssignmentsPermissionDeniedParameters](../../../../models/v2/admin/errors/RemoveMarkingRoleAssignmentsPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed](../../../../models/v2/admin/errors/RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowed.md)
- [foundry_sdk.v2.admin.errors.RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowedParameters](../../../../models/v2/admin/errors/RemoveMarkingRoleAssignmentsRemoveAllAdministratorsNotAllowedParameters.md)
- [foundry_sdk.v2.admin.models.MarkingRole](../../../../models/v2/admin/models/MarkingRole.md)
- [foundry_sdk.v2.admin.models.MarkingRoleUpdate](../../../../models/v2/admin/models/MarkingRoleUpdate.md)
- [foundry_sdk.v2.admin.models.RemoveMarkingRoleAssignmentsRequest](../../../../models/v2/admin/models/RemoveMarkingRoleAssignmentsRequest.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/MarkingRoleAssignment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](remove.md)
