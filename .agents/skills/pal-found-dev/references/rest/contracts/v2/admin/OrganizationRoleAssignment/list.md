# v2.admin.OrganizationRoleAssignment.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List all principals who are assigned a role for the given Organization.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Organization.OrganizationRoleAssignment.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, organization_rid: core_models.OrganizationRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.ListOrganizationRoleAssignmentsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| organization_rid | core_models.OrganizationRid | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ListOrganizationRoleAssignmentsPermissionDenied | The provided token does not have permission to list assigned roles for this organization. |
| OrganizationNotFound | The given Organization could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/organizations/{organizationRid}/roleAssignments'
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
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
admin_models.ListOrganizationRoleAssignmentsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ListOrganizationRoleAssignmentsPermissionDenied': admin_errors.ListOrganizationRoleAssignmentsPermissionDenied, 'OrganizationNotFound': admin_errors.OrganizationNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.ListOrganizationRoleAssignmentsResponse`. Ordinary async return: `typing.Awaitable[admin_models.ListOrganizationRoleAssignmentsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.ListOrganizationRoleAssignmentsResponse |
| sync_raw | ApiResponse[admin_models.ListOrganizationRoleAssignmentsResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListOrganizationRoleAssignmentsResponse] |
| async_ordinary | typing.Awaitable[admin_models.ListOrganizationRoleAssignmentsResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListOrganizationRoleAssignmentsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListOrganizationRoleAssignmentsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.ListOrganizationRoleAssignmentsPermissionDenied](../../../../models/v2/admin/errors/ListOrganizationRoleAssignmentsPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ListOrganizationRoleAssignmentsPermissionDeniedParameters](../../../../models/v2/admin/errors/ListOrganizationRoleAssignmentsPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFound](../../../../models/v2/admin/errors/OrganizationNotFound.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFoundParameters](../../../../models/v2/admin/errors/OrganizationNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.ListOrganizationRoleAssignmentsResponse](../../../../models/v2/admin/models/ListOrganizationRoleAssignmentsResponse.md)
- [foundry_sdk.v2.admin.models.OrganizationRoleAssignment](../../../../models/v2/admin/models/OrganizationRoleAssignment.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.PrincipalType](../../../../models/v2/core/models/PrincipalType.md)
- [foundry_sdk.v2.core.models.RoleId](../../../../models/v2/core/models/RoleId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/OrganizationRoleAssignment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
