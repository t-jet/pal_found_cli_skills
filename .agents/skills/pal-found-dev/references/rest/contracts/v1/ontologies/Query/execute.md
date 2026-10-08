# v1.ontologies.Query.execute


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Executes a Query using the given parameters. Optional parameters do not need to be supplied.

## SDK invocation contract

```python
def execute(self, ontology_rid: ontologies_models.OntologyRid, query_api_name: ontologies_models.QueryApiName, *, parameters: typing.Dict[ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]], attribution: typing.Optional[core_models.Attribution]=None, trace_parent: typing.Optional[core_models.TraceParent]=None, trace_state: typing.Optional[core_models.TraceState]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ExecuteQueryResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology_rid | ontologies_models.OntologyRid | required | The unique Resource Identifier (RID) of the Ontology that contains the Query. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. |
| query_api_name | ontologies_models.QueryApiName | required | The API name of the Query to execute. |
| parameters | typing.Dict[ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]] | required | Value shape and constraints are in its referenced local type definition. |
| attribution | typing.Optional[core_models.Attribution] | None | The Attribution to be used when executing this request. |
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
'/v1/ontologies/{ontologyRid}/queries/{queryApiName}/execute'
```

**query_params**

```python
{}
```

**path_params**

```python
{'ontologyRid': ontology_rid, 'queryApiName': query_api_name}
```

**header_params**

```python
{'attribution': attribution, 'traceParent': trace_parent, 'traceState': trace_state, 'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.ExecuteQueryRequest(parameters=parameters)
```

**response_type**

```python
ontologies_models.ExecuteQueryResponse
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

Ordinary sync return: `ontologies_models.ExecuteQueryResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.ExecuteQueryResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ExecuteQueryResponse |
| sync_raw | ApiResponse[ontologies_models.ExecuteQueryResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ExecuteQueryResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.ExecuteQueryResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ExecuteQueryResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ExecuteQueryResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.models.Attribution](../../../../models/v1/core/models/Attribution.md)
- [foundry_sdk.v1.core.models.TraceParent](../../../../models/v1/core/models/TraceParent.md)
- [foundry_sdk.v1.core.models.TraceState](../../../../models/v1/core/models/TraceState.md)
- [foundry_sdk.v1.ontologies.models.DataValue](../../../../models/v1/ontologies/models/DataValue.md)
- [foundry_sdk.v1.ontologies.models.ExecuteQueryRequest](../../../../models/v1/ontologies/models/ExecuteQueryRequest.md)
- [foundry_sdk.v1.ontologies.models.ExecuteQueryResponse](../../../../models/v1/ontologies/models/ExecuteQueryResponse.md)
- [foundry_sdk.v1.ontologies.models.OntologyRid](../../../../models/v1/ontologies/models/OntologyRid.md)
- [foundry_sdk.v1.ontologies.models.ParameterId](../../../../models/v1/ontologies/models/ParameterId.md)
- [foundry_sdk.v1.ontologies.models.QueryApiName](../../../../models/v1/ontologies/models/QueryApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/Query.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](execute.md)
