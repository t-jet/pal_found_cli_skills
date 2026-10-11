# v2.ontologies.OntologyInterface.aggregate


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

:::callout{theme=warning title=Warning}
This endpoint will be removed once TS OSDK is updated to use `objectSets/aggregate` with interface object
sets.
:::
Perform functions on object fields in the specified ontology and of the specified interface type. Any
properties specified in the query must be shared property type API names defined on the interface.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.OntologyInterface.aggregate`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def aggregate(self, ontology: ontologies_models.OntologyIdentifier, interface_type: ontologies_models.InterfaceTypeApiName, *, aggregation: typing.List[ontologies_models.AggregationV2], group_by: typing.List[ontologies_models.AggregationGroupByV2], accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest]=None, branch: typing.Optional[core_models.FoundryBranch]=None, preview: typing.Optional[core_models.PreviewMode]=None, where: typing.Optional[ontologies_models.SearchJsonQueryV2]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.AggregateObjectsResponseV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| interface_type | ontologies_models.InterfaceTypeApiName | required | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**. |
| aggregation | typing.List[ontologies_models.AggregationV2] | required | Value shape and constraints are in its referenced local type definition. |
| group_by | typing.List[ontologies_models.AggregationGroupByV2] | required | Value shape and constraints are in its referenced local type definition. |
| accuracy | typing.Optional[ontologies_models.AggregationAccuracyRequest] | None | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to aggregate objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| where | typing.Optional[ontologies_models.SearchJsonQueryV2] | None | Value shape and constraints are in its referenced local type definition. |
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
'/v2/ontologies/{ontology}/interfaces/{interfaceType}/aggregate'
```

**query_params**

```python
{'branch': branch, 'preview': preview}
```

**path_params**

```python
{'ontology': ontology, 'interfaceType': interface_type}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.AggregateObjectsRequestV2(aggregation=aggregation, where=where, group_by=group_by, accuracy=accuracy)
```

**response_type**

