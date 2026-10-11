# v2.admin.Marking.create


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new Marking.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Marking.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, *, category_id: admin_models.MarkingCategoryId, initial_members: typing.List[core_models.PrincipalId], initial_role_assignments: typing.List[admin_models.MarkingRoleUpdate], name: admin_models.MarkingName, description: typing.Optional[str]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.Marking: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| category_id | admin_models.MarkingCategoryId | required | Value shape and constraints are in its referenced local type definition. |
| initial_members | typing.List[core_models.PrincipalId] | required | Users and Groups that will be able to view resources protected by this Marking. This can be changed later through the MarkingMember operations. |
| initial_role_assignments | typing.List[admin_models.MarkingRoleUpdate] | required | The initial roles that will be assigned when the Marking is created. At least one ADMINISTER role must be provided. This can be changed later through the MarkingRoleAssignment operations. WARNING: If you do not include your own principal ID or the ID of a Group that you are a member of, you will create a Marking that you cannot administer. |
| name | admin_models.MarkingName | required | Value shape and constraints are in its referenced local type definition. |
| description | typing.Optional[str] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateMarkingMissingInitialAdminRole | At least one ADMINISTER role assignment must be provided when creating a marking. |
| CreateMarkingPermissionDenied | Could not create the Marking. |
| GetMarkingCategoryPermissionDenied | The provided token does not have permission to view the marking category. |
| MarkingCategoryNotFound | The given MarkingCategory could not be found. |
| MarkingNameInCategoryAlreadyExists | A marking with the same name already exists in the category. |
| MarkingNameIsEmpty | The marking name is empty. |
| PrincipalNotFound | A principal (User or Group) with the given PrincipalId could not be found |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/markings'
```

**query_params**

```python
{}
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
admin_models.CreateMarkingRequest(initial_role_assignments=initial_role_assignments, initial_members=initial_members, name=name, description=description, category_id=category_id)
```

**response_type**

```python
admin_models.Marking
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CreateMarkingMissingInitialAdminRole': admin_errors.CreateMarkingMissingInitialAdminRole, 'CreateMarkingPermissionDenied': admin_errors.CreateMarkingPermissionDenied, 'GetMarkingCategoryPermissionDenied': admin_errors.GetMarkingCategoryPermissionDenied, 'MarkingCategoryNotFound': admin_errors.MarkingCategoryNotFound, 'MarkingNameInCategoryAlreadyExists': admin_errors.MarkingNameInCategoryAlreadyExists, 'MarkingNameIsEmpty': admin_errors.MarkingNameIsEmpty, 'PrincipalNotFound': admin_errors.PrincipalNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.Marking`. Ordinary async return: `typing.Awaitable[admin_models.Marking]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.Marking |
| sync_raw | ApiResponse[admin_models.Marking] |
| sync_streaming | StreamingContextManager[admin_models.Marking] |
| async_ordinary | typing.Awaitable[admin_models.Marking] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.Marking]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.Marking]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.CreateMarkingMissingInitialAdminRole](../../../../models/v2/admin/errors/CreateMarkingMissingInitialAdminRole.md)
- [foundry_sdk.v2.admin.errors.CreateMarkingMissingInitialAdminRoleParameters](../../../../models/v2/admin/errors/CreateMarkingMissingInitialAdminRoleParameters.md)
- [foundry_sdk.v2.admin.errors.CreateMarkingPermissionDenied](../../../../models/v2/admin/errors/CreateMarkingPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.CreateMarkingPermissionDeniedParameters](../../../../models/v2/admin/errors/CreateMarkingPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.GetMarkingCategoryPermissionDenied](../../../../models/v2/admin/errors/GetMarkingCategoryPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetMarkingCategoryPermissionDeniedParameters](../../../../models/v2/admin/errors/GetMarkingCategoryPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingCategoryNotFound](../../../../models/v2/admin/errors/MarkingCategoryNotFound.md)
- [foundry_sdk.v2.admin.errors.MarkingCategoryNotFoundParameters](../../../../models/v2/admin/errors/MarkingCategoryNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingNameInCategoryAlreadyExists](../../../../models/v2/admin/errors/MarkingNameInCategoryAlreadyExists.md)
- [foundry_sdk.v2.admin.errors.MarkingNameInCategoryAlreadyExistsParameters](../../../../models/v2/admin/errors/MarkingNameInCategoryAlreadyExistsParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingNameIsEmpty](../../../../models/v2/admin/errors/MarkingNameIsEmpty.md)
- [foundry_sdk.v2.admin.errors.MarkingNameIsEmptyParameters](../../../../models/v2/admin/errors/MarkingNameIsEmptyParameters.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFound](../../../../models/v2/admin/errors/PrincipalNotFound.md)
- [foundry_sdk.v2.admin.errors.PrincipalNotFoundParameters](../../../../models/v2/admin/errors/PrincipalNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.CreateMarkingRequest](../../../../models/v2/admin/models/CreateMarkingRequest.md)
- [foundry_sdk.v2.admin.models.Marking](../../../../models/v2/admin/models/Marking.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryId](../../../../models/v2/admin/models/MarkingCategoryId.md)
- [foundry_sdk.v2.admin.models.MarkingName](../../../../models/v2/admin/models/MarkingName.md)
- [foundry_sdk.v2.admin.models.MarkingRole](../../../../models/v2/admin/models/MarkingRole.md)
- [foundry_sdk.v2.admin.models.MarkingRoleUpdate](../../../../models/v2/admin/models/MarkingRoleUpdate.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Marking.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
