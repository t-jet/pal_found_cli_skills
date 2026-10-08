# v2.streams.Subscriber.create


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Register a new subscriber for a stream. Subscribers maintain server-side offset tracking,
allowing reliable consumption without client-side state management.

If a subscriber with the same ID already exists for this stream, the existing registration
is returned. If a subscriber with the same ID exists for a different stream, an error is returned.

## SDK invocation contract

```python
def create(self, dataset_rid: core_models.DatasetRid, stream_branch_name: core_models.BranchName, *, subscriber_id: streams_models.SubscriberId, preview: typing.Optional[core_models.PreviewMode]=None, read_position: typing.Optional[streams_models.ReadPosition]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> streams_models.Subscriber: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| stream_branch_name | core_models.BranchName | required | Value shape and constraints are in its referenced local type definition. |
| subscriber_id | streams_models.SubscriberId | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| read_position | typing.Optional[streams_models.ReadPosition] | None | Where to start reading from. Defaults to `earliest` if not specified. The `readPosition` determines where the subscriber will start reading: - `earliest`: Start from the beginning of each partition (offset 0). Use this to process all historical data. - `latest`: Start from the current end of each partition. Use this to skip historical data and only process new records arriving after registration. - `specific`: Start from explicit offsets for each partition. Use this to resume from a known checkpoint. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateSubscriberPermissionDenied | Could not create the Subscriber. |
| SubscriberAlreadyExists | A subscriber with this ID already exists for a different stream. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/streams/datasets/{datasetRid}/streams/{streamBranchName}/subscribers'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'datasetRid': dataset_rid, 'streamBranchName': stream_branch_name}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
streams_models.CreateSubscriberRequest(subscriber_id=subscriber_id, read_position=read_position)
```

**response_type**

```python
streams_models.Subscriber
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CreateSubscriberPermissionDenied': streams_errors.CreateSubscriberPermissionDenied, 'SubscriberAlreadyExists': streams_errors.SubscriberAlreadyExists}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `streams_models.Subscriber`. Ordinary async return: `typing.Awaitable[streams_models.Subscriber]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | streams_models.Subscriber |
| sync_raw | ApiResponse[streams_models.Subscriber] |
| sync_streaming | StreamingContextManager[streams_models.Subscriber] |
| async_ordinary | typing.Awaitable[streams_models.Subscriber] |
| async_raw | Awaitable[AsyncApiResponse[streams_models.Subscriber]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[streams_models.Subscriber]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.streams.errors.CreateSubscriberPermissionDenied](../../../../models/v2/streams/errors/CreateSubscriberPermissionDenied.md)
- [foundry_sdk.v2.streams.errors.CreateSubscriberPermissionDeniedParameters](../../../../models/v2/streams/errors/CreateSubscriberPermissionDeniedParameters.md)
- [foundry_sdk.v2.streams.errors.SubscriberAlreadyExists](../../../../models/v2/streams/errors/SubscriberAlreadyExists.md)
- [foundry_sdk.v2.streams.errors.SubscriberAlreadyExistsParameters](../../../../models/v2/streams/errors/SubscriberAlreadyExistsParameters.md)
- [foundry_sdk.v2.streams.models.CreateSubscriberRequest](../../../../models/v2/streams/models/CreateSubscriberRequest.md)
- [foundry_sdk.v2.streams.models.EarliestPosition](../../../../models/v2/streams/models/EarliestPosition.md)
- [foundry_sdk.v2.streams.models.LatestPosition](../../../../models/v2/streams/models/LatestPosition.md)
- [foundry_sdk.v2.streams.models.PartitionId](../../../../models/v2/streams/models/PartitionId.md)
- [foundry_sdk.v2.streams.models.PartitionOffsets](../../../../models/v2/streams/models/PartitionOffsets.md)
- [foundry_sdk.v2.streams.models.ReadPosition](../../../../models/v2/streams/models/ReadPosition.md)
- [foundry_sdk.v2.streams.models.SpecificPosition](../../../../models/v2/streams/models/SpecificPosition.md)
- [foundry_sdk.v2.streams.models.Subscriber](../../../../models/v2/streams/models/Subscriber.md)
- [foundry_sdk.v2.streams.models.SubscriberId](../../../../models/v2/streams/models/SubscriberId.md)
- [foundry_sdk.v2.streams.models.ViewRid](../../../../models/v2/streams/models/ViewRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/streams/Subscriber.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
