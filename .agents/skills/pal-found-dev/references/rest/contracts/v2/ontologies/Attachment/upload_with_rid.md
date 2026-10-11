# v2.ontologies.Attachment.upload_with_rid


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

This endpoint is identical to `/v2/ontologies/attachments/upload` but additionally accepts a previously
generated `AttachmentRid`.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.Attachment.upload_with_rid`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def upload_with_rid(self, attachment_rid: ontologies_models.AttachmentRid, body: bytes, *, content_length: core_models.ContentLength, content_type: core_models.ContentType, filename: core_models.Filename, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.AttachmentV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| attachment_rid | ontologies_models.AttachmentRid | required | The `AttachmentRid` of the attachment being uploaded. |
| body | bytes | required | Body of the request |
| content_length | core_models.ContentLength | required | The size in bytes of the file content being uploaded. |
| content_type | core_models.ContentType | required | The media type of the file being uploaded. |
| filename | core_models.Filename | required | The name of the file being uploaded. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/ontologies/attachments/upload/{attachmentRid}'
```

**query_params**

```python
{'filename': filename, 'preview': preview}
```

**path_params**

```python
{'attachmentRid': attachment_rid}
```

**header_params**

```python
{'Content-Length': content_length, 'Content-Type': content_type, 'Content-Type': '*/*', 'Accept': 'application/json'}
```

**body**

```python
body
```

**response_type**

```python
ontologies_models.AttachmentV2
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

Ordinary sync return: `ontologies_models.AttachmentV2`. Ordinary async return: `typing.Awaitable[ontologies_models.AttachmentV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.AttachmentV2 |
| sync_raw | ApiResponse[ontologies_models.AttachmentV2] |
| sync_streaming | StreamingContextManager[ontologies_models.AttachmentV2] |
| async_ordinary | typing.Awaitable[ontologies_models.AttachmentV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.AttachmentV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.AttachmentV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.ContentLength](../../../../models/v2/core/models/ContentLength.md)
- [foundry_sdk.v2.core.models.ContentType](../../../../models/v2/core/models/ContentType.md)
- [foundry_sdk.v2.core.models.Filename](../../../../models/v2/core/models/Filename.md)
- [foundry_sdk.v2.core.models.MediaType](../../../../models/v2/core/models/MediaType.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.SizeBytes](../../../../models/v2/core/models/SizeBytes.md)
- [foundry_sdk.v2.ontologies.models.AttachmentRid](../../../../models/v2/ontologies/models/AttachmentRid.md)
- [foundry_sdk.v2.ontologies.models.AttachmentV2](../../../../models/v2/ontologies/models/AttachmentV2.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/Attachment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](upload_with_rid.md)
