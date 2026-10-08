# v2.media_sets.MediaSet.clear


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Clears (soft-deletes) the media item at the specified path within a media set, making it and all older
media items at that path un-retrievable.

A branch name, branch RID, or view RID may optionally be specified. If none is specified,
the item will be cleared from the default branch. If more than one is specified, an error is thrown.

For transactional media sets, a transaction ID must be provided. The deletion will not be
visible until the transaction is committed.

## SDK invocation contract

```python
def clear(self, media_set_rid: core_models.MediaSetRid, *, media_item_path: core_models.MediaItemPath, branch_name: typing.Optional[media_sets_models.BranchName]=None, branch_rid: typing.Optional[media_sets_models.BranchRid]=None, preview: typing.Optional[core_models.PreviewMode]=None, transaction_id: typing.Optional[media_sets_models.TransactionId]=None, view_rid: typing.Optional[core_models.MediaSetViewRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| media_set_rid | core_models.MediaSetRid | required | The RID of the media set. |
| media_item_path | core_models.MediaItemPath | required | The path of the media item to clear. |
| branch_name | typing.Optional[media_sets_models.BranchName] | None | Specifies the specific branch by name from which this media item will be cleared. May not be provided if branch rid or view rid are provided. |
| branch_rid | typing.Optional[media_sets_models.BranchRid] | None | Specifies the specific branch by rid from which this media item will be cleared. May not be provided if branch name or view rid are provided. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| transaction_id | typing.Optional[media_sets_models.TransactionId] | None | The ID of the transaction associated with this request. Required if this is a transactional media set. |
| view_rid | typing.Optional[core_models.MediaSetViewRid] | None | Specifies the specific view by rid from which this media item will be cleared. May not be provided if branch name or branch rid are provided. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'DELETE'
```

**resource_path**

```python
'/v2/mediasets/{mediaSetRid}/items/clearAtPath'
```

**query_params**

```python
{'mediaItemPath': media_item_path, 'branchName': branch_name, 'branchRid': branch_rid, 'preview': preview, 'transactionId': transaction_id, 'viewRid': view_rid}
```

**path_params**

```python
{'mediaSetRid': media_set_rid}
```

**header_params**

```python
{}
```

**body**

```python
None
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
{}
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
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.MediaItemPath](../../../../models/v2/core/models/MediaItemPath.md)
- [foundry_sdk.v2.core.models.MediaSetRid](../../../../models/v2/core/models/MediaSetRid.md)
- [foundry_sdk.v2.core.models.MediaSetViewRid](../../../../models/v2/core/models/MediaSetViewRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.media_sets.models.BranchName](../../../../models/v2/media_sets/models/BranchName.md)
- [foundry_sdk.v2.media_sets.models.BranchRid](../../../../models/v2/media_sets/models/BranchRid.md)
- [foundry_sdk.v2.media_sets.models.TransactionId](../../../../models/v2/media_sets/models/TransactionId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/media_sets/MediaSet.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](clear.md)
