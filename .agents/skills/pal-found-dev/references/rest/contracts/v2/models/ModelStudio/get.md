# v2.models.ModelStudio.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets details about a Model Studio by its RID.

## SDK invocation contract

```python
def get(self, model_studio_rid: models_models.ModelStudioRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.ModelStudio: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| model_studio_rid | models_models.ModelStudioRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ModelStudioNotFound | The requested Model Studio was not found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/models/modelStudios/{modelStudioRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'modelStudioRid': model_studio_rid}
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
models_models.ModelStudio
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ModelStudioNotFound': models_errors.ModelStudioNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.ModelStudio`. Ordinary async return: `typing.Awaitable[models_models.ModelStudio]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.ModelStudio |
| sync_raw | ApiResponse[models_models.ModelStudio] |
| sync_streaming | StreamingContextManager[models_models.ModelStudio] |
| async_ordinary | typing.Awaitable[models_models.ModelStudio] |
| async_raw | Awaitable[AsyncApiResponse[models_models.ModelStudio]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.ModelStudio]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)
- [foundry_sdk.v2.models.errors.ModelStudioNotFound](../../../../models/v2/models/errors/ModelStudioNotFound.md)
- [foundry_sdk.v2.models.errors.ModelStudioNotFoundParameters](../../../../models/v2/models/errors/ModelStudioNotFoundParameters.md)
- [foundry_sdk.v2.models.models.ModelStudio](../../../../models/v2/models/models/ModelStudio.md)
- [foundry_sdk.v2.models.models.ModelStudioRid](../../../../models/v2/models/models/ModelStudioRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/ModelStudio.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
