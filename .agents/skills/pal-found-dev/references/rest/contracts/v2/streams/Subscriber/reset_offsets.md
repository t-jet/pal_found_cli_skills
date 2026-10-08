# v2.streams.Subscriber.reset_offsets


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Reset subscriber offsets to a specific position. Use this to replay data from the
beginning, skip to the latest records, or jump to specific offsets.

The `position` parameter determines where reading will resume:
- `earliest`: Reset to the beginning of each partition (offset 0)
- `latest`: Reset to the current end of each partition
- `specific`: Reset to explicit offsets for each partition

## SDK invocation contract

```python
def reset_offsets(self, dataset_rid: core_models.DatasetRid, stream_branch_name: core_models.BranchName, subscriber_subscriber_id: streams_models.SubscriberId, *, position: streams_models.ReadPosition, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> streams_models.PartitionOffsets: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| stream_branch_name | core_models.BranchName | required | Value shape and constraints are in its referenced local type definition. |
| subscriber_subscriber_id | streams_models.SubscriberId | required | Value shape and constraints are in its referenced local type definition. |
| position | streams_models.ReadPosition | required | The position to reset offsets to. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ResetSubscriberOffsetsPermissionDenied | Could not resetOffsets the Subscriber. |
| SubscriberNotFound | No subscriber with the given ID was found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/resetOffsets'
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
streams_models.ResetSubscriberOffsetsRequest(position=position)
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
{'ResetSubscriberOffsetsPermissionDenied': streams_errors.ResetSubscriberOffsetsPermissionDenied, 'SubscriberNotFound': streams_errors.SubscriberNotFound}
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
- [foundry_sdk.v2.streams.errors.ResetSubscriberOffsetsPermissionDenied](../../../../models/v2/streams/errors/ResetSubscriberOffsetsPermissionDenied.md)
- [foundry_sdk.v2.streams.errors.ResetSubscriberOffsetsPermissionDeniedParameters](../../../../models/v2/streams/errors/ResetSubscriberOffsetsPermissionDeniedParameters.md)
- [foundry_sdk.v2.streams.errors.SubscriberNotFound](../../../../models/v2/streams/errors/SubscriberNotFound.md)
- [foundry_sdk.v2.streams.errors.SubscriberNotFoundParameters](../../../../models/v2/streams/errors/SubscriberNotFoundParameters.md)
- [foundry_sdk.v2.streams.models.EarliestPosition](../../../../models/v2/streams/models/EarliestPosition.md)
- [foundry_sdk.v2.streams.models.LatestPosition](../../../../models/v2/streams/models/LatestPosition.md)
- [foundry_sdk.v2.streams.models.PartitionId](../../../../models/v2/streams/models/PartitionId.md)
- [foundry_sdk.v2.streams.models.PartitionOffsets](../../../../models/v2/streams/models/PartitionOffsets.md)
- [foundry_sdk.v2.streams.models.ReadPosition](../../../../models/v2/streams/models/ReadPosition.md)
- [foundry_sdk.v2.streams.models.ResetSubscriberOffsetsRequest](../../../../models/v2/streams/models/ResetSubscriberOffsetsRequest.md)
- [foundry_sdk.v2.streams.models.SpecificPosition](../../../../models/v2/streams/models/SpecificPosition.md)
- [foundry_sdk.v2.streams.models.SubscriberId](../../../../models/v2/streams/models/SubscriberId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/streams/Subscriber.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](reset_offsets.md)
