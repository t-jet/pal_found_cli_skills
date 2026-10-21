# v2.sql_queries.SqlQuery.execute_ontology


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Executes a SQL query against the Ontology. Results are returned synchronously in
[Apache Arrow](../../../../v2/sql_queries/index.md) format.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.sql_queries.SqlQuery.execute_ontology`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def execute_ontology(self, *, query: str, branch: typing.Optional[core_models.FoundryBranch]=None, dry_run: typing.Optional[bool]=None, ontology_identifier: typing.Optional[ontologies_models.OntologyIdentifier]=None, parameters: typing.Optional[sql_queries_models.Parameters]=None, preview: typing.Optional[core_models.PreviewMode]=None, row_limit: typing.Optional[int]=None, scenario_rid: typing.Optional[sql_queries_models.ScenarioRid]=None, table_providers: typing.Optional[typing.Dict[sql_queries_models.TableName, ontologies_models.ObjectSet]]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> bytes: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| query | str | required | The SQL query to execute. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to execute the query against. If not specified, the default (main) branch is used. |
| dry_run | typing.Optional[bool] | None | If true, parse and validate the query without executing it. Defaults to false. |
| ontology_identifier | typing.Optional[ontologies_models.OntologyIdentifier] | None | Either an ontology RID or an ontology API name. |
| parameters | typing.Optional[sql_queries_models.Parameters] | None | Parameters for the SQL query. Can be either unnamed positional parameters or a named parameter mapping. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| row_limit | typing.Optional[int] | None | Maximum number of rows to return. |
| scenario_rid | typing.Optional[sql_queries_models.ScenarioRid] | None | The scenario to evaluate the query against. If not specified, no scenario is applied. |
| table_providers | typing.Optional[typing.Dict[sql_queries_models.TableName, ontologies_models.ObjectSet]] | None | Map of table providers, requires ontologyIdentifier to be provided otherwise it will throw. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ExecuteOntologySqlQueryPermissionDenied | Could not executeOntology the SqlQuery. |
| OntologyObjectTypeNotFound | The ontology query referenced an object type RID that does not exist or is not visible to the requesting user. Verify the RID (e.g. via list-object-types or get-object-type-details) and retry. |
| OntologyQueryFailed | The Ontology query failed. |
| OntologyQueryInvalidObjectBackend | The ontology query references object types or link types indexed in Object Storage V1, which is incompatible with Ontology SQL. Migrate the entities to Object Storage V2 or remove them from the query. |
| OntologyQueryNestedObjectSetTooLarge | The query references too many objects across joins, link lookups, or sub-queries. Narrow the scope (add filters, reduce joins, restrict object types) and retry. The actual and maximum object counts are returned as parameters. |
| OntologyQueryStringColumnTooLong | A string column in the query result contains a value larger than the platform's per-cell size limit. Exclude or filter the column, or scope the query to skip the oversized rows. |
| QueryParseError | The query cannot be parsed. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/sqlQueries/executeOntology'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/octet-stream'}
```

**body**

```python
sql_queries_models.ExecuteOntologySqlQueryRequest(query=query, parameters=parameters, row_limit=row_limit, dry_run=dry_run, branch=branch, scenario_rid=scenario_rid, ontology_identifier=ontology_identifier, table_providers=table_providers)
```

**response_type**

```python
bytes
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ExecuteOntologySqlQueryPermissionDenied': sql_queries_errors.ExecuteOntologySqlQueryPermissionDenied, 'OntologyObjectTypeNotFound': sql_queries_errors.OntologyObjectTypeNotFound, 'OntologyQueryFailed': sql_queries_errors.OntologyQueryFailed, 'OntologyQueryInvalidObjectBackend': sql_queries_errors.OntologyQueryInvalidObjectBackend, 'OntologyQueryNestedObjectSetTooLarge': sql_queries_errors.OntologyQueryNestedObjectSetTooLarge, 'OntologyQueryStringColumnTooLong': sql_queries_errors.OntologyQueryStringColumnTooLong, 'QueryParseError': sql_queries_errors.QueryParseError}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `bytes`. Ordinary async return: `typing.Awaitable[bytes]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | bytes |
| sync_raw | ApiResponse[bytes] |
| sync_streaming | StreamingContextManager[bytes] |
| async_ordinary | typing.Awaitable[bytes] |
| async_raw | Awaitable[AsyncApiResponse[bytes]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[bytes]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

[Part 1](execute_ontology.md) | [Part 2](execute_ontology-2.md)
