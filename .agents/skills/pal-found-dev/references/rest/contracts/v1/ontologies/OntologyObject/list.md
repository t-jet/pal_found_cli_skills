# v1.ontologies.OntologyObject.list


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists the objects for the given Ontology and object type.

This endpoint supports filtering objects.
See the [Filtering Objects documentation](../../../../../ontology/queries.md) for details.

Note that this endpoint does not guarantee consistency. Changes to the data could result in missing or
repeated objects in the response pages.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Each page may be smaller or larger than the requested page size. However, it
is guaranteed that if there are more results available, at least one result will be present
in the response.

Note that null value properties will not be returned.

## SDK invocation contract

```python
def list(self, ontology_rid: ontologies_models.OntologyRid, object_type: ontologies_models.ObjectTypeApiName, *, order_by: typing.Optional[ontologies_models.OrderBy]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, properties: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[ontologies_models.OntologyObject]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology_rid | ontologies_models.OntologyRid | required | The unique Resource Identifier (RID) of the Ontology that contains the objects. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |
| order_by | typing.Optional[ontologies_models.OrderBy] | None | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](../../../../client-behavior.md) for details. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| properties | typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] | None | The properties of the object type that should be included in the response. Omit this parameter to get all the properties. |
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
'/v1/ontologies/{ontologyRid}/objects/{objectType}'
```

**query_params**

```python
{'orderBy': order_by, 'pageSize': page_size, 'pageToken': page_token, 'properties': properties}
```

**path_params**

```python
{'ontologyRid': ontology_rid, 'objectType': object_type}
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
ontologies_models.ListObjectsResponse
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
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[ontologies_models.OntologyObject]`. Ordinary async return: `core.AsyncResourceIterator[ontologies_models.OntologyObject]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[ontologies_models.OntologyObject] |
| sync_raw | ApiResponse[ontologies_models.ListObjectsResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ListObjectsResponse] |
| async_ordinary | core.AsyncResourceIterator[ontologies_models.OntologyObject] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListObjectsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListObjectsResponse]] |

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
- [foundry_sdk.v1.ontologies.models.ListObjectsResponse](../../../../models/v1/ontologies/models/ListObjectsResponse.md)
- [foundry_sdk.v1.ontologies.models.ObjectRid](../../../../models/v1/ontologies/models/ObjectRid.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeApiName](../../../../models/v1/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.OntologyObject](../../../../models/v1/ontologies/models/OntologyObject.md)
- [foundry_sdk.v1.ontologies.models.OntologyRid](../../../../models/v1/ontologies/models/OntologyRid.md)
- [foundry_sdk.v1.ontologies.models.OrderBy](../../../../models/v1/ontologies/models/OrderBy.md)
- [foundry_sdk.v1.ontologies.models.PropertyApiName](../../../../models/v1/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v1.ontologies.models.PropertyValue](../../../../models/v1/ontologies/models/PropertyValue.md)
- [foundry_sdk.v1.ontologies.models.SelectedPropertyApiName](../../../../models/v1/ontologies/models/SelectedPropertyApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/OntologyObject.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Use the operation's filter model to combine property predicates, then validate names and types against the object type. [Local procedure](../../../../../ontology/queries.md).
- Page size is a request hint. Continue with the returned nextPageToken until absent; bound pages and reject a repeated token. [Local procedure](../../../../client-behavior.md).

[Part 1](list.md)
