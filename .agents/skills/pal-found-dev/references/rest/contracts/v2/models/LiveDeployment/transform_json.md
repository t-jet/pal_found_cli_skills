# v2.models.LiveDeployment.transform_json


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Performs inference on the live deployment.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.LiveDeployment.transform_json`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def transform_json(self, live_deployment_rid: models_models.LiveDeploymentRid, *, input: typing.Dict[str, typing.Any], attribution: typing.Optional[core_models.Attribution]=None, preview: typing.Optional[core_models.PreviewMode]=None, trace_parent: typing.Optional[core_models.TraceParent]=None, trace_state: typing.Optional[core_models.TraceState]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.TransformLiveDeploymentResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| live_deployment_rid | models_models.LiveDeploymentRid | required | Value shape and constraints are in its referenced local type definition. |
| input | typing.Dict[str, typing.Any] | required | The input data for the model inference. The structure should match the model's transform API specification, where each key is an input name and the value is the corresponding input data. |
| attribution | typing.Optional[core_models.Attribution] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| trace_parent | typing.Optional[core_models.TraceParent] | None | Value shape and constraints are in its referenced local type definition. |
| trace_state | typing.Optional[core_models.TraceState] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| InferenceFailure | The inference request failed due to a model execution error or unexpected internal issue. This typically indicates a problem with the model itself rather than the input data. |
| InferenceInvalidInput | The inference request contains invalid input data that does not match the model's API specification. Check the error type for specific validation failure details. |
| InferenceTimeout | The live deployment took longer than 5 minutes to respond to the inference request. This typically indicates the model execution is taking too long or the deployment is under heavy load. |
| LiveDeploymentNotFound | The specified live deployment was not found. |
| TransformJsonLiveDeploymentPermissionDenied | Could not transformJson the LiveDeployment. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/models/liveDeployments/{liveDeploymentRid}/transformJson'
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
{'attribution': attribution, 'traceParent': trace_parent, 'traceState': trace_state, 'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
models_models.TransformJsonLiveDeploymentRequest(input=input)
```

**response_type**

```python
models_models.TransformLiveDeploymentResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'InferenceFailure': models_errors.InferenceFailure, 'InferenceInvalidInput': models_errors.InferenceInvalidInput, 'InferenceTimeout': models_errors.InferenceTimeout, 'LiveDeploymentNotFound': models_errors.LiveDeploymentNotFound, 'TransformJsonLiveDeploymentPermissionDenied': models_errors.TransformJsonLiveDeploymentPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.TransformLiveDeploymentResponse`. Ordinary async return: `typing.Awaitable[models_models.TransformLiveDeploymentResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.TransformLiveDeploymentResponse |
| sync_raw | ApiResponse[models_models.TransformLiveDeploymentResponse] |
| sync_streaming | StreamingContextManager[models_models.TransformLiveDeploymentResponse] |
| async_ordinary | typing.Awaitable[models_models.TransformLiveDeploymentResponse] |
| async_raw | Awaitable[AsyncApiResponse[models_models.TransformLiveDeploymentResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.TransformLiveDeploymentResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.Attribution](../../../../models/v2/core/models/Attribution.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.TraceParent](../../../../models/v2/core/models/TraceParent.md)
- [foundry_sdk.v2.core.models.TraceState](../../../../models/v2/core/models/TraceState.md)
- [foundry_sdk.v2.models.errors.InferenceFailure](../../../../models/v2/models/errors/InferenceFailure.md)
- [foundry_sdk.v2.models.errors.InferenceFailureParameters](../../../../models/v2/models/errors/InferenceFailureParameters.md)
- [foundry_sdk.v2.models.errors.InferenceInvalidInput](../../../../models/v2/models/errors/InferenceInvalidInput.md)
- [foundry_sdk.v2.models.errors.InferenceInvalidInputParameters](../../../../models/v2/models/errors/InferenceInvalidInputParameters.md)
- [foundry_sdk.v2.models.errors.InferenceTimeout](../../../../models/v2/models/errors/InferenceTimeout.md)
- [foundry_sdk.v2.models.errors.InferenceTimeoutParameters](../../../../models/v2/models/errors/InferenceTimeoutParameters.md)
- [foundry_sdk.v2.models.errors.LiveDeploymentNotFound](../../../../models/v2/models/errors/LiveDeploymentNotFound.md)
- [foundry_sdk.v2.models.errors.LiveDeploymentNotFoundParameters](../../../../models/v2/models/errors/LiveDeploymentNotFoundParameters.md)
- [foundry_sdk.v2.models.errors.TransformJsonLiveDeploymentPermissionDenied](../../../../models/v2/models/errors/TransformJsonLiveDeploymentPermissionDenied.md)
- [foundry_sdk.v2.models.errors.TransformJsonLiveDeploymentPermissionDeniedParameters](../../../../models/v2/models/errors/TransformJsonLiveDeploymentPermissionDeniedParameters.md)
- [foundry_sdk.v2.models.models.InconsistentArrayDimensionsError](../../../../models/v2/models/models/InconsistentArrayDimensionsError.md)
- [foundry_sdk.v2.models.models.InferenceInputErrorType](../../../../models/v2/models/models/InferenceInputErrorType.md)
- [foundry_sdk.v2.models.models.InvalidArrayShapeError](../../../../models/v2/models/models/InvalidArrayShapeError.md)
- [foundry_sdk.v2.models.models.InvalidMapFormatError](../../../../models/v2/models/models/InvalidMapFormatError.md)
- [foundry_sdk.v2.models.models.InvalidTabularFormatError](../../../../models/v2/models/models/InvalidTabularFormatError.md)
- [foundry_sdk.v2.models.models.LiveDeploymentRid](../../../../models/v2/models/models/LiveDeploymentRid.md)
- [foundry_sdk.v2.models.models.RequiredValueMissingError](../../../../models/v2/models/models/RequiredValueMissingError.md)
- [foundry_sdk.v2.models.models.TransformJsonLiveDeploymentRequest](../../../../models/v2/models/models/TransformJsonLiveDeploymentRequest.md)
- [foundry_sdk.v2.models.models.TransformLiveDeploymentResponse](../../../../models/v2/models/models/TransformLiveDeploymentResponse.md)
- [foundry_sdk.v2.models.models.TypeMismatchError](../../../../models/v2/models/models/TypeMismatchError.md)
- [foundry_sdk.v2.models.models.UnknownInputNameError](../../../../models/v2/models/models/UnknownInputNameError.md)
- [foundry_sdk.v2.models.models.UnsupportedTypeError](../../../../models/v2/models/models/UnsupportedTypeError.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/LiveDeployment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](transform_json.md)
