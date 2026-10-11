# v2.functions.Execution.get_result


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Poll for the result of an async query execution.

Returns a discriminated union:
- running: execution is still in progress.
- succeeded: execution completed successfully with a return value.

If the execution failed, a service error is thrown.

Use the timeout parameter for long-polling: the server holds the
connection open for up to the specified number of seconds. If the
execution completes within that window, the result is returned
immediately. Otherwise, the running variant is returned.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.functions.Execution.get_result`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_result(self, execution_id: functions_models.ExecutionId, *, preview: typing.Optional[core_models.PreviewMode]=None, timeout: typing.Optional[int]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> functions_models.GetExecutionResultResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| execution_id | functions_models.ExecutionId | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| timeout | typing.Optional[int] | None | Maximum time in seconds to hold the connection open while waiting for execution to complete. Default: 0 (immediate status check). Values above 280 are clamped to 280. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetResultExecutionPermissionDenied | Could not getResult the Execution. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/functions/executions/{executionId}/getResult'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'executionId': execution_id}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
functions_models.GetResultExecutionRequest(timeout=timeout)
```

**response_type**

```python
functions_models.GetExecutionResultResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetResultExecutionPermissionDenied': functions_errors.GetResultExecutionPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `functions_models.GetExecutionResultResponse`. Ordinary async return: `typing.Awaitable[functions_models.GetExecutionResultResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | functions_models.GetExecutionResultResponse |
| sync_raw | ApiResponse[functions_models.GetExecutionResultResponse] |
| sync_streaming | StreamingContextManager[functions_models.GetExecutionResultResponse] |
| async_ordinary | typing.Awaitable[functions_models.GetExecutionResultResponse] |
| async_raw | Awaitable[AsyncApiResponse[functions_models.GetExecutionResultResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[functions_models.GetExecutionResultResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.functions.errors.GetResultExecutionPermissionDenied](../../../../models/v2/functions/errors/GetResultExecutionPermissionDenied.md)
- [foundry_sdk.v2.functions.errors.GetResultExecutionPermissionDeniedParameters](../../../../models/v2/functions/errors/GetResultExecutionPermissionDeniedParameters.md)
- [foundry_sdk.v2.functions.models.DataValue](../../../../models/v2/functions/models/DataValue.md)
- [foundry_sdk.v2.functions.models.ExecutionId](../../../../models/v2/functions/models/ExecutionId.md)
- [foundry_sdk.v2.functions.models.GetExecutionResultResponse](../../../../models/v2/functions/models/GetExecutionResultResponse.md)
- [foundry_sdk.v2.functions.models.GetResultExecutionRequest](../../../../models/v2/functions/models/GetResultExecutionRequest.md)
- [foundry_sdk.v2.functions.models.RunningExecution](../../../../models/v2/functions/models/RunningExecution.md)
- [foundry_sdk.v2.functions.models.SucceededExecution](../../../../models/v2/functions/models/SucceededExecution.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/functions/Execution.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_result.md)
