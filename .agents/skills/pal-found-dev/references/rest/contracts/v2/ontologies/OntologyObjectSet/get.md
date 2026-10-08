# v2.ontologies.OntologyObjectSet.get


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets the definition of the `ObjectSet` with the given RID.

## SDK invocation contract

```python
def get(self, ontology: ontologies_models.OntologyIdentifier, object_set_rid: ontologies_models.ObjectSetRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ObjectSet: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_set_rid | ontologies_models.ObjectSetRid | required | The RID of the object set. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
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
'/v2/ontologies/{ontology}/objectSets/{objectSetRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'ontology': ontology, 'objectSetRid': object_set_rid}
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
ontologies_models.ObjectSet
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

Ordinary sync return: `ontologies_models.ObjectSet`. Ordinary async return: `typing.Awaitable[ontologies_models.ObjectSet]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ObjectSet |
| sync_raw | ApiResponse[ontologies_models.ObjectSet] |
| sync_streaming | StreamingContextManager[ontologies_models.ObjectSet] |
| async_ordinary | typing.Awaitable[ontologies_models.ObjectSet] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ObjectSet]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ObjectSet]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.Distance](../../../../models/v2/core/models/Distance.md)
- [foundry_sdk.v2.core.models.DistanceUnit](../../../../models/v2/core/models/DistanceUnit.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.geo.models.BBox](../../../../models/v2/geo/models/BBox.md)
- [foundry_sdk.v2.geo.models.Coordinate](../../../../models/v2/geo/models/Coordinate.md)
- [foundry_sdk.v2.geo.models.GeoPoint](../../../../models/v2/geo/models/GeoPoint.md)
- [foundry_sdk.v2.geo.models.LinearRing](../../../../models/v2/geo/models/LinearRing.md)
- [foundry_sdk.v2.geo.models.Polygon](../../../../models/v2/geo/models/Polygon.md)
- [foundry_sdk.v2.geo.models.Position](../../../../models/v2/geo/models/Position.md)
- [foundry_sdk.v2.ontologies.models.AbsoluteValuePropertyExpression](../../../../models/v2/ontologies/models/AbsoluteValuePropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.AddPropertyExpression](../../../../models/v2/ontologies/models/AddPropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.AllOfRule](../../../../models/v2/ontologies/models/AllOfRule.md)
- [foundry_sdk.v2.ontologies.models.AndQueryV2](../../../../models/v2/ontologies/models/AndQueryV2.md)
- [foundry_sdk.v2.ontologies.models.AnyOfRule](../../../../models/v2/ontologies/models/AnyOfRule.md)
- [foundry_sdk.v2.ontologies.models.ApplyReducersAndExtractMainValueLoadLevel](../../../../models/v2/ontologies/models/ApplyReducersAndExtractMainValueLoadLevel.md)
- [foundry_sdk.v2.ontologies.models.ApplyReducersLoadLevel](../../../../models/v2/ontologies/models/ApplyReducersLoadLevel.md)
- [foundry_sdk.v2.ontologies.models.BoundingBoxValue](../../../../models/v2/ontologies/models/BoundingBoxValue.md)
- [foundry_sdk.v2.ontologies.models.CenterPoint](../../../../models/v2/ontologies/models/CenterPoint.md)
- [foundry_sdk.v2.ontologies.models.CenterPointTypes](../../../../models/v2/ontologies/models/CenterPointTypes.md)
- [foundry_sdk.v2.ontologies.models.ContainsAllTermsInOrderPrefixLastTerm](../../../../models/v2/ontologies/models/ContainsAllTermsInOrderPrefixLastTerm.md)
- [foundry_sdk.v2.ontologies.models.ContainsAllTermsInOrderQuery](../../../../models/v2/ontologies/models/ContainsAllTermsInOrderQuery.md)
- [foundry_sdk.v2.ontologies.models.ContainsAllTermsQuery](../../../../models/v2/ontologies/models/ContainsAllTermsQuery.md)
- [foundry_sdk.v2.ontologies.models.ContainsAnyTermQuery](../../../../models/v2/ontologies/models/ContainsAnyTermQuery.md)
- [foundry_sdk.v2.ontologies.models.ContainsQueryV2](../../../../models/v2/ontologies/models/ContainsQueryV2.md)
- [foundry_sdk.v2.ontologies.models.DerivedPropertyApiName](../../../../models/v2/ontologies/models/DerivedPropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.DerivedPropertyDefinition](../../../../models/v2/ontologies/models/DerivedPropertyDefinition.md)
- [foundry_sdk.v2.ontologies.models.DividePropertyExpression](../../../../models/v2/ontologies/models/DividePropertyExpression.md)
- [foundry_sdk.v2.ontologies.models.DoesNotIntersectBoundingBoxQuery](../../../../models/v2/ontologies/models/DoesNotIntersectBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.DoesNotIntersectPolygonQuery](../../../../models/v2/ontologies/models/DoesNotIntersectPolygonQuery.md)
- [foundry_sdk.v2.ontologies.models.DoubleVector](../../../../models/v2/ontologies/models/DoubleVector.md)
- [foundry_sdk.v2.ontologies.models.EqualsQueryV2](../../../../models/v2/ontologies/models/EqualsQueryV2.md)
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
- [foundry_sdk.v2.ontologies.models.MethodObjectSet](../../../../models/v2/ontologies/models/MethodObjectSet.md)
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
- [foundry_sdk.v2.ontologies.models.OrQueryV2](../../../../models/v2/ontologies/models/OrQueryV2.md)
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
- [foundry_sdk.v2.ontologies.models.TitlePropertySelector](../../../../models/v2/ontologies/models/TitlePropertySelector.md)
- [foundry_sdk.v2.ontologies.models.WildcardQuery](../../../../models/v2/ontologies/models/WildcardQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinBoundingBoxPoint](../../../../models/v2/ontologies/models/WithinBoundingBoxPoint.md)
- [foundry_sdk.v2.ontologies.models.WithinBoundingBoxQuery](../../../../models/v2/ontologies/models/WithinBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinDistanceOfQuery](../../../../models/v2/ontologies/models/WithinDistanceOfQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinPolygonQuery](../../../../models/v2/ontologies/models/WithinPolygonQuery.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/OntologyObjectSet.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
