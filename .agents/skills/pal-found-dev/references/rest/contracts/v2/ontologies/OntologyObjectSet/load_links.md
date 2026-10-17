# v2.ontologies.OntologyObjectSet.load_links


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Loads the specified links from the defined object set.

Links are defined as a link type API name and object locators for the source and target objects
where only the `__primaryKey` and `__apiName` properties are loaded.

Links are grouped by source object locator; however, the links for a given source object may be
split over multiple entries with the same source object locator.

Please keep these limitations in mind:
- Links returned may be stale. For example, primary keys returned by this endpoint may not exist anymore.
- This endpoint requests links for 1,000 objects at a time. If, for any page of 1,000 objects, there are more
  than 100,000 links present, results are limited to 100,000 links and should be considered partial.
- This endpoint does not support OSv1 links and will return an error if links provided are backed by OSv1.
- This endpoint currently does not support interface object sets or interface links, but support will be added in the near future.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.OntologyObjectSet.load_links`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def load_links(self, ontology: ontologies_models.OntologyIdentifier, *, links: typing.List[ontologies_models.LinkTypeApiName], object_set: ontologies_models.ObjectSet, branch: typing.Optional[core_models.FoundryBranch]=None, execute_in_memory_only: typing.Optional[bool]=None, include_compute_usage: typing.Optional[core_models.IncludeComputeUsage]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, trace_parent: typing.Optional[core_models.TraceParent]=None, trace_state: typing.Optional[core_models.TraceState]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.LoadObjectSetLinksResponseV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| links | typing.List[ontologies_models.LinkTypeApiName] | required | Value shape and constraints are in its referenced local type definition. |
| object_set | ontologies_models.ObjectSet | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to aggregate the objects from. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. |
| execute_in_memory_only | typing.Optional[bool] | None | If true, the request fails with an error when it cannot be computed in-memory. Use this to opt into fast failure on requests that would otherwise require heavier computation. Defaults to false. |
| include_compute_usage | typing.Optional[core_models.IncludeComputeUsage] | None | Value shape and constraints are in its referenced local type definition. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package rid of the generated SDK. |
| sdk_version | typing.Optional[ontologies_models.SdkVersion] | None | The package version of the generated SDK. |
| trace_parent | typing.Optional[core_models.TraceParent] | None | The W3C trace parent header included in the request. |
| trace_state | typing.Optional[core_models.TraceState] | None | The W3C trace state header included in the request. |
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
'/v2/ontologies/{ontology}/objectSets/loadLinks'
```

**query_params**

```python
{'branch': branch, 'executeInMemoryOnly': execute_in_memory_only, 'preview': preview, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version}
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
ontologies_models.LoadObjectSetLinksRequestV2(object_set=object_set, links=links, page_token=page_token, include_compute_usage=include_compute_usage)
```

**response_type**

```python
ontologies_models.LoadObjectSetLinksResponseV2
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

Ordinary sync return: `ontologies_models.LoadObjectSetLinksResponseV2`. Ordinary async return: `typing.Awaitable[ontologies_models.LoadObjectSetLinksResponseV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.LoadObjectSetLinksResponseV2 |
| sync_raw | ApiResponse[ontologies_models.LoadObjectSetLinksResponseV2] |
| sync_streaming | StreamingContextManager[ontologies_models.LoadObjectSetLinksResponseV2] |
| async_ordinary | typing.Awaitable[ontologies_models.LoadObjectSetLinksResponseV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.LoadObjectSetLinksResponseV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.LoadObjectSetLinksResponseV2]] |

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
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
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
- [foundry_sdk.v2.ontologies.models.LinkedObjectLocator](../../../../models/v2/ontologies/models/LinkedObjectLocator.md)
- [foundry_sdk.v2.ontologies.models.LinksFromObject](../../../../models/v2/ontologies/models/LinksFromObject.md)
- [foundry_sdk.v2.ontologies.models.LoadObjectSetLinksRequestV2](../../../../models/v2/ontologies/models/LoadObjectSetLinksRequestV2.md)
- [foundry_sdk.v2.ontologies.models.LoadObjectSetLinksResponseV2](../../../../models/v2/ontologies/models/LoadObjectSetLinksResponseV2.md)
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
- [foundry_sdk.v2.ontologies.models.OntologyObjectV2](../../../../models/v2/ontologies/models/OntologyObjectV2.md)
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
- [foundry_sdk.v2.ontologies.models.TitlePropertySelector](../../../../models/v2/ontologies/models/TitlePropertySelector.md)
- [foundry_sdk.v2.ontologies.models.WildcardQuery](../../../../models/v2/ontologies/models/WildcardQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinBoundingBoxPoint](../../../../models/v2/ontologies/models/WithinBoundingBoxPoint.md)
- [foundry_sdk.v2.ontologies.models.WithinBoundingBoxQuery](../../../../models/v2/ontologies/models/WithinBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinDistanceOfQuery](../../../../models/v2/ontologies/models/WithinDistanceOfQuery.md)
- [foundry_sdk.v2.ontologies.models.WithinPolygonQuery](../../../../models/v2/ontologies/models/WithinPolygonQuery.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

[Part 1](load_links.md) | [Part 2](load_links-2.md)
