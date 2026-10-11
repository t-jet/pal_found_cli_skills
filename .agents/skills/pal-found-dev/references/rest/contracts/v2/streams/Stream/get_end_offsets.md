# v2.streams.Stream.get_end_offsets


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the end offsets for all partitions of a stream. The end offset is the offset of the next record that will be written to the partition.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.streams.Dataset.Stream.get_end_offsets`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_end_offsets(self, dataset_rid: core_models.DatasetRid, stream_branch_name: core_models.BranchName, *, preview: typing.Optional[core_models.PreviewMode]=None, view_rid: typing.Optional[streams_models.ViewRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> streams_models.GetEndOffsetsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| stream_branch_name | core_models.BranchName | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| view_rid | typing.Optional[streams_models.ViewRid] | None | If provided, this endpoint will only read from the stream corresponding to the specified view RID. If not provided, this endpoint will read from the latest stream on the branch. Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetEndOffsetsForStreamPermissionDenied | Could not getEndOffsets the Stream. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/getEndOffsets'
```

**query_params**

```python
{'preview': preview, 'viewRid': view_rid}
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
streams_models.GetEndOffsetsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetEndOffsetsForStreamPermissionDenied': streams_errors.GetEndOffsetsForStreamPermissionDenied}
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

Ordinary sync return: `streams_models.GetEndOffsetsResponse`. Ordinary async return: `typing.Awaitable[streams_models.GetEndOffsetsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | streams_models.GetEndOffsetsResponse |
| sync_raw | ApiResponse[streams_models.GetEndOffsetsResponse] |
| sync_streaming | StreamingContextManager[streams_models.GetEndOffsetsResponse] |
| async_ordinary | typing.Awaitable[streams_models.GetEndOffsetsResponse] |
| async_raw | Awaitable[AsyncApiResponse[streams_models.GetEndOffsetsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[streams_models.GetEndOffsetsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.streams.errors.GetEndOffsetsForStreamPermissionDenied](../../../../models/v2/streams/errors/GetEndOffsetsForStreamPermissionDenied.md)
- [foundry_sdk.v2.streams.errors.GetEndOffsetsForStreamPermissionDeniedParameters](../../../../models/v2/streams/errors/GetEndOffsetsForStreamPermissionDeniedParameters.md)
- [foundry_sdk.v2.streams.models.GetEndOffsetsResponse](../../../../models/v2/streams/models/GetEndOffsetsResponse.md)
- [foundry_sdk.v2.streams.models.PartitionId](../../../../models/v2/streams/models/PartitionId.md)
- [foundry_sdk.v2.streams.models.ViewRid](../../../../models/v2/streams/models/ViewRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/streams/Stream.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_end_offsets.md)
