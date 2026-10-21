# v2.admin.CbacMarkingRestrictions.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Returns disallowed, implied, and required markings for the given set of marking IDs.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.CbacMarkingRestrictions.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, *, marking_ids: typing.Optional[typing.List[core_models.MarkingId]]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.CbacMarkingRestrictions: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| marking_ids | typing.Optional[typing.List[core_models.MarkingId]] | None | The marking IDs for which to get restrictions. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CbacMarkingRestrictionsNotFound | The given CbacMarkingRestrictions could not be found. |
| CbacUnavailable | CBAC is not available. |
| GetCbacMarkingRestrictionInfoPermissionDenied | The provided token does not have permission to get the CBAC marking restrictions for the markings. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/cbacMarkingRestrictions'
```

**query_params**

```python
{'markingIds': marking_ids, 'preview': preview}
```

**path_params**

```python
{}
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
admin_models.CbacMarkingRestrictions
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CbacMarkingRestrictionsNotFound': admin_errors.CbacMarkingRestrictionsNotFound, 'CbacUnavailable': admin_errors.CbacUnavailable, 'GetCbacMarkingRestrictionInfoPermissionDenied': admin_errors.GetCbacMarkingRestrictionInfoPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.CbacMarkingRestrictions`. Ordinary async return: `typing.Awaitable[admin_models.CbacMarkingRestrictions]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.CbacMarkingRestrictions |
| sync_raw | ApiResponse[admin_models.CbacMarkingRestrictions] |
| sync_streaming | StreamingContextManager[admin_models.CbacMarkingRestrictions] |
| async_ordinary | typing.Awaitable[admin_models.CbacMarkingRestrictions] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.CbacMarkingRestrictions]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.CbacMarkingRestrictions]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.admin.errors.CbacMarkingRestrictionsNotFound](../../../../models/v2/admin/errors/CbacMarkingRestrictionsNotFound.md)
- [foundry_sdk.v2.admin.errors.CbacMarkingRestrictionsNotFoundParameters](../../../../models/v2/admin/errors/CbacMarkingRestrictionsNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.CbacUnavailable](../../../../models/v2/admin/errors/CbacUnavailable.md)
- [foundry_sdk.v2.admin.errors.CbacUnavailableParameters](../../../../models/v2/admin/errors/CbacUnavailableParameters.md)
- [foundry_sdk.v2.admin.errors.GetCbacMarkingRestrictionInfoPermissionDenied](../../../../models/v2/admin/errors/GetCbacMarkingRestrictionInfoPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetCbacMarkingRestrictionInfoPermissionDeniedParameters](../../../../models/v2/admin/errors/GetCbacMarkingRestrictionInfoPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.CbacMarkingRestrictions](../../../../models/v2/admin/models/CbacMarkingRestrictions.md)
- [foundry_sdk.v2.admin.models.CbacMarkingRestrictionsIsValid](../../../../models/v2/admin/models/CbacMarkingRestrictionsIsValid.md)
- [foundry_sdk.v2.admin.models.CbacMarkingRestrictionsUserSatisfiesMarkings](../../../../models/v2/admin/models/CbacMarkingRestrictionsUserSatisfiesMarkings.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/CbacMarkingRestrictions.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
