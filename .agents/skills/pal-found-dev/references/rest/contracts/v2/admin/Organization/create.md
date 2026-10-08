# v2.admin.Organization.create


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new Organization.

## SDK invocation contract

```python
def create(self, *, administrators: typing.List[core_models.PrincipalId], enrollment_rid: core_models.EnrollmentRid, name: admin_models.OrganizationName, description: typing.Optional[str]=None, host: typing.Optional[admin_models.HostName]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.Organization: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| administrators | typing.List[core_models.PrincipalId] | required | The initial administrators of the Organization. At least one principal must be provided. |
| enrollment_rid | core_models.EnrollmentRid | required | The RID of the Enrollment that this Organization belongs to. This must be provided. |
| name | admin_models.OrganizationName | required | Value shape and constraints are in its referenced local type definition. |
| description | typing.Optional[str] | None | Value shape and constraints are in its referenced local type definition. |
| host | typing.Optional[admin_models.HostName] | None | The primary host name of the Organization. This should be used when constructing URLs for users of this Organization. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateOrganizationMissingInitialAdminRole | At least one organization:administrator role grant must be provided when creating a organization. |
| CreateOrganizationPermissionDenied | Could not create the Organization. |
| EnrollmentNotFound | The given Enrollment could not be found. |
| OrganizationNameAlreadyExists | An organization with the same name already exists. |
| OrganizationNotFound | The given Organization could not be found. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/organizations'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
admin_models.CreateOrganizationRequest(administrators=administrators, enrollment_rid=enrollment_rid, name=name, host=host, description=description)
```

**response_type**

```python
admin_models.Organization
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CreateOrganizationMissingInitialAdminRole': admin_errors.CreateOrganizationMissingInitialAdminRole, 'CreateOrganizationPermissionDenied': admin_errors.CreateOrganizationPermissionDenied, 'EnrollmentNotFound': admin_errors.EnrollmentNotFound, 'OrganizationNameAlreadyExists': admin_errors.OrganizationNameAlreadyExists, 'OrganizationNotFound': admin_errors.OrganizationNotFound, 'PrincipalNotFound': admin_errors.PrincipalNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.Organization`. Ordinary async return: `typing.Awaitable[admin_models.Organization]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.Organization |
| sync_raw | ApiResponse[admin_models.Organization] |
| sync_streaming | StreamingContextManager[admin_models.Organization] |
| async_ordinary | typing.Awaitable[admin_models.Organization] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.Organization]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.Organization]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.CreateOrganizationMissingInitialAdminRole](../../../../models/v2/admin/errors/CreateOrganizationMissingInitialAdminRole.md)
- [foundry_sdk.v2.admin.errors.CreateOrganizationMissingInitialAdminRoleParameters](../../../../models/v2/admin/errors/CreateOrganizationMissingInitialAdminRoleParameters.md)
- [foundry_sdk.v2.admin.errors.CreateOrganizationPermissionDenied](../../../../models/v2/admin/errors/CreateOrganizationPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.CreateOrganizationPermissionDeniedParameters](../../../../models/v2/admin/errors/CreateOrganizationPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.EnrollmentNotFound](../../../../models/v2/admin/errors/EnrollmentNotFound.md)
- [foundry_sdk.v2.admin.errors.EnrollmentNotFoundParameters](../../../../models/v2/admin/errors/EnrollmentNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.OrganizationNameAlreadyExists](../../../../models/v2/admin/errors/OrganizationNameAlreadyExists.md)
- [foundry_sdk.v2.admin.errors.OrganizationNameAlreadyExistsParameters](../../../../models/v2/admin/errors/OrganizationNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFound](../../../../models/v2/admin/errors/OrganizationNotFound.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFoundParameters](../../../../models/v2/admin/errors/OrganizationNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFound](../../../../models/v2/admin/errors/PrincipalNotFound.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFoundParameters](../../../../models/v2/admin/errors/PrincipalNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.CreateOrganizationRequest](../../../../models/v2/admin/models/CreateOrganizationRequest.md)
- [foundry_sdk.v2.admin.models.HostName](../../../../models/v2/admin/models/HostName.md)
- [foundry_sdk.v2.admin.models.Organization](../../../../models/v2/admin/models/Organization.md)
- [foundry_sdk.v2.admin.models.OrganizationName](../../../../models/v2/admin/models/OrganizationName.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../../../models/v2/core/models/EnrollmentRid.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Organization.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
