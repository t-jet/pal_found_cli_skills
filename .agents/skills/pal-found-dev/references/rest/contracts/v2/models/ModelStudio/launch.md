# v2.models.ModelStudio.launch


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Launches a new training run for the Model Studio using the latest configuration version.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.ModelStudio.launch`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def launch(self, model_studio_rid: models_models.ModelStudioRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.ModelStudioRun: ...
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
| LaunchModelStudioPermissionDenied | Permission denied to launch a Model Studio run. |
| ModelStudioNotFound | The requested Model Studio was not found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/models/modelStudios/{modelStudioRid}/launch'
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
models_models.ModelStudioRun
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'LaunchModelStudioPermissionDenied': models_errors.LaunchModelStudioPermissionDenied, 'ModelStudioNotFound': models_errors.ModelStudioNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.ModelStudioRun`. Ordinary async return: `typing.Awaitable[models_models.ModelStudioRun]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.ModelStudioRun |
| sync_raw | ApiResponse[models_models.ModelStudioRun] |
| sync_streaming | StreamingContextManager[models_models.ModelStudioRun] |
| async_ordinary | typing.Awaitable[models_models.ModelStudioRun] |
| async_raw | Awaitable[AsyncApiResponse[models_models.ModelStudioRun]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.ModelStudioRun]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.models.errors.LaunchModelStudioPermissionDenied](../../../../models/v2/models/errors/LaunchModelStudioPermissionDenied.md)
- [foundry_sdk.v2.models.errors.LaunchModelStudioPermissionDeniedParameters](../../../../models/v2/models/errors/LaunchModelStudioPermissionDeniedParameters.md)
- [foundry_sdk.v2.models.errors.ModelStudioNotFound](../../../../models/v2/models/errors/ModelStudioNotFound.md)
- [foundry_sdk.v2.models.errors.ModelStudioNotFoundParameters](../../../../models/v2/models/errors/ModelStudioNotFoundParameters.md)
- [foundry_sdk.v2.models.models.ExperimentRid](../../../../models/v2/models/models/ExperimentRid.md)
- [foundry_sdk.v2.models.models.ModelRid](../../../../models/v2/models/models/ModelRid.md)
- [foundry_sdk.v2.models.models.ModelStudioConfigVersionNumber](../../../../models/v2/models/models/ModelStudioConfigVersionNumber.md)
- [foundry_sdk.v2.models.models.ModelStudioRid](../../../../models/v2/models/models/ModelStudioRid.md)
- [foundry_sdk.v2.models.models.ModelStudioRun](../../../../models/v2/models/models/ModelStudioRun.md)
- [foundry_sdk.v2.models.models.ModelStudioRunBuildRid](../../../../models/v2/models/models/ModelStudioRunBuildRid.md)
- [foundry_sdk.v2.models.models.ModelStudioRunJobRid](../../../../models/v2/models/models/ModelStudioRunJobRid.md)
- [foundry_sdk.v2.models.models.ModelStudioRunModelOutput](../../../../models/v2/models/models/ModelStudioRunModelOutput.md)
- [foundry_sdk.v2.models.models.ModelStudioRunOutput](../../../../models/v2/models/models/ModelStudioRunOutput.md)
- [foundry_sdk.v2.models.models.ModelVersionRid](../../../../models/v2/models/models/ModelVersionRid.md)
- [foundry_sdk.v2.models.models.OutputAlias](../../../../models/v2/models/models/OutputAlias.md)
- [foundry_sdk.v2.models.models.RunId](../../../../models/v2/models/models/RunId.md)
- [foundry_sdk.v2.orchestration.models.BuildStatus](../../../../models/v2/orchestration/models/BuildStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/ModelStudio.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](launch.md)
