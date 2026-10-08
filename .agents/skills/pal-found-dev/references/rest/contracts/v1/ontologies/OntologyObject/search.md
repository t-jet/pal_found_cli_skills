# v1.ontologies.OntologyObject.search


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Search for objects in the specified ontology and object type. The request body is used
to filter objects based on the specified query. The supported queries are:

| Query type            | Description                                                                       | Supported Types                 |
|----------|-----------------------------------------------------------------------------------|---------------------------------|
| lt       | The provided property is less than the provided value.                            | number, string, date, timestamp |
| gt       | The provided property is greater than the provided value.                         | number, string, date, timestamp |
| lte      | The provided property is less than or equal to the provided value.                | number, string, date, timestamp |
| gte      | The provided property is greater than or equal to the provided value.             | number, string, date, timestamp |
| eq       | The provided property is exactly equal to the provided value.                     | number, string, date, timestamp |
| isNull   | The provided property is (or is not) null.                                        | all                             |
| contains | The provided property contains the provided value.                                | array                           |
| not      | The sub-query does not match.                                                     | N/A (applied on a query)        |
| and      | All the sub-queries match.                                                        | N/A (applied on queries)        |
| or       | At least one of the sub-queries match.                                            | N/A (applied on queries)        |
| prefix   | The provided property starts with the provided term.                              | string                          |
| phrase   | The provided property contains the provided term as a substring.                  | string                          |
| anyTerm  | The provided property contains at least one of the terms separated by whitespace. | string                          |
| allTerms | The provided property contains all the terms separated by whitespace.             | string                          |

Queries can be at most three levels deep. By default, terms are separated by whitespace or punctuation (`?!,:;-[](){}'"~`). Periods (`.`) on their own are ignored.
Partial terms are not matched by terms filters except where explicitly noted.

## SDK invocation contract

```python
def search(self, ontology_rid: ontologies_models.OntologyRid, object_type: ontologies_models.ObjectTypeApiName, *, fields: typing.List[ontologies_models.PropertyApiName], query: ontologies_models.SearchJsonQuery, order_by: typing.Optional[ontologies_models.SearchOrderBy]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.SearchObjectsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology_rid | ontologies_models.OntologyRid | required | The unique Resource Identifier (RID) of the Ontology that contains the objects. |
| object_type | ontologies_models.ObjectTypeApiName | required | The type of the requested objects. |
| fields | typing.List[ontologies_models.PropertyApiName] | required | The API names of the object type properties to include in the response. |
| query | ontologies_models.SearchJsonQuery | required | Value shape and constraints are in its referenced local type definition. |
| order_by | typing.Optional[ontologies_models.SearchOrderBy] | None | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | Value shape and constraints are in its referenced local type definition. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
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
'/v1/ontologies/{ontologyRid}/objects/{objectType}/search'
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
ontologies_models.SearchObjectsRequest(query=query, order_by=order_by, page_size=page_size, page_token=page_token, fields=fields)
```

**response_type**

```python
ontologies_models.SearchObjectsResponse
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

Ordinary sync return: `ontologies_models.SearchObjectsResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.SearchObjectsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.SearchObjectsResponse |
| sync_raw | ApiResponse[ontologies_models.SearchObjectsResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.SearchObjectsResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.SearchObjectsResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.SearchObjectsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.SearchObjectsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.models.PageSize](../../../../models/v1/core/models/PageSize.md)
- [foundry_sdk.v1.core.models.PageToken](../../../../models/v1/core/models/PageToken.md)
- [foundry_sdk.v1.core.models.TotalCount](../../../../models/v1/core/models/TotalCount.md)
- [foundry_sdk.v1.ontologies.models.AllTermsQuery](../../../../models/v1/ontologies/models/AllTermsQuery.md)
- [foundry_sdk.v1.ontologies.models.AndQuery](../../../../models/v1/ontologies/models/AndQuery.md)
- [foundry_sdk.v1.ontologies.models.AnyTermQuery](../../../../models/v1/ontologies/models/AnyTermQuery.md)
- [foundry_sdk.v1.ontologies.models.ContainsQuery](../../../../models/v1/ontologies/models/ContainsQuery.md)
- [foundry_sdk.v1.ontologies.models.EqualsQuery](../../../../models/v1/ontologies/models/EqualsQuery.md)
- [foundry_sdk.v1.ontologies.models.FieldNameV1](../../../../models/v1/ontologies/models/FieldNameV1.md)
- [foundry_sdk.v1.ontologies.models.Fuzzy](../../../../models/v1/ontologies/models/Fuzzy.md)
- [foundry_sdk.v1.ontologies.models.GtQuery](../../../../models/v1/ontologies/models/GtQuery.md)
- [foundry_sdk.v1.ontologies.models.GteQuery](../../../../models/v1/ontologies/models/GteQuery.md)
- [foundry_sdk.v1.ontologies.models.IsNullQuery](../../../../models/v1/ontologies/models/IsNullQuery.md)
- [foundry_sdk.v1.ontologies.models.LtQuery](../../../../models/v1/ontologies/models/LtQuery.md)
- [foundry_sdk.v1.ontologies.models.LteQuery](../../../../models/v1/ontologies/models/LteQuery.md)
- [foundry_sdk.v1.ontologies.models.NotQuery](../../../../models/v1/ontologies/models/NotQuery.md)
- [foundry_sdk.v1.ontologies.models.ObjectRid](../../../../models/v1/ontologies/models/ObjectRid.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeApiName](../../../../models/v1/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.OntologyObject](../../../../models/v1/ontologies/models/OntologyObject.md)
- [foundry_sdk.v1.ontologies.models.OntologyRid](../../../../models/v1/ontologies/models/OntologyRid.md)
- [foundry_sdk.v1.ontologies.models.OrQuery](../../../../models/v1/ontologies/models/OrQuery.md)
- [foundry_sdk.v1.ontologies.models.PhraseQuery](../../../../models/v1/ontologies/models/PhraseQuery.md)
- [foundry_sdk.v1.ontologies.models.PrefixQuery](../../../../models/v1/ontologies/models/PrefixQuery.md)
- [foundry_sdk.v1.ontologies.models.PropertyApiName](../../../../models/v1/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v1.ontologies.models.PropertyValue](../../../../models/v1/ontologies/models/PropertyValue.md)
- [foundry_sdk.v1.ontologies.models.SearchJsonQuery](../../../../models/v1/ontologies/models/SearchJsonQuery.md)
- [foundry_sdk.v1.ontologies.models.SearchObjectsRequest](../../../../models/v1/ontologies/models/SearchObjectsRequest.md)
- [foundry_sdk.v1.ontologies.models.SearchObjectsResponse](../../../../models/v1/ontologies/models/SearchObjectsResponse.md)
- [foundry_sdk.v1.ontologies.models.SearchOrderBy](../../../../models/v1/ontologies/models/SearchOrderBy.md)
- [foundry_sdk.v1.ontologies.models.SearchOrdering](../../../../models/v1/ontologies/models/SearchOrdering.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/OntologyObject.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](search.md)
