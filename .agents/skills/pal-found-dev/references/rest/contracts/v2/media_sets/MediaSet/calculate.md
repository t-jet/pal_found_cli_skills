# v2.media_sets.MediaSet.calculate


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Starts calculation of a thumbnail for a given image.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.media_sets.MediaSet.calculate`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def calculate(self, media_set_rid: core_models.MediaSetRid, media_item_rid: core_models.MediaItemRid, *, preview: typing.Optional[core_models.PreviewMode]=None, read_token: typing.Optional[core_models.MediaItemReadToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> media_sets_models.TrackedTransformationResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| media_set_rid | core_models.MediaSetRid | required | The RID of the media set. |
| media_item_rid | core_models.MediaItemRid | required | The RID of the media item. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| read_token | typing.Optional[core_models.MediaItemReadToken] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform/imagery/thumbnail/calculate'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'mediaSetRid': media_set_rid, 'mediaItemRid': media_item_rid}
```

**header_params**

```python
{'ReadToken': read_token, 'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
media_sets_models.TrackedTransformationResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `media_sets_models.TrackedTransformationResponse`. Ordinary async return: `typing.Awaitable[media_sets_models.TrackedTransformationResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | media_sets_models.TrackedTransformationResponse |
| sync_raw | ApiResponse[media_sets_models.TrackedTransformationResponse] |
| sync_streaming | StreamingContextManager[media_sets_models.TrackedTransformationResponse] |
| async_ordinary | typing.Awaitable[media_sets_models.TrackedTransformationResponse] |
| async_raw | Awaitable[AsyncApiResponse[media_sets_models.TrackedTransformationResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[media_sets_models.TrackedTransformationResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.MediaItemReadToken](../../../../models/v2/core/models/MediaItemReadToken.md)
- [foundry_sdk.v2.core.models.MediaItemRid](../../../../models/v2/core/models/MediaItemRid.md)
- [foundry_sdk.v2.core.models.MediaSetRid](../../../../models/v2/core/models/MediaSetRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.media_sets.models.TrackedTransformationFailedResponse](../../../../models/v2/media_sets/models/TrackedTransformationFailedResponse.md)
- [foundry_sdk.v2.media_sets.models.TrackedTransformationPendingResponse](../../../../models/v2/media_sets/models/TrackedTransformationPendingResponse.md)
- [foundry_sdk.v2.media_sets.models.TrackedTransformationResponse](../../../../models/v2/media_sets/models/TrackedTransformationResponse.md)
- [foundry_sdk.v2.media_sets.models.TrackedTransformationSuccessfulResponse](../../../../models/v2/media_sets/models/TrackedTransformationSuccessfulResponse.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/media_sets/MediaSet.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](calculate.md)
