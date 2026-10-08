# v2.media_sets.MediaSet.upload_media


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Uploads a temporary media item. If the media item isn't persisted within 1 hour, the item will be deleted.

If multiple resources are attributed to, usage will be attributed to the first one in the list.

The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
Third-party applications using this endpoint via OAuth2 must request the following operation scopes: `api:ontologies-read api:ontologies-write`.

## SDK invocation contract

```python
def upload_media(self, body: bytes, *, filename: core_models.MediaItemPath, attribution: typing.Optional[core_models.Attribution]=None, media_item_rid: typing.Optional[core_models.MediaItemRid]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core_models.MediaReference: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| body | bytes | required | Body of the request |
| filename | core_models.MediaItemPath | required | A user-defined label for a media item within a media set. Required if the backing media set requires paths. Uploading multiple files to the same path will result in only the most recent file being associated with the path. |
| attribution | typing.Optional[core_models.Attribution] | None | used for passing through usage attribution |
| media_item_rid | typing.Optional[core_models.MediaItemRid] | None | An optional RID to use for the media item to create. If omitted, the server will automatically generate a RID. In most cases, the server-generated RID should be preferred; only specify a custom RID if your workflow strictly requires deterministic or client-controlled identifiers. The RID must be in the format of `ri.mio.<instance>.media-item.<UUID>`, where `<instance>` is the same as the instance part of the media set RID, and `<UUID>` is a UUID. An `InvalidMediaItemRid` error will be thrown if the RID is not in the expected format. A `MediaItemRidAlreadyExists` error will be thrown if the media set already contains a media item with the same RID. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/mediasets/media/upload'
```

**query_params**

```python
{'filename': filename, 'mediaItemRid': media_item_rid, 'preview': preview}
```

**path_params**

```python
{}
```

**header_params**

```python
{'attribution': attribution, 'Content-Type': '*/*', 'Accept': 'application/json'}
```

**body**

```python
body
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
- [foundry_sdk.v2.core.models.Attribution](../../../../models/v2/core/models/Attribution.md)
- [foundry_sdk.v2.core.models.MediaItemPath](../../../../models/v2/core/models/MediaItemPath.md)
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

[Part 1](upload_media.md)
