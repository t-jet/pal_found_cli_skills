# v2.ontologies.OntologyObjectSet.aggregate


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

## SDK invocation contract

```python
def aggregate(self, ontology: ontologies_models.OntologyIdentifier, *, aggregation: typing.List[ontologies_models.AggregationV2], group_by: typing.List[ontologies_models.AggregationGroupByV2], object_set: ontologies_models.ObjectSet, accuracy: typing.Optional[ontologies_models.AggregationAccuracyRequest]=None, branch: typing.Optional[core_models.FoundryBranch]=None, execute_in_memory_only: typing.Optional[bool]=None, include_compute_usage: typing.Optional[core_models.IncludeComputeUsage]=None, scenario_rid: typing.Optional[ontologies_models.OntologyScenarioRid]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, trace_parent: typing.Optional[core_models.TraceParent]=None, trace_state: typing.Optional[core_models.TraceState]=None, transaction_id: typing.Optional[ontologies_models.OntologyTransactionId]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.AggregateObjectsResponseV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| aggregation | typing.List[ontologies_models.AggregationV2] | required | Value shape and constraints are in its referenced local type definition. |
| group_by | typing.List[ontologies_models.AggregationGroupByV2] | required | Value shape and constraints are in its referenced local type definition. |
| object_set | ontologies_models.ObjectSet | required | Value shape and constraints are in its referenced local type definition. |
| accuracy | typing.Optional[ontologies_models.AggregationAccuracyRequest] | None | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to aggregate the objects from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. |
| execute_in_memory_only | typing.Optional[bool] | None | If true, the request fails with an error when it cannot be computed in-memory. Use this to opt into fast failure on requests that would otherwise require heavier computation. Defaults to false. |
| include_compute_usage | typing.Optional[core_models.IncludeComputeUsage] | None | Value shape and constraints are in its referenced local type definition. |
| scenario_rid | typing.Optional[ontologies_models.OntologyScenarioRid] | None | The resource identifier of an ontology scenario to aggregate the objects on. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package rid of the generated SDK. |
| sdk_version | typing.Optional[ontologies_models.SdkVersion] | None | The package version of the generated SDK. |
| trace_parent | typing.Optional[core_models.TraceParent] | None | The W3C trace parent header included in the request. |
| trace_state | typing.Optional[core_models.TraceState] | None | The W3C trace state header included in the request. |
| transaction_id | typing.Optional[ontologies_models.OntologyTransactionId] | None | The ID of an Ontology transaction to read from. Transactions are an experimental feature and all workflows may not be supported. |
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
'/v2/ontologies/{ontology}/objectSets/aggregate'
```

**query_params**

```python
{'branch': branch, 'executeInMemoryOnly': execute_in_memory_only, 'scenarioRid': scenario_rid, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version, 'transactionId': transaction_id}
```

**path_params**

```python
{'ontology': ontology}
```

**header_params**

