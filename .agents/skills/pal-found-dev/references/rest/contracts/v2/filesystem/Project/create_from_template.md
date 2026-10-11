# v2.filesystem.Project.create_from_template


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a project from a project template.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Project.create_from_template`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create_from_template(self, *, template_rid: filesystem_models.ProjectTemplateRid, variable_values: typing.Dict[filesystem_models.ProjectTemplateVariableId, filesystem_models.ProjectTemplateVariableValue], default_roles: typing.Optional[typing.List[core_models.RoleId]]=None, organization_rids: typing.Optional[typing.List[core_models.OrganizationRid]]=None, project_description: typing.Optional[str]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> filesystem_models.Project: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| template_rid | filesystem_models.ProjectTemplateRid | required | Value shape and constraints are in its referenced local type definition. |
| variable_values | typing.Dict[filesystem_models.ProjectTemplateVariableId, filesystem_models.ProjectTemplateVariableValue] | required | Value shape and constraints are in its referenced local type definition. |
| default_roles | typing.Optional[typing.List[core_models.RoleId]] | None | Value shape and constraints are in its referenced local type definition. |
| organization_rids | typing.Optional[typing.List[core_models.OrganizationRid]] | None | Value shape and constraints are in its referenced local type definition. |
| project_description | typing.Optional[str] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AddGroupToParentGroupPermissionDenied | The user is not authorized to add a a group to the parent group required to create the project from template. |
| CreateGroupPermissionDenied | The user is not authorized to create the group in the organization required to create the project from template. |
| CreateProjectFromTemplatePermissionDenied | Could not createFromTemplate the Project. |
| CreateProjectNoOwnerLikeRoleGrant | The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role. |
| DefaultRolesNotInSpaceRoleSet | The requested default roles are not in the role set of the space for the project template. |
| InvalidDefaultRoles | Either the user has not passed default roles for a template with suggested default roles, or has passed default roles for a template with fixed default roles. |
| InvalidDescription | Either the user has not passed a value for a template with unset project description, or has passed a value for a template with fixed project description. |
| InvalidOrganizationHierarchy | Organizations on a project must also exist on the parent space. This error is thrown if the configuration of a project's organizations (on creation or subsequently) results in the project being marked with either no organizations in a marked space, or with an organization that is not present on the parent space. |
| InvalidOrganizations | Either the user has not passed organizations for a template with suggested organizations, or has passed organization for a template with fixed organizations. |
| InvalidPrincipalIdsForGroupTemplate | The template requested for project creation contains principal IDs that do not exist. |
| InvalidVariable | A variable referenced in the request to create project from template is not defined on the template. |
| InvalidVariableEnumOption | The value passed in the request to create project from template for an enum type variable is not a valid option. |
| MissingVariableValue | A variable defined on the template requested for project creation does not have a value set in the request. |
| NotAuthorizedToApplyOrganization | The user is not authorized to apply at least one of the organization markings required to create the project from template. |
| OrganizationsNotFound | At least one organization RID could not be found. |
| ProjectNotFound | The given Project could not be found. |
| ProjectTemplateNotFound | The project template RID referenced cannot be found. |
| TemplateGroupNameConflict | Creating the project from template would attempt to create new groups with names conflicting either with other new groups, or existing groups. |
| TemplateMarkingNameConflict | Creating the project from template would attempt to create new markings with names conflicting either with other new markings, or existing markings. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/filesystem/projects/createFromTemplate'
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
filesystem_models.CreateProjectFromTemplateRequest(template_rid=template_rid, variable_values=variable_values, default_roles=default_roles, organization_rids=organization_rids, project_description=project_description)
```

**response_type**

