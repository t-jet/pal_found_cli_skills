# v2.sql_queries.SqlQuery.execute


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Executes a new query. Only the user that invoked the query can operate on the query. The size of query
results are limited by default to 1 million rows. Contact your Palantir representative to discuss limit
increases.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.sql_queries.SqlQuery.execute`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def execute(self, *, query: str, fallback_branch_ids: typing.Optional[typing.List[core_models.BranchName]]=None, serialization_format: typing.Optional[sql_queries_models.SerializationFormat]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> sql_queries_models.QueryStatus: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| query | str | required | The SQL query to execute. Queries should conform to the [Spark SQL dialect](../../../../../pipelines/sql.md). This supports SELECT queries only. Datasets can be referenced in SQL queries by path or by RID. See the [documentation](../../../../../pipelines/sql.md) for more details. |
| fallback_branch_ids | typing.Optional[typing.List[core_models.BranchName]] | None | The list of branch ids to use as fallbacks if the query fails to execute on the primary branch. If a is not explicitly provided in the SQL query, the resource will be queried on the first fallback branch provided that exists. If no fallback branches are provided the default branch is used. This is `master` for most enrollments. |
| serialization_format | typing.Optional[sql_queries_models.SerializationFormat] | None | The format used to serialize query results. If not specified, defaults to `ARROW`. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ColumnTypesNotSupported | The query result contains column types that are not supported by the requested serialization format. |
| ExecuteSqlQueryPermissionDenied | Could not execute the SqlQuery. |
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
'/v2/sqlQueries/execute'
```

**query_params**

```python
{}
```

**path_params**

```python
{}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
sql_queries_models.ExecuteSqlQueryRequest(query=query, fallback_branch_ids=fallback_branch_ids, serialization_format=serialization_format)
```

**response_type**

```python
sql_queries_models.QueryStatus
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ColumnTypesNotSupported': sql_queries_errors.ColumnTypesNotSupported, 'ExecuteSqlQueryPermissionDenied': sql_queries_errors.ExecuteSqlQueryPermissionDenied, 'QueryCanceled': sql_queries_errors.QueryCanceled, 'QueryFailed': sql_queries_errors.QueryFailed, 'QueryParseError': sql_queries_errors.QueryParseError, 'QueryPermissionDenied': sql_queries_errors.QueryPermissionDenied, 'QueryRunning': sql_queries_errors.QueryRunning, 'ReadQueryInputsPermissionDenied': sql_queries_errors.ReadQueryInputsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `sql_queries_models.QueryStatus`. Ordinary async return: `typing.Awaitable[sql_queries_models.QueryStatus]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | sql_queries_models.QueryStatus |
| sync_raw | ApiResponse[sql_queries_models.QueryStatus] |
| sync_streaming | StreamingContextManager[sql_queries_models.QueryStatus] |
| async_ordinary | typing.Awaitable[sql_queries_models.QueryStatus] |
| async_raw | Awaitable[AsyncApiResponse[sql_queries_models.QueryStatus]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[sql_queries_models.QueryStatus]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.sql_queries.errors.ColumnTypesNotSupported](../../../../models/v2/sql_queries/errors/ColumnTypesNotSupported.md)
- [foundry_sdk.v2.sql_queries.errors.ColumnTypesNotSupportedParameters](../../../../models/v2/sql_queries/errors/ColumnTypesNotSupportedParameters.md)
- [foundry_sdk.v2.sql_queries.errors.ExecuteSqlQueryPermissionDenied](../../../../models/v2/sql_queries/errors/ExecuteSqlQueryPermissionDenied.md)
- [foundry_sdk.v2.sql_queries.errors.ExecuteSqlQueryPermissionDeniedParameters](../../../../models/v2/sql_queries/errors/ExecuteSqlQueryPermissionDeniedParameters.md)
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
- [foundry_sdk.v2.sql_queries.models.CanceledQueryStatus](../../../../models/v2/sql_queries/models/CanceledQueryStatus.md)
- [foundry_sdk.v2.sql_queries.models.ExecuteSqlQueryRequest](../../../../models/v2/sql_queries/models/ExecuteSqlQueryRequest.md)
- [foundry_sdk.v2.sql_queries.models.FailedQueryStatus](../../../../models/v2/sql_queries/models/FailedQueryStatus.md)
- [foundry_sdk.v2.sql_queries.models.QueryStatus](../../../../models/v2/sql_queries/models/QueryStatus.md)
- [foundry_sdk.v2.sql_queries.models.RunningQueryStatus](../../../../models/v2/sql_queries/models/RunningQueryStatus.md)
- [foundry_sdk.v2.sql_queries.models.SerializationFormat](../../../../models/v2/sql_queries/models/SerializationFormat.md)
- [foundry_sdk.v2.sql_queries.models.SqlQueryId](../../../../models/v2/sql_queries/models/SqlQueryId.md)
- [foundry_sdk.v2.sql_queries.models.SucceededQueryStatus](../../../../models/v2/sql_queries/models/SucceededQueryStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/sql_queries/SqlQuery.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- This query uses Spark SQL SELECT syntax. Bind dataset references using the operation's declared form and validate schema before execution. [Local procedure](../../../../../pipelines/sql.md).

[Part 1](execute.md)
