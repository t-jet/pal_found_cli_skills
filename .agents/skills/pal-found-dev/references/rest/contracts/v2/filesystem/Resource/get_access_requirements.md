# v2.filesystem.Resource.get_access_requirements


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Returns a list of access requirements a user needs in order to view a resource. Access requirements are
composed of Organizations and Markings, and can either be applied directly to the resource or inherited.

## SDK invocation contract

```python
def get_access_requirements(self, resource_rid: filesystem_models.ResourceRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> filesystem_models.AccessRequirements: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| resource_rid | filesystem_models.ResourceRid | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetAccessRequirementsPermissionDenied | Could not getAccessRequirements the Resource. |
| ResourceNotFound | The given Resource could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/filesystem/resources/{resourceRid}/getAccessRequirements'
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
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
filesystem_models.AccessRequirements
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetAccessRequirementsPermissionDenied': filesystem_errors.GetAccessRequirementsPermissionDenied, 'ResourceNotFound': filesystem_errors.ResourceNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `filesystem_models.AccessRequirements`. Ordinary async return: `typing.Awaitable[filesystem_models.AccessRequirements]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | filesystem_models.AccessRequirements |
| sync_raw | ApiResponse[filesystem_models.AccessRequirements] |
| sync_streaming | StreamingContextManager[filesystem_models.AccessRequirements] |
| async_ordinary | typing.Awaitable[filesystem_models.AccessRequirements] |
| async_raw | Awaitable[AsyncApiResponse[filesystem_models.AccessRequirements]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[filesystem_models.AccessRequirements]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.filesystem.errors.GetAccessRequirementsPermissionDenied](../../../../models/v2/filesystem/errors/GetAccessRequirementsPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.GetAccessRequirementsPermissionDeniedParameters](../../../../models/v2/filesystem/errors/GetAccessRequirementsPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFound](../../../../models/v2/filesystem/errors/ResourceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFoundParameters](../../../../models/v2/filesystem/errors/ResourceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.AccessRequirements](../../../../models/v2/filesystem/models/AccessRequirements.md)
- [foundry_sdk.v2.filesystem.models.IsDirectlyApplied](../../../../models/v2/filesystem/models/IsDirectlyApplied.md)
- [foundry_sdk.v2.filesystem.models.Marking](../../../../models/v2/filesystem/models/Marking.md)
- [foundry_sdk.v2.filesystem.models.Organization](../../../../models/v2/filesystem/models/Organization.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Resource.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_access_requirements.md)
