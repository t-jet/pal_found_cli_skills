# SQL query operations

Dataset SQL supports SELECT queries in Spark SQL over Foundry datasets referenced by path or RID. Submission returns a query status and ID; results are Apache Arrow. Ontology SQL returns Arrow bytes synchronously. Examples require read access to the referenced data. See SDK `docs/v2/SqlQueries/SqlQuery.md` and [querying datasets with SQL](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets).

### sql_query.execute

Submit a dataset query. `--query` is required. `--fallback-branch-ids-json` gives an ordered list of branches to try when execution on the primary branch fails. For a dataset reference without an explicit branch, Foundry uses the first listed fallback branch that exists; without a list it uses the default branch (`master` in most enrollments). A reference with an explicit branch uses that branch. The `QueryStatus` response contains an ID and current state. Submission does not guarantee completion. Results default to a one-million-row limit. Invalid SQL, non-SELECT statements, or inaccessible datasets can fail.

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

Run SQL against Ontology data. This private-beta endpoint returns Apache Arrow bytes synchronously. It provides no query ID for `get-status` or `get-results`. The CLI saves bytes and prints download metadata. `--dry-run` validates without execution; `--row-limit` caps rows. `--parameters-json` accepts the SDK's named or positional typed parameters. An inaccessible object type or unavailable beta access fails.

**Example:**
```bash
pal-found-sql-queries query execute-ontology --query 'SELECT * FROM `ri.ontology.main.object-type.example`' --row-limit 10
```

Replace the sample object type RID with one visible to the caller.
