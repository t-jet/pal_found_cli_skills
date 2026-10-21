# v2.models.LiveDeployment.create


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new live deployment for a model version with the specified runtime configuration. The deployment will begin provisioning compute resources and deploying the target model version.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.LiveDeployment.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, *, deployment_type: models_models.CreateLiveDeploymentTarget, runtime_configuration: models_models.LiveDeploymentRuntimeConfiguration, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.LiveDeployment: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| deployment_type | models_models.CreateLiveDeploymentTarget | required | The target model source for the live deployment. Determines which model and version selection strategy to use when creating the deployment. |
| runtime_configuration | models_models.LiveDeploymentRuntimeConfiguration | required | The compute resource configuration for the deployment. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateLiveDeploymentPermissionDenied | Could not create the LiveDeployment. |
| GpuTypeNotAvailable | The requested GPU type is not available. Use a GPU type that is available in the deployment's resource queue. |
| InvalidGpuCount | The GPU count is invalid. The GPU count must be between 1 and the maximum allowed for the requested GPU type. |
| ModelNotFound | The given Model could not be found. |
| ThreadCountTooHigh | The specified thread count exceeds the maximum allowed value. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/models/liveDeployments'
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
models_models.CreateLiveDeploymentRequest(deployment_type=deployment_type, runtime_configuration=runtime_configuration)
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
{'CreateLiveDeploymentPermissionDenied': models_errors.CreateLiveDeploymentPermissionDenied, 'GpuTypeNotAvailable': models_errors.GpuTypeNotAvailable, 'InvalidGpuCount': models_errors.InvalidGpuCount, 'ModelNotFound': models_errors.ModelNotFound, 'ThreadCountTooHigh': models_errors.ThreadCountTooHigh}
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
- [foundry_sdk.v2.models.errors.CreateLiveDeploymentPermissionDenied](../../../../models/v2/models/errors/CreateLiveDeploymentPermissionDenied.md)
- [foundry_sdk.v2.models.errors.CreateLiveDeploymentPermissionDeniedParameters](../../../../models/v2/models/errors/CreateLiveDeploymentPermissionDeniedParameters.md)
- [foundry_sdk.v2.models.errors.GpuTypeNotAvailable](../../../../models/v2/models/errors/GpuTypeNotAvailable.md)
- [foundry_sdk.v2.models.errors.GpuTypeNotAvailableParameters](../../../../models/v2/models/errors/GpuTypeNotAvailableParameters.md)
- [foundry_sdk.v2.models.errors.InvalidGpuCount](../../../../models/v2/models/errors/InvalidGpuCount.md)
- [foundry_sdk.v2.models.errors.InvalidGpuCountParameters](../../../../models/v2/models/errors/InvalidGpuCountParameters.md)
- [foundry_sdk.v2.models.errors.ModelNotFound](../../../../models/v2/models/errors/ModelNotFound.md)
- [foundry_sdk.v2.models.errors.ModelNotFoundParameters](../../../../models/v2/models/errors/ModelNotFoundParameters.md)
- [foundry_sdk.v2.models.errors.ThreadCountTooHigh](../../../../models/v2/models/errors/ThreadCountTooHigh.md)
- [foundry_sdk.v2.models.errors.ThreadCountTooHighParameters](../../../../models/v2/models/errors/ThreadCountTooHighParameters.md)
- [foundry_sdk.v2.models.models.CreateLiveDeploymentRequest](../../../../models/v2/models/models/CreateLiveDeploymentRequest.md)
- [foundry_sdk.v2.models.models.CreateLiveDeploymentTarget](../../../../models/v2/models/models/CreateLiveDeploymentTarget.md)
- [foundry_sdk.v2.models.models.DirectCreateLiveDeploymentTarget](../../../../models/v2/models/models/DirectCreateLiveDeploymentTarget.md)
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

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/LiveDeployment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
