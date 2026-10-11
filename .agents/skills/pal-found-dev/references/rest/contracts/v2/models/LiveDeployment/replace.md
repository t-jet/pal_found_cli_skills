# v2.models.LiveDeployment.replace


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Updates the runtime configuration of the live deployment. The deployment will apply the new configuration to the running replicas.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.LiveDeployment.replace`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def replace(self, live_deployment_rid: models_models.LiveDeploymentRid, *, runtime_configuration: models_models.LiveDeploymentRuntimeConfiguration, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.LiveDeployment: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| live_deployment_rid | models_models.LiveDeploymentRid | required | Value shape and constraints are in its referenced local type definition. |
| runtime_configuration | models_models.LiveDeploymentRuntimeConfiguration | required | The compute resource configuration for the deployment. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GpuTypeNotAvailable | The requested GPU type is not available. Use a GPU type that is available in the deployment's resource queue. |
| InvalidGpuCount | The GPU count is invalid. The GPU count must be between 1 and the maximum allowed for the requested GPU type. |
| LiveDeploymentNotFound | The specified live deployment was not found. |
| ReplaceLiveDeploymentPermissionDenied | Could not replace the LiveDeployment. |
| ThreadCountTooHigh | The specified thread count exceeds the maximum allowed value. |
| UnsupportedLiveDeployment | The Live Deployment type is not supported by the API. |

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/models/liveDeployments/{liveDeploymentRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'liveDeploymentRid': live_deployment_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
models_models.ReplaceLiveDeploymentRequest(runtime_configuration=runtime_configuration)
```

**response_type**

```python
models_models.LiveDeployment
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GpuTypeNotAvailable': models_errors.GpuTypeNotAvailable, 'InvalidGpuCount': models_errors.InvalidGpuCount, 'LiveDeploymentNotFound': models_errors.LiveDeploymentNotFound, 'ReplaceLiveDeploymentPermissionDenied': models_errors.ReplaceLiveDeploymentPermissionDenied, 'ThreadCountTooHigh': models_errors.ThreadCountTooHigh, 'UnsupportedLiveDeployment': models_errors.UnsupportedLiveDeployment}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.LiveDeployment`. Ordinary async return: `typing.Awaitable[models_models.LiveDeployment]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.LiveDeployment |
| sync_raw | ApiResponse[models_models.LiveDeployment] |
| sync_streaming | StreamingContextManager[models_models.LiveDeployment] |
| async_ordinary | typing.Awaitable[models_models.LiveDeployment] |
| async_raw | Awaitable[AsyncApiResponse[models_models.LiveDeployment]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.LiveDeployment]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.Duration](../../../../models/v2/core/models/Duration.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.TimeUnit](../../../../models/v2/core/models/TimeUnit.md)
- [foundry_sdk.v2.models.errors.GpuTypeNotAvailable](../../../../models/v2/models/errors/GpuTypeNotAvailable.md)
- [foundry_sdk.v2.models.errors.GpuTypeNotAvailableParameters](../../../../models/v2/models/errors/GpuTypeNotAvailableParameters.md)
- [foundry_sdk.v2.models.errors.InvalidGpuCount](../../../../models/v2/models/errors/InvalidGpuCount.md)
- [foundry_sdk.v2.models.errors.InvalidGpuCountParameters](../../../../models/v2/models/errors/InvalidGpuCountParameters.md)
- [foundry_sdk.v2.models.errors.LiveDeploymentNotFound](../../../../models/v2/models/errors/LiveDeploymentNotFound.md)
- [foundry_sdk.v2.models.errors.LiveDeploymentNotFoundParameters](../../../../models/v2/models/errors/LiveDeploymentNotFoundParameters.md)
- [foundry_sdk.v2.models.errors.ReplaceLiveDeploymentPermissionDenied](../../../../models/v2/models/errors/ReplaceLiveDeploymentPermissionDenied.md)
- [foundry_sdk.v2.models.errors.ReplaceLiveDeploymentPermissionDeniedParameters](../../../../models/v2/models/errors/ReplaceLiveDeploymentPermissionDeniedParameters.md)
- [foundry_sdk.v2.models.errors.ThreadCountTooHigh](../../../../models/v2/models/errors/ThreadCountTooHigh.md)
- [foundry_sdk.v2.models.errors.ThreadCountTooHighParameters](../../../../models/v2/models/errors/ThreadCountTooHighParameters.md)
- [foundry_sdk.v2.models.errors.UnsupportedLiveDeployment](../../../../models/v2/models/errors/UnsupportedLiveDeployment.md)
- [foundry_sdk.v2.models.errors.UnsupportedLiveDeploymentParameters](../../../../models/v2/models/errors/UnsupportedLiveDeploymentParameters.md)
- [foundry_sdk.v2.models.models.GpuType](../../../../models/v2/models/models/GpuType.md)
- [foundry_sdk.v2.models.models.LiveDeployment](../../../../models/v2/models/models/LiveDeployment.md)
- [foundry_sdk.v2.models.models.LiveDeploymentGpu](../../../../models/v2/models/models/LiveDeploymentGpu.md)
- [foundry_sdk.v2.models.models.LiveDeploymentModelVersion](../../../../models/v2/models/models/LiveDeploymentModelVersion.md)
- [foundry_sdk.v2.models.models.LiveDeploymentRid](../../../../models/v2/models/models/LiveDeploymentRid.md)
- [foundry_sdk.v2.models.models.LiveDeploymentRuntimeConfiguration](../../../../models/v2/models/models/LiveDeploymentRuntimeConfiguration.md)
- [foundry_sdk.v2.models.models.LiveDeploymentScalingConfiguration](../../../../models/v2/models/models/LiveDeploymentScalingConfiguration.md)
- [foundry_sdk.v2.models.models.LiveDeploymentState](../../../../models/v2/models/models/LiveDeploymentState.md)
- [foundry_sdk.v2.models.models.LiveDeploymentStatus](../../../../models/v2/models/models/LiveDeploymentStatus.md)
- [foundry_sdk.v2.models.models.ModelRid](../../../../models/v2/models/models/ModelRid.md)
- [foundry_sdk.v2.models.models.ModelVersionRid](../../../../models/v2/models/models/ModelVersionRid.md)
- [foundry_sdk.v2.models.models.ReplaceLiveDeploymentRequest](../../../../models/v2/models/models/ReplaceLiveDeploymentRequest.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/LiveDeployment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](replace.md)
