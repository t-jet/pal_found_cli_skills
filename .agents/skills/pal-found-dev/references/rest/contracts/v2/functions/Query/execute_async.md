# v2.functions.Query.execute_async


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Submits a Query for asynchronous execution. Returns either an execution ID
for polling, or the complete result if execution finished immediately.

Use the Execution resource's getResult endpoint to poll for the
result of a submitted execution.

## SDK invocation contract

```python
def execute_async(self, query_api_name: functions_models.QueryApiName, *, parameters: typing.Dict[functions_models.ParameterId, typing.Optional[functions_models.DataValue]], attribution: typing.Optional[core_models.Attribution]=None, branch: typing.Optional[core_models.FoundryBranch]=None, ontology: typing.Optional[ontologies_models.OntologyIdentifier]=None, preview: typing.Optional[core_models.PreviewMode]=None, trace_parent: typing.Optional[core_models.TraceParent]=None, trace_state: typing.Optional[core_models.TraceState]=None, transaction_id: typing.Optional[functions_models.TransactionId]=None, version: typing.Optional[functions_models.FunctionVersion]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> functions_models.ExecuteQueryAsyncResponse: ...
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
| ExecuteAsyncQueryPermissionDenied | Could not executeAsync the Query. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/functions/queries/{queryApiName}/executeAsync'
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
{'attribution': attribution, 'traceParent': trace_parent, 'traceState': trace_state, 'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
functions_models.ExecuteAsyncQueryRequest(ontology=ontology, parameters=parameters, version=version, branch=branch)
```

**response_type**

```python
functions_models.ExecuteQueryAsyncResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ExecuteAsyncQueryPermissionDenied': functions_errors.ExecuteAsyncQueryPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `functions_models.ExecuteQueryAsyncResponse`. Ordinary async return: `typing.Awaitable[functions_models.ExecuteQueryAsyncResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | functions_models.ExecuteQueryAsyncResponse |
| sync_raw | ApiResponse[functions_models.ExecuteQueryAsyncResponse] |
| sync_streaming | StreamingContextManager[functions_models.ExecuteQueryAsyncResponse] |
| async_ordinary | typing.Awaitable[functions_models.ExecuteQueryAsyncResponse] |
| async_raw | Awaitable[AsyncApiResponse[functions_models.ExecuteQueryAsyncResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[functions_models.ExecuteQueryAsyncResponse]] |

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
- [foundry_sdk.v2.functions.errors.ExecuteAsyncQueryPermissionDenied](../../../../models/v2/functions/errors/ExecuteAsyncQueryPermissionDenied.md)
- [foundry_sdk.v2.functions.errors.ExecuteAsyncQueryPermissionDeniedParameters](../../../../models/v2/functions/errors/ExecuteAsyncQueryPermissionDeniedParameters.md)
- [foundry_sdk.v2.functions.models.DataValue](../../../../models/v2/functions/models/DataValue.md)
- [foundry_sdk.v2.functions.models.ExecuteAsyncQueryRequest](../../../../models/v2/functions/models/ExecuteAsyncQueryRequest.md)
- [foundry_sdk.v2.functions.models.ExecuteQueryAsyncResponse](../../../../models/v2/functions/models/ExecuteQueryAsyncResponse.md)
- [foundry_sdk.v2.functions.models.ExecutionCompleted](../../../../models/v2/functions/models/ExecutionCompleted.md)
- [foundry_sdk.v2.functions.models.ExecutionId](../../../../models/v2/functions/models/ExecutionId.md)
- [foundry_sdk.v2.functions.models.ExecutionSubmitted](../../../../models/v2/functions/models/ExecutionSubmitted.md)
- [foundry_sdk.v2.functions.models.FunctionVersion](../../../../models/v2/functions/models/FunctionVersion.md)
- [foundry_sdk.v2.functions.models.ParameterId](../../../../models/v2/functions/models/ParameterId.md)
- [foundry_sdk.v2.functions.models.QueryApiName](../../../../models/v2/functions/models/QueryApiName.md)
- [foundry_sdk.v2.functions.models.TransactionId](../../../../models/v2/functions/models/TransactionId.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/functions/Query.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](execute_async.md)
