# v2.models.LiveDeployment.list


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists direct live deployments for the specified Model, optionally filtered by branch. Only direct deployments (those tracking the latest model version on a branch) are returned.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.LiveDeployment.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, *, model_rid: models_models.ModelRid, branch: typing.Optional[core_models.BranchName]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.ListLiveDeploymentsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| model_rid | models_models.ModelRid | required | The Resource Identifier (RID) of the Model to list live deployments for. |
| branch | typing.Optional[core_models.BranchName] | None | If provided, only return the live deployment associated with this branch. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ModelNotFound | The given Model could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/models/liveDeployments'
```

**query_params**

```python
{'modelRid': model_rid, 'branch': branch, 'preview': preview}
```

**path_params**

```python
{}
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
models_models.ListLiveDeploymentsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ModelNotFound': models_errors.ModelNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.ListLiveDeploymentsResponse`. Ordinary async return: `typing.Awaitable[models_models.ListLiveDeploymentsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.ListLiveDeploymentsResponse |
| sync_raw | ApiResponse[models_models.ListLiveDeploymentsResponse] |
| sync_streaming | StreamingContextManager[models_models.ListLiveDeploymentsResponse] |
| async_ordinary | typing.Awaitable[models_models.ListLiveDeploymentsResponse] |
| async_raw | Awaitable[AsyncApiResponse[models_models.ListLiveDeploymentsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.ListLiveDeploymentsResponse]] |

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
- [foundry_sdk.v2.models.errors.ModelNotFound](../../../../models/v2/models/errors/ModelNotFound.md)
- [foundry_sdk.v2.models.errors.ModelNotFoundParameters](../../../../models/v2/models/errors/ModelNotFoundParameters.md)
- [foundry_sdk.v2.models.models.GpuType](../../../../models/v2/models/models/GpuType.md)
- [foundry_sdk.v2.models.models.ListLiveDeploymentsResponse](../../../../models/v2/models/models/ListLiveDeploymentsResponse.md)
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

[Part 1](list.md)
