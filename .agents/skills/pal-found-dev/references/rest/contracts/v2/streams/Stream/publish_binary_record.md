# v2.streams.Stream.publish_binary_record


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Publish a single binary record to the stream. The stream's schema must be a single binary field.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.streams.Dataset.Stream.publish_binary_record`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def publish_binary_record(self, dataset_rid: core_models.DatasetRid, stream_branch_name: core_models.BranchName, body: bytes, *, view_rid: typing.Optional[streams_models.ViewRid]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| stream_branch_name | core_models.BranchName | required | Value shape and constraints are in its referenced local type definition. |
| body | bytes | required | The binary record to publish to the stream |
| view_rid | typing.Optional[streams_models.ViewRid] | None | If provided, this endpoint will only write to the stream corresponding to the specified view RID. If not provided, this endpoint will write to the latest stream on the branch. Providing this value is an advanced configuration, to be used when additional control over the underlying streaming data structures is needed. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| PublishBinaryRecordToStreamPermissionDenied | Could not publishBinaryRecord the Stream. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/highScale/streams/datasets/{datasetRid}/streams/{streamBranchName}/publishBinaryRecord'
```

**query_params**

```python
{'viewRid': view_rid}
```

**path_params**

```python
{'datasetRid': dataset_rid, 'streamBranchName': stream_branch_name}
```

**header_params**

```python
{'Content-Type': 'application/octet-stream'}
```

**body**

```python
body
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
{'PublishBinaryRecordToStreamPermissionDenied': streams_errors.PublishBinaryRecordToStreamPermissionDenied}
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
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.streams.errors.PublishBinaryRecordToStreamPermissionDenied](../../../../models/v2/streams/errors/PublishBinaryRecordToStreamPermissionDenied.md)
- [foundry_sdk.v2.streams.errors.PublishBinaryRecordToStreamPermissionDeniedParameters](../../../../models/v2/streams/errors/PublishBinaryRecordToStreamPermissionDeniedParameters.md)
- [foundry_sdk.v2.streams.models.ViewRid](../../../../models/v2/streams/models/ViewRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/streams/Stream.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](publish_binary_record.md)
