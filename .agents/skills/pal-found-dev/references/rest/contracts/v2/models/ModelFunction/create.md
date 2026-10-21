# v2.models.ModelFunction.create


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a function for the model.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.Model.Function.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, model_rid: models_models.ModelRid, *, api_name: models_models.ModelFunctionApiName, display_name: models_models.ModelFunctionDisplayName, is_row_wise: models_models.ModelFunctionIsRowWise, ontology_binding: typing.Optional[ontologies_models.OntologyRid]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.ModelFunction: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| model_rid | models_models.ModelRid | required | Value shape and constraints are in its referenced local type definition. |
| api_name | models_models.ModelFunctionApiName | required | Value shape and constraints are in its referenced local type definition. |
| display_name | models_models.ModelFunctionDisplayName | required | Value shape and constraints are in its referenced local type definition. |
| is_row_wise | models_models.ModelFunctionIsRowWise | required | Value shape and constraints are in its referenced local type definition. |
| ontology_binding | typing.Optional[ontologies_models.OntologyRid] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateModelFunctionPermissionDenied | Could not create the ModelFunction. |
| FunctionAlreadyExists | A function already exists for this model. |
| InvalidFunctionApiName | The provided API name for the function is invalid. |
| ModelApiTypeUnsupportedForFunction | The model API contains a data type that is not supported for Ontology function creation. |
| ModelNotFound | The given Model could not be found. |
| OntologyBindingRequired | An ontologyBinding is required when creating or replacing a model function. |
| OntologyNotFound | The specified ontology was not found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/models/{modelRid}/function'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'modelRid': model_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
models_models.CreateModelFunctionRequest(api_name=api_name, ontology_binding=ontology_binding, is_row_wise=is_row_wise, display_name=display_name)
```

**response_type**

```python
models_models.ModelFunction
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CreateModelFunctionPermissionDenied': models_errors.CreateModelFunctionPermissionDenied, 'FunctionAlreadyExists': models_errors.FunctionAlreadyExists, 'InvalidFunctionApiName': models_errors.InvalidFunctionApiName, 'ModelApiTypeUnsupportedForFunction': models_errors.ModelApiTypeUnsupportedForFunction, 'ModelNotFound': models_errors.ModelNotFound, 'OntologyBindingRequired': models_errors.OntologyBindingRequired, 'OntologyNotFound': models_errors.OntologyNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.ModelFunction`. Ordinary async return: `typing.Awaitable[models_models.ModelFunction]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.ModelFunction |
| sync_raw | ApiResponse[models_models.ModelFunction] |
| sync_streaming | StreamingContextManager[models_models.ModelFunction] |
| async_ordinary | typing.Awaitable[models_models.ModelFunction] |
| async_raw | Awaitable[AsyncApiResponse[models_models.ModelFunction]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.ModelFunction]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.models.errors.CreateModelFunctionPermissionDenied](../../../../models/v2/models/errors/CreateModelFunctionPermissionDenied.md)
- [foundry_sdk.v2.models.errors.CreateModelFunctionPermissionDeniedParameters](../../../../models/v2/models/errors/CreateModelFunctionPermissionDeniedParameters.md)
- [foundry_sdk.v2.models.errors.FunctionAlreadyExists](../../../../models/v2/models/errors/FunctionAlreadyExists.md)
- [foundry_sdk.v2.models.errors.FunctionAlreadyExistsParameters](../../../../models/v2/models/errors/FunctionAlreadyExistsParameters.md)
- [foundry_sdk.v2.models.errors.InvalidFunctionApiName](../../../../models/v2/models/errors/InvalidFunctionApiName.md)
- [foundry_sdk.v2.models.errors.InvalidFunctionApiNameParameters](../../../../models/v2/models/errors/InvalidFunctionApiNameParameters.md)
- [foundry_sdk.v2.models.errors.ModelApiTypeUnsupportedForFunction](../../../../models/v2/models/errors/ModelApiTypeUnsupportedForFunction.md)
- [foundry_sdk.v2.models.errors.ModelApiTypeUnsupportedForFunctionParameters](../../../../models/v2/models/errors/ModelApiTypeUnsupportedForFunctionParameters.md)
- [foundry_sdk.v2.models.errors.ModelNotFound](../../../../models/v2/models/errors/ModelNotFound.md)
- [foundry_sdk.v2.models.errors.ModelNotFoundParameters](../../../../models/v2/models/errors/ModelNotFoundParameters.md)
- [foundry_sdk.v2.models.errors.OntologyBindingRequired](../../../../models/v2/models/errors/OntologyBindingRequired.md)
- [foundry_sdk.v2.models.errors.OntologyBindingRequiredParameters](../../../../models/v2/models/errors/OntologyBindingRequiredParameters.md)
- [foundry_sdk.v2.models.errors.OntologyNotFound](../../../../models/v2/models/errors/OntologyNotFound.md)
- [foundry_sdk.v2.models.errors.OntologyNotFoundParameters](../../../../models/v2/models/errors/OntologyNotFoundParameters.md)
- [foundry_sdk.v2.models.models.CreateModelFunctionRequest](../../../../models/v2/models/models/CreateModelFunctionRequest.md)
- [foundry_sdk.v2.models.models.ModelFunction](../../../../models/v2/models/models/ModelFunction.md)
- [foundry_sdk.v2.models.models.ModelFunctionApiName](../../../../models/v2/models/models/ModelFunctionApiName.md)
- [foundry_sdk.v2.models.models.ModelFunctionDisplayName](../../../../models/v2/models/models/ModelFunctionDisplayName.md)
- [foundry_sdk.v2.models.models.ModelFunctionFunctionRid](../../../../models/v2/models/models/ModelFunctionFunctionRid.md)
- [foundry_sdk.v2.models.models.ModelFunctionFunctionVersion](../../../../models/v2/models/models/ModelFunctionFunctionVersion.md)
- [foundry_sdk.v2.models.models.ModelFunctionIsRowWise](../../../../models/v2/models/models/ModelFunctionIsRowWise.md)
- [foundry_sdk.v2.models.models.ModelRid](../../../../models/v2/models/models/ModelRid.md)
- [foundry_sdk.v2.ontologies.models.OntologyRid](../../../../models/v2/ontologies/models/OntologyRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/ModelFunction.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
