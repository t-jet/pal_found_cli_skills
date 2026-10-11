# v2.admin.Organization.list_available_roles


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List all roles that can be assigned to a principal for the given Organization.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Organization.list_available_roles`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list_available_roles(self, organization_rid: core_models.OrganizationRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.ListAvailableOrganizationRolesResponse: ...
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
| ListAvailableRolesOrganizationPermissionDenied | Could not listAvailableRoles the Organization. |
| OrganizationNotFound | The given Organization could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/organizations/{organizationRid}/listAvailableRoles'
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
admin_models.ListAvailableOrganizationRolesResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ListAvailableRolesOrganizationPermissionDenied': admin_errors.ListAvailableRolesOrganizationPermissionDenied, 'OrganizationNotFound': admin_errors.OrganizationNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.ListAvailableOrganizationRolesResponse`. Ordinary async return: `typing.Awaitable[admin_models.ListAvailableOrganizationRolesResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.ListAvailableOrganizationRolesResponse |
| sync_raw | ApiResponse[admin_models.ListAvailableOrganizationRolesResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListAvailableOrganizationRolesResponse] |
| async_ordinary | typing.Awaitable[admin_models.ListAvailableOrganizationRolesResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListAvailableOrganizationRolesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListAvailableOrganizationRolesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.admin.errors.ListAvailableRolesOrganizationPermissionDenied](../../../../models/v2/admin/errors/ListAvailableRolesOrganizationPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ListAvailableRolesOrganizationPermissionDeniedParameters](../../../../models/v2/admin/errors/ListAvailableRolesOrganizationPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFound](../../../../models/v2/admin/errors/OrganizationNotFound.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFoundParameters](../../../../models/v2/admin/errors/OrganizationNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.ListAvailableOrganizationRolesResponse](../../../../models/v2/admin/models/ListAvailableOrganizationRolesResponse.md)
- [foundry_sdk.v2.core.models.Operation](../../../../models/v2/core/models/Operation.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.Role](../../../../models/v2/core/models/Role.md)
- [foundry_sdk.v2.core.models.RoleContext](../../../../models/v2/core/models/RoleContext.md)
- [foundry_sdk.v2.core.models.RoleId](../../../../models/v2/core/models/RoleId.md)
- [foundry_sdk.v2.core.models.RoleSetId](../../../../models/v2/core/models/RoleSetId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Organization.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list_available_roles.md)
