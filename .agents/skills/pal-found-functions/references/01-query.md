# Query, value type, and version id operations

This part documents the `query` (5), `value_type` (1), and `version_id` (1)
resource clients (7 operations). A query is a server-side function; executing
it computes a result.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/functions/scripts/pal_found_functions_cli.py`;
SDK `foundry_sdk/v2/functions/{query,value_type,version_id}.py` at pinned
commit `2da67907`. Reviewer architect (CODEREVIEW-049), 2026-10-03. QA
baseline TESTCASE-008.

## Operation records

### query.execute

- **Class**: execute (read, may consume compute). Runs a query.
- **Preconditions**: a query version you can execute.
- **Effect**: computes and returns the query result; consumes function
  compute.
- **Inputs**: positional `query_rid`; `--parameters` JSON; `--version`.
- **Success**: the query result.
- **Failure**: exit 1 invalid parameters; exit 5 timeout (do not assume
  completion).
- **Example**: `pal-found-functions query execute <QUERY_RID> --parameters '{"customerId":"c1"}'`.

### query.get

- **Class**: read. Returns a query definition by RID.
- **Preconditions**: can read the query.
- **Effect**: returns the query metadata.
- **Inputs**: positional `query_rid`.
- **Success**: the query record.
- **Failure**: exit 4 if missing.

### query.get_by_rid

- **Class**: read. Returns a query by RID (alias of `get`).
- **Preconditions**: can read the query.
- **Effect**: returns the query record.
- **Inputs**: positional `query_rid`.

### query.get_by_rid_batch

- **Class**: read. Returns several queries.
- **Preconditions**: can read each.
- **Effect**: returns a batch of query records.
- **Inputs**: positional JSON body list of RIDs.
- **Success**: list of queries.

### query.streaming_execute

- **Class**: execute (read, streaming). Runs a query and streams the result.
- **Preconditions**: a query you can execute.
- **Effect**: streams the result rows; zero exit means the stream ended.
- **Inputs**: positional `query_rid`; `--parameters`, stream options.
- **Success**: a stream of result rows.
- **Failure**: exit 5 timeout mid-stream.

### value_type.get

- **Class**: read. Returns a value type used by queries.
- **Preconditions**: can read the value type.
- **Effect**: returns the value type definition.
- **Inputs**: positional `value_type_rid`.
- **Success**: the value type.

### version_id.get

- **Class**: read. Returns version id metadata.
- **Preconditions**: can read the version.
- **Effect**: returns version id info for a function/query.
- **Inputs**: positional `version_id`.
- **Success**: the version metadata.

## Evidence and review

Reviewed against the installed `pal-found-functions` parser and pinned SDK
sources (commit `2da67907`). `query.execute`/`streaming_execute` compute and
consume compute (AC-D-013-09); they return results but a timeout does not prove
server completion. The rest are reads. No unsupported operation is documented
as callable.
