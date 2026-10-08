# v2.functions.Execution.cancel


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Cancel a running async query execution. This endpoint is idempotent.

## SDK invocation contract

```python
def cancel(self, execution_id: functions_models.ExecutionId, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> functions_models.CancelExecutionResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| execution_id | functions_models.ExecutionId | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CancelExecutionPermissionDenied | Could not cancel the Execution. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/functions/executions/{executionId}/cancel'
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
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
functions_models.CancelExecutionResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CancelExecutionPermissionDenied': functions_errors.CancelExecutionPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `functions_models.CancelExecutionResponse`. Ordinary async return: `typing.Awaitable[functions_models.CancelExecutionResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | functions_models.CancelExecutionResponse |
| sync_raw | ApiResponse[functions_models.CancelExecutionResponse] |
| sync_streaming | StreamingContextManager[functions_models.CancelExecutionResponse] |
| async_ordinary | typing.Awaitable[functions_models.CancelExecutionResponse] |
| async_raw | Awaitable[AsyncApiResponse[functions_models.CancelExecutionResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[functions_models.CancelExecutionResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.functions.errors.CancelExecutionPermissionDenied](../../../../models/v2/functions/errors/CancelExecutionPermissionDenied.md)
- [foundry_sdk.v2.functions.errors.CancelExecutionPermissionDeniedParameters](../../../../models/v2/functions/errors/CancelExecutionPermissionDeniedParameters.md)
- [foundry_sdk.v2.functions.models.CancelExecutionResponse](../../../../models/v2/functions/models/CancelExecutionResponse.md)
- [foundry_sdk.v2.functions.models.ExecutionId](../../../../models/v2/functions/models/ExecutionId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/functions/Execution.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](cancel.md)
