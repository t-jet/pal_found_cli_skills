# v2.ontologies.OntologyObjectSet.aggregate


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Aggregates the ontology objects present in the `ObjectSet` from the provided object set definition.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.OntologyObjectSet.aggregate`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

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

[Part 1](aggregate.md) | [Part 2](aggregate-2.md)
