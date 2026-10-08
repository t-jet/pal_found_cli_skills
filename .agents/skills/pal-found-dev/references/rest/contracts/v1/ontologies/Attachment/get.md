# v1.ontologies.Attachment.get


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the metadata of an attachment.

## SDK invocation contract

```python
def get(self, attachment_rid: ontologies_models.AttachmentRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.Attachment: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| attachment_rid | ontologies_models.AttachmentRid | required | The RID of the attachment. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v1/attachments/{attachmentRid}'
```

**query_params**

```python
{}
```

**path_params**

```python
{'attachmentRid': attachment_rid}
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
ontologies_models.Attachment
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

Ordinary sync return: `ontologies_models.Attachment`. Ordinary async return: `typing.Awaitable[ontologies_models.Attachment]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.Attachment |
| sync_raw | ApiResponse[ontologies_models.Attachment] |
| sync_streaming | StreamingContextManager[ontologies_models.Attachment] |
| async_ordinary | typing.Awaitable[ontologies_models.Attachment] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.Attachment]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.Attachment]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.models.Filename](../../../../models/v1/core/models/Filename.md)
- [foundry_sdk.v1.core.models.MediaType](../../../../models/v1/core/models/MediaType.md)
- [foundry_sdk.v1.core.models.SizeBytes](../../../../models/v1/core/models/SizeBytes.md)
- [foundry_sdk.v1.ontologies.models.Attachment](../../../../models/v1/ontologies/models/Attachment.md)
- [foundry_sdk.v1.ontologies.models.AttachmentRid](../../../../models/v1/ontologies/models/AttachmentRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/Attachment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
