# v2.ontologies.OntologyInterface.search


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

:::callout{theme=warning title=Warning}
  This endpoint will be removed once TS OSDK is updated to use `objectSets/loadObjects` with interface object
  sets.
:::
Search for objects in the specified ontology and interface type. Any properties specified in the "where" or
"orderBy" parameters must be shared property type API names defined on the interface. The following search
queries are supported:

| Query type                              | Description                                                                                                       | Supported Types                 |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------|
| lt                                      | The provided property is less than the provided value.                                                            | number, string, date, timestamp |
| gt                                      | The provided property is greater than the provided value.                                                         | number, string, date, timestamp |
| lte                                     | The provided property is less than or equal to the provided value.                                                | number, string, date, timestamp |
| gte                                     | The provided property is greater than or equal to the provided value.                                             | number, string, date, timestamp |
| eq                                      | The provided property is exactly equal to the provided value.                                                     | number, string, date, timestamp |
| isNull                                  | The provided property is (or is not) null.                                                                        | all                             |
| contains                                | The provided property contains the provided value.                                                                | array                           |
| not                                     | The sub-query does not match.                                                                                     | N/A (applied on a query)        |
| and                                     | All the sub-queries match.                                                                                        | N/A (applied on queries)        |
| or                                      | At least one of the sub-queries match.                                                                            | N/A (applied on queries)        |
| startsWith                              | The provided property starts with the provided term.                                                              | string                          |
| containsAllTermsInOrderPrefixLastTerm   | The provided property contains all the terms provided in order. The last term can be a partial prefix match.      | string                          |
| containsAllTermsInOrder                 | The provided property contains the provided terms as a substring.                                                 | string                          |
| containsAnyTerm                         | The provided property contains at least one of the terms separated by whitespace.                                 | string                          |
| containsAllTerms                        | The provided property contains all the terms separated by whitespace.                                             | string                          |

Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
Partial terms are not matched by terms filters except where explicitly noted.

Attempting to use an unsupported query will result in a validation error. Third-party applications using this
endpoint via OAuth2 must request the following operation scope: `api:ontologies-read`.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.OntologyInterface.search`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def search(self, ontology: ontologies_models.OntologyIdentifier, interface_type: ontologies_models.InterfaceTypeApiName, *, augmented_interface_property_types: typing.Dict[ontologies_models.InterfaceTypeApiName, typing.List[ontologies_models.InterfacePropertyApiName]], augmented_properties: typing.Dict[ontologies_models.ObjectTypeApiName, typing.List[ontologies_models.PropertyApiName]], augmented_shared_property_types: typing.Dict[ontologies_models.InterfaceTypeApiName, typing.List[ontologies_models.SharedPropertyTypeApiName]], other_interface_types: typing.List[ontologies_models.InterfaceTypeApiName], selected_interface_property_types: typing.List[ontologies_models.InterfacePropertyApiName], selected_object_types: typing.List[ontologies_models.ObjectTypeApiName], selected_shared_property_types: typing.List[ontologies_models.SharedPropertyTypeApiName], branch: typing.Optional[core_models.FoundryBranch]=None, order_by: typing.Optional[ontologies_models.SearchOrderByV2]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, where: typing.Optional[ontologies_models.SearchJsonQueryV2]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.SearchObjectsResponseV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| interface_type | ontologies_models.InterfaceTypeApiName | required | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager**. |
| augmented_interface_property_types | typing.Dict[ontologies_models.InterfaceTypeApiName, typing.List[ontologies_models.InterfacePropertyApiName]] | required | A map from interface type API name to a list of interface property type API names. For each returned object, if the object implements an interface that is a key in the map, then we augment the response for that object type with the list of properties specified in the value. |
| augmented_properties | typing.Dict[ontologies_models.ObjectTypeApiName, typing.List[ontologies_models.PropertyApiName]] | required | A map from object type API name to a list of property type API names. For each returned object, if the object’s object type is a key in the map, then we augment the response for that object type with the list of properties specified in the value. |
| augmented_shared_property_types | typing.Dict[ontologies_models.InterfaceTypeApiName, typing.List[ontologies_models.SharedPropertyTypeApiName]] | required | A map from interface type API name to a list of shared property type API names. For each returned object, if the object implements an interface that is a key in the map, then we augment the response for that object type with the list of properties specified in the value. |
| other_interface_types | typing.List[ontologies_models.InterfaceTypeApiName] | required | A list of interface type API names. Object types must implement all the mentioned interfaces in order to be included in the response. |
| selected_interface_property_types | typing.List[ontologies_models.InterfacePropertyApiName] | required | A list of interface property type API names of the interface type that should be included in the response. Omit this parameter to include all properties of the interface type in the response. |
| selected_object_types | typing.List[ontologies_models.ObjectTypeApiName] | required | A list of object type API names that should be included in the response. If non-empty, object types that are not mentioned will not be included in the response even if they implement the specified interface. Omit the parameter to include all object types. |
| selected_shared_property_types | typing.List[ontologies_models.SharedPropertyTypeApiName] | required | A list of shared property type API names of the interface type that should be included in the response. Omit this parameter to include all properties of the interface type in the response. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to search objects from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
| order_by | typing.Optional[ontologies_models.SearchOrderByV2] | None | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | Value shape and constraints are in its referenced local type definition. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
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
'/v2/ontologies/{ontology}/interfaces/{interfaceType}/search'
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
ontologies_models.SearchObjectsForInterfaceRequest(where=where, order_by=order_by, augmented_properties=augmented_properties, augmented_shared_property_types=augmented_shared_property_types, augmented_interface_property_types=augmented_interface_property_types, selected_shared_property_types=selected_shared_property_types, selected_interface_property_types=selected_interface_property_types, selected_object_types=selected_object_types, other_interface_types=other_interface_types, page_size=page_size, page_token=page_token)
```

