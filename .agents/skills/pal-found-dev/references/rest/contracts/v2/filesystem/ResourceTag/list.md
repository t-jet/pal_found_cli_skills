# v2.filesystem.ResourceTag.list


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List the tags applied to a resource.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Resource.Tag.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, resource_rid: filesystem_models.ResourceRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> filesystem_models.ListResourceTagsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| resource_rid | filesystem_models.ResourceRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ResourceNotFound | The given Resource could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/filesystem/resources/{resourceRid}/tags'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'resourceRid': resource_rid}
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
filesystem_models.ListResourceTagsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ResourceNotFound': filesystem_errors.ResourceNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `filesystem_models.ListResourceTagsResponse`. Ordinary async return: `typing.Awaitable[filesystem_models.ListResourceTagsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | filesystem_models.ListResourceTagsResponse |
| sync_raw | ApiResponse[filesystem_models.ListResourceTagsResponse] |
| sync_streaming | StreamingContextManager[filesystem_models.ListResourceTagsResponse] |
| async_ordinary | typing.Awaitable[filesystem_models.ListResourceTagsResponse] |
| async_raw | Awaitable[AsyncApiResponse[filesystem_models.ListResourceTagsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[filesystem_models.ListResourceTagsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFound](../../../../models/v2/filesystem/errors/ResourceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNotFoundParameters](../../../../models/v2/filesystem/errors/ResourceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.ListResourceTagsResponse](../../../../models/v2/filesystem/models/ListResourceTagsResponse.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceTag](../../../../models/v2/filesystem/models/ResourceTag.md)
- [foundry_sdk.v2.filesystem.models.ResourceTagDisplayName](../../../../models/v2/filesystem/models/ResourceTagDisplayName.md)
- [foundry_sdk.v2.filesystem.models.TagRid](../../../../models/v2/filesystem/models/TagRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/ResourceTag.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
