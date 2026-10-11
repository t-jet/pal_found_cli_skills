# v2.streams.Subscriber.commit_offsets


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Explicitly commit offsets for a subscriber. Required when `autoCommit` is false.

Pass the last offset you processed for each partition.

For example, if you processed a record at offset 50, commit `{"0": 50}` and the next
read from partition "0" will start at offset 51.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.streams.Dataset.Stream.Subscriber.commit_offsets`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def commit_offsets(self, dataset_rid: core_models.DatasetRid, stream_branch_name: core_models.BranchName, subscriber_subscriber_id: streams_models.SubscriberId, *, offsets: streams_models.PartitionOffsets, preview: typing.Optional[core_models.PreviewMode]=None, view_rid: typing.Optional[streams_models.ViewRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> streams_models.PartitionOffsets: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| stream_branch_name | core_models.BranchName | required | Value shape and constraints are in its referenced local type definition. |
| subscriber_subscriber_id | streams_models.SubscriberId | required | Value shape and constraints are in its referenced local type definition. |
| offsets | streams_models.PartitionOffsets | required | The last processed offset for each partition. The server will store these as read positions (offset + 1), so the next read starts after the committed offset. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| view_rid | typing.Optional[streams_models.ViewRid] | None | The view RID to commit offsets for. If not provided, uses the latest view for the dataset/branch. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CommitSubscriberOffsetsPermissionDenied | Could not commitOffsets the Subscriber. |
| SubscriberNotFound | No subscriber with the given ID was found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/commitOffsets'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'datasetRid': dataset_rid, 'streamBranchName': stream_branch_name, 'subscriberSubscriberId': subscriber_subscriber_id}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
streams_models.CommitSubscriberOffsetsRequest(view_rid=view_rid, offsets=offsets)
```

**response_type**

```python
streams_models.PartitionOffsets
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CommitSubscriberOffsetsPermissionDenied': streams_errors.CommitSubscriberOffsetsPermissionDenied, 'SubscriberNotFound': streams_errors.SubscriberNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

**endpoint_type**

```python
core.EndpointType.HIGH_SCALE
```

## Response modes

Ordinary sync return: `streams_models.PartitionOffsets`. Ordinary async return: `typing.Awaitable[streams_models.PartitionOffsets]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | streams_models.PartitionOffsets |
| sync_raw | ApiResponse[streams_models.PartitionOffsets] |
| sync_streaming | StreamingContextManager[streams_models.PartitionOffsets] |
| async_ordinary | typing.Awaitable[streams_models.PartitionOffsets] |
| async_raw | Awaitable[AsyncApiResponse[streams_models.PartitionOffsets]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[streams_models.PartitionOffsets]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.streams.errors.CommitSubscriberOffsetsPermissionDenied](../../../../models/v2/streams/errors/CommitSubscriberOffsetsPermissionDenied.md)
- [foundry_sdk.v2.streams.errors.CommitSubscriberOffsetsPermissionDeniedParameters](../../../../models/v2/streams/errors/CommitSubscriberOffsetsPermissionDeniedParameters.md)
- [foundry_sdk.v2.streams.errors.SubscriberNotFound](../../../../models/v2/streams/errors/SubscriberNotFound.md)
- [foundry_sdk.v2.streams.errors.SubscriberNotFoundParameters](../../../../models/v2/streams/errors/SubscriberNotFoundParameters.md)
- [foundry_sdk.v2.streams.models.CommitSubscriberOffsetsRequest](../../../../models/v2/streams/models/CommitSubscriberOffsetsRequest.md)
- [foundry_sdk.v2.streams.models.PartitionId](../../../../models/v2/streams/models/PartitionId.md)
- [foundry_sdk.v2.streams.models.PartitionOffsets](../../../../models/v2/streams/models/PartitionOffsets.md)
- [foundry_sdk.v2.streams.models.SubscriberId](../../../../models/v2/streams/models/SubscriberId.md)
- [foundry_sdk.v2.streams.models.ViewRid](../../../../models/v2/streams/models/ViewRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/streams/Subscriber.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](commit_offsets.md)
