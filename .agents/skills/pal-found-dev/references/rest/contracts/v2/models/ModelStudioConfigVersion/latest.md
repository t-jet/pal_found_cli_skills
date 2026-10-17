# v2.models.ModelStudioConfigVersion.latest


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets the latest configuration version for a Model Studio.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.ModelStudio.ConfigVersion.latest`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def latest(self, model_studio_rid: models_models.ModelStudioRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> typing.Optional[models_models.ModelStudioConfigVersion]: ...
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
| LatestModelStudioConfigVersionsPermissionDenied | Could not latest the ModelStudioConfigVersion. |
| ModelStudioNotFound | The requested Model Studio was not found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/models/modelStudios/{modelStudioRid}/configVersions/latest'
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
typing.Optional[models_models.ModelStudioConfigVersion]
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'LatestModelStudioConfigVersionsPermissionDenied': models_errors.LatestModelStudioConfigVersionsPermissionDenied, 'ModelStudioNotFound': models_errors.ModelStudioNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `typing.Optional[models_models.ModelStudioConfigVersion]`. Ordinary async return: `typing.Awaitable[typing.Optional[models_models.ModelStudioConfigVersion]]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | typing.Optional[models_models.ModelStudioConfigVersion] |
| sync_raw | ApiResponse[typing.Optional[models_models.ModelStudioConfigVersion]] |
| sync_streaming | StreamingContextManager[typing.Optional[models_models.ModelStudioConfigVersion]] |
| async_ordinary | typing.Awaitable[typing.Optional[models_models.ModelStudioConfigVersion]] |
| async_raw | Awaitable[AsyncApiResponse[typing.Optional[models_models.ModelStudioConfigVersion]]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[typing.Optional[models_models.ModelStudioConfigVersion]]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.ColumnName](../../../../models/v2/core/models/ColumnName.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.models.errors.LatestModelStudioConfigVersionsPermissionDenied](../../../../models/v2/models/errors/LatestModelStudioConfigVersionsPermissionDenied.md)
- [foundry_sdk.v2.models.errors.LatestModelStudioConfigVersionsPermissionDeniedParameters](../../../../models/v2/models/errors/LatestModelStudioConfigVersionsPermissionDeniedParameters.md)
- [foundry_sdk.v2.models.errors.ModelStudioNotFound](../../../../models/v2/models/errors/ModelStudioNotFound.md)
- [foundry_sdk.v2.models.errors.ModelStudioNotFoundParameters](../../../../models/v2/models/errors/ModelStudioNotFoundParameters.md)
- [foundry_sdk.v2.models.models.ColumnTypeSpecId](../../../../models/v2/models/models/ColumnTypeSpecId.md)
- [foundry_sdk.v2.models.models.DatasetInput](../../../../models/v2/models/models/DatasetInput.md)
- [foundry_sdk.v2.models.models.GpuType](../../../../models/v2/models/models/GpuType.md)
- [foundry_sdk.v2.models.models.InputAlias](../../../../models/v2/models/models/InputAlias.md)
- [foundry_sdk.v2.models.models.ModelOutput](../../../../models/v2/models/models/ModelOutput.md)
- [foundry_sdk.v2.models.models.ModelRid](../../../../models/v2/models/models/ModelRid.md)
- [foundry_sdk.v2.models.models.ModelStudioConfigVersion](../../../../models/v2/models/models/ModelStudioConfigVersion.md)
- [foundry_sdk.v2.models.models.ModelStudioConfigVersionName](../../../../models/v2/models/models/ModelStudioConfigVersionName.md)
- [foundry_sdk.v2.models.models.ModelStudioConfigVersionNumber](../../../../models/v2/models/models/ModelStudioConfigVersionNumber.md)
- [foundry_sdk.v2.models.models.ModelStudioInput](../../../../models/v2/models/models/ModelStudioInput.md)
- [foundry_sdk.v2.models.models.ModelStudioOutput](../../../../models/v2/models/models/ModelStudioOutput.md)
- [foundry_sdk.v2.models.models.ModelStudioRid](../../../../models/v2/models/models/ModelStudioRid.md)
- [foundry_sdk.v2.models.models.ModelStudioWorkerConfig](../../../../models/v2/models/models/ModelStudioWorkerConfig.md)
- [foundry_sdk.v2.models.models.OutputAlias](../../../../models/v2/models/models/OutputAlias.md)
- [foundry_sdk.v2.models.models.ResourceConfiguration](../../../../models/v2/models/models/ResourceConfiguration.md)
- [foundry_sdk.v2.models.models.TrainerId](../../../../models/v2/models/models/TrainerId.md)
- [foundry_sdk.v2.models.models.TrainerVersionLocator](../../../../models/v2/models/models/TrainerVersionLocator.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/ModelStudioConfigVersion.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](latest.md)