```python
filesystem_models.Project
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AddGroupToParentGroupPermissionDenied': filesystem_errors.AddGroupToParentGroupPermissionDenied, 'CreateGroupPermissionDenied': filesystem_errors.CreateGroupPermissionDenied, 'CreateProjectFromTemplatePermissionDenied': filesystem_errors.CreateProjectFromTemplatePermissionDenied, 'CreateProjectNoOwnerLikeRoleGrant': filesystem_errors.CreateProjectNoOwnerLikeRoleGrant, 'DefaultRolesNotInSpaceRoleSet': filesystem_errors.DefaultRolesNotInSpaceRoleSet, 'InvalidDefaultRoles': filesystem_errors.InvalidDefaultRoles, 'InvalidDescription': filesystem_errors.InvalidDescription, 'InvalidOrganizationHierarchy': filesystem_errors.InvalidOrganizationHierarchy, 'InvalidOrganizations': filesystem_errors.InvalidOrganizations, 'InvalidPrincipalIdsForGroupTemplate': filesystem_errors.InvalidPrincipalIdsForGroupTemplate, 'InvalidVariable': filesystem_errors.InvalidVariable, 'InvalidVariableEnumOption': filesystem_errors.InvalidVariableEnumOption, 'MissingVariableValue': filesystem_errors.MissingVariableValue, 'NotAuthorizedToApplyOrganization': filesystem_errors.NotAuthorizedToApplyOrganization, 'OrganizationsNotFound': filesystem_errors.OrganizationsNotFound, 'ProjectNotFound': filesystem_errors.ProjectNotFound, 'ProjectTemplateNotFound': filesystem_errors.ProjectTemplateNotFound, 'TemplateGroupNameConflict': filesystem_errors.TemplateGroupNameConflict, 'TemplateMarkingNameConflict': filesystem_errors.TemplateMarkingNameConflict}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `filesystem_models.Project`. Ordinary async return: `typing.Awaitable[filesystem_models.Project]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | filesystem_models.Project |
| sync_raw | ApiResponse[filesystem_models.Project] |
| sync_streaming | StreamingContextManager[filesystem_models.Project] |
| async_ordinary | typing.Awaitable[filesystem_models.Project] |
| async_raw | Awaitable[AsyncApiResponse[filesystem_models.Project]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[filesystem_models.Project]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.GroupName](../../../../models/v2/core/models/GroupName.md)
- [foundry_sdk.v2.core.models.GroupRid](../../../../models/v2/core/models/GroupRid.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.RoleId](../../../../models/v2/core/models/RoleId.md)
- [foundry_sdk.v2.core.models.UpdatedBy](../../../../models/v2/core/models/UpdatedBy.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../../../models/v2/core/models/UpdatedTime.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)
- [foundry_sdk.v2.filesystem.errors.AddGroupToParentGroupPermissionDenied](../../../../models/v2/filesystem/errors/AddGroupToParentGroupPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.AddGroupToParentGroupPermissionDeniedParameters](../../../../models/v2/filesystem/errors/AddGroupToParentGroupPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.CreateGroupPermissionDenied](../../../../models/v2/filesystem/errors/CreateGroupPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.CreateGroupPermissionDeniedParameters](../../../../models/v2/filesystem/errors/CreateGroupPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.CreateProjectFromTemplatePermissionDenied](../../../../models/v2/filesystem/errors/CreateProjectFromTemplatePermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.CreateProjectFromTemplatePermissionDeniedParameters](../../../../models/v2/filesystem/errors/CreateProjectFromTemplatePermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.CreateProjectNoOwnerLikeRoleGrant](../../../../models/v2/filesystem/errors/CreateProjectNoOwnerLikeRoleGrant.md)
- [foundry_sdk.v2.filesystem.errors.CreateProjectNoOwnerLikeRoleGrantParameters](../../../../models/v2/filesystem/errors/CreateProjectNoOwnerLikeRoleGrantParameters.md)
- [foundry_sdk.v2.filesystem.errors.DefaultRolesNotInSpaceRoleSet](../../../../models/v2/filesystem/errors/DefaultRolesNotInSpaceRoleSet.md)
- [foundry_sdk.v2.filesystem.errors.DefaultRolesNotInSpaceRoleSetParameters](../../../../models/v2/filesystem/errors/DefaultRolesNotInSpaceRoleSetParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDefaultRoles](../../../../models/v2/filesystem/errors/InvalidDefaultRoles.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDefaultRolesParameters](../../../../models/v2/filesystem/errors/InvalidDefaultRolesParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDescription](../../../../models/v2/filesystem/errors/InvalidDescription.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDescriptionParameters](../../../../models/v2/filesystem/errors/InvalidDescriptionParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidOrganizationHierarchy](../../../../models/v2/filesystem/errors/InvalidOrganizationHierarchy.md)
- [foundry_sdk.v2.filesystem.errors.InvalidOrganizationHierarchyParameters](../../../../models/v2/filesystem/errors/InvalidOrganizationHierarchyParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidOrganizations](../../../../models/v2/filesystem/errors/InvalidOrganizations.md)
- [foundry_sdk.v2.filesystem.errors.InvalidOrganizationsParameters](../../../../models/v2/filesystem/errors/InvalidOrganizationsParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidPrincipalIdsForGroupTemplate](../../../../models/v2/filesystem/errors/InvalidPrincipalIdsForGroupTemplate.md)
- [foundry_sdk.v2.filesystem.errors.InvalidPrincipalIdsForGroupTemplateParameters](../../../../models/v2/filesystem/errors/InvalidPrincipalIdsForGroupTemplateParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidVariable](../../../../models/v2/filesystem/errors/InvalidVariable.md)
- [foundry_sdk.v2.filesystem.errors.InvalidVariableEnumOption](../../../../models/v2/filesystem/errors/InvalidVariableEnumOption.md)
- [foundry_sdk.v2.filesystem.errors.InvalidVariableEnumOptionParameters](../../../../models/v2/filesystem/errors/InvalidVariableEnumOptionParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidVariableParameters](../../../../models/v2/filesystem/errors/InvalidVariableParameters.md)
- [foundry_sdk.v2.filesystem.errors.MissingVariableValue](../../../../models/v2/filesystem/errors/MissingVariableValue.md)
- [foundry_sdk.v2.filesystem.errors.MissingVariableValueParameters](../../../../models/v2/filesystem/errors/MissingVariableValueParameters.md)
- [foundry_sdk.v2.filesystem.errors.NotAuthorizedToApplyOrganization](../../../../models/v2/filesystem/errors/NotAuthorizedToApplyOrganization.md)
- [foundry_sdk.v2.filesystem.errors.NotAuthorizedToApplyOrganizationParameters](../../../../models/v2/filesystem/errors/NotAuthorizedToApplyOrganizationParameters.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationsNotFound](../../../../models/v2/filesystem/errors/OrganizationsNotFound.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationsNotFoundParameters](../../../../models/v2/filesystem/errors/OrganizationsNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFound](../../../../models/v2/filesystem/errors/ProjectNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFoundParameters](../../../../models/v2/filesystem/errors/ProjectNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.ProjectTemplateNotFound](../../../../models/v2/filesystem/errors/ProjectTemplateNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ProjectTemplateNotFoundParameters](../../../../models/v2/filesystem/errors/ProjectTemplateNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.TemplateGroupNameConflict](../../../../models/v2/filesystem/errors/TemplateGroupNameConflict.md)
- [foundry_sdk.v2.filesystem.errors.TemplateGroupNameConflictParameters](../../../../models/v2/filesystem/errors/TemplateGroupNameConflictParameters.md)
- [foundry_sdk.v2.filesystem.errors.TemplateMarkingNameConflict](../../../../models/v2/filesystem/errors/TemplateMarkingNameConflict.md)
- [foundry_sdk.v2.filesystem.errors.TemplateMarkingNameConflictParameters](../../../../models/v2/filesystem/errors/TemplateMarkingNameConflictParameters.md)
- [foundry_sdk.v2.filesystem.models.CreateProjectFromTemplateRequest](../../../../models/v2/filesystem/models/CreateProjectFromTemplateRequest.md)
- [foundry_sdk.v2.filesystem.models.Project](../../../../models/v2/filesystem/models/Project.md)
- [foundry_sdk.v2.filesystem.models.ProjectResourceLevelRoleGrantsAllowed](../../../../models/v2/filesystem/models/ProjectResourceLevelRoleGrantsAllowed.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.ProjectTemplateRid](../../../../models/v2/filesystem/models/ProjectTemplateRid.md)
- [foundry_sdk.v2.filesystem.models.ProjectTemplateVariableId](../../../../models/v2/filesystem/models/ProjectTemplateVariableId.md)
- [foundry_sdk.v2.filesystem.models.ProjectTemplateVariableValue](../../../../models/v2/filesystem/models/ProjectTemplateVariableValue.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](../../../../models/v2/filesystem/models/ResourcePath.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](../../../../models/v2/filesystem/models/SpaceRid.md)
- [foundry_sdk.v2.filesystem.models.TrashStatus](../../../../models/v2/filesystem/models/TrashStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Project.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create_from_template.md)
