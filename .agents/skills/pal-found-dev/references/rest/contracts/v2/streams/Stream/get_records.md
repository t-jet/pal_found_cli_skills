# v2.streams.Stream.get_records


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get a batch of records from a stream for a given partition. Offsets are ordered from [0, inf) but may be sparse (e.g.: 0, 2, 3, 5).
Binary field values are returned as base64-encoded strings. Decode them to retrieve the original bytes.

## SDK invocation contract

```python
def get_records(self, dataset_rid: core_models.DatasetRid, stream_branch_name: core_models.BranchName, *, limit: int, partition_id: streams_models.PartitionId, preview: typing.Optional[core_models.PreviewMode]=None, start_offset: typing.Optional[core.Long]=None, view_rid: typing.Optional[streams_models.ViewRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> streams_models.GetRecordsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| stream_branch_name | core_models.BranchName | required | Value shape and constraints are in its referenced local type definition. |
| limit | int | required | The total number of records to be retrieved. The response may contain fewer records than requested depending on number of records in the partition and server-defined limits. |
| partition_id | streams_models.PartitionId | required | The ID of the partition to retrieve records from. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| start_offset | typing.Optional[core.Long] | None | The inclusive beginning of the range to be retrieved. Leave empty when reading from the beginning of the partition. |
| view_rid | typing.Optional[streams_models.ViewRid] | None | If provided, this endpoint will only read from the stream corresponding to the specified view RID. If not provided, this endpoint will read from the latest stream on the branch. Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetRecordsFromStreamPermissionDenied | Could not getRecords the Stream. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/getRecords'
```

**query_params**

```python
{'limit': limit, 'partitionId': partition_id, 'preview': preview, 'startOffset': start_offset, 'viewRid': view_rid}
```

**path_params**

```python
{'datasetRid': dataset_rid, 'streamBranchName': stream_branch_name}
```

**header_params**

```python
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
streams_models.GetRecordsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetRecordsFromStreamPermissionDenied': streams_errors.GetRecordsFromStreamPermissionDenied}
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

Ordinary sync return: `streams_models.GetRecordsResponse`. Ordinary async return: `typing.Awaitable[streams_models.GetRecordsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | streams_models.GetRecordsResponse |
| sync_raw | ApiResponse[streams_models.GetRecordsResponse] |
| sync_streaming | StreamingContextManager[streams_models.GetRecordsResponse] |
| async_ordinary | typing.Awaitable[streams_models.GetRecordsResponse] |
| async_raw | Awaitable[AsyncApiResponse[streams_models.GetRecordsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[streams_models.GetRecordsResponse]] |

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
- [foundry_sdk.v2.streams.errors.GetRecordsFromStreamPermissionDenied](../../../../models/v2/streams/errors/GetRecordsFromStreamPermissionDenied.md)
- [foundry_sdk.v2.streams.errors.GetRecordsFromStreamPermissionDeniedParameters](../../../../models/v2/streams/errors/GetRecordsFromStreamPermissionDeniedParameters.md)
- [foundry_sdk.v2.streams.models.GetRecordsResponse](../../../../models/v2/streams/models/GetRecordsResponse.md)
- [foundry_sdk.v2.streams.models.PartitionId](../../../../models/v2/streams/models/PartitionId.md)
- [foundry_sdk.v2.streams.models.Record](../../../../models/v2/streams/models/Record.md)
- [foundry_sdk.v2.streams.models.RecordWithOffset](../../../../models/v2/streams/models/RecordWithOffset.md)
- [foundry_sdk.v2.streams.models.ViewRid](../../../../models/v2/streams/models/ViewRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/streams/Stream.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_records.md)
