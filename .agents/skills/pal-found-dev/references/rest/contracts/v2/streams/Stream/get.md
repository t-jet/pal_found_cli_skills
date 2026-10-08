# v2.streams.Stream.get


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get a stream by its branch name. If the branch does not exist, there is no stream on that branch, or the
user does not have permission to access the stream, a 404 error will be returned.

## SDK invocation contract

```python
def get(self, dataset_rid: core_models.DatasetRid, stream_branch_name: core_models.BranchName, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> streams_models.Stream: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| stream_branch_name | core_models.BranchName | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| InvalidFieldSchema | The field schema failed validations |
| InvalidStreamNoSchema | The requested stream exists but is invalid, as it does not have a schema. |
| InvalidStreamType | The stream type is invalid. |
| StreamNotFound | The given Stream could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/streams/datasets/{datasetRid}/streams/{streamBranchName}'
```

**query_params**

```python
{}
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
streams_models.Stream
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'InvalidFieldSchema': core_errors.InvalidFieldSchema, 'InvalidStreamNoSchema': streams_errors.InvalidStreamNoSchema, 'InvalidStreamType': streams_errors.InvalidStreamType, 'StreamNotFound': streams_errors.StreamNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `streams_models.Stream`. Ordinary async return: `typing.Awaitable[streams_models.Stream]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | streams_models.Stream |
| sync_raw | ApiResponse[streams_models.Stream] |
| sync_streaming | StreamingContextManager[streams_models.Stream] |
| async_ordinary | typing.Awaitable[streams_models.Stream] |
| async_raw | Awaitable[AsyncApiResponse[streams_models.Stream]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[streams_models.Stream]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.errors.InvalidFieldSchema](../../../../models/v2/core/errors/InvalidFieldSchema.md)
- [foundry_sdk.v2.core.errors.InvalidFieldSchemaParameters](../../../../models/v2/core/errors/InvalidFieldSchemaParameters.md)
- [foundry_sdk.v2.core.models.ArrayFieldType](../../../../models/v2/core/models/ArrayFieldType.md)
- [foundry_sdk.v2.core.models.BinaryType](../../../../models/v2/core/models/BinaryType.md)
- [foundry_sdk.v2.core.models.BooleanType](../../../../models/v2/core/models/BooleanType.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.ByteType](../../../../models/v2/core/models/ByteType.md)
- [foundry_sdk.v2.core.models.ChangeDataCaptureConfiguration](../../../../models/v2/core/models/ChangeDataCaptureConfiguration.md)
- [foundry_sdk.v2.core.models.CustomMetadata](../../../../models/v2/core/models/CustomMetadata.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.DateType](../../../../models/v2/core/models/DateType.md)
- [foundry_sdk.v2.core.models.DecimalType](../../../../models/v2/core/models/DecimalType.md)
- [foundry_sdk.v2.core.models.DoubleType](../../../../models/v2/core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.Field](../../../../models/v2/core/models/Field.md)
- [foundry_sdk.v2.core.models.FieldDataType](../../../../models/v2/core/models/FieldDataType.md)
- [foundry_sdk.v2.core.models.FieldName](../../../../models/v2/core/models/FieldName.md)
- [foundry_sdk.v2.core.models.FieldSchema](../../../../models/v2/core/models/FieldSchema.md)
- [foundry_sdk.v2.core.models.FloatType](../../../../models/v2/core/models/FloatType.md)
- [foundry_sdk.v2.core.models.FullRowChangeDataCaptureConfiguration](../../../../models/v2/core/models/FullRowChangeDataCaptureConfiguration.md)
- [foundry_sdk.v2.core.models.IntegerType](../../../../models/v2/core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../../../models/v2/core/models/LongType.md)
- [foundry_sdk.v2.core.models.MapFieldType](../../../../models/v2/core/models/MapFieldType.md)
- [foundry_sdk.v2.core.models.ShortType](../../../../models/v2/core/models/ShortType.md)
- [foundry_sdk.v2.core.models.StreamSchema](../../../../models/v2/core/models/StreamSchema.md)
- [foundry_sdk.v2.core.models.StringType](../../../../models/v2/core/models/StringType.md)
- [foundry_sdk.v2.core.models.StructFieldType](../../../../models/v2/core/models/StructFieldType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../../../models/v2/core/models/TimestampType.md)
- [foundry_sdk.v2.streams.errors.InvalidStreamNoSchema](../../../../models/v2/streams/errors/InvalidStreamNoSchema.md)
- [foundry_sdk.v2.streams.errors.InvalidStreamNoSchemaParameters](../../../../models/v2/streams/errors/InvalidStreamNoSchemaParameters.md)
- [foundry_sdk.v2.streams.errors.InvalidStreamType](../../../../models/v2/streams/errors/InvalidStreamType.md)
- [foundry_sdk.v2.streams.errors.InvalidStreamTypeParameters](../../../../models/v2/streams/errors/InvalidStreamTypeParameters.md)
- [foundry_sdk.v2.streams.errors.StreamNotFound](../../../../models/v2/streams/errors/StreamNotFound.md)
- [foundry_sdk.v2.streams.errors.StreamNotFoundParameters](../../../../models/v2/streams/errors/StreamNotFoundParameters.md)
- [foundry_sdk.v2.streams.models.Compressed](../../../../models/v2/streams/models/Compressed.md)
- [foundry_sdk.v2.streams.models.PartitionsCount](../../../../models/v2/streams/models/PartitionsCount.md)
- [foundry_sdk.v2.streams.models.Stream](../../../../models/v2/streams/models/Stream.md)
- [foundry_sdk.v2.streams.models.StreamType](../../../../models/v2/streams/models/StreamType.md)
- [foundry_sdk.v2.streams.models.ViewRid](../../../../models/v2/streams/models/ViewRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/streams/Stream.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
