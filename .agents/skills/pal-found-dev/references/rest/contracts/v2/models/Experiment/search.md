# v2.models.Experiment.search


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Search experiments using complex nested queries on experiment metadata, parameters, series,
and summary metrics. Supports AND/OR/NOT combinations and various predicates.
Returns a maximum of 100 results per page.

## SDK invocation contract

```python
def search(self, model_rid: models_models.ModelRid, *, order_by: typing.Optional[models_models.SearchExperimentsOrderBy]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, where: typing.Optional[models_models.SearchExperimentsFilter]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.SearchExperimentsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| model_rid | models_models.ModelRid | required | Value shape and constraints are in its referenced local type definition. |
| order_by | typing.Optional[models_models.SearchExperimentsOrderBy] | None | The field to sort by. Default is to sort by relevance. |
| page_size | typing.Optional[core_models.PageSize] | None | The maximum number of results to return. Default 50, maximum of 100. |
| page_token | typing.Optional[core_models.PageToken] | None | PageToken to identify the next page to retrieve. Leave empty for the first request. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| where | typing.Optional[models_models.SearchExperimentsFilter] | None | Optional search filter for filtering experiments. If not provided, all experiments for the model are returned. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| InvalidExperimentSearchFilter | The search filter is invalid. This can occur when using an unsupported operator and value type combination in a parameter filter, filtering by an unsupported status, or providing a malformed filter. |
| SearchExperimentsPermissionDenied | Could not search the Experiment. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/models/{modelRid}/experiments/search'
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
models_models.SearchExperimentsRequest(where=where, order_by=order_by, page_size=page_size, page_token=page_token)
```

**response_type**

```python
models_models.SearchExperimentsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'InvalidExperimentSearchFilter': models_errors.InvalidExperimentSearchFilter, 'SearchExperimentsPermissionDenied': models_errors.SearchExperimentsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.SearchExperimentsResponse`. Ordinary async return: `typing.Awaitable[models_models.SearchExperimentsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.SearchExperimentsResponse |
| sync_raw | ApiResponse[models_models.SearchExperimentsResponse] |
| sync_streaming | StreamingContextManager[models_models.SearchExperimentsResponse] |
| async_ordinary | typing.Awaitable[models_models.SearchExperimentsResponse] |
| async_raw | Awaitable[AsyncApiResponse[models_models.SearchExperimentsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.SearchExperimentsResponse]] |

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
- [foundry_sdk.v2.core.models.OrderByDirection](../../../../models/v2/core/models/OrderByDirection.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.SizeBytes](../../../../models/v2/core/models/SizeBytes.md)
- [foundry_sdk.v2.models.errors.InvalidExperimentSearchFilter](../../../../models/v2/models/errors/InvalidExperimentSearchFilter.md)
- [foundry_sdk.v2.models.errors.InvalidExperimentSearchFilterParameters](../../../../models/v2/models/errors/InvalidExperimentSearchFilterParameters.md)
- [foundry_sdk.v2.models.errors.SearchExperimentsPermissionDenied](../../../../models/v2/models/errors/SearchExperimentsPermissionDenied.md)
- [foundry_sdk.v2.models.errors.SearchExperimentsPermissionDeniedParameters](../../../../models/v2/models/errors/SearchExperimentsPermissionDeniedParameters.md)
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
- [foundry_sdk.v2.models.models.SearchExperimentsAndFilter](../../../../models/v2/models/models/SearchExperimentsAndFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsContainsFilter](../../../../models/v2/models/models/SearchExperimentsContainsFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsContainsFilterField](../../../../models/v2/models/models/SearchExperimentsContainsFilterField.md)
- [foundry_sdk.v2.models.models.SearchExperimentsEqualsFilter](../../../../models/v2/models/models/SearchExperimentsEqualsFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsEqualsFilterField](../../../../models/v2/models/models/SearchExperimentsEqualsFilterField.md)
- [foundry_sdk.v2.models.models.SearchExperimentsFilter](../../../../models/v2/models/models/SearchExperimentsFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsNotFilter](../../../../models/v2/models/models/SearchExperimentsNotFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsNumericFilterOperator](../../../../models/v2/models/models/SearchExperimentsNumericFilterOperator.md)
- [foundry_sdk.v2.models.models.SearchExperimentsOrFilter](../../../../models/v2/models/models/SearchExperimentsOrFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsOrderBy](../../../../models/v2/models/models/SearchExperimentsOrderBy.md)
- [foundry_sdk.v2.models.models.SearchExperimentsOrderByField](../../../../models/v2/models/models/SearchExperimentsOrderByField.md)
- [foundry_sdk.v2.models.models.SearchExperimentsParameterFilter](../../../../models/v2/models/models/SearchExperimentsParameterFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsParameterFilterOperator](../../../../models/v2/models/models/SearchExperimentsParameterFilterOperator.md)
- [foundry_sdk.v2.models.models.SearchExperimentsRequest](../../../../models/v2/models/models/SearchExperimentsRequest.md)
- [foundry_sdk.v2.models.models.SearchExperimentsResponse](../../../../models/v2/models/models/SearchExperimentsResponse.md)
- [foundry_sdk.v2.models.models.SearchExperimentsSeriesFilter](../../../../models/v2/models/models/SearchExperimentsSeriesFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsSeriesFilterField](../../../../models/v2/models/models/SearchExperimentsSeriesFilterField.md)
- [foundry_sdk.v2.models.models.SearchExperimentsStartsWithFilter](../../../../models/v2/models/models/SearchExperimentsStartsWithFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsStartsWithFilterField](../../../../models/v2/models/models/SearchExperimentsStartsWithFilterField.md)
- [foundry_sdk.v2.models.models.SearchExperimentsSummaryMetricFilter](../../../../models/v2/models/models/SearchExperimentsSummaryMetricFilter.md)
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

[Part 1](search.md)
