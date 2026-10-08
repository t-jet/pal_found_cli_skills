# v2.admin.OrganizationGuestMember.list


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all guest members of an Organization.

## SDK invocation contract

```python
def list(self, organization_rid: core_models.OrganizationRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.ListOrganizationGuestMembersResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| organization_rid | core_models.OrganizationRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ListOrganizationGuestMembersPermissionDenied | The provided token does not have permission to list guest members for this organization. |
| OrganizationNotFound | The given Organization could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/organizations/{organizationRid}/guestMembers'
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
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
admin_models.ListOrganizationGuestMembersResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ListOrganizationGuestMembersPermissionDenied': admin_errors.ListOrganizationGuestMembersPermissionDenied, 'OrganizationNotFound': admin_errors.OrganizationNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.ListOrganizationGuestMembersResponse`. Ordinary async return: `typing.Awaitable[admin_models.ListOrganizationGuestMembersResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.ListOrganizationGuestMembersResponse |
| sync_raw | ApiResponse[admin_models.ListOrganizationGuestMembersResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListOrganizationGuestMembersResponse] |
| async_ordinary | typing.Awaitable[admin_models.ListOrganizationGuestMembersResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListOrganizationGuestMembersResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListOrganizationGuestMembersResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.ListOrganizationGuestMembersPermissionDenied](../../../../models/v2/admin/errors/ListOrganizationGuestMembersPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ListOrganizationGuestMembersPermissionDeniedParameters](../../../../models/v2/admin/errors/ListOrganizationGuestMembersPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFound](../../../../models/v2/admin/errors/OrganizationNotFound.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFoundParameters](../../../../models/v2/admin/errors/OrganizationNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.ListOrganizationGuestMembersResponse](../../../../models/v2/admin/models/ListOrganizationGuestMembersResponse.md)
- [foundry_sdk.v2.admin.models.OrganizationGuestMember](../../../../models/v2/admin/models/OrganizationGuestMember.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.PrincipalType](../../../../models/v2/core/models/PrincipalType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/OrganizationGuestMember.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
