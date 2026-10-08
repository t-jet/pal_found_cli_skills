# v2.admin.EnrollmentRoleAssignment.remove


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Remove roles from principals for the given Enrollment. At most 100 role assignments can be removed in a single request.

## SDK invocation contract

```python
def remove(self, enrollment_rid: core_models.EnrollmentRid, *, role_assignments: typing.List[core_models.RoleAssignmentUpdate], preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| enrollment_rid | core_models.EnrollmentRid | required | Value shape and constraints are in its referenced local type definition. |
| role_assignments | typing.List[core_models.RoleAssignmentUpdate] | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| EnrollmentNotFound | The given Enrollment could not be found. |
| EnrollmentRoleNotFound | One of the provided role IDs was not found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| RemoveEnrollmentRoleAssignmentsPermissionDenied | Could not remove the EnrollmentRoleAssignment. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/enrollments/{enrollmentRid}/roleAssignments/remove'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'enrollmentRid': enrollment_rid}
```

**header_params**

```python
{'Content-Type': 'application/json'}
```

**body**

```python
admin_models.RemoveEnrollmentRoleAssignmentsRequest(role_assignments=role_assignments)
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
{'EnrollmentNotFound': admin_errors.EnrollmentNotFound, 'EnrollmentRoleNotFound': admin_errors.EnrollmentRoleNotFound, 'PrincipalNotFound': admin_errors.PrincipalNotFound, 'RemoveEnrollmentRoleAssignmentsPermissionDenied': admin_errors.RemoveEnrollmentRoleAssignmentsPermissionDenied}
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
- [foundry_sdk.v2.admin.errors.EnrollmentNotFound](../../../../models/v2/admin/errors/EnrollmentNotFound.md)
- [foundry_sdk.v2.admin.errors.EnrollmentNotFoundParameters](../../../../models/v2/admin/errors/EnrollmentNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.EnrollmentRoleNotFound](../../../../models/v2/admin/errors/EnrollmentRoleNotFound.md)
- [foundry_sdk.v2.admin.errors.EnrollmentRoleNotFoundParameters](../../../../models/v2/admin/errors/EnrollmentRoleNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFound](../../../../models/v2/admin/errors/PrincipalNotFound.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFoundParameters](../../../../models/v2/admin/errors/PrincipalNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.RemoveEnrollmentRoleAssignmentsPermissionDenied](../../../../models/v2/admin/errors/RemoveEnrollmentRoleAssignmentsPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.RemoveEnrollmentRoleAssignmentsPermissionDeniedParameters](../../../../models/v2/admin/errors/RemoveEnrollmentRoleAssignmentsPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.RemoveEnrollmentRoleAssignmentsRequest](../../../../models/v2/admin/models/RemoveEnrollmentRoleAssignmentsRequest.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../../../models/v2/core/models/EnrollmentRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.RoleAssignmentUpdate](../../../../models/v2/core/models/RoleAssignmentUpdate.md)
- [foundry_sdk.v2.core.models.RoleId](../../../../models/v2/core/models/RoleId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/EnrollmentRoleAssignment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](remove.md)
