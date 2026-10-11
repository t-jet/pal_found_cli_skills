# v2.models.ModelStudioTrainer.list


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all available trainers for Model Studios.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.ModelStudioTrainer.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.ListModelStudioTrainersResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
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
'/v2/models/modelStudioTrainers'
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
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
models_models.ListModelStudioTrainersResponse
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

Ordinary sync return: `models_models.ListModelStudioTrainersResponse`. Ordinary async return: `typing.Awaitable[models_models.ListModelStudioTrainersResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.ListModelStudioTrainersResponse |
| sync_raw | ApiResponse[models_models.ListModelStudioTrainersResponse] |
| sync_streaming | StreamingContextManager[models_models.ListModelStudioTrainersResponse] |
| async_ordinary | typing.Awaitable[models_models.ListModelStudioTrainersResponse] |
| async_raw | Awaitable[AsyncApiResponse[models_models.ListModelStudioTrainersResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.ListModelStudioTrainersResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.models.models.ListModelStudioTrainersResponse](../../../../models/v2/models/models/ListModelStudioTrainersResponse.md)
- [foundry_sdk.v2.models.models.ModelStudioTrainer](../../../../models/v2/models/models/ModelStudioTrainer.md)
- [foundry_sdk.v2.models.models.ModelStudioTrainerExperimental](../../../../models/v2/models/models/ModelStudioTrainerExperimental.md)
- [foundry_sdk.v2.models.models.TrainerDescription](../../../../models/v2/models/models/TrainerDescription.md)
- [foundry_sdk.v2.models.models.TrainerId](../../../../models/v2/models/models/TrainerId.md)
- [foundry_sdk.v2.models.models.TrainerInputsSpecification](../../../../models/v2/models/models/TrainerInputsSpecification.md)
- [foundry_sdk.v2.models.models.TrainerName](../../../../models/v2/models/models/TrainerName.md)
- [foundry_sdk.v2.models.models.TrainerOutputsSpecification](../../../../models/v2/models/models/TrainerOutputsSpecification.md)
- [foundry_sdk.v2.models.models.TrainerSchemaDefinition](../../../../models/v2/models/models/TrainerSchemaDefinition.md)
- [foundry_sdk.v2.models.models.TrainerType](../../../../models/v2/models/models/TrainerType.md)
- [foundry_sdk.v2.models.models.TrainerVersion](../../../../models/v2/models/models/TrainerVersion.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/ModelStudioTrainer.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
