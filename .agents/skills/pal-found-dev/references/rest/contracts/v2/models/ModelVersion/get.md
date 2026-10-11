# v2.models.ModelVersion.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Retrieves a Model Version by its Resource Identifier (RID).

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.Model.Version.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, model_rid: models_models.ModelRid, model_version_rid: models_models.ModelVersionRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.ModelVersion: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| model_rid | models_models.ModelRid | required | Value shape and constraints are in its referenced local type definition. |
| model_version_rid | models_models.ModelVersionRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ModelVersionNotFound | The given ModelVersion could not be found. |
| UnsupportedModelSource | The Model Version has a source type that is not supported by the API. This can occur when the model was created through a legacy or internal workflow that is not exposed through the public API. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/models/{modelRid}/versions/{modelVersionRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'modelRid': model_rid, 'modelVersionRid': model_version_rid}
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
models_models.ModelVersion
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ModelVersionNotFound': models_errors.ModelVersionNotFound, 'UnsupportedModelSource': models_errors.UnsupportedModelSource}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.ModelVersion`. Ordinary async return: `typing.Awaitable[models_models.ModelVersion]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.ModelVersion |
| sync_raw | ApiResponse[models_models.ModelVersion] |
| sync_streaming | StreamingContextManager[models_models.ModelVersion] |
| async_ordinary | typing.Awaitable[models_models.ModelVersion] |
| async_raw | Awaitable[AsyncApiResponse[models_models.ModelVersion]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.ModelVersion]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BooleanType](../../../../models/v2/core/models/BooleanType.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.DateType](../../../../models/v2/core/models/DateType.md)
- [foundry_sdk.v2.core.models.DoubleType](../../../../models/v2/core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.FloatType](../../../../models/v2/core/models/FloatType.md)
- [foundry_sdk.v2.core.models.IntegerType](../../../../models/v2/core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../../../models/v2/core/models/LongType.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.StringType](../../../../models/v2/core/models/StringType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../../../models/v2/core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.UnsupportedType](../../../../models/v2/core/models/UnsupportedType.md)
- [foundry_sdk.v2.core.models.UnsupportedTypeParamKey](../../../../models/v2/core/models/UnsupportedTypeParamKey.md)
- [foundry_sdk.v2.core.models.UnsupportedTypeParamValue](../../../../models/v2/core/models/UnsupportedTypeParamValue.md)
- [foundry_sdk.v2.models.errors.ModelVersionNotFound](../../../../models/v2/models/errors/ModelVersionNotFound.md)
- [foundry_sdk.v2.models.errors.ModelVersionNotFoundParameters](../../../../models/v2/models/errors/ModelVersionNotFoundParameters.md)
- [foundry_sdk.v2.models.errors.UnsupportedModelSource](../../../../models/v2/models/errors/UnsupportedModelSource.md)
- [foundry_sdk.v2.models.errors.UnsupportedModelSourceParameters](../../../../models/v2/models/errors/UnsupportedModelSourceParameters.md)
- [foundry_sdk.v2.models.models.ExperimentRid](../../../../models/v2/models/models/ExperimentRid.md)
- [foundry_sdk.v2.models.models.ModelApi](../../../../models/v2/models/models/ModelApi.md)
- [foundry_sdk.v2.models.models.ModelApiAnyType](../../../../models/v2/models/models/ModelApiAnyType.md)
- [foundry_sdk.v2.models.models.ModelApiArrayType](../../../../models/v2/models/models/ModelApiArrayType.md)
- [foundry_sdk.v2.models.models.ModelApiColumn](../../../../models/v2/models/models/ModelApiColumn.md)
- [foundry_sdk.v2.models.models.ModelApiDataType](../../../../models/v2/models/models/ModelApiDataType.md)
- [foundry_sdk.v2.models.models.ModelApiInput](../../../../models/v2/models/models/ModelApiInput.md)
- [foundry_sdk.v2.models.models.ModelApiMapType](../../../../models/v2/models/models/ModelApiMapType.md)
- [foundry_sdk.v2.models.models.ModelApiOutput](../../../../models/v2/models/models/ModelApiOutput.md)
- [foundry_sdk.v2.models.models.ModelApiParameterType](../../../../models/v2/models/models/ModelApiParameterType.md)
- [foundry_sdk.v2.models.models.ModelApiTabularFormat](../../../../models/v2/models/models/ModelApiTabularFormat.md)
- [foundry_sdk.v2.models.models.ModelApiTabularType](../../../../models/v2/models/models/ModelApiTabularType.md)
- [foundry_sdk.v2.models.models.ModelRid](../../../../models/v2/models/models/ModelRid.md)
- [foundry_sdk.v2.models.models.ModelVersion](../../../../models/v2/models/models/ModelVersion.md)
- [foundry_sdk.v2.models.models.ModelVersionCodeRepositorySource](../../../../models/v2/models/models/ModelVersionCodeRepositorySource.md)
- [foundry_sdk.v2.models.models.ModelVersionCodeWorkspaceSource](../../../../models/v2/models/models/ModelVersionCodeWorkspaceSource.md)
- [foundry_sdk.v2.models.models.ModelVersionContainerizedSource](../../../../models/v2/models/models/ModelVersionContainerizedSource.md)
- [foundry_sdk.v2.models.models.ModelVersionExternalSource](../../../../models/v2/models/models/ModelVersionExternalSource.md)
- [foundry_sdk.v2.models.models.ModelVersionModelStudioSource](../../../../models/v2/models/models/ModelVersionModelStudioSource.md)
- [foundry_sdk.v2.models.models.ModelVersionPromotedSource](../../../../models/v2/models/models/ModelVersionPromotedSource.md)
- [foundry_sdk.v2.models.models.ModelVersionRid](../../../../models/v2/models/models/ModelVersionRid.md)
- [foundry_sdk.v2.models.models.ModelVersionSdkSource](../../../../models/v2/models/models/ModelVersionSdkSource.md)
- [foundry_sdk.v2.models.models.ModelVersionSource](../../../../models/v2/models/models/ModelVersionSource.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/ModelVersion.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