```python
{'traceParent': trace_parent, 'traceState': trace_state, 'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.AggregateObjectSetRequestV2(aggregation=aggregation, object_set=object_set, group_by=group_by, accuracy=accuracy, include_compute_usage=include_compute_usage)
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
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.ComputeSeconds](../../../../models/v2/core/models/ComputeSeconds.md)
- [foundry_sdk.v2.core.models.Distance](../../../../models/v2/core/models/Distance.md)
- [foundry_sdk.v2.core.models.DistanceUnit](../../../../models/v2/core/models/DistanceUnit.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.IncludeComputeUsage](../../../../models/v2/core/models/IncludeComputeUsage.md)
- [foundry_sdk.v2.core.models.TraceParent](../../../../models/v2/core/models/TraceParent.md)
- [foundry_sdk.v2.core.models.TraceState](../../../../models/v2/core/models/TraceState.md)
- [foundry_sdk.v2.geo.models.BBox](../../../../models/v2/geo/models/BBox.md)
- [foundry_sdk.v2.geo.models.Coordinate](../../../../models/v2/geo/models/Coordinate.md)
- [foundry_sdk.v2.geo.models.GeoPoint](../../../../models/v2/geo/models/GeoPoint.md)
- [foundry_sdk.v2.geo.models.LinearRing](../../../../models/v2/geo/models/LinearRing.md)
- [foundry_sdk.v2.geo.models.Polygon](../../../../models/v2/geo/models/Polygon.md)
- [foundry_sdk.v2.geo.models.Position](../../../../models/v2/geo/models/Position.md)
- [foundry_sdk.v2.ontologies.models.AbsoluteValuePropertyExpression](../../../../models/v2/ontologies/models/AbsoluteValuePropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.AddPropertyExpression](../../../../models/v2/ontologies/models/AddPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.AggregateObjectSetRequestV2](../../../../models/v2/ontologies/models/AggregateObjectSetRequestV2.md)
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
- [foundry_sdk.v2.ontologies.models.DerivedPropertyApiName](../../../../models/v2/ontologies/models/DerivedPropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.DerivedPropertyDefinition](../../../../models/v2/ontologies/models/DerivedPropertyDefinition.md)
- [foundry_sdk.v2.ontologies.models.DividePropertyExpression](../../../../models/v2/ontologies/models/DividePropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.DoesNotIntersectBoundingBoxQuery](../../../../models/v2/ontologies/models/DoesNotIntersectBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.DoesNotIntersectPolygonQuery](../../../../models/v2/ontologies/models/DoesNotIntersectPolygonQuery.md)
- [foundry_sdk.v2.ontologies.models.DoubleVector](../../../../models/v2/ontologies/models/DoubleVector.md)
- [foundry_sdk.v2.ontologies.models.EqualsQueryV2](../../../../models/v2/ontologies/models/EqualsQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ExactDistinctAggregationV2](../../../../models/v2/ontologies/models/ExactDistinctAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.ExtractDatePart](../../../../models/v2/ontologies/models/ExtractDatePart.md)
- [foundry_sdk.v2.ontologies.models.ExtractMainValueLoadLevel](../../../../models/v2/ontologies/models/ExtractMainValueLoadLevel.md)
- [foundry_sdk.v2.ontologies.models.ExtractPropertyExpression](../../../../models/v2/ontologies/models/ExtractPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.FuzzyRule](../../../../models/v2/ontologies/models/FuzzyRule.md)
- [foundry_sdk.v2.ontologies.models.FuzzyV2](../../../../models/v2/ontologies/models/FuzzyV2.md)
- [foundry_sdk.v2.ontologies.models.GeoJsonString](../../../../models/v2/ontologies/models/GeoJsonString.md)
- [foundry_sdk.v2.ontologies.models.GeoShapeV2Geometry](../../../../models/v2/ontologies/models/GeoShapeV2Geometry.md)
- [foundry_sdk.v2.ontologies.models.GeoShapeV2Query](../../../../models/v2/ontologies/models/GeoShapeV2Query.md)
- [foundry_sdk.v2.ontologies.models.GetSelectedPropertyOperation](../../../../models/v2/ontologies/models/GetSelectedPropertyOperation.md)
- [foundry_sdk.v2.ontologies.models.GreatestPropertyExpression](../../../../models/v2/ontologies/models/GreatestPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.GtQueryV2](../../../../models/v2/ontologies/models/GtQueryV2.md)
- [foundry_sdk.v2.ontologies.models.GteQueryV2](../../../../models/v2/ontologies/models/GteQueryV2.md)
- [foundry_sdk.v2.ontologies.models.InQuery](../../../../models/v2/ontologies/models/InQuery.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeApiName](../../../../models/v2/ontologies/models/InterfaceLinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.IntersectsBoundingBoxQuery](../../../../models/v2/ontologies/models/IntersectsBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.IntersectsPolygonQuery](../../../../models/v2/ontologies/models/IntersectsPolygonQuery.md)
- [foundry_sdk.v2.ontologies.models.IntervalQuery](../../../../models/v2/ontologies/models/IntervalQuery.md)
- [foundry_sdk.v2.ontologies.models.IntervalQueryRule](../../../../models/v2/ontologies/models/IntervalQueryRule.md)
- [foundry_sdk.v2.ontologies.models.IsNullQueryV2](../../../../models/v2/ontologies/models/IsNullQueryV2.md)
- [foundry_sdk.v2.ontologies.models.LeastPropertyExpression](../../../../models/v2/ontologies/models/LeastPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LtQueryV2](../../../../models/v2/ontologies/models/LtQueryV2.md)
- [foundry_sdk.v2.ontologies.models.LteQueryV2](../../../../models/v2/ontologies/models/LteQueryV2.md)
- [foundry_sdk.v2.ontologies.models.MatchRule](../../../../models/v2/ontologies/models/MatchRule.md)
- [foundry_sdk.v2.ontologies.models.MaxAggregationV2](../../../../models/v2/ontologies/models/MaxAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.MethodObjectSet](../../../../models/v2/ontologies/models/MethodObjectSet.md)
- [foundry_sdk.v2.ontologies.models.MinAggregationV2](../../../../models/v2/ontologies/models/MinAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.MultiplyPropertyExpression](../../../../models/v2/ontologies/models/MultiplyPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.NearestNeighborsQuery](../../../../models/v2/ontologies/models/NearestNeighborsQuery.md)
- [foundry_sdk.v2.ontologies.models.NearestNeighborsQueryText](../../../../models/v2/ontologies/models/NearestNeighborsQueryText.md)
- [foundry_sdk.v2.ontologies.models.NegatePropertyExpression](../../../../models/v2/ontologies/models/NegatePropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.NotQueryV2](../../../../models/v2/ontologies/models/NotQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ObjectRid](../../../../models/v2/ontologies/models/ObjectRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectSet](../../../../models/v2/ontologies/models/ObjectSet.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetAsBaseObjectTypesType](../../../../models/v2/ontologies/models/ObjectSetAsBaseObjectTypesType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetAsTypeType](../../../../models/v2/ontologies/models/ObjectSetAsTypeType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetBaseType](../../../../models/v2/ontologies/models/ObjectSetBaseType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetFilterType](../../../../models/v2/ontologies/models/ObjectSetFilterType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetInterfaceBaseType](../../../../models/v2/ontologies/models/ObjectSetInterfaceBaseType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetInterfaceLinkSearchAroundType](../../../../models/v2/ontologies/models/ObjectSetInterfaceLinkSearchAroundType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetIntersectionType](../../../../models/v2/ontologies/models/ObjectSetIntersectionType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetMethodInputType](../../../../models/v2/ontologies/models/ObjectSetMethodInputType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetNearestNeighborsType](../../../../models/v2/ontologies/models/ObjectSetNearestNeighborsType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetReferenceType](../../../../models/v2/ontologies/models/ObjectSetReferenceType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetRid](../../../../models/v2/ontologies/models/ObjectSetRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetSearchAroundType](../../../../models/v2/ontologies/models/ObjectSetSearchAroundType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetStaticType](../../../../models/v2/ontologies/models/ObjectSetStaticType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetSubtractType](../../../../models/v2/ontologies/models/ObjectSetSubtractType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetUnionType](../../../../models/v2/ontologies/models/ObjectSetUnionType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetWithPropertiesType](../../../../models/v2/ontologies/models/ObjectSetWithPropertiesType.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyScenarioRid](../../../../models/v2/ontologies/models/OntologyScenarioRid.md)
- [foundry_sdk.v2.ontologies.models.OntologyTransactionId](../../../../models/v2/ontologies/models/OntologyTransactionId.md)
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
- [foundry_sdk.v2.ontologies.models.SdkPackageRid](../../../../models/v2/ontologies/models/SdkPackageRid.md)
- [foundry_sdk.v2.ontologies.models.SdkVersion](../../../../models/v2/ontologies/models/SdkVersion.md)
- [foundry_sdk.v2.ontologies.models.SearchJsonQueryV2](../../../../models/v2/ontologies/models/SearchJsonQueryV2.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyApproximateDistinctAggregation](../../../../models/v2/ontologies/models/SelectedPropertyApproximateDistinctAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyApproximatePercentileAggregation](../../../../models/v2/ontologies/models/SelectedPropertyApproximatePercentileAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyAvgAggregation](../../../../models/v2/ontologies/models/SelectedPropertyAvgAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyCollectListAggregation](../../../../models/v2/ontologies/models/SelectedPropertyCollectListAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyCollectSetAggregation](../../../../models/v2/ontologies/models/SelectedPropertyCollectSetAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyCountAggregation](../../../../models/v2/ontologies/models/SelectedPropertyCountAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyExactDistinctAggregation](../../../../models/v2/ontologies/models/SelectedPropertyExactDistinctAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyExpression](../../../../models/v2/ontologies/models/SelectedPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyMaxAggregation](../../../../models/v2/ontologies/models/SelectedPropertyMaxAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyMinAggregation](../../../../models/v2/ontologies/models/SelectedPropertyMinAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyOperation](../../../../models/v2/ontologies/models/SelectedPropertyOperation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertySumAggregation](../../../../models/v2/ontologies/models/SelectedPropertySumAggregation.md)
- [foundry_sdk.v2.ontologies.models.SpatialFilterMode](../../../../models/v2/ontologies/models/SpatialFilterMode.md)
- [foundry_sdk.v2.ontologies.models.StartsWithQuery](../../../../models/v2/ontologies/models/StartsWithQuery.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](../../../../models/v2/ontologies/models/StructFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldSelector](../../../../models/v2/ontologies/models/StructFieldSelector.md)
- [foundry_sdk.v2.ontologies.models.SubtractPropertyExpression](../../../../models/v2/ontologies/models/SubtractPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.SumAggregationV2](../../../../models/v2/ontologies/models/SumAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.TimeUnit](../../../../models/v2/ontologies/models/TimeUnit.md)
- [foundry_sdk.v2.ontologies.models.TitlePropertySelector](../../../../models/v2/ontologies/models/TitlePropertySelector.md)
- [foundry_sdk.v2.ontologies.models.WildcardQuery](../../../../models/v2/ontologies/models/WildcardQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinBoundingBoxPoint](../../../../models/v2/ontologies/models/WithinBoundingBoxPoint.md)
- [foundry_sdk.v2.ontologies.models.WithinBoundingBoxQuery](../../../../models/v2/ontologies/models/WithinBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinDistanceOfQuery](../../../../models/v2/ontologies/models/WithinDistanceOfQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinPolygonQuery](../../../../models/v2/ontologies/models/WithinPolygonQuery.md)

[Part 1](aggregate.md) | [Part 2](aggregate-2.md)
