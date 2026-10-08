# v2.models.ModelStudioConfigVersion.create


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new Model Studio configuration version.

## SDK invocation contract

```python
def create(self, model_studio_rid: models_models.ModelStudioRid, *, name: models_models.ModelStudioConfigVersionName, resources: models_models.ResourceConfiguration, trainer_id: models_models.TrainerId, worker_config: models_models.ModelStudioWorkerConfig, changelog: typing.Optional[str]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.ModelStudioConfigVersion: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| model_studio_rid | models_models.ModelStudioRid | required | Value shape and constraints are in its referenced local type definition. |
| name | models_models.ModelStudioConfigVersionName | required | Human readable name of the configuration version and experiment. |
| resources | models_models.ResourceConfiguration | required | The compute resources allocated for training runs. |
| trainer_id | models_models.TrainerId | required | The identifier of the trainer to use for this configuration. |
| worker_config | models_models.ModelStudioWorkerConfig | required | The worker configuration including inputs, outputs, and custom settings. |
| changelog | typing.Optional[str] | None | Changelog describing changes in this version. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateConfigValidationError | The provided configuration is invalid. |
| CreateModelStudioConfigVersionPermissionDenied | Could not create the ModelStudioConfigVersion. |
| ModelStudioNotFound | The requested Model Studio was not found. |
| TrainerNotFound | The specified trainer does not exist. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/models/modelStudios/{modelStudioRid}/configVersions'
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
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
models_models.CreateModelStudioConfigVersionRequest(name=name, resources=resources, changelog=changelog, worker_config=worker_config, trainer_id=trainer_id)
```

**response_type**

