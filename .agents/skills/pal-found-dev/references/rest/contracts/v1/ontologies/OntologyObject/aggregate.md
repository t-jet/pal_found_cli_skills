# v1.ontologies.OntologyObject.aggregate


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Perform functions on object fields in the specified ontology and object type.

## Public Python client route

With a configured `foundry_sdk.v1.FoundryClient` named `client`, call `client.ontologies.OntologyObject.aggregate`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def aggregate(self, ontology_rid: ontologies_models.OntologyRid, object_type: ontologies_models.ObjectTypeApiName, *, aggregation: typing.List[ontologies_models.Aggregation], group_by: typing.List[ontologies_models.AggregationGroupBy], query: typing.Optional[ontologies_models.SearchJsonQuery]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.AggregateObjectsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology_rid | ontologies_models.OntologyRid | required | The unique Resource Identifier (RID) of the Ontology that contains the objects. |
| object_type | ontologies_models.ObjectTypeApiName | required | The type of the object to aggregate on. |
| aggregation | typing.List[ontologies_models.Aggregation] | required | Value shape and constraints are in its referenced local type definition. |
| group_by | typing.List[ontologies_models.AggregationGroupBy] | required | Value shape and constraints are in its referenced local type definition. |
| query | typing.Optional[ontologies_models.SearchJsonQuery] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v1/ontologies/{ontologyRid}/objects/{objectType}/aggregate'
```

**query_params**

```python
{}
```

**path_params**

```python
{'ontologyRid': ontology_rid, 'objectType': object_type}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.AggregateObjectsRequest(aggregation=aggregation, query=query, group_by=group_by)
```

**response_type**

```python
ontologies_models.AggregateObjectsResponse
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

Ordinary sync return: `ontologies_models.AggregateObjectsResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.AggregateObjectsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.AggregateObjectsResponse |
| sync_raw | ApiResponse[ontologies_models.AggregateObjectsResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.AggregateObjectsResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.AggregateObjectsResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.AggregateObjectsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.AggregateObjectsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.models.PageToken](../../../../models/v1/core/models/PageToken.md)
- [foundry_sdk.v1.ontologies.models.AggregateObjectsRequest](../../../../models/v1/ontologies/models/AggregateObjectsRequest.md)
- [foundry_sdk.v1.ontologies.models.AggregateObjectsResponse](../../../../models/v1/ontologies/models/AggregateObjectsResponse.md)
- [foundry_sdk.v1.ontologies.models.AggregateObjectsResponseItem](../../../../models/v1/ontologies/models/AggregateObjectsResponseItem.md)
- [foundry_sdk.v1.ontologies.models.Aggregation](../../../../models/v1/ontologies/models/Aggregation.md)
- [foundry_sdk.v1.ontologies.models.AggregationDurationGrouping](../../../../models/v1/ontologies/models/AggregationDurationGrouping.md)
- [foundry_sdk.v1.ontologies.models.AggregationExactGrouping](../../../../models/v1/ontologies/models/AggregationExactGrouping.md)
- [foundry_sdk.v1.ontologies.models.AggregationFixedWidthGrouping](../../../../models/v1/ontologies/models/AggregationFixedWidthGrouping.md)
- [foundry_sdk.v1.ontologies.models.AggregationGroupBy](../../../../models/v1/ontologies/models/AggregationGroupBy.md)
- [foundry_sdk.v1.ontologies.models.AggregationGroupKey](../../../../models/v1/ontologies/models/AggregationGroupKey.md)
- [foundry_sdk.v1.ontologies.models.AggregationGroupValue](../../../../models/v1/ontologies/models/AggregationGroupValue.md)
- [foundry_sdk.v1.ontologies.models.AggregationMetricName](../../../../models/v1/ontologies/models/AggregationMetricName.md)
- [foundry_sdk.v1.ontologies.models.AggregationMetricResult](../../../../models/v1/ontologies/models/AggregationMetricResult.md)
- [foundry_sdk.v1.ontologies.models.AggregationRange](../../../../models/v1/ontologies/models/AggregationRange.md)
- [foundry_sdk.v1.ontologies.models.AggregationRangesGrouping](../../../../models/v1/ontologies/models/AggregationRangesGrouping.md)
- [foundry_sdk.v1.ontologies.models.AllTermsQuery](../../../../models/v1/ontologies/models/AllTermsQuery.md)
- [foundry_sdk.v1.ontologies.models.AndQuery](../../../../models/v1/ontologies/models/AndQuery.md)
- [foundry_sdk.v1.ontologies.models.AnyTermQuery](../../../../models/v1/ontologies/models/AnyTermQuery.md)
- [foundry_sdk.v1.ontologies.models.ApproximateDistinctAggregation](../../../../models/v1/ontologies/models/ApproximateDistinctAggregation.md)
- [foundry_sdk.v1.ontologies.models.AvgAggregation](../../../../models/v1/ontologies/models/AvgAggregation.md)
- [foundry_sdk.v1.ontologies.models.ContainsQuery](../../../../models/v1/ontologies/models/ContainsQuery.md)
- [foundry_sdk.v1.ontologies.models.CountAggregation](../../../../models/v1/ontologies/models/CountAggregation.md)
- [foundry_sdk.v1.ontologies.models.Duration](../../../../models/v1/ontologies/models/Duration.md)
- [foundry_sdk.v1.ontologies.models.EqualsQuery](../../../../models/v1/ontologies/models/EqualsQuery.md)
- [foundry_sdk.v1.ontologies.models.FieldNameV1](../../../../models/v1/ontologies/models/FieldNameV1.md)
- [foundry_sdk.v1.ontologies.models.Fuzzy](../../../../models/v1/ontologies/models/Fuzzy.md)
- [foundry_sdk.v1.ontologies.models.GtQuery](../../../../models/v1/ontologies/models/GtQuery.md)
- [foundry_sdk.v1.ontologies.models.GteQuery](../../../../models/v1/ontologies/models/GteQuery.md)
- [foundry_sdk.v1.ontologies.models.IsNullQuery](../../../../models/v1/ontologies/models/IsNullQuery.md)
- [foundry_sdk.v1.ontologies.models.LtQuery](../../../../models/v1/ontologies/models/LtQuery.md)
- [foundry_sdk.v1.ontologies.models.LteQuery](../../../../models/v1/ontologies/models/LteQuery.md)
- [foundry_sdk.v1.ontologies.models.MaxAggregation](../../../../models/v1/ontologies/models/MaxAggregation.md)
- [foundry_sdk.v1.ontologies.models.MinAggregation](../../../../models/v1/ontologies/models/MinAggregation.md)
- [foundry_sdk.v1.ontologies.models.NotQuery](../../../../models/v1/ontologies/models/NotQuery.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeApiName](../../../../models/v1/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.OntologyRid](../../../../models/v1/ontologies/models/OntologyRid.md)
- [foundry_sdk.v1.ontologies.models.OrQuery](../../../../models/v1/ontologies/models/OrQuery.md)
- [foundry_sdk.v1.ontologies.models.PhraseQuery](../../../../models/v1/ontologies/models/PhraseQuery.md)
- [foundry_sdk.v1.ontologies.models.PrefixQuery](../../../../models/v1/ontologies/models/PrefixQuery.md)
- [foundry_sdk.v1.ontologies.models.PropertyValue](../../../../models/v1/ontologies/models/PropertyValue.md)
- [foundry_sdk.v1.ontologies.models.SearchJsonQuery](../../../../models/v1/ontologies/models/SearchJsonQuery.md)
- [foundry_sdk.v1.ontologies.models.SumAggregation](../../../../models/v1/ontologies/models/SumAggregation.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/OntologyObject.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](aggregate.md)
