# v2.admin.CbacBanner.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Returns a classification banner string and colors for the given set of marking IDs.

## SDK invocation contract

```python
def get(self, *, display_type: typing.Optional[admin_models.ClassificationBannerDisplayType]=None, marking_ids: typing.Optional[typing.List[core_models.MarkingId]]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.CbacBanner: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| display_type | typing.Optional[admin_models.ClassificationBannerDisplayType] | None | The display type of the banner. Defaults to PORTION_MARKING. BANNER_LINE is the long classification string used in the header of a document; PORTION_MARKING is a short classification string used for individual paragraphs |
| marking_ids | typing.Optional[typing.List[core_models.MarkingId]] | None | The marking IDs for which to generate a banner. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CbacBannerNotFound | The given CbacBanner could not be found. |
| CbacUnavailable | CBAC is not available. |
| GetCbacBannerPermissionDenied | The provided token does not have permission to get the CBAC banner for the markings. |
| UnknownClassificationBannerDisplayType | The provided classification banner display type is not recognized. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/cbacBanner'
```

**query_params**

```python
{'displayType': display_type, 'markingIds': marking_ids, 'preview': preview}
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
admin_models.CbacBanner
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CbacBannerNotFound': admin_errors.CbacBannerNotFound, 'CbacUnavailable': admin_errors.CbacUnavailable, 'GetCbacBannerPermissionDenied': admin_errors.GetCbacBannerPermissionDenied, 'UnknownClassificationBannerDisplayType': admin_errors.UnknownClassificationBannerDisplayType}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.CbacBanner`. Ordinary async return: `typing.Awaitable[admin_models.CbacBanner]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.CbacBanner |
| sync_raw | ApiResponse[admin_models.CbacBanner] |
| sync_streaming | StreamingContextManager[admin_models.CbacBanner] |
| async_ordinary | typing.Awaitable[admin_models.CbacBanner] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.CbacBanner]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.CbacBanner]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.admin.errors.CbacBannerNotFound](../../../../models/v2/admin/errors/CbacBannerNotFound.md)
- [foundry_sdk.v2.admin.errors.CbacBannerNotFoundParameters](../../../../models/v2/admin/errors/CbacBannerNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.CbacUnavailable](../../../../models/v2/admin/errors/CbacUnavailable.md)
- [foundry_sdk.v2.admin.errors.CbacUnavailableParameters](../../../../models/v2/admin/errors/CbacUnavailableParameters.md)
- [foundry_sdk.v2.admin.errors.GetCbacBannerPermissionDenied](../../../../models/v2/admin/errors/GetCbacBannerPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetCbacBannerPermissionDeniedParameters](../../../../models/v2/admin/errors/GetCbacBannerPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.UnknownClassificationBannerDisplayType](../../../../models/v2/admin/errors/UnknownClassificationBannerDisplayType.md)
- [foundry_sdk.v2.admin.errors.UnknownClassificationBannerDisplayTypeParameters](../../../../models/v2/admin/errors/UnknownClassificationBannerDisplayTypeParameters.md)
- [foundry_sdk.v2.admin.models.CbacBanner](../../../../models/v2/admin/models/CbacBanner.md)
- [foundry_sdk.v2.admin.models.CbacBannerClassificationString](../../../../models/v2/admin/models/CbacBannerClassificationString.md)
- [foundry_sdk.v2.admin.models.ClassificationBannerDisplayType](../../../../models/v2/admin/models/ClassificationBannerDisplayType.md)
- [foundry_sdk.v2.core.models.Color](../../../../models/v2/core/models/Color.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/CbacBanner.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
