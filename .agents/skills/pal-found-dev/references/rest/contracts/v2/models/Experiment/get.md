# v2.models.Experiment.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Retrieve a single experiment with all metadata, parameters, series metadata, and summary metrics.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.Model.Experiment.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, model_rid: models_models.ModelRid, experiment_rid: models_models.ExperimentRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.Experiment: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| model_rid | models_models.ModelRid | required | Value shape and constraints are in its referenced local type definition. |
| experiment_rid | models_models.ExperimentRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ExperimentNotFound | The given Experiment could not be found. |
| ModelExperimentNotFound | The requested experiment was not found or the user lacks permission to access it. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/models/{modelRid}/experiments/{experimentRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'modelRid': model_rid, 'experimentRid': experiment_rid}
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
models_models.Experiment
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ExperimentNotFound': models_errors.ExperimentNotFound, 'ModelExperimentNotFound': models_errors.ModelExperimentNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.Experiment`. Ordinary async return: `typing.Awaitable[models_models.Experiment]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.Experiment |
| sync_raw | ApiResponse[models_models.Experiment] |
| sync_streaming | StreamingContextManager[models_models.Experiment] |
| async_ordinary | typing.Awaitable[models_models.Experiment] |
| async_raw | Awaitable[AsyncApiResponse[models_models.Experiment]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.Experiment]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.JobRid](../../../../models/v2/core/models/JobRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.SizeBytes](../../../../models/v2/core/models/SizeBytes.md)
- [foundry_sdk.v2.models.errors.ExperimentNotFound](../../../../models/v2/models/errors/ExperimentNotFound.md)
- [foundry_sdk.v2.models.errors.ExperimentNotFoundParameters](../../../../models/v2/models/errors/ExperimentNotFoundParameters.md)
- [foundry_sdk.v2.models.errors.ModelExperimentNotFound](../../../../models/v2/models/errors/ModelExperimentNotFound.md)
- [foundry_sdk.v2.models.errors.ModelExperimentNotFoundParameters](../../../../models/v2/models/errors/ModelExperimentNotFoundParameters.md)
- [foundry_sdk.v2.models.models.BooleanParameter](../../../../models/v2/models/models/BooleanParameter.md)
- [foundry_sdk.v2.models.models.DatetimeParameter](../../../../models/v2/models/models/DatetimeParameter.md)
- [foundry_sdk.v2.models.models.DoubleParameter](../../../../models/v2/models/models/DoubleParameter.md)
- [foundry_sdk.v2.models.models.DoubleSeriesAggregations](../../../../models/v2/models/models/DoubleSeriesAggregations.md)
- [foundry_sdk.v2.models.models.Experiment](../../../../models/v2/models/models/Experiment.md)
- [foundry_sdk.v2.models.models.ExperimentArtifactDetails](../../../../models/v2/models/models/ExperimentArtifactDetails.md)
- [foundry_sdk.v2.models.models.ExperimentArtifactMetadata](../../../../models/v2/models/models/ExperimentArtifactMetadata.md)
- [foundry_sdk.v2.models.models.ExperimentArtifactName](../../../../models/v2/models/models/ExperimentArtifactName.md)
- [foundry_sdk.v2.models.models.ExperimentAuthoringSource](../../../../models/v2/models/models/ExperimentAuthoringSource.md)
- [foundry_sdk.v2.models.models.ExperimentCodeWorkspaceSource](../../../../models/v2/models/models/ExperimentCodeWorkspaceSource.md)
- [foundry_sdk.v2.models.models.ExperimentRid](../../../../models/v2/models/models/ExperimentRid.md)
- [foundry_sdk.v2.models.models.ExperimentSdkSource](../../../../models/v2/models/models/ExperimentSdkSource.md)
- [foundry_sdk.v2.models.models.ExperimentSource](../../../../models/v2/models/models/ExperimentSource.md)
- [foundry_sdk.v2.models.models.ExperimentStatus](../../../../models/v2/models/models/ExperimentStatus.md)
- [foundry_sdk.v2.models.models.ExperimentTagText](../../../../models/v2/models/models/ExperimentTagText.md)
- [foundry_sdk.v2.models.models.IntegerParameter](../../../../models/v2/models/models/IntegerParameter.md)
- [foundry_sdk.v2.models.models.ModelRid](../../../../models/v2/models/models/ModelRid.md)
- [foundry_sdk.v2.models.models.ModelVersionRid](../../../../models/v2/models/models/ModelVersionRid.md)
- [foundry_sdk.v2.models.models.Parameter](../../../../models/v2/models/models/Parameter.md)
- [foundry_sdk.v2.models.models.ParameterName](../../../../models/v2/models/models/ParameterName.md)
- [foundry_sdk.v2.models.models.ParameterValue](../../../../models/v2/models/models/ParameterValue.md)
- [foundry_sdk.v2.models.models.SeriesAggregations](../../../../models/v2/models/models/SeriesAggregations.md)
- [foundry_sdk.v2.models.models.SeriesAggregationsValue](../../../../models/v2/models/models/SeriesAggregationsValue.md)
- [foundry_sdk.v2.models.models.SeriesName](../../../../models/v2/models/models/SeriesName.md)
- [foundry_sdk.v2.models.models.StringParameter](../../../../models/v2/models/models/StringParameter.md)
- [foundry_sdk.v2.models.models.SummaryMetric](../../../../models/v2/models/models/SummaryMetric.md)
- [foundry_sdk.v2.models.models.SummaryMetricAggregation](../../../../models/v2/models/models/SummaryMetricAggregation.md)
- [foundry_sdk.v2.models.models.TableArtifactDetails](../../../../models/v2/models/models/TableArtifactDetails.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/Experiment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
