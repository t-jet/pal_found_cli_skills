# v2.admin.OrganizationGuestMember.add


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Adds principals as guest members of an Organization. Attempting to add a primary member through this endpoint will not add the principal as a guest, but will still return a successful response.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Organization.OrganizationGuestMember.add`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def add(self, organization_rid: core_models.OrganizationRid, *, principal_ids: typing.List[core_models.PrincipalId], preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| organization_rid | core_models.OrganizationRid | required | Value shape and constraints are in its referenced local type definition. |
| principal_ids | typing.List[core_models.PrincipalId] | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AddOrganizationGuestMembersPermissionDenied | Could not add the OrganizationGuestMember. |
| OrganizationNotFound | The given Organization could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/organizations/{organizationRid}/guestMembers/add'
```

**query_params**

```python
{'preview': preview}
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
admin_models.AddOrganizationGuestMembersRequest(principal_ids=principal_ids)
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
{'AddOrganizationGuestMembersPermissionDenied': admin_errors.AddOrganizationGuestMembersPermissionDenied, 'OrganizationNotFound': admin_errors.OrganizationNotFound, 'PrincipalNotFound': admin_errors.PrincipalNotFound}
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
- [foundry_sdk.v2.admin.errors.AddOrganizationGuestMembersPermissionDenied](../../../../models/v2/admin/errors/AddOrganizationGuestMembersPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.AddOrganizationGuestMembersPermissionDeniedParameters](../../../../models/v2/admin/errors/AddOrganizationGuestMembersPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFound](../../../../models/v2/admin/errors/OrganizationNotFound.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFoundParameters](../../../../models/v2/admin/errors/OrganizationNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFound](../../../../models/v2/admin/errors/PrincipalNotFound.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFoundParameters](../../../../models/v2/admin/errors/PrincipalNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.AddOrganizationGuestMembersRequest](../../../../models/v2/admin/models/AddOrganizationGuestMembersRequest.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/OrganizationGuestMember.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](add.md)
