# v2.media_sets.MediaSet.register


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Registers a media item that currently resides in a federated media store. Registration will validate the item
against the media set's schema and perform initial metadata extraction.
This endpoint is only applicable for federated media sets.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.media_sets.MediaSet.register`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def register(self, media_set_rid: core_models.MediaSetRid, *, physical_item_name: str, branch_name: typing.Optional[media_sets_models.BranchName]=None, media_item_path: typing.Optional[core_models.MediaItemPath]=None, preview: typing.Optional[core_models.PreviewMode]=None, transaction_id: typing.Optional[media_sets_models.TransactionId]=None, view_rid: typing.Optional[core_models.MediaSetViewRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> media_sets_models.RegisterMediaItemResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| media_set_rid | core_models.MediaSetRid | required | Value shape and constraints are in its referenced local type definition. |
| physical_item_name | str | required | The relative path within the federated media store where the media item exists. |
| branch_name | typing.Optional[media_sets_models.BranchName] | None | Specifies the specific branch by name to which this media item will be registered. |
| media_item_path | typing.Optional[core_models.MediaItemPath] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| transaction_id | typing.Optional[media_sets_models.TransactionId] | None | The id of the transaction associated with this request. Required for transactional media sets. |
| view_rid | typing.Optional[core_models.MediaSetViewRid] | None | Specifies the specific view by rid to which this media item will be registered. |
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
'/v2/mediasets/{mediaSetRid}/items/register'
```

**query_params**

```python
{'branchName': branch_name, 'preview': preview, 'transactionId': transaction_id, 'viewRid': view_rid}
```

**path_params**

```python
{'mediaSetRid': media_set_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
media_sets_models.RegisterMediaItemRequest(physical_item_name=physical_item_name, media_item_path=media_item_path)
```

**response_type**

```python
media_sets_models.RegisterMediaItemResponse
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

Ordinary sync return: `media_sets_models.RegisterMediaItemResponse`. Ordinary async return: `typing.Awaitable[media_sets_models.RegisterMediaItemResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | media_sets_models.RegisterMediaItemResponse |
| sync_raw | ApiResponse[media_sets_models.RegisterMediaItemResponse] |
| sync_streaming | StreamingContextManager[media_sets_models.RegisterMediaItemResponse] |
| async_ordinary | typing.Awaitable[media_sets_models.RegisterMediaItemResponse] |
| async_raw | Awaitable[AsyncApiResponse[media_sets_models.RegisterMediaItemResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[media_sets_models.RegisterMediaItemResponse]] |

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
- [foundry_sdk.v2.core.models.MediaType](../../../../models/v2/core/models/MediaType.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.media_sets.models.BranchName](../../../../models/v2/media_sets/models/BranchName.md)
- [foundry_sdk.v2.media_sets.models.RegisterMediaItemRequest](../../../../models/v2/media_sets/models/RegisterMediaItemRequest.md)
- [foundry_sdk.v2.media_sets.models.RegisterMediaItemResponse](../../../../models/v2/media_sets/models/RegisterMediaItemResponse.md)
- [foundry_sdk.v2.media_sets.models.TransactionId](../../../../models/v2/media_sets/models/TransactionId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/media_sets/MediaSet.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](register.md)
