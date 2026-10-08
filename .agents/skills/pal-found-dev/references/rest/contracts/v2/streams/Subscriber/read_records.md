# v2.streams.Subscriber.read_records


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Fetch records for a subscriber starting from their committed offset. Returns records
grouped by partition.

If `autoCommit` is true, offsets are automatically committed after the records are
fetched, so the next read will start from where this one left off.

If `autoCommit` is false, you must call `commitOffsets` to update the read position.
Use manual commits for at-least-once processing where you need to ensure records are
processed before acknowledging them.

## SDK invocation contract

```python
def read_records(self, dataset_rid: core_models.DatasetRid, stream_branch_name: core_models.BranchName, subscriber_subscriber_id: streams_models.SubscriberId, *, auto_commit: typing.Optional[bool]=None, limit: typing.Optional[int]=None, partition_ids: typing.Optional[typing.List[streams_models.PartitionId]]=None, preview: typing.Optional[core_models.PreviewMode]=None, view_rid: typing.Optional[streams_models.ViewRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> streams_models.ReadSubscriberRecordsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| stream_branch_name | core_models.BranchName | required | Value shape and constraints are in its referenced local type definition. |
| subscriber_subscriber_id | streams_models.SubscriberId | required | Value shape and constraints are in its referenced local type definition. |
| auto_commit | typing.Optional[bool] | None | If true, the read position is automatically committed after reading records. The committed position will be the offset after the last record read. If false, you must call the `commitOffsets` endpoint to commit offsets. Defaults to false. |
| limit | typing.Optional[int] | None | Maximum number of records to return across all partitions. Defaults to 100, max 1000. If a value greater than 1000 is requested, only 1000 records will be returned. |
| partition_ids | typing.Optional[typing.List[streams_models.PartitionId]] | None | If specified, only read from these partitions. Otherwise, read from all partitions. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| view_rid | typing.Optional[streams_models.ViewRid] | None | The view RID to read from. If not provided, reads from the latest view for the dataset/branch. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ReadRecordsFromSubscriberPermissionDenied | Could not readRecords the Subscriber. |
| SubscriberNotFound | No subscriber with the given ID was found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers/{subscriberSubscriberId}/readRecords'
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
streams_models.ReadRecordsFromSubscriberRequest(view_rid=view_rid, limit=limit, partition_ids=partition_ids, auto_commit=auto_commit)
```

**response_type**

```python
streams_models.ReadSubscriberRecordsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ReadRecordsFromSubscriberPermissionDenied': streams_errors.ReadRecordsFromSubscriberPermissionDenied, 'SubscriberNotFound': streams_errors.SubscriberNotFound}
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

Ordinary sync return: `streams_models.ReadSubscriberRecordsResponse`. Ordinary async return: `typing.Awaitable[streams_models.ReadSubscriberRecordsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | streams_models.ReadSubscriberRecordsResponse |
| sync_raw | ApiResponse[streams_models.ReadSubscriberRecordsResponse] |
| sync_streaming | StreamingContextManager[streams_models.ReadSubscriberRecordsResponse] |
| async_ordinary | typing.Awaitable[streams_models.ReadSubscriberRecordsResponse] |
| async_raw | Awaitable[AsyncApiResponse[streams_models.ReadSubscriberRecordsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[streams_models.ReadSubscriberRecordsResponse]] |

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
- [foundry_sdk.v2.streams.errors.ReadRecordsFromSubscriberPermissionDenied](../../../../models/v2/streams/errors/ReadRecordsFromSubscriberPermissionDenied.md)
- [foundry_sdk.v2.streams.errors.ReadRecordsFromSubscriberPermissionDeniedParameters](../../../../models/v2/streams/errors/ReadRecordsFromSubscriberPermissionDeniedParameters.md)
- [foundry_sdk.v2.streams.errors.SubscriberNotFound](../../../../models/v2/streams/errors/SubscriberNotFound.md)
- [foundry_sdk.v2.streams.errors.SubscriberNotFoundParameters](../../../../models/v2/streams/errors/SubscriberNotFoundParameters.md)
- [foundry_sdk.v2.streams.models.PartitionId](../../../../models/v2/streams/models/PartitionId.md)
- [foundry_sdk.v2.streams.models.PartitionRecords](../../../../models/v2/streams/models/PartitionRecords.md)
- [foundry_sdk.v2.streams.models.ReadRecordsFromSubscriberRequest](../../../../models/v2/streams/models/ReadRecordsFromSubscriberRequest.md)
- [foundry_sdk.v2.streams.models.ReadSubscriberRecordsResponse](../../../../models/v2/streams/models/ReadSubscriberRecordsResponse.md)
- [foundry_sdk.v2.streams.models.Record](../../../../models/v2/streams/models/Record.md)
- [foundry_sdk.v2.streams.models.RecordWithOffset](../../../../models/v2/streams/models/RecordWithOffset.md)
- [foundry_sdk.v2.streams.models.SubscriberId](../../../../models/v2/streams/models/SubscriberId.md)
- [foundry_sdk.v2.streams.models.ViewRid](../../../../models/v2/streams/models/ViewRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/streams/Subscriber.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](read_records.md)
