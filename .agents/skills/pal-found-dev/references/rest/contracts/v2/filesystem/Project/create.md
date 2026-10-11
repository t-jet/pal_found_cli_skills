# v2.filesystem.Project.create


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new Project.

Note that third-party applications using this endpoint via OAuth2 cannot be associated with an
Ontology SDK as this will reduce the scope of operations to only those within specified projects.
When creating the application, select "No, I won't use an Ontology SDK" on the Resources page.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Project.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, *, default_roles: typing.List[core_models.RoleId], display_name: filesystem_models.ResourceDisplayName, organization_rids: typing.List[core_models.OrganizationRid], role_grants: typing.Dict[core_models.RoleId, typing.List[filesystem_models.PrincipalWithId]], space_rid: filesystem_models.SpaceRid, description: typing.Optional[str]=None, resource_level_role_grants_allowed: typing.Optional[bool]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> filesystem_models.Project: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| default_roles | typing.List[core_models.RoleId] | required | Value shape and constraints are in its referenced local type definition. |
| display_name | filesystem_models.ResourceDisplayName | required | Value shape and constraints are in its referenced local type definition. |
| organization_rids | typing.List[core_models.OrganizationRid] | required | Value shape and constraints are in its referenced local type definition. |
| role_grants | typing.Dict[core_models.RoleId, typing.List[filesystem_models.PrincipalWithId]] | required | Value shape and constraints are in its referenced local type definition. |
| space_rid | filesystem_models.SpaceRid | required | Value shape and constraints are in its referenced local type definition. |
| description | typing.Optional[str] | None | Value shape and constraints are in its referenced local type definition. |
| resource_level_role_grants_allowed | typing.Optional[bool] | None | Whether role grants should be allowed on individual resources within the Project. When not specified, defaults to true. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateProjectNoOwnerLikeRoleGrant | The create project request would create a project with no principal being granted an owner-like role. As a result, there would be no user with administrative privileges over the project. A role is defined to be owner-like if it has the `compass:edit-project` operation. In the common case of the default role-set, this is just the `compass:manage` role. |
| CreateProjectPermissionDenied | Could not create the Project. |
| InvalidDisplayName | The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters. |
| InvalidRoleIds | A roleId referenced in either default roles or role grants does not exist in the project role set for the space. |
| OrganizationMarkingNotOnSpace | At least one of the organization markings associated with a passed organization is not applied on the requested space. |
| OrganizationsNotFound | At least one organization RID could not be found. |
| ProjectCreationNotSupported | Project creation is not supported in the current user's space. |
| ProjectNameAlreadyExists | The requested display name for the created project is already being used in the space. |
| ProjectNotFound | The given Project could not be found. |
| SpaceNotFound | The given Space could not be found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/filesystem/projects/create'
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
filesystem_models.CreateProjectRequest(display_name=display_name, description=description, space_rid=space_rid, role_grants=role_grants, default_roles=default_roles, organization_rids=organization_rids, resource_level_role_grants_allowed=resource_level_role_grants_allowed)
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
{'CreateProjectNoOwnerLikeRoleGrant': filesystem_errors.CreateProjectNoOwnerLikeRoleGrant, 'CreateProjectPermissionDenied': filesystem_errors.CreateProjectPermissionDenied, 'InvalidDisplayName': filesystem_errors.InvalidDisplayName, 'InvalidRoleIds': filesystem_errors.InvalidRoleIds, 'OrganizationMarkingNotOnSpace': filesystem_errors.OrganizationMarkingNotOnSpace, 'OrganizationsNotFound': filesystem_errors.OrganizationsNotFound, 'ProjectCreationNotSupported': filesystem_errors.ProjectCreationNotSupported, 'ProjectNameAlreadyExists': filesystem_errors.ProjectNameAlreadyExists, 'ProjectNotFound': filesystem_errors.ProjectNotFound, 'SpaceNotFound': filesystem_errors.SpaceNotFound}
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
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.PrincipalType](../../../../models/v2/core/models/PrincipalType.md)
- [foundry_sdk.v2.core.models.RoleId](../../../../models/v2/core/models/RoleId.md)
- [foundry_sdk.v2.core.models.UpdatedBy](../../../../models/v2/core/models/UpdatedBy.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../../../models/v2/core/models/UpdatedTime.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)
- [foundry_sdk.v2.filesystem.errors.CreateProjectNoOwnerLikeRoleGrant](../../../../models/v2/filesystem/errors/CreateProjectNoOwnerLikeRoleGrant.md)
- [foundry_sdk.v2.filesystem.errors.CreateProjectNoOwnerLikeRoleGrantParameters](../../../../models/v2/filesystem/errors/CreateProjectNoOwnerLikeRoleGrantParameters.md)
- [foundry_sdk.v2.filesystem.errors.CreateProjectPermissionDenied](../../../../models/v2/filesystem/errors/CreateProjectPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.CreateProjectPermissionDeniedParameters](../../../../models/v2/filesystem/errors/CreateProjectPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayName](../../../../models/v2/filesystem/errors/InvalidDisplayName.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayNameParameters](../../../../models/v2/filesystem/errors/InvalidDisplayNameParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidRoleIds](../../../../models/v2/filesystem/errors/InvalidRoleIds.md)
- [foundry_sdk.v2.filesystem.errors.InvalidRoleIdsParameters](../../../../models/v2/filesystem/errors/InvalidRoleIdsParameters.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationMarkingNotOnSpace](../../../../models/v2/filesystem/errors/OrganizationMarkingNotOnSpace.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationMarkingNotOnSpaceParameters](../../../../models/v2/filesystem/errors/OrganizationMarkingNotOnSpaceParameters.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationsNotFound](../../../../models/v2/filesystem/errors/OrganizationsNotFound.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationsNotFoundParameters](../../../../models/v2/filesystem/errors/OrganizationsNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.ProjectCreationNotSupported](../../../../models/v2/filesystem/errors/ProjectCreationNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.ProjectCreationNotSupportedParameters](../../../../models/v2/filesystem/errors/ProjectCreationNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNameAlreadyExists](../../../../models/v2/filesystem/errors/ProjectNameAlreadyExists.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNameAlreadyExistsParameters](../../../../models/v2/filesystem/errors/ProjectNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFound](../../../../models/v2/filesystem/errors/ProjectNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFoundParameters](../../../../models/v2/filesystem/errors/ProjectNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNotFound](../../../../models/v2/filesystem/errors/SpaceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNotFoundParameters](../../../../models/v2/filesystem/errors/SpaceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.CreateProjectRequest](../../../../models/v2/filesystem/models/CreateProjectRequest.md)
- [foundry_sdk.v2.filesystem.models.PrincipalWithId](../../../../models/v2/filesystem/models/PrincipalWithId.md)
- [foundry_sdk.v2.filesystem.models.Project](../../../../models/v2/filesystem/models/Project.md)
- [foundry_sdk.v2.filesystem.models.ProjectResourceLevelRoleGrantsAllowed](../../../../models/v2/filesystem/models/ProjectResourceLevelRoleGrantsAllowed.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](../../../../models/v2/filesystem/models/ResourcePath.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](../../../../models/v2/filesystem/models/SpaceRid.md)
- [foundry_sdk.v2.filesystem.models.TrashStatus](../../../../models/v2/filesystem/models/TrashStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Project.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
