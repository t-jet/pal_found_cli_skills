# v2.functions.Query.streaming_execute_events


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Executes a Query and returns results as a Server-Sent Events (`text/event-stream`) stream.
By default, this executes the latest version of the query. The latest version is the one
that was most recently published, which may be a pre-release version.

This endpoint supports all Query functions. Each SSE event's `data` field is a JSON-encoded
`StreamingExecuteQueryResponse` – either a data batch (`type: data`) carrying one or more
result values, or an error (`type: error`) emitted before stream termination if execution
fails. Non-streaming functions emit a single data event containing the entire result;
streaming functions emit a data event per batch as results become available.

Per the Server-Sent Events specification, each event is terminated by a blank line:

```
data: {"type":"data","value":[{"productId":"SKU-001","price":29.99}]}

data: {"type":"error","errorCode":"INVALID_ARGUMENT","errorName":"QueryRuntimeError","errorInstanceId":"3f8a9c7b-2e4d-4a1f-9b8c-7d6e5f4a3b2c","errorDescription":"Division by zero","parameters":{}}

```

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.functions.Query.streaming_execute_events`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def streaming_execute_events(self, query_api_name: functions_models.QueryApiName, *, parameters: typing.Dict[functions_models.ParameterId, typing.Optional[functions_models.DataValue]], attribution: typing.Optional[core_models.Attribution]=None, branch: typing.Optional[core_models.FoundryBranch]=None, ontology: typing.Optional[ontologies_models.OntologyIdentifier]=None, preview: typing.Optional[core_models.PreviewMode]=None, trace_parent: typing.Optional[core_models.TraceParent]=None, trace_state: typing.Optional[core_models.TraceState]=None, transaction_id: typing.Optional[functions_models.TransactionId]=None, version: typing.Optional[functions_models.FunctionVersion]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.SseContextManager[functions_models.StreamingExecuteQueryResponse]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| query_api_name | functions_models.QueryApiName | required | Value shape and constraints are in its referenced local type definition. |
| parameters | typing.Dict[functions_models.ParameterId, typing.Optional[functions_models.DataValue]] | required | Value shape and constraints are in its referenced local type definition. |
| attribution | typing.Optional[core_models.Attribution] | None | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to execute the query from. If not specified, the default branch is used. When provided without `version`, the latest version on this branch is used. When provided with `version`, the specified version must exist on the branch. |
| ontology | typing.Optional[ontologies_models.OntologyIdentifier] | None | Optional ontology identifier (RID or API name). When provided, executes an ontology-scoped function. When omitted, executes a global function. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| trace_parent | typing.Optional[core_models.TraceParent] | None | Value shape and constraints are in its referenced local type definition. |
| trace_state | typing.Optional[core_models.TraceState] | None | Value shape and constraints are in its referenced local type definition. |
| transaction_id | typing.Optional[functions_models.TransactionId] | None | The ID of a transaction to read from. Transactions are an experimental feature and not all workflows may be supported. |
| version | typing.Optional[functions_models.FunctionVersion] | None | The version of the query to execute. When used with `branch`, the specified version must exist on the branch. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| StreamingExecuteEventsQueryPermissionDenied | Could not streamingExecuteEvents the Query. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/functions/queries/{queryApiName}/streamingExecuteEvents'
```

**query_params**

```python
{'preview': preview, 'transactionId': transaction_id}
```

**path_params**

```python
{'queryApiName': query_api_name}
```

**header_params**

```python
{'attribution': attribution, 'traceParent': trace_parent, 'traceState': trace_state, 'Content-Type': 'application/json', 'Accept': 'text/event-stream'}
```

**body**

```python
functions_models.StreamingExecuteEventsQueryRequest(ontology=ontology, parameters=parameters, version=version, branch=branch)
```

**response_type**

```python
functions_models.StreamingExecuteQueryResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'StreamingExecuteEventsQueryPermissionDenied': functions_errors.StreamingExecuteEventsQueryPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'SSE')
```

## Response modes

Ordinary sync return: `core.SseContextManager[functions_models.StreamingExecuteQueryResponse]`. Ordinary async return: `core.AsyncSseContextManager[functions_models.StreamingExecuteQueryResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.SseContextManager[functions_models.StreamingExecuteQueryResponse] |
| sync_raw | ApiResponse[functions_models.StreamingExecuteQueryResponse] |
| sync_streaming | SseContextManager[functions_models.StreamingExecuteQueryResponse] |
| async_ordinary | core.AsyncSseContextManager[functions_models.StreamingExecuteQueryResponse] |
| async_raw | Awaitable[AsyncApiResponse[functions_models.StreamingExecuteQueryResponse]] |
| async_streaming | AsyncSseContextManager[functions_models.StreamingExecuteQueryResponse] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.Attribution](../../../../models/v2/core/models/Attribution.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.TraceParent](../../../../models/v2/core/models/TraceParent.md)
- [foundry_sdk.v2.core.models.TraceState](../../../../models/v2/core/models/TraceState.md)
- [foundry_sdk.v2.functions.errors.StreamingExecuteEventsQueryPermissionDenied](../../../../models/v2/functions/errors/StreamingExecuteEventsQueryPermissionDenied.md)
- [foundry_sdk.v2.functions.errors.StreamingExecuteEventsQueryPermissionDeniedParameters](../../../../models/v2/functions/errors/StreamingExecuteEventsQueryPermissionDeniedParameters.md)
- [foundry_sdk.v2.functions.models.DataValue](../../../../models/v2/functions/models/DataValue.md)
- [foundry_sdk.v2.functions.models.FunctionVersion](../../../../models/v2/functions/models/FunctionVersion.md)
- [foundry_sdk.v2.functions.models.ParameterId](../../../../models/v2/functions/models/ParameterId.md)
- [foundry_sdk.v2.functions.models.QueryApiName](../../../../models/v2/functions/models/QueryApiName.md)
- [foundry_sdk.v2.functions.models.StreamingExecuteEventsQueryRequest](../../../../models/v2/functions/models/StreamingExecuteEventsQueryRequest.md)
- [foundry_sdk.v2.functions.models.StreamingExecuteQueryResponse](../../../../models/v2/functions/models/StreamingExecuteQueryResponse.md)
- [foundry_sdk.v2.functions.models.StreamingQueryData](../../../../models/v2/functions/models/StreamingQueryData.md)
- [foundry_sdk.v2.functions.models.StreamingQueryError](../../../../models/v2/functions/models/StreamingQueryError.md)
- [foundry_sdk.v2.functions.models.TransactionId](../../../../models/v2/functions/models/TransactionId.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/functions/Query.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](streaming_execute_events.md)
