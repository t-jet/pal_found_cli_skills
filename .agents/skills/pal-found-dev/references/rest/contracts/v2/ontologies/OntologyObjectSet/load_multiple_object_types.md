# v2.ontologies.OntologyObjectSet.load_multiple_object_types


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Load the ontology objects present in the `ObjectSet` from the provided object set definition. The resulting
objects may be scoped to an object type, in which all the selected properties on the object type are returned, or scoped
to an interface, in which only the object type properties that implement the properties of any interfaces in its
scope are returned. For objects that are scoped to an interface in the result, a mapping from interface to
object implementation is returned in order to interpret the objects as the interfaces that they implement.

For Object Storage V1 backed objects, this endpoint returns a maximum of 10,000 objects. After 10,000 objects have been returned and if more objects
are available, attempting to load another page will result in an `ObjectsExceededLimit` error being returned. There is no limit on Object Storage V2 backed objects.

Note that null value properties will not be returned. In addition, property metadata (rid, apiName, and primaryKey)
will be prefixed with '$' instead of '__' as is the case in `loadObjects`.

Vector properties will not be returned unless included in the `select` parameter.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.OntologyObjectSet.load_multiple_object_types`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def load_multiple_object_types(self, ontology: ontologies_models.OntologyIdentifier, *, object_set: ontologies_models.ObjectSet, select: typing.List[ontologies_models.SelectedPropertyApiName], branch: typing.Optional[core_models.FoundryBranch]=None, exclude_rid: typing.Optional[bool]=None, execute_in_memory_only: typing.Optional[bool]=None, include_compute_usage: typing.Optional[core_models.IncludeComputeUsage]=None, load_property_securities: typing.Optional[bool]=None, order_by: typing.Optional[ontologies_models.SearchOrderByV2]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, reference_signing_options: typing.Optional[ontologies_models.ReferenceSigningOptions]=None, scenario_rid: typing.Optional[ontologies_models.OntologyScenarioRid]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, select_v2: typing.Optional[typing.List[ontologies_models.PropertyIdentifier]]=None, snapshot: typing.Optional[bool]=None, trace_parent: typing.Optional[core_models.TraceParent]=None, trace_state: typing.Optional[core_models.TraceState]=None, transaction_id: typing.Optional[ontologies_models.OntologyTransactionId]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_set | ontologies_models.ObjectSet | required | Value shape and constraints are in its referenced local type definition. |
| select | typing.List[ontologies_models.SelectedPropertyApiName] | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to load the object set for multiple object types. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. |
| exclude_rid | typing.Optional[bool] | None | A flag to exclude the retrieval of the `$rid` property. Setting this to true may improve performance of this endpoint for object types in OSV2. |
| execute_in_memory_only | typing.Optional[bool] | None | If true, the request fails with an error when it cannot be computed in-memory. Use this to opt into fast failure on requests that would otherwise require heavier computation. Defaults to false. |
| include_compute_usage | typing.Optional[core_models.IncludeComputeUsage] | None | Value shape and constraints are in its referenced local type definition. |
| load_property_securities | typing.Optional[bool] | None | A flag to load the securities for all properties. Setting this flag to true will return a list of securities in the `propertySecurities` field of the response. Returned objects will return all properties as Secured Property Values, which provide the property data as well an index into the `propertySecurities` list. This feature is experimental and not yet generally available. |
| order_by | typing.Optional[ontologies_models.SearchOrderByV2] | None | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | Value shape and constraints are in its referenced local type definition. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| reference_signing_options | typing.Optional[ontologies_models.ReferenceSigningOptions] | None | Value shape and constraints are in its referenced local type definition. |
| scenario_rid | typing.Optional[ontologies_models.OntologyScenarioRid] | None | The resource identifier of an ontology scenario to load the object set from. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package rid of the generated SDK. |
| sdk_version | typing.Optional[ontologies_models.SdkVersion] | None | The package version of the generated SDK. |
| select_v2 | typing.Optional[typing.List[ontologies_models.PropertyIdentifier]] | None | The identifiers of the properties to include in the response. Only selectV2 or select should be populated, but not both. |
| snapshot | typing.Optional[bool] | None | A flag to use snapshot consistency when paging. Setting this to true will give you a consistent view from before you start paging through the results, ensuring you do not get duplicate or missing items. Setting this to false will let new results enter as you page, but you may encounter duplicate or missing items. This defaults to false if not specified, which means you will always get the latest results. |
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
'/v2/ontologies/{ontology}/objectSets/loadObjectsMultipleObjectTypes'
```

**query_params**

```python
{'branch': branch, 'executeInMemoryOnly': execute_in_memory_only, 'preview': preview, 'scenarioRid': scenario_rid, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version, 'transactionId': transaction_id}
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
ontologies_models.LoadObjectSetV2MultipleObjectTypesRequest(object_set=object_set, order_by=order_by, select=select, select_v2=select_v2, page_token=page_token, page_size=page_size, exclude_rid=exclude_rid, load_property_securities=load_property_securities, snapshot=snapshot, include_compute_usage=include_compute_usage, reference_signing_options=reference_signing_options)
```

**response_type**

```python
ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse
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

Ordinary sync return: `ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse |
| sync_raw | ApiResponse[ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.LoadObjectSetV2MultipleObjectTypesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

[Part 1](load_multiple_object_types.md) | [Part 2](load_multiple_object_types-2.md)
