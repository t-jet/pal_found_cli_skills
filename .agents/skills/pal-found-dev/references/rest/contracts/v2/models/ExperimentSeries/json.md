# v2.models.ExperimentSeries.json


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Retrieve raw time-series data for a single series in JSON format.
Results are paginated with a default page size of 200 and a maximum of 1000.

## SDK invocation contract

```python
def json(self, model_rid: models_models.ModelRid, experiment_rid: models_models.ExperimentRid, experiment_series_name: models_models.SeriesName, *, offset: typing.Optional[int]=None, page_size: typing.Optional[core_models.PageSize]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.Series: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| model_rid | models_models.ModelRid | required | Value shape and constraints are in its referenced local type definition. |
| experiment_rid | models_models.ExperimentRid | required | Value shape and constraints are in its referenced local type definition. |
| experiment_series_name | models_models.SeriesName | required | Value shape and constraints are in its referenced local type definition. |
| offset | typing.Optional[int] | None | Number of values to skip from the beginning. Defaults to 0. |
| page_size | typing.Optional[core_models.PageSize] | None | Maximum number of values to return per page. Default is 200, maximum is 1000. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ExperimentSeriesNotFound | The requested series was not found in the experiment. |
| JsonExperimentSeriesPermissionDenied | Could not json the ExperimentSeries. |
| ModelExperimentNotFound | The requested experiment was not found or the user lacks permission to access it. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/models/{modelRid}/experiments/{experimentRid}/series/{experimentSeriesName}/json'
```

**query_params**

```python
{'offset': offset, 'pageSize': page_size, 'preview': preview}
```

**path_params**

```python
{'modelRid': model_rid, 'experimentRid': experiment_rid, 'experimentSeriesName': experiment_series_name}
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
models_models.Series
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ExperimentSeriesNotFound': models_errors.ExperimentSeriesNotFound, 'JsonExperimentSeriesPermissionDenied': models_errors.JsonExperimentSeriesPermissionDenied, 'ModelExperimentNotFound': models_errors.ModelExperimentNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.Series`. Ordinary async return: `typing.Awaitable[models_models.Series]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.Series |
| sync_raw | ApiResponse[models_models.Series] |
| sync_streaming | StreamingContextManager[models_models.Series] |
| async_ordinary | typing.Awaitable[models_models.Series] |
| async_raw | Awaitable[AsyncApiResponse[models_models.Series]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.Series]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.models.errors.ExperimentSeriesNotFound](../../../../models/v2/models/errors/ExperimentSeriesNotFound.md)
- [foundry_sdk.v2.models.errors.ExperimentSeriesNotFoundParameters](../../../../models/v2/models/errors/ExperimentSeriesNotFoundParameters.md)
- [foundry_sdk.v2.models.errors.JsonExperimentSeriesPermissionDenied](../../../../models/v2/models/errors/JsonExperimentSeriesPermissionDenied.md)
- [foundry_sdk.v2.models.errors.JsonExperimentSeriesPermissionDeniedParameters](../../../../models/v2/models/errors/JsonExperimentSeriesPermissionDeniedParameters.md)
- [foundry_sdk.v2.models.errors.ModelExperimentNotFound](../../../../models/v2/models/errors/ModelExperimentNotFound.md)
- [foundry_sdk.v2.models.errors.ModelExperimentNotFoundParameters](../../../../models/v2/models/errors/ModelExperimentNotFoundParameters.md)
- [foundry_sdk.v2.models.models.DoubleSeriesV1](../../../../models/v2/models/models/DoubleSeriesV1.md)
- [foundry_sdk.v2.models.models.DoubleSeriesValueV1](../../../../models/v2/models/models/DoubleSeriesValueV1.md)
- [foundry_sdk.v2.models.models.EpochMillis](../../../../models/v2/models/models/EpochMillis.md)
- [foundry_sdk.v2.models.models.ExperimentRid](../../../../models/v2/models/models/ExperimentRid.md)
- [foundry_sdk.v2.models.models.ModelRid](../../../../models/v2/models/models/ModelRid.md)
- [foundry_sdk.v2.models.models.Series](../../../../models/v2/models/models/Series.md)
- [foundry_sdk.v2.models.models.SeriesName](../../../../models/v2/models/models/SeriesName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/ExperimentSeries.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](json.md)
