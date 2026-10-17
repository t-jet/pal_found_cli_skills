# v2.media_sets.MediaSet.upload


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Uploads a media item to an existing media set.
The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
A branch name, or branch rid, or view rid may optionally be specified.  If none is specified, the item will be uploaded to the default branch. If more than one is specified, an error is thrown.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.media_sets.MediaSet.upload`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def upload(self, media_set_rid: core_models.MediaSetRid, body: bytes, *, branch_name: typing.Optional[media_sets_models.BranchName]=None, branch_rid: typing.Optional[media_sets_models.BranchRid]=None, media_item_path: typing.Optional[core_models.MediaItemPath]=None, media_item_rid: typing.Optional[core_models.MediaItemRid]=None, preview: typing.Optional[core_models.PreviewMode]=None, transaction_id: typing.Optional[media_sets_models.TransactionId]=None, view_rid: typing.Optional[core_models.MediaSetViewRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> media_sets_models.PutMediaItemResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| media_set_rid | core_models.MediaSetRid | required | Value shape and constraints are in its referenced local type definition. |
| body | bytes | required | Body of the request |
| branch_name | typing.Optional[media_sets_models.BranchName] | None | Specifies the specific branch by name to which this media item will be uploaded. May not be provided if branch rid or view rid are provided. |
| branch_rid | typing.Optional[media_sets_models.BranchRid] | None | Specifies the specific branch by rid to which this media item will be uploaded. May not be provided if branch name or view rid are provided. |
| media_item_path | typing.Optional[core_models.MediaItemPath] | None | An identifier for a media item within a media set. Necessary if the backing media set requires paths. |
| media_item_rid | typing.Optional[core_models.MediaItemRid] | None | An optional RID to use for the media item to create. If omitted, the server will automatically generate a RID. In most cases, the server-generated RID should be preferred; only specify a custom RID if your workflow strictly requires deterministic or client-controlled identifiers. The RID must be in the format of `ri.mio.<instance>.media-item.<UUID>`, where `<instance>` is the same as the instance part of the media set RID, and `<UUID>` is a UUID. An `InvalidMediaItemRid` error will be thrown if the RID is not in the expected format. A `MediaItemRidAlreadyExists` error will be thrown if the media set already contains a media item with the same RID. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| transaction_id | typing.Optional[media_sets_models.TransactionId] | None | The id of the transaction associated with this request. Required if this is a transactional media set. |
| view_rid | typing.Optional[core_models.MediaSetViewRid] | None | Specifies the specific view by rid to which this media item will be uploaded. May not be provided if branch name or branch rid are provided. |
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
'/v2/mediasets/{mediaSetRid}/items'
```

**query_params**

```python
{'branchName': branch_name, 'branchRid': branch_rid, 'mediaItemPath': media_item_path, 'mediaItemRid': media_item_rid, 'preview': preview, 'transactionId': transaction_id, 'viewRid': view_rid}
```

**path_params**

```python
{'mediaSetRid': media_set_rid}
```

**header_params**

```python
{'Content-Type': '*/*', 'Accept': 'application/json'}
```

**body**

```python
body
```

**response_type**

```python
media_sets_models.PutMediaItemResponse
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

Ordinary sync return: `media_sets_models.PutMediaItemResponse`. Ordinary async return: `typing.Awaitable[media_sets_models.PutMediaItemResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | media_sets_models.PutMediaItemResponse |
| sync_raw | ApiResponse[media_sets_models.PutMediaItemResponse] |
| sync_streaming | StreamingContextManager[media_sets_models.PutMediaItemResponse] |
| async_ordinary | typing.Awaitable[media_sets_models.PutMediaItemResponse] |
| async_raw | Awaitable[AsyncApiResponse[media_sets_models.PutMediaItemResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[media_sets_models.PutMediaItemResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.MediaItemPath](../../../../models/v2/core/models/MediaItemPath.md)
- [foundry_sdk.v2.core.models.MediaItemRid](../../../../models/v2/core/models/MediaItemRid.md)
- [foundry_sdk.v2.core.models.MediaSetRid](../../../../models/v2/core/models/MediaSetRid.md)
- [foundry_sdk.v2.core.models.MediaSetViewRid](../../../../models/v2/core/models/MediaSetViewRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.media_sets.models.BranchName](../../../../models/v2/media_sets/models/BranchName.md)
- [foundry_sdk.v2.media_sets.models.BranchRid](../../../../models/v2/media_sets/models/BranchRid.md)
- [foundry_sdk.v2.media_sets.models.PutMediaItemResponse](../../../../models/v2/media_sets/models/PutMediaItemResponse.md)
- [foundry_sdk.v2.media_sets.models.TransactionId](../../../../models/v2/media_sets/models/TransactionId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/media_sets/MediaSet.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](upload.md)