```python
ontologies_models.AggregateObjectsResponseV2
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

Ordinary sync return: `ontologies_models.AggregateObjectsResponseV2`. Ordinary async return: `typing.Awaitable[ontologies_models.AggregateObjectsResponseV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.AggregateObjectsResponseV2 |
| sync_raw | ApiResponse[ontologies_models.AggregateObjectsResponseV2] |
| sync_streaming | StreamingContextManager[ontologies_models.AggregateObjectsResponseV2] |
| async_ordinary | typing.Awaitable[ontologies_models.AggregateObjectsResponseV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.AggregateObjectsResponseV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.AggregateObjectsResponseV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.ComputeSeconds](../../../../models/v2/core/models/ComputeSeconds.md)
- [foundry_sdk.v2.core.models.Distance](../../../../models/v2/core/models/Distance.md)
- [foundry_sdk.v2.core.models.DistanceUnit](../../../../models/v2/core/models/DistanceUnit.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.geo.models.BBox](../../../../models/v2/geo/models/BBox.md)
- [foundry_sdk.v2.geo.models.Coordinate](../../../../models/v2/geo/models/Coordinate.md)
- [foundry_sdk.v2.geo.models.GeoPoint](../../../../models/v2/geo/models/GeoPoint.md)
- [foundry_sdk.v2.geo.models.LinearRing](../../../../models/v2/geo/models/LinearRing.md)
- [foundry_sdk.v2.geo.models.Polygon](../../../../models/v2/geo/models/Polygon.md)
- [foundry_sdk.v2.geo.models.Position](../../../../models/v2/geo/models/Position.md)
- [foundry_sdk.v2.ontologies.models.AggregateObjectsRequestV2](../../../../models/v2/ontologies/models/AggregateObjectsRequestV2.md)
- [foundry_sdk.v2.ontologies.models.AggregateObjectsResponseItemV2](../../../../models/v2/ontologies/models/AggregateObjectsResponseItemV2.md)
- [foundry_sdk.v2.ontologies.models.AggregateObjectsResponseV2](../../../../models/v2/ontologies/models/AggregateObjectsResponseV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationAccuracy](../../../../models/v2/ontologies/models/AggregationAccuracy.md)
- [foundry_sdk.v2.ontologies.models.AggregationAccuracyRequest](../../../../models/v2/ontologies/models/AggregationAccuracyRequest.md)
- [foundry_sdk.v2.ontologies.models.AggregationDurationGroupingV2](../../../../models/v2/ontologies/models/AggregationDurationGroupingV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationExactGroupingV2](../../../../models/v2/ontologies/models/AggregationExactGroupingV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationFixedWidthGroupingV2](../../../../models/v2/ontologies/models/AggregationFixedWidthGroupingV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationGroupByV2](../../../../models/v2/ontologies/models/AggregationGroupByV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationGroupKeyV2](../../../../models/v2/ontologies/models/AggregationGroupKeyV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationGroupValueV2](../../../../models/v2/ontologies/models/AggregationGroupValueV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationMetricName](../../../../models/v2/ontologies/models/AggregationMetricName.md)
- [foundry_sdk.v2.ontologies.models.AggregationMetricResultV2](../../../../models/v2/ontologies/models/AggregationMetricResultV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationRangeV2](../../../../models/v2/ontologies/models/AggregationRangeV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationRangesGroupingV2](../../../../models/v2/ontologies/models/AggregationRangesGroupingV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationV2](../../../../models/v2/ontologies/models/AggregationV2.md)
- [foundry_sdk.v2.ontologies.models.AllOfRule](../../../../models/v2/ontologies/models/AllOfRule.md)
- [foundry_sdk.v2.ontologies.models.AndQueryV2](../../../../models/v2/ontologies/models/AndQueryV2.md)
- [foundry_sdk.v2.ontologies.models.AnyOfRule](../../../../models/v2/ontologies/models/AnyOfRule.md)
- [foundry_sdk.v2.ontologies.models.ApplyReducersAndExtractMainValueLoadLevel](../../../../models/v2/ontologies/models/ApplyReducersAndExtractMainValueLoadLevel.md)
- [foundry_sdk.v2.ontologies.models.ApplyReducersLoadLevel](../../../../models/v2/ontologies/models/ApplyReducersLoadLevel.md)
- [foundry_sdk.v2.ontologies.models.ApproximateDistinctAggregationV2](../../../../models/v2/ontologies/models/ApproximateDistinctAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.ApproximatePercentileAggregationV2](../../../../models/v2/ontologies/models/ApproximatePercentileAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.AvgAggregationV2](../../../../models/v2/ontologies/models/AvgAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.BoundingBoxValue](../../../../models/v2/ontologies/models/BoundingBoxValue.md)
- [foundry_sdk.v2.ontologies.models.CenterPoint](../../../../models/v2/ontologies/models/CenterPoint.md)
- [foundry_sdk.v2.ontologies.models.CenterPointTypes](../../../../models/v2/ontologies/models/CenterPointTypes.md)
- [foundry_sdk.v2.ontologies.models.ContainsAllTermsInOrderPrefixLastTerm](../../../../models/v2/ontologies/models/ContainsAllTermsInOrderPrefixLastTerm.md)
- [foundry_sdk.v2.ontologies.models.ContainsAllTermsInOrderQuery](../../../../models/v2/ontologies/models/ContainsAllTermsInOrderQuery.md)
- [foundry_sdk.v2.ontologies.models.ContainsAllTermsQuery](../../../../models/v2/ontologies/models/ContainsAllTermsQuery.md)
- [foundry_sdk.v2.ontologies.models.ContainsAnyTermQuery](../../../../models/v2/ontologies/models/ContainsAnyTermQuery.md)
- [foundry_sdk.v2.ontologies.models.ContainsQueryV2](../../../../models/v2/ontologies/models/ContainsQueryV2.md)
- [foundry_sdk.v2.ontologies.models.CountAggregationV2](../../../../models/v2/ontologies/models/CountAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.DoesNotIntersectBoundingBoxQuery](../../../../models/v2/ontologies/models/DoesNotIntersectBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.DoesNotIntersectPolygonQuery](../../../../models/v2/ontologies/models/DoesNotIntersectPolygonQuery.md)
- [foundry_sdk.v2.ontologies.models.EqualsQueryV2](../../../../models/v2/ontologies/models/EqualsQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ExactDistinctAggregationV2](../../../../models/v2/ontologies/models/ExactDistinctAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.ExtractMainValueLoadLevel](../../../../models/v2/ontologies/models/ExtractMainValueLoadLevel.md)
- [foundry_sdk.v2.ontologies.models.FuzzyRule](../../../../models/v2/ontologies/models/FuzzyRule.md)
- [foundry_sdk.v2.ontologies.models.FuzzyV2](../../../../models/v2/ontologies/models/FuzzyV2.md)
- [foundry_sdk.v2.ontologies.models.GeoJsonString](../../../../models/v2/ontologies/models/GeoJsonString.md)
- [foundry_sdk.v2.ontologies.models.GeoShapeV2Geometry](../../../../models/v2/ontologies/models/GeoShapeV2Geometry.md)
- [foundry_sdk.v2.ontologies.models.GeoShapeV2Query](../../../../models/v2/ontologies/models/GeoShapeV2Query.md)
- [foundry_sdk.v2.ontologies.models.GtQueryV2](../../../../models/v2/ontologies/models/GtQueryV2.md)
- [foundry_sdk.v2.ontologies.models.GteQueryV2](../../../../models/v2/ontologies/models/GteQueryV2.md)
- [foundry_sdk.v2.ontologies.models.InQuery](../../../../models/v2/ontologies/models/InQuery.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](../../../../models/v2/ontologies/models/InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.IntersectsBoundingBoxQuery](../../../../models/v2/ontologies/models/IntersectsBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.IntersectsPolygonQuery](../../../../models/v2/ontologies/models/IntersectsPolygonQuery.md)
- [foundry_sdk.v2.ontologies.models.IntervalQuery](../../../../models/v2/ontologies/models/IntervalQuery.md)
- [foundry_sdk.v2.ontologies.models.IntervalQueryRule](../../../../models/v2/ontologies/models/IntervalQueryRule.md)
- [foundry_sdk.v2.ontologies.models.IsNullQueryV2](../../../../models/v2/ontologies/models/IsNullQueryV2.md)
- [foundry_sdk.v2.ontologies.models.LtQueryV2](../../../../models/v2/ontologies/models/LtQueryV2.md)
- [foundry_sdk.v2.ontologies.models.LteQueryV2](../../../../models/v2/ontologies/models/LteQueryV2.md)
- [foundry_sdk.v2.ontologies.models.MatchRule](../../../../models/v2/ontologies/models/MatchRule.md)
- [foundry_sdk.v2.ontologies.models.MaxAggregationV2](../../../../models/v2/ontologies/models/MaxAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.MinAggregationV2](../../../../models/v2/ontologies/models/MinAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.NotQueryV2](../../../../models/v2/ontologies/models/NotQueryV2.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OrQueryV2](../../../../models/v2/ontologies/models/OrQueryV2.md)
- [foundry_sdk.v2.ontologies.models.OrderByDirection](../../../../models/v2/ontologies/models/OrderByDirection.md)
- [foundry_sdk.v2.ontologies.models.PolygonValue](../../../../models/v2/ontologies/models/PolygonValue.md)
- [foundry_sdk.v2.ontologies.models.PrefixOnLastTokenRule](../../../../models/v2/ontologies/models/PrefixOnLastTokenRule.md)
- [foundry_sdk.v2.ontologies.models.PrimaryKeyPropertySelector](../../../../models/v2/ontologies/models/PrimaryKeyPropertySelector.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiNameSelector](../../../../models/v2/ontologies/models/PropertyApiNameSelector.md)
- [foundry_sdk.v2.ontologies.models.PropertyIdentifier](../../../../models/v2/ontologies/models/PropertyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.PropertyLoadLevel](../../../../models/v2/ontologies/models/PropertyLoadLevel.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](../../../../models/v2/ontologies/models/PropertyValue.md)
- [foundry_sdk.v2.ontologies.models.PropertyWithLoadLevelSelector](../../../../models/v2/ontologies/models/PropertyWithLoadLevelSelector.md)
- [foundry_sdk.v2.ontologies.models.RegexQuery](../../../../models/v2/ontologies/models/RegexQuery.md)
- [foundry_sdk.v2.ontologies.models.RelativeDateRangeBound](../../../../models/v2/ontologies/models/RelativeDateRangeBound.md)
- [foundry_sdk.v2.ontologies.models.RelativeDateRangeQuery](../../../../models/v2/ontologies/models/RelativeDateRangeQuery.md)
- [foundry_sdk.v2.ontologies.models.RelativePointInTime](../../../../models/v2/ontologies/models/RelativePointInTime.md)
- [foundry_sdk.v2.ontologies.models.RelativeTimeUnit](../../../../models/v2/ontologies/models/RelativeTimeUnit.md)
- [foundry_sdk.v2.ontologies.models.SearchJsonQueryV2](../../../../models/v2/ontologies/models/SearchJsonQueryV2.md)
- [foundry_sdk.v2.ontologies.models.SpatialFilterMode](../../../../models/v2/ontologies/models/SpatialFilterMode.md)
- [foundry_sdk.v2.ontologies.models.StartsWithQuery](../../../../models/v2/ontologies/models/StartsWithQuery.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](../../../../models/v2/ontologies/models/StructFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldSelector](../../../../models/v2/ontologies/models/StructFieldSelector.md)
- [foundry_sdk.v2.ontologies.models.SumAggregationV2](../../../../models/v2/ontologies/models/SumAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.TimeUnit](../../../../models/v2/ontologies/models/TimeUnit.md)
- [foundry_sdk.v2.ontologies.models.TitlePropertySelector](../../../../models/v2/ontologies/models/TitlePropertySelector.md)
- [foundry_sdk.v2.ontologies.models.WildcardQuery](../../../../models/v2/ontologies/models/WildcardQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinBoundingBoxPoint](../../../../models/v2/ontologies/models/WithinBoundingBoxPoint.md)
- [foundry_sdk.v2.ontologies.models.WithinBoundingBoxQuery](../../../../models/v2/ontologies/models/WithinBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinDistanceOfQuery](../../../../models/v2/ontologies/models/WithinDistanceOfQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinPolygonQuery](../../../../models/v2/ontologies/models/WithinPolygonQuery.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/OntologyInterface.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](aggregate.md)
