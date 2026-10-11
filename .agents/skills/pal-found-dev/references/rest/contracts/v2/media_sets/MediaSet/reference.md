# v2.media_sets.MediaSet.reference


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets the [media reference](../../../../v2/media_sets/MediaSet.md) for this media item.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.media_sets.MediaSet.reference`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def reference(self, media_set_rid: core_models.MediaSetRid, media_item_rid: core_models.MediaItemRid, *, preview: typing.Optional[core_models.PreviewMode]=None, read_token: typing.Optional[core_models.MediaItemReadToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core_models.MediaReference: ...
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
'/v2/mediasets/{mediaSetRid}/items/{mediaItemRid}/reference'
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
core_models.MediaReference
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

Ordinary sync return: `core_models.MediaReference`. Ordinary async return: `typing.Awaitable[core_models.MediaReference]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core_models.MediaReference |
| sync_raw | ApiResponse[core_models.MediaReference] |
| sync_streaming | StreamingContextManager[core_models.MediaReference] |
| async_ordinary | typing.Awaitable[core_models.MediaReference] |
| async_raw | Awaitable[AsyncApiResponse[core_models.MediaReference]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[core_models.MediaReference]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.MediaItemReadToken](../../../../models/v2/core/models/MediaItemReadToken.md)
- [foundry_sdk.v2.core.models.MediaItemRid](../../../../models/v2/core/models/MediaItemRid.md)
- [foundry_sdk.v2.core.models.MediaReference](../../../../models/v2/core/models/MediaReference.md)
- [foundry_sdk.v2.core.models.MediaSetRid](../../../../models/v2/core/models/MediaSetRid.md)
- [foundry_sdk.v2.core.models.MediaSetViewItem](../../../../models/v2/core/models/MediaSetViewItem.md)
- [foundry_sdk.v2.core.models.MediaSetViewItemWrapper](../../../../models/v2/core/models/MediaSetViewItemWrapper.md)
- [foundry_sdk.v2.core.models.MediaSetViewRid](../../../../models/v2/core/models/MediaSetViewRid.md)
- [foundry_sdk.v2.core.models.MediaType](../../../../models/v2/core/models/MediaType.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.Reference](../../../../models/v2/core/models/Reference.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/media_sets/MediaSet.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A media reference identifies an item for use by another capability; it is different from downloading item bytes. [Local procedure](../../../../v2/media_sets/MediaSet.md).

[Part 1](reference.md)
