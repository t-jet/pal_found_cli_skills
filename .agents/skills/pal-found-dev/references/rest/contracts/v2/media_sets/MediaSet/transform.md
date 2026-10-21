# v2.media_sets.MediaSet.transform


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Initiates a transformation on a media item. Returns a job ID that can be used to check the status and retrieve
the result of the transformation.

Transforming a media item requires that you are able to read the media item, either via `api:mediasets-read` or
via a `MediaItemReadToken`

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.media_sets.MediaSet.transform`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def transform(self, media_set_rid: core_models.MediaSetRid, media_item_rid: core_models.MediaItemRid, *, transformation: media_sets_models.Transformation, attribution: typing.Optional[core_models.Attribution]=None, preview: typing.Optional[core_models.PreviewMode]=None, token: typing.Optional[core_models.MediaItemReadToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> media_sets_models.TransformMediaItemResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| media_set_rid | core_models.MediaSetRid | required | The RID of the media set. |
| media_item_rid | core_models.MediaItemRid | required | The RID of the media item. |
| transformation | media_sets_models.Transformation | required | Value shape and constraints are in its referenced local type definition. |
| attribution | typing.Optional[core_models.Attribution] | None | Optional resource to attribute LLM calls on behalf of. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| token | typing.Optional[core_models.MediaItemReadToken] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/transform'
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
{'Attribution': attribution, 'Token': token, 'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
media_sets_models.TransformMediaItemRequest(transformation=transformation)
```

**response_type**

```python
media_sets_models.TransformMediaItemResponse
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

Ordinary sync return: `media_sets_models.TransformMediaItemResponse`. Ordinary async return: `typing.Awaitable[media_sets_models.TransformMediaItemResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | media_sets_models.TransformMediaItemResponse |
| sync_raw | ApiResponse[media_sets_models.TransformMediaItemResponse] |
| sync_streaming | StreamingContextManager[media_sets_models.TransformMediaItemResponse] |
| async_ordinary | typing.Awaitable[media_sets_models.TransformMediaItemResponse] |
| async_raw | Awaitable[AsyncApiResponse[media_sets_models.TransformMediaItemResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[media_sets_models.TransformMediaItemResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

[Part 1](transform.md) | [Part 2](transform-2.md)
