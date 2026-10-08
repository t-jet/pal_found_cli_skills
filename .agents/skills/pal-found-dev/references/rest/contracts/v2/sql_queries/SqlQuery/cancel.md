# v2.sql_queries.SqlQuery.cancel


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Cancels a query. If the query is no longer running this is effectively a no-op.

## SDK invocation contract

```python
def cancel(self, sql_query_id: sql_queries_models.SqlQueryId, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> None: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| sql_query_id | sql_queries_models.SqlQueryId | required | The unique identifier for a query. Note that query IDs are not URL-safe and must be URL-encoded when used in API endpoints. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CancelSqlQueryPermissionDenied | Could not cancel the SqlQuery. |
| QueryCanceled | The query was canceled. |
| QueryFailed | The query failed. |
| QueryParseError | The query cannot be parsed. |
| QueryPermissionDenied | The provided token does not have permission to access the given query. |
| QueryRunning | The query is running. |
| ReadQueryInputsPermissionDenied | The provided token does not have permission to access the inputs to the query. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/sqlQueries/{sqlQueryId}/cancel'
```

**query_params**

```python
{}
```

**path_params**

```python
{'sqlQueryId': sql_query_id}
```

**header_params**

```python
{}
```

**body**

```python
None
```

**response_type**

```python
None
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CancelSqlQueryPermissionDenied': sql_queries_errors.CancelSqlQueryPermissionDenied, 'QueryCanceled': sql_queries_errors.QueryCanceled, 'QueryFailed': sql_queries_errors.QueryFailed, 'QueryParseError': sql_queries_errors.QueryParseError, 'QueryPermissionDenied': sql_queries_errors.QueryPermissionDenied, 'QueryRunning': sql_queries_errors.QueryRunning, 'ReadQueryInputsPermissionDenied': sql_queries_errors.ReadQueryInputsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `None`. Ordinary async return: `typing.Awaitable[None]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | None |
| sync_raw | ApiResponse[None] |
| sync_streaming | Not exposed |
| async_ordinary | typing.Awaitable[None] |
| async_raw | Awaitable[AsyncApiResponse[None]] |
| async_streaming | Not exposed |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.sql_queries.errors.CancelSqlQueryPermissionDenied](../../../../models/v2/sql_queries/errors/CancelSqlQueryPermissionDenied.md)
- [foundry_sdk.v2.sql_queries.errors.CancelSqlQueryPermissionDeniedParameters](../../../../models/v2/sql_queries/errors/CancelSqlQueryPermissionDeniedParameters.md)
- [foundry_sdk.v2.sql_queries.errors.QueryCanceled](../../../../models/v2/sql_queries/errors/QueryCanceled.md)
- [foundry_sdk.v2.sql_queries.errors.QueryCanceledParameters](../../../../models/v2/sql_queries/errors/QueryCanceledParameters.md)
- [foundry_sdk.v2.sql_queries.errors.QueryFailed](../../../../models/v2/sql_queries/errors/QueryFailed.md)
- [foundry_sdk.v2.sql_queries.errors.QueryFailedParameters](../../../../models/v2/sql_queries/errors/QueryFailedParameters.md)
- [foundry_sdk.v2.sql_queries.errors.QueryParseError](../../../../models/v2/sql_queries/errors/QueryParseError.md)
- [foundry_sdk.v2.sql_queries.errors.QueryParseErrorParameters](../../../../models/v2/sql_queries/errors/QueryParseErrorParameters.md)
- [foundry_sdk.v2.sql_queries.errors.QueryPermissionDenied](../../../../models/v2/sql_queries/errors/QueryPermissionDenied.md)
- [foundry_sdk.v2.sql_queries.errors.QueryPermissionDeniedParameters](../../../../models/v2/sql_queries/errors/QueryPermissionDeniedParameters.md)
- [foundry_sdk.v2.sql_queries.errors.QueryRunning](../../../../models/v2/sql_queries/errors/QueryRunning.md)
- [foundry_sdk.v2.sql_queries.errors.QueryRunningParameters](../../../../models/v2/sql_queries/errors/QueryRunningParameters.md)
- [foundry_sdk.v2.sql_queries.errors.ReadQueryInputsPermissionDenied](../../../../models/v2/sql_queries/errors/ReadQueryInputsPermissionDenied.md)
- [foundry_sdk.v2.sql_queries.errors.ReadQueryInputsPermissionDeniedParameters](../../../../models/v2/sql_queries/errors/ReadQueryInputsPermissionDeniedParameters.md)
- [foundry_sdk.v2.sql_queries.models.SqlQueryId](../../../../models/v2/sql_queries/models/SqlQueryId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/sql_queries/SqlQuery.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](cancel.md)
