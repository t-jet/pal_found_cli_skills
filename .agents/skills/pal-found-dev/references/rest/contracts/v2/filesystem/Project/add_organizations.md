# v2.filesystem.Project.add_organizations


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Adds a list of Organizations to a Project.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Project.add_organizations`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def add_organizations(self, project_rid: filesystem_models.ProjectRid, *, organization_rids: typing.List[core_models.OrganizationRid], request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| project_rid | filesystem_models.ProjectRid | required | Value shape and constraints are in its referenced local type definition. |
| organization_rids | typing.List[core_models.OrganizationRid] | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AddOrganizationsPermissionDenied | Could not addOrganizations the Project. |
| InvalidOrganizationHierarchy | Organizations on a project must also exist on the parent space. This error is thrown if the configuration of a project's organizations (on creation or subsequently) results in the project being marked with either no organizations in a marked space, or with an organization that is not present on the parent space. |
| OrganizationsNotFound | At least one organization RID could not be found. |
| ProjectNotFound | The given Project could not be found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/filesystem/projects/{projectRid}/addOrganizations'
```

**query_params**

```python
{}
```

**path_params**

```python
{'projectRid': project_rid}
```

**header_params**

```python
{'Content-Type': 'application/json'}
```

**body**

```python
filesystem_models.AddOrganizationsRequest(organization_rids=organization_rids)
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
{'AddOrganizationsPermissionDenied': filesystem_errors.AddOrganizationsPermissionDenied, 'InvalidOrganizationHierarchy': filesystem_errors.InvalidOrganizationHierarchy, 'OrganizationsNotFound': filesystem_errors.OrganizationsNotFound, 'ProjectNotFound': filesystem_errors.ProjectNotFound}
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
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.filesystem.errors.AddOrganizationsPermissionDenied](../../../../models/v2/filesystem/errors/AddOrganizationsPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.AddOrganizationsPermissionDeniedParameters](../../../../models/v2/filesystem/errors/AddOrganizationsPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.InvalidOrganizationHierarchy](../../../../models/v2/filesystem/errors/InvalidOrganizationHierarchy.md)
- [foundry_sdk.v2.filesystem.errors.InvalidOrganizationHierarchyParameters](../../../../models/v2/filesystem/errors/InvalidOrganizationHierarchyParameters.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationsNotFound](../../../../models/v2/filesystem/errors/OrganizationsNotFound.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationsNotFoundParameters](../../../../models/v2/filesystem/errors/OrganizationsNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFound](../../../../models/v2/filesystem/errors/ProjectNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFoundParameters](../../../../models/v2/filesystem/errors/ProjectNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.AddOrganizationsRequest](../../../../models/v2/filesystem/models/AddOrganizationsRequest.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Project.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](add_organizations.md)
