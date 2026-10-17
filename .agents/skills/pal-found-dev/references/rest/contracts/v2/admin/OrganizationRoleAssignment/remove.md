# v2.admin.OrganizationRoleAssignment.remove


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Remove roles from principals for the given Organization. At most 100 role assignments can be removed in a single request.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Organization.OrganizationRoleAssignment.remove`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def remove(self, organization_rid: core_models.OrganizationRid, *, role_assignments: typing.List[core_models.RoleAssignmentUpdate], request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| organization_rid | core_models.OrganizationRid | required | Value shape and constraints are in its referenced local type definition. |
| role_assignments | typing.List[core_models.RoleAssignmentUpdate] | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| OrganizationNotFound | The given Organization could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| RemoveOrganizationRoleAssignmentsPermissionDenied | Could not remove the OrganizationRoleAssignment. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/organizations/{organizationRid}/roleAssignments/remove'
```

**query_params**

```python
{}
```

**path_params**

```python
{'organizationRid': organization_rid}
```

**header_params**

```python
{'Content-Type': 'application/json'}
```

**body**

```python
admin_models.RemoveOrganizationRoleAssignmentsRequest(role_assignments=role_assignments)
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
{'OrganizationNotFound': admin_errors.OrganizationNotFound, 'PrincipalNotFound': admin_errors.PrincipalNotFound, 'RemoveOrganizationRoleAssignmentsPermissionDenied': admin_errors.RemoveOrganizationRoleAssignmentsPermissionDenied}
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
- [foundry_sdk.v2.admin.errors.OrganizationNotFound](../../../../models/v2/admin/errors/OrganizationNotFound.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFoundParameters](../../../../models/v2/admin/errors/OrganizationNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFound](../../../../models/v2/admin/errors/PrincipalNotFound.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFoundParameters](../../../../models/v2/admin/errors/PrincipalNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.RemoveOrganizationRoleAssignmentsPermissionDenied](../../../../models/v2/admin/errors/RemoveOrganizationRoleAssignmentsPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.RemoveOrganizationRoleAssignmentsPermissionDeniedParameters](../../../../models/v2/admin/errors/RemoveOrganizationRoleAssignmentsPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.RemoveOrganizationRoleAssignmentsRequest](../../../../models/v2/admin/models/RemoveOrganizationRoleAssignmentsRequest.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.RoleAssignmentUpdate](../../../../models/v2/core/models/RoleAssignmentUpdate.md)
- [foundry_sdk.v2.core.models.RoleId](../../../../models/v2/core/models/RoleId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/OrganizationRoleAssignment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](remove.md)