```python
models_models.ModelStudioConfigVersion
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CreateConfigValidationError': models_errors.CreateConfigValidationError, 'CreateModelStudioConfigVersionPermissionDenied': models_errors.CreateModelStudioConfigVersionPermissionDenied, 'ModelStudioNotFound': models_errors.ModelStudioNotFound, 'TrainerNotFound': models_errors.TrainerNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.ModelStudioConfigVersion`. Ordinary async return: `typing.Awaitable[models_models.ModelStudioConfigVersion]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.ModelStudioConfigVersion |
| sync_raw | ApiResponse[models_models.ModelStudioConfigVersion] |
| sync_streaming | StreamingContextManager[models_models.ModelStudioConfigVersion] |
| async_ordinary | typing.Awaitable[models_models.ModelStudioConfigVersion] |
| async_raw | Awaitable[AsyncApiResponse[models_models.ModelStudioConfigVersion]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.ModelStudioConfigVersion]] |

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
- [foundry_sdk.v2.models.errors.CreateConfigValidationError](../../../../models/v2/models/errors/CreateConfigValidationError.md)
- [foundry_sdk.v2.models.errors.CreateConfigValidationErrorParameters](../../../../models/v2/models/errors/CreateConfigValidationErrorParameters.md)
- [foundry_sdk.v2.models.errors.CreateModelStudioConfigVersionPermissionDenied](../../../../models/v2/models/errors/CreateModelStudioConfigVersionPermissionDenied.md)
- [foundry_sdk.v2.models.errors.CreateModelStudioConfigVersionPermissionDeniedParameters](../../../../models/v2/models/errors/CreateModelStudioConfigVersionPermissionDeniedParameters.md)
- [foundry_sdk.v2.models.errors.ModelStudioNotFound](../../../../models/v2/models/errors/ModelStudioNotFound.md)
- [foundry_sdk.v2.models.errors.ModelStudioNotFoundParameters](../../../../models/v2/models/errors/ModelStudioNotFoundParameters.md)
- [foundry_sdk.v2.models.errors.TrainerNotFound](../../../../models/v2/models/errors/TrainerNotFound.md)
- [foundry_sdk.v2.models.errors.TrainerNotFoundParameters](../../../../models/v2/models/errors/TrainerNotFoundParameters.md)
- [foundry_sdk.v2.models.models.ChangelogTooLongError](../../../../models/v2/models/models/ChangelogTooLongError.md)
- [foundry_sdk.v2.models.models.ColumnTypeSpecId](../../../../models/v2/models/models/ColumnTypeSpecId.md)
- [foundry_sdk.v2.models.models.CreateConfigValidationFailureReason](../../../../models/v2/models/models/CreateConfigValidationFailureReason.md)
- [foundry_sdk.v2.models.models.CreateModelStudioConfigVersionRequest](../../../../models/v2/models/models/CreateModelStudioConfigVersionRequest.md)
- [foundry_sdk.v2.models.models.DatasetInput](../../../../models/v2/models/models/DatasetInput.md)
- [foundry_sdk.v2.models.models.DatasetSchemaNotFoundError](../../../../models/v2/models/models/DatasetSchemaNotFoundError.md)
- [foundry_sdk.v2.models.models.FieldValidationError](../../../../models/v2/models/models/FieldValidationError.md)
- [foundry_sdk.v2.models.models.GpuType](../../../../models/v2/models/models/GpuType.md)
- [foundry_sdk.v2.models.models.InputAlias](../../../../models/v2/models/models/InputAlias.md)
- [foundry_sdk.v2.models.models.InvalidResourceConfigurationError](../../../../models/v2/models/models/InvalidResourceConfigurationError.md)
- [foundry_sdk.v2.models.models.JsonSchemaValidationError](../../../../models/v2/models/models/JsonSchemaValidationError.md)
- [foundry_sdk.v2.models.models.MissingRequiredDatasetColumnError](../../../../models/v2/models/models/MissingRequiredDatasetColumnError.md)
- [foundry_sdk.v2.models.models.MissingWorkerConfigInputDatasetColumnMappingError](../../../../models/v2/models/models/MissingWorkerConfigInputDatasetColumnMappingError.md)
- [foundry_sdk.v2.models.models.MissingWorkerConfigInputError](../../../../models/v2/models/models/MissingWorkerConfigInputError.md)
- [foundry_sdk.v2.models.models.MissingWorkerConfigInputObjectSetPropertyMappingError](../../../../models/v2/models/models/MissingWorkerConfigInputObjectSetPropertyMappingError.md)
- [foundry_sdk.v2.models.models.MissingWorkerConfigOutputError](../../../../models/v2/models/models/MissingWorkerConfigOutputError.md)
- [foundry_sdk.v2.models.models.ModelOutput](../../../../models/v2/models/models/ModelOutput.md)
- [foundry_sdk.v2.models.models.ModelRid](../../../../models/v2/models/models/ModelRid.md)
- [foundry_sdk.v2.models.models.ModelStudioConfigVersion](../../../../models/v2/models/models/ModelStudioConfigVersion.md)
- [foundry_sdk.v2.models.models.ModelStudioConfigVersionName](../../../../models/v2/models/models/ModelStudioConfigVersionName.md)
- [foundry_sdk.v2.models.models.ModelStudioConfigVersionNumber](../../../../models/v2/models/models/ModelStudioConfigVersionNumber.md)
- [foundry_sdk.v2.models.models.ModelStudioInput](../../../../models/v2/models/models/ModelStudioInput.md)
- [foundry_sdk.v2.models.models.ModelStudioOutput](../../../../models/v2/models/models/ModelStudioOutput.md)
- [foundry_sdk.v2.models.models.ModelStudioRid](../../../../models/v2/models/models/ModelStudioRid.md)
- [foundry_sdk.v2.models.models.ModelStudioWorkerConfig](../../../../models/v2/models/models/ModelStudioWorkerConfig.md)
- [foundry_sdk.v2.models.models.MultipleColumnsNotAllowedForTrainerError](../../../../models/v2/models/models/MultipleColumnsNotAllowedForTrainerError.md)
- [foundry_sdk.v2.models.models.MultiplePropertiesNotAllowedForTrainerError](../../../../models/v2/models/models/MultiplePropertiesNotAllowedForTrainerError.md)
- [foundry_sdk.v2.models.models.OtherValidationError](../../../../models/v2/models/models/OtherValidationError.md)
- [foundry_sdk.v2.models.models.OutputAlias](../../../../models/v2/models/models/OutputAlias.md)
- [foundry_sdk.v2.models.models.OutputResourceInDifferentProjectError](../../../../models/v2/models/models/OutputResourceInDifferentProjectError.md)
- [foundry_sdk.v2.models.models.OutputResourceNotFoundError](../../../../models/v2/models/models/OutputResourceNotFoundError.md)
- [foundry_sdk.v2.models.models.ResourceConfiguration](../../../../models/v2/models/models/ResourceConfiguration.md)
- [foundry_sdk.v2.models.models.TrainerId](../../../../models/v2/models/models/TrainerId.md)
- [foundry_sdk.v2.models.models.TrainerVersionLocator](../../../../models/v2/models/models/TrainerVersionLocator.md)
- [foundry_sdk.v2.models.models.UnknownColumnSpecIdInConfigColumnMappingError](../../../../models/v2/models/models/UnknownColumnSpecIdInConfigColumnMappingError.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/ModelStudioConfigVersion.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