**response_type**

```python
ontologies_models.SearchObjectsResponseV2
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

Ordinary sync return: `ontologies_models.SearchObjectsResponseV2`. Ordinary async return: `typing.Awaitable[ontologies_models.SearchObjectsResponseV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.SearchObjectsResponseV2 |
| sync_raw | ApiResponse[ontologies_models.SearchObjectsResponseV2] |
| sync_streaming | StreamingContextManager[ontologies_models.SearchObjectsResponseV2] |
| async_ordinary | typing.Awaitable[ontologies_models.SearchObjectsResponseV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.SearchObjectsResponseV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.SearchObjectsResponseV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.Distance](../../../../models/v2/core/models/Distance.md)
- [foundry_sdk.v2.core.models.DistanceUnit](../../../../models/v2/core/models/DistanceUnit.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.TotalCount](../../../../models/v2/core/models/TotalCount.md)
- [foundry_sdk.v2.geo.models.BBox](../../../../models/v2/geo/models/BBox.md)
- [foundry_sdk.v2.geo.models.Coordinate](../../../../models/v2/geo/models/Coordinate.md)
- [foundry_sdk.v2.geo.models.GeoPoint](../../../../models/v2/geo/models/GeoPoint.md)
- [foundry_sdk.v2.geo.models.LinearRing](../../../../models/v2/geo/models/LinearRing.md)
- [foundry_sdk.v2.geo.models.Polygon](../../../../models/v2/geo/models/Polygon.md)
- [foundry_sdk.v2.geo.models.Position](../../../../models/v2/geo/models/Position.md)
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
- [foundry_sdk.v2.ontologies.models.DoesNotIntersectBoundingBoxQuery](../../../../models/v2/ontologies/models/DoesNotIntersectBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.DoesNotIntersectPolygonQuery](../../../../models/v2/ontologies/models/DoesNotIntersectPolygonQuery.md)
- [foundry_sdk.v2.ontologies.models.EqualsQueryV2](../../../../models/v2/ontologies/models/EqualsQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ExtractMainValueLoadLevel](../../../../models/v2/ontologies/models/ExtractMainValueLoadLevel.md)
- [foundry_sdk.v2.ontologies.models.FuzzyRule](../../../../models/v2/ontologies/models/FuzzyRule.md)
- [foundry_sdk.v2.ontologies.models.FuzzyV2](../../../../models/v2/ontologies/models/FuzzyV2.md)
- [foundry_sdk.v2.ontologies.models.GeoJsonString](../../../../models/v2/ontologies/models/GeoJsonString.md)
- [foundry_sdk.v2.ontologies.models.GeoShapeV2Geometry](../../../../models/v2/ontologies/models/GeoShapeV2Geometry.md)
- [foundry_sdk.v2.ontologies.models.GeoShapeV2Query](../../../../models/v2/ontologies/models/GeoShapeV2Query.md)
- [foundry_sdk.v2.ontologies.models.GtQueryV2](../../../../models/v2/ontologies/models/GtQueryV2.md)
- [foundry_sdk.v2.ontologies.models.GteQueryV2](../../../../models/v2/ontologies/models/GteQueryV2.md)
- [foundry_sdk.v2.ontologies.models.InQuery](../../../../models/v2/ontologies/models/InQuery.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyApiName](../../../../models/v2/ontologies/models/InterfacePropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](../../../../models/v2/ontologies/models/InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.IntersectsBoundingBoxQuery](../../../../models/v2/ontologies/models/IntersectsBoundingBoxQuery.md)
- [foundry_sdk.v2.ontologies.models.IntersectsPolygonQuery](../../../../models/v2/ontologies/models/IntersectsPolygonQuery.md)
- [foundry_sdk.v2.ontologies.models.IntervalQuery](../../../../models/v2/ontologies/models/IntervalQuery.md)
- [foundry_sdk.v2.ontologies.models.IntervalQueryRule](../../../../models/v2/ontologies/models/IntervalQueryRule.md)
- [foundry_sdk.v2.ontologies.models.IsNullQueryV2](../../../../models/v2/ontologies/models/IsNullQueryV2.md)
- [foundry_sdk.v2.ontologies.models.LtQueryV2](../../../../models/v2/ontologies/models/LtQueryV2.md)
- [foundry_sdk.v2.ontologies.models.LteQueryV2](../../../../models/v2/ontologies/models/LteQueryV2.md)
- [foundry_sdk.v2.ontologies.models.MatchRule](../../../../models/v2/ontologies/models/MatchRule.md)
- [foundry_sdk.v2.ontologies.models.NotQueryV2](../../../../models/v2/ontologies/models/NotQueryV2.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
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
- [foundry_sdk.v2.ontologies.models.SearchJsonQueryV2](../../../../models/v2/ontologies/models/SearchJsonQueryV2.md)
- [foundry_sdk.v2.ontologies.models.SearchObjectsForInterfaceRequest](../../../../models/v2/ontologies/models/SearchObjectsForInterfaceRequest.md)
- [foundry_sdk.v2.ontologies.models.SearchObjectsResponseV2](../../../../models/v2/ontologies/models/SearchObjectsResponseV2.md)
- [foundry_sdk.v2.ontologies.models.SearchOrderByType](../../../../models/v2/ontologies/models/SearchOrderByType.md)
- [foundry_sdk.v2.ontologies.models.SearchOrderByV2](../../../../models/v2/ontologies/models/SearchOrderByV2.md)
- [foundry_sdk.v2.ontologies.models.SearchOrderingV2](../../../../models/v2/ontologies/models/SearchOrderingV2.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeApiName](../../../../models/v2/ontologies/models/SharedPropertyTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.SpatialFilterMode](../../../../models/v2/ontologies/models/SpatialFilterMode.md)
- [foundry_sdk.v2.ontologies.models.StartsWithQuery](../../../../models/v2/ontologies/models/StartsWithQuery.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](../../../../models/v2/ontologies/models/StructFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldSelector](../../../../models/v2/ontologies/models/StructFieldSelector.md)
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

[Part 1](search.md)
