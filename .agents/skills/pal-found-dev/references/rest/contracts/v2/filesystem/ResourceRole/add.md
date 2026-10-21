# v2.filesystem.ResourceRole.add


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning



## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Resource.Role.add`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def add(self, resource_rid: filesystem_models.ResourceRid, *, roles: typing.List[filesystem_models.ResourceRoleIdentifier], request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| resource_rid | filesystem_models.ResourceRid | required | Value shape and constraints are in its referenced local type definition. |
| roles | typing.List[filesystem_models.ResourceRoleIdentifier] | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AddResourceRolesPermissionDenied | Could not add the ResourceRole. |
| InvalidRoleIds | A roleId referenced in either default roles or role grants does not exist in the project role set for the space. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |
| ResourceNotFound | The given Resource could not be found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/filesystem/resources/{resourceRid}/roles/add'
```

**query_params**

```python
{}
```

**path_params**

```python
{'resourceRid': resource_rid}
```

**header_params**

```python
{'Content-Type': 'application/json'}
```

**body**

```python
filesystem_models.AddResourceRolesRequest(roles=roles)
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
{'AddResourceRolesPermissionDenied': filesystem_errors.AddResourceRolesPermissionDenied, 'InvalidRoleIds': filesystem_errors.InvalidRoleIds, 'PrincipalNotFound': admin_errors.PrincipalNotFound, 'ResourceNotFound': filesystem_errors.ResourceNotFound}
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
- [foundry_sdk.v2.admin.errors.PrincipalNotFound](../../../../models/v2/admin/errors/PrincipalNotFound.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFoundParameters](../../../../models/v2/admin/errors/PrincipalNotFoundParameters.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.RoleId](../../../../models/v2/core/models/RoleId.md)
- [foundry_sdk.v2.filesystem.errors.AddResourceRolesPermissionDenied](../../../../models/v2/filesystem/errors/AddResourceRolesPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.AddResourceRolesPermissionDeniedParameters](../../../../models/v2/filesystem/errors/AddResourceRolesPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidRoleIds](../../../../models/v2/filesystem/errors/InvalidRoleIds.md)
- [foundry_sdk.v2.filesystem.errors.InvalidRoleIdsParameters](../../../../models/v2/filesystem/errors/InvalidRoleIdsParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFound](../../../../models/v2/filesystem/errors/ResourceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFoundParameters](../../../../models/v2/filesystem/errors/ResourceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.AddResourceRolesRequest](../../../../models/v2/filesystem/models/AddResourceRolesRequest.md)
- [foundry_sdk.v2.filesystem.models.Everyone](../../../../models/v2/filesystem/models/Everyone.md)
- [foundry_sdk.v2.filesystem.models.PrincipalIdOnly](../../../../models/v2/filesystem/models/PrincipalIdOnly.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceRoleIdentifier](../../../../models/v2/filesystem/models/ResourceRoleIdentifier.md)
- [foundry_sdk.v2.filesystem.models.ResourceRolePrincipalIdentifier](../../../../models/v2/filesystem/models/ResourceRolePrincipalIdentifier.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/ResourceRole.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](add.md)
