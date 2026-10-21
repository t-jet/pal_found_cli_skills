# SQL query operations

Dataset SQL reads Foundry datasets with Spark SQL `SELECT`. Name a dataset by its path or RID and use backticks around a path, as in the example below. The caller needs read access to every referenced dataset. This query interface reads data; it does not create a transform or change a dataset. A submitted query returns an ID and status, then runs asynchronously. Keep the ID, check status, and retrieve Apache Arrow results only after success. A client timeout during polling does not cancel server execution. Ontology SQL is a separate private-beta operation that returns Arrow bytes synchronously and has no dataset query ID.

### sql_query.execute

Submit a dataset query. `--query` is required. `--fallback-branch-ids-json` controls branch resolution for dataset references without an explicit branch: Foundry uses the first listed branch that exists, or the default branch when no list is supplied. A reference with an explicit branch uses that branch. The `QueryStatus` response contains an ID and current state. Submission does not guarantee completion. Results default to a one-million-row limit. Invalid SQL, non-SELECT statements, or inaccessible datasets can fail.

**Example:**
```bash
pal-found-sql-queries query execute --query 'SELECT * FROM `/Operations/Orders` LIMIT 10' --fallback-branch-ids-json '["master"]'
```

Only the invoking user can operate on the query later. Preserve its returned ID.

### sql_query.get_status

Read the current state of a submitted dataset query. The response distinguishes running, succeeded, failed, and canceled states without changing the query. The ID comes from `execute`; an unknown query or one owned by another user cannot be inspected.

**Example:** `pal-found-sql-queries query get-status '<SQL_QUERY_ID>'`

### sql_query.get_results

Retrieve Arrow results by query ID. The endpoint uses long polling; a request can time out after one minute while execution continues. Retry the read or check status. The CLI saves bounded binary content in its configured download directory and prints file metadata. `--output` selects the filename there. It does not print Arrow bytes to stdout.

**Example:** `pal-found-sql-queries query get-results '<SQL_QUERY_ID>' --output orders.arrow`

Call after success. Failed, canceled, unknown, or inaccessible queries have no usable result. A client timeout alone does not establish server failure.

### sql_query.cancel

Request cancellation by query ID. Cancellation of a query that has stopped is a no-op. The SDK returns no resource body (HTTP 204). Check status afterward if you need the final state.

**Example:** `pal-found-sql-queries query cancel '<SQL_QUERY_ID>'`

### sql_query.execute_ontology

Run SQL against Ontology data. This Public Beta endpoint returns Apache Arrow bytes synchronously. It provides no query ID for `get-status` or `get-results`. The CLI saves bytes and prints download metadata. `--dry-run` validates without execution; `--row-limit` caps rows. `--parameters-json` accepts the SDK's named or positional typed parameters. An inaccessible object type or unavailable beta access fails.

**Example:**
```bash
pal-found-sql-queries query execute-ontology --query 'SELECT * FROM `ri.ontology.main.object-type.example`' --row-limit 10
```

Replace the sample object type RID with one visible to the caller.

Optional source: [Foundry dataset SQL and identifier syntax](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets).
