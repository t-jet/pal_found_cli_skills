# v2.streams.Dataset.create


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a streaming dataset with a stream on the specified branch, or if no branch is specified, on the
default branch ('master' for most enrollments). For more information on streaming datasets, refer to the
[streams](../../../../v2/streams/index.md) user documentation.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.streams.Dataset.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, *, name: datasets_models.DatasetName, parent_folder_rid: filesystem_models.FolderRid, schema: core_models.StreamSchema, branch_name: typing.Optional[core_models.BranchName]=None, compressed: typing.Optional[streams_models.Compressed]=None, partitions_count: typing.Optional[streams_models.PartitionsCount]=None, preview: typing.Optional[core_models.PreviewMode]=None, stream_type: typing.Optional[streams_models.StreamType]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> streams_models.Dataset: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| name | datasets_models.DatasetName | required | Value shape and constraints are in its referenced local type definition. |
| parent_folder_rid | filesystem_models.FolderRid | required | Value shape and constraints are in its referenced local type definition. |
| schema | core_models.StreamSchema | required | The Foundry schema to apply to the new stream. |
| branch_name | typing.Optional[core_models.BranchName] | None | The branch to create the initial stream on. If not specified, the default branch will be used ('master' for most enrollments). |
| compressed | typing.Optional[streams_models.Compressed] | None | Whether or not compression is enabled for the stream. Defaults to false. |
| partitions_count | typing.Optional[streams_models.PartitionsCount] | None | The number of partitions for the Foundry stream. Generally, each partition can handle about 5 mb/s of data, so for higher volume streams, more partitions are recommended. If not specified, 1 partition is used. This value cannot be changed later. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| stream_type | typing.Optional[streams_models.StreamType] | None | A conceptual representation of the expected shape of the data for a stream. HIGH_THROUGHPUT and LOW_LATENCY are not compatible with each other. Defaults to LOW_LATENCY. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CannotCreateStreamingDatasetInUserFolder | Cannot create a streaming dataset in a user folder. |
| CreateStreamingDatasetPermissionDenied | Could not create the Dataset. |
| InvalidFieldSchema | The field schema failed validations |
| InvalidSchema | The schema failed validations |
| InvalidStreamType | The stream type is invalid. |
| ResourceNameAlreadyExists | The provided resource name is already in use by another resource in the same folder. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/streams/datasets/create'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
streams_models.CreateStreamingDatasetRequest(name=name, parent_folder_rid=parent_folder_rid, schema_=schema, branch_name=branch_name, partitions_count=partitions_count, stream_type=stream_type, compressed=compressed)
```

**response_type**

```python
streams_models.Dataset
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CannotCreateStreamingDatasetInUserFolder': streams_errors.CannotCreateStreamingDatasetInUserFolder, 'CreateStreamingDatasetPermissionDenied': streams_errors.CreateStreamingDatasetPermissionDenied, 'InvalidFieldSchema': core_errors.InvalidFieldSchema, 'InvalidSchema': core_errors.InvalidSchema, 'InvalidStreamType': streams_errors.InvalidStreamType, 'ResourceNameAlreadyExists': filesystem_errors.ResourceNameAlreadyExists}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `streams_models.Dataset`. Ordinary async return: `typing.Awaitable[streams_models.Dataset]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | streams_models.Dataset |
| sync_raw | ApiResponse[streams_models.Dataset] |
| sync_streaming | StreamingContextManager[streams_models.Dataset] |
| async_ordinary | typing.Awaitable[streams_models.Dataset] |
| async_raw | Awaitable[AsyncApiResponse[streams_models.Dataset]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[streams_models.Dataset]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.errors.InvalidFieldSchema](../../../../models/v2/core/errors/InvalidFieldSchema.md)
- [foundry_sdk.v2.core.errors.InvalidFieldSchemaParameters](../../../../models/v2/core/errors/InvalidFieldSchemaParameters.md)
- [foundry_sdk.v2.core.errors.InvalidSchema](../../../../models/v2/core/errors/InvalidSchema.md)
- [foundry_sdk.v2.core.errors.InvalidSchemaParameters](../../../../models/v2/core/errors/InvalidSchemaParameters.md)
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
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.ShortType](../../../../models/v2/core/models/ShortType.md)
- [foundry_sdk.v2.core.models.StreamSchema](../../../../models/v2/core/models/StreamSchema.md)
- [foundry_sdk.v2.core.models.StringType](../../../../models/v2/core/models/StringType.md)
- [foundry_sdk.v2.core.models.StructFieldType](../../../../models/v2/core/models/StructFieldType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../../../models/v2/core/models/TimestampType.md)
- [foundry_sdk.v2.datasets.models.DatasetName](../../../../models/v2/datasets/models/DatasetName.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExists](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExists.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExistsParameters](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)
- [foundry_sdk.v2.streams.errors.CannotCreateStreamingDatasetInUserFolder](../../../../models/v2/streams/errors/CannotCreateStreamingDatasetInUserFolder.md)
- [foundry_sdk.v2.streams.errors.CannotCreateStreamingDatasetInUserFolderParameters](../../../../models/v2/streams/errors/CannotCreateStreamingDatasetInUserFolderParameters.md)
- [foundry_sdk.v2.streams.errors.CreateStreamingDatasetPermissionDenied](../../../../models/v2/streams/errors/CreateStreamingDatasetPermissionDenied.md)
- [foundry_sdk.v2.streams.errors.CreateStreamingDatasetPermissionDeniedParameters](../../../../models/v2/streams/errors/CreateStreamingDatasetPermissionDeniedParameters.md)
- [foundry_sdk.v2.streams.errors.InvalidStreamType](../../../../models/v2/streams/errors/InvalidStreamType.md)
- [foundry_sdk.v2.streams.errors.InvalidStreamTypeParameters](../../../../models/v2/streams/errors/InvalidStreamTypeParameters.md)
- [foundry_sdk.v2.streams.models.Compressed](../../../../models/v2/streams/models/Compressed.md)
- [foundry_sdk.v2.streams.models.CreateStreamingDatasetRequest](../../../../models/v2/streams/models/CreateStreamingDatasetRequest.md)
- [foundry_sdk.v2.streams.models.Dataset](../../../../models/v2/streams/models/Dataset.md)
- [foundry_sdk.v2.streams.models.PartitionsCount](../../../../models/v2/streams/models/PartitionsCount.md)
- [foundry_sdk.v2.streams.models.StreamType](../../../../models/v2/streams/models/StreamType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/streams/Dataset.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A stream dataset accepts records through its configured stream source; creation and ingestion have separate contracts. [Local procedure](../../../../v2/streams/index.md).

[Part 1](create.md)
