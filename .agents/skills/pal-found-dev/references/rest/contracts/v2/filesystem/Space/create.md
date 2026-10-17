# v2.filesystem.Space.create


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new Space.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Space.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, *, deletion_policy_organizations: typing.List[core_models.OrganizationRid], display_name: filesystem_models.ResourceDisplayName, enrollment_rid: core_models.EnrollmentRid, organizations: typing.List[core_models.OrganizationRid], default_role_set_id: typing.Optional[core_models.RoleSetId]=None, description: typing.Optional[str]=None, file_system_id: typing.Optional[filesystem_models.FileSystemId]=None, preview: typing.Optional[core_models.PreviewMode]=None, usage_account_rid: typing.Optional[filesystem_models.UsageAccountRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> filesystem_models.Space: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| deletion_policy_organizations | typing.List[core_models.OrganizationRid] | required | By default, this Space will use a Last Out deletion policy, meaning that this Space and its projects will be deleted when the last Organization listed here is deleted. Only Organizations in the Space's Enrollment can be included here. |
| display_name | filesystem_models.ResourceDisplayName | required | Value shape and constraints are in its referenced local type definition. |
| enrollment_rid | core_models.EnrollmentRid | required | The RID of the Enrollment that this Space belongs to. |
| organizations | typing.List[core_models.OrganizationRid] | required | The list of Organizations that are provisioned access to this Space. In order to access this Space, a user must be a member of at least one of these Organizations. |
| default_role_set_id | typing.Optional[core_models.RoleSetId] | None | The ID of the default Role Set for this Space, which defines the set of roles that Projects in this Space must use. If not provided, the default Role Set for Projects will be used. |
| description | typing.Optional[str] | None | The description of the Space. |
| file_system_id | typing.Optional[filesystem_models.FileSystemId] | None | The ID of the Filesystem for this Space, which is where the contents of the Space are stored. If not provided, the default Filesystem for this Enrollment will be used. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| usage_account_rid | typing.Optional[filesystem_models.UsageAccountRid] | None | The RID of the Usage Account for this Space. Resource usage for projects in this space will accrue to this Usage Account by default. If not provided, the default Usage Account for this Enrollment will be used. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateSpacePermissionDenied | Could not create the Space. |
| EnrollmentNotFound | An enrollment was not found for the user. |
| OrganizationsNotFound | At least one organization RID could not be found. |
| RoleSetNotFound | The role set provided in the request to create or replace a space could not be found. |
| SpaceInternalError | An internal error occurred when trying to create or replace the space. |
| SpaceInvalidArgument | An invalid argument was provided in the request to create or replace a space. |
| SpaceNameInvalid | The provided space name is invalid. It may be a reserved name or contain invalid characters. |
| SpaceNotFound | The given Space could not be found. |
| UsageAccountServiceIsNotPresent | The Usage Accounts service is unexpectedly not present. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/filesystem/spaces'
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
filesystem_models.CreateSpaceRequest(enrollment_rid=enrollment_rid, usage_account_rid=usage_account_rid, file_system_id=file_system_id, display_name=display_name, organizations=organizations, description=description, deletion_policy_organizations=deletion_policy_organizations, default_role_set_id=default_role_set_id)
```

**response_type**

```python
filesystem_models.Space
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CreateSpacePermissionDenied': filesystem_errors.CreateSpacePermissionDenied, 'EnrollmentNotFound': filesystem_errors.EnrollmentNotFound, 'OrganizationsNotFound': filesystem_errors.OrganizationsNotFound, 'RoleSetNotFound': filesystem_errors.RoleSetNotFound, 'SpaceInternalError': filesystem_errors.SpaceInternalError, 'SpaceInvalidArgument': filesystem_errors.SpaceInvalidArgument, 'SpaceNameInvalid': filesystem_errors.SpaceNameInvalid, 'SpaceNotFound': filesystem_errors.SpaceNotFound, 'UsageAccountServiceIsNotPresent': filesystem_errors.UsageAccountServiceIsNotPresent}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `filesystem_models.Space`. Ordinary async return: `typing.Awaitable[filesystem_models.Space]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | filesystem_models.Space |
| sync_raw | ApiResponse[filesystem_models.Space] |
| sync_streaming | StreamingContextManager[filesystem_models.Space] |
| async_ordinary | typing.Awaitable[filesystem_models.Space] |
| async_raw | Awaitable[AsyncApiResponse[filesystem_models.Space]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[filesystem_models.Space]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../../../models/v2/core/models/EnrollmentRid.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.RoleSetId](../../../../models/v2/core/models/RoleSetId.md)
- [foundry_sdk.v2.filesystem.errors.CreateSpacePermissionDenied](../../../../models/v2/filesystem/errors/CreateSpacePermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.CreateSpacePermissionDeniedParameters](../../../../models/v2/filesystem/errors/CreateSpacePermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.EnrollmentNotFound](../../../../models/v2/filesystem/errors/EnrollmentNotFound.md)
- [foundry_sdk.v2.filesystem.errors.EnrollmentNotFoundParameters](../../../../models/v2/filesystem/errors/EnrollmentNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationsNotFound](../../../../models/v2/filesystem/errors/OrganizationsNotFound.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationsNotFoundParameters](../../../../models/v2/filesystem/errors/OrganizationsNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.RoleSetNotFound](../../../../models/v2/filesystem/errors/RoleSetNotFound.md)
- [foundry_sdk.v2.filesystem.errors.RoleSetNotFoundParameters](../../../../models/v2/filesystem/errors/RoleSetNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.SpaceInternalError](../../../../models/v2/filesystem/errors/SpaceInternalError.md)
- [foundry_sdk.v2.filesystem.errors.SpaceInternalErrorParameters](../../../../models/v2/filesystem/errors/SpaceInternalErrorParameters.md)
- [foundry_sdk.v2.filesystem.errors.SpaceInvalidArgument](../../../../models/v2/filesystem/errors/SpaceInvalidArgument.md)
- [foundry_sdk.v2.filesystem.errors.SpaceInvalidArgumentParameters](../../../../models/v2/filesystem/errors/SpaceInvalidArgumentParameters.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNameInvalid](../../../../models/v2/filesystem/errors/SpaceNameInvalid.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNameInvalidParameters](../../../../models/v2/filesystem/errors/SpaceNameInvalidParameters.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNotFound](../../../../models/v2/filesystem/errors/SpaceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNotFoundParameters](../../../../models/v2/filesystem/errors/SpaceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.UsageAccountServiceIsNotPresent](../../../../models/v2/filesystem/errors/UsageAccountServiceIsNotPresent.md)
- [foundry_sdk.v2.filesystem.errors.UsageAccountServiceIsNotPresentParameters](../../../../models/v2/filesystem/errors/UsageAccountServiceIsNotPresentParameters.md)
- [foundry_sdk.v2.filesystem.models.CreateSpaceRequest](../../../../models/v2/filesystem/models/CreateSpaceRequest.md)
- [foundry_sdk.v2.filesystem.models.FileSystemId](../../../../models/v2/filesystem/models/FileSystemId.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](../../../../models/v2/filesystem/models/ResourcePath.md)
- [foundry_sdk.v2.filesystem.models.Space](../../../../models/v2/filesystem/models/Space.md)
- [foundry_sdk.v2.filesystem.models.SpaceMavenIdentifier](../../../../models/v2/filesystem/models/SpaceMavenIdentifier.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](../../../../models/v2/filesystem/models/SpaceRid.md)
- [foundry_sdk.v2.filesystem.models.UsageAccountRid](../../../../models/v2/filesystem/models/UsageAccountRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Space.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
