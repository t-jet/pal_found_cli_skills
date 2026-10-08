# v2.admin.MarkingCategory.create


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new MarkingCategory.

## SDK invocation contract

```python
def create(self, *, description: admin_models.MarkingCategoryDescription, initial_permissions: admin_models.MarkingCategoryPermissions, name: admin_models.MarkingCategoryName, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.MarkingCategory: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| description | admin_models.MarkingCategoryDescription | required | Value shape and constraints are in its referenced local type definition. |
| initial_permissions | admin_models.MarkingCategoryPermissions | required | The initial permissions for the Marking Category. This can be changed later through MarkingCategoryPermission operations. The provided permissions must include at least one ADMINISTER role assignment. WARNING: If you do not list your own principal ID or the ID of a Group that you are a member of as an ADMINISTER, you will create a Marking Category that you cannot administer. |
| name | admin_models.MarkingCategoryName | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateMarkingCategoryMissingInitialAdminRole | At least one ADMINISTER role assignment must be provided when creating a marking category. |
| CreateMarkingCategoryMissingOrganization | At least one organization must be provided when creating a marking category. |
| CreateMarkingCategoryPermissionDenied | Could not create the MarkingCategory. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/markingCategories'
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
admin_models.CreateMarkingCategoryRequest(initial_permissions=initial_permissions, name=name, description=description)
```

**response_type**

```python
admin_models.MarkingCategory
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CreateMarkingCategoryMissingInitialAdminRole': admin_errors.CreateMarkingCategoryMissingInitialAdminRole, 'CreateMarkingCategoryMissingOrganization': admin_errors.CreateMarkingCategoryMissingOrganization, 'CreateMarkingCategoryPermissionDenied': admin_errors.CreateMarkingCategoryPermissionDenied, 'PrincipalNotFound': admin_errors.PrincipalNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.MarkingCategory`. Ordinary async return: `typing.Awaitable[admin_models.MarkingCategory]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.MarkingCategory |
| sync_raw | ApiResponse[admin_models.MarkingCategory] |
| sync_streaming | StreamingContextManager[admin_models.MarkingCategory] |
| async_ordinary | typing.Awaitable[admin_models.MarkingCategory] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.MarkingCategory]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.MarkingCategory]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.CreateMarkingCategoryMissingInitialAdminRole](../../../../models/v2/admin/errors/CreateMarkingCategoryMissingInitialAdminRole.md)
- [foundry_sdk.v2.admin.errors.CreateMarkingCategoryMissingInitialAdminRoleParameters](../../../../models/v2/admin/errors/CreateMarkingCategoryMissingInitialAdminRoleParameters.md)
- [foundry_sdk.v2.admin.errors.CreateMarkingCategoryMissingOrganization](../../../../models/v2/admin/errors/CreateMarkingCategoryMissingOrganization.md)
- [foundry_sdk.v2.admin.errors.CreateMarkingCategoryMissingOrganizationParameters](../../../../models/v2/admin/errors/CreateMarkingCategoryMissingOrganizationParameters.md)
- [foundry_sdk.v2.admin.errors.CreateMarkingCategoryPermissionDenied](../../../../models/v2/admin/errors/CreateMarkingCategoryPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.CreateMarkingCategoryPermissionDeniedParameters](../../../../models/v2/admin/errors/CreateMarkingCategoryPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFound](../../../../models/v2/admin/errors/PrincipalNotFound.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFoundParameters](../../../../models/v2/admin/errors/PrincipalNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.CreateMarkingCategoryRequest](../../../../models/v2/admin/models/CreateMarkingCategoryRequest.md)
- [foundry_sdk.v2.admin.models.MarkingCategory](../../../../models/v2/admin/models/MarkingCategory.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryDescription](../../../../models/v2/admin/models/MarkingCategoryDescription.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryId](../../../../models/v2/admin/models/MarkingCategoryId.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryName](../../../../models/v2/admin/models/MarkingCategoryName.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryPermissions](../../../../models/v2/admin/models/MarkingCategoryPermissions.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryPermissionsIsPublic](../../../../models/v2/admin/models/MarkingCategoryPermissionsIsPublic.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryRole](../../../../models/v2/admin/models/MarkingCategoryRole.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryRoleAssignment](../../../../models/v2/admin/models/MarkingCategoryRoleAssignment.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryType](../../../../models/v2/admin/models/MarkingCategoryType.md)
- [foundry_sdk.v2.admin.models.MarkingType](../../../../models/v2/admin/models/MarkingType.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/MarkingCategory.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
