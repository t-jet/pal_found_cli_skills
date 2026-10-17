# v2.filesystem.Resource.remove_markings


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Removes Markings from a resource.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Resource.remove_markings`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def remove_markings(self, resource_rid: filesystem_models.ResourceRid, *, marking_ids: typing.List[core_models.MarkingId], request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| resource_rid | filesystem_models.ResourceRid | required | Value shape and constraints are in its referenced local type definition. |
| marking_ids | typing.List[core_models.MarkingId] | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ForbiddenOperationOnAutosavedResource | Performing this operation on an autosaved resource is not supported. |
| ForbiddenOperationOnHiddenResource | Performing this operation on a hidden resource is not supported. |
| MarkingNotFound | A provided marking ID cannot be found. |
| OrganizationMarkingNotSupported | Adding an organization marking as a regular marking is not supported. Use the organization endpoints on a project resource instead. |
| RemoveMarkingsPermissionDenied | Could not removeMarkings the Resource. |
| ResourceNotFound | The given Resource could not be found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/filesystem/resources/{resourceRid}/removeMarkings'
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
{'Content-Type': 'application/json'}
```

**body**

```python
filesystem_models.RemoveMarkingsRequest(marking_ids=marking_ids)
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
{'ForbiddenOperationOnAutosavedResource': filesystem_errors.ForbiddenOperationOnAutosavedResource, 'ForbiddenOperationOnHiddenResource': filesystem_errors.ForbiddenOperationOnHiddenResource, 'MarkingNotFound': filesystem_errors.MarkingNotFound, 'OrganizationMarkingNotSupported': filesystem_errors.OrganizationMarkingNotSupported, 'RemoveMarkingsPermissionDenied': filesystem_errors.RemoveMarkingsPermissionDenied, 'ResourceNotFound': filesystem_errors.ResourceNotFound}
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
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.filesystem.errors.ForbiddenOperationOnAutosavedResource](../../../../models/v2/filesystem/errors/ForbiddenOperationOnAutosavedResource.md)
- [foundry_sdk.v2.filesystem.errors.ForbiddenOperationOnAutosavedResourceParameters](../../../../models/v2/filesystem/errors/ForbiddenOperationOnAutosavedResourceParameters.md)
- [foundry_sdk.v2.filesystem.errors.ForbiddenOperationOnHiddenResource](../../../../models/v2/filesystem/errors/ForbiddenOperationOnHiddenResource.md)
- [foundry_sdk.v2.filesystem.errors.ForbiddenOperationOnHiddenResourceParameters](../../../../models/v2/filesystem/errors/ForbiddenOperationOnHiddenResourceParameters.md)
- [foundry_sdk.v2.filesystem.errors.MarkingNotFound](../../../../models/v2/filesystem/errors/MarkingNotFound.md)
- [foundry_sdk.v2.filesystem.errors.MarkingNotFoundParameters](../../../../models/v2/filesystem/errors/MarkingNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationMarkingNotSupported](../../../../models/v2/filesystem/errors/OrganizationMarkingNotSupported.md)
- [foundry_sdk.v2.filesystem.errors.OrganizationMarkingNotSupportedParameters](../../../../models/v2/filesystem/errors/OrganizationMarkingNotSupportedParameters.md)
- [foundry_sdk.v2.filesystem.errors.RemoveMarkingsPermissionDenied](../../../../models/v2/filesystem/errors/RemoveMarkingsPermissionDenied.md)
- [foundry_sdk.v2.filesystem.errors.RemoveMarkingsPermissionDeniedParameters](../../../../models/v2/filesystem/errors/RemoveMarkingsPermissionDeniedParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFound](../../../../models/v2/filesystem/errors/ResourceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFoundParameters](../../../../models/v2/filesystem/errors/ResourceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.RemoveMarkingsRequest](../../../../models/v2/filesystem/models/RemoveMarkingsRequest.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Resource.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](remove_markings.md)
