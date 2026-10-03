# SQL query lifecycle

This part documents the `sql_query` resource client (5 operations, CLI
subcommand `query`). A query goes: `execute` (or `execute_ontology`), poll
`get_status`, download `get_results`, and `cancel` if needed.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/sql_queries/scripts/pal_found_sql_queries_cli.py`;
SDK `foundry_sdk/v2/sql_queries/sql_query.py` at pinned commit `2da67907`.
Reviewer architect (CODEREVIEW-051), 2026-10-03. QA baseline TESTCASE-015.

## Operation records

### sql_query.cancel

- **Class**: change (write). Cancels an in-progress query.
- **Preconditions**: a running query you can cancel.
- **Effect**: cancels the query if it is running.
- **Inputs**: positional `query_id`.
- **Success**: returns the canceled query.
- **Failure**: exit 1 if query already finished/not cancellable.

### sql_query.execute

- **Class**: execute (write, async, may start compute). Runs a SQL query.
- **Preconditions**: a valid query string you can run.
- **Effect**: starts the query; acceptance is not proof it finished.
- **Inputs**: `--query-string`; `--parameters-json`;
  `--fallback-branch-ids-json`.
- **Success**: returns a query id; poll `get_status` for completion.
- **Failure**: exit 5 on timeout; query may still be running.
- **Example**: `pal-found-sql-queries query execute --query-string "SELECT * FROM \`dataset\`"`.

### sql_query.execute_ontology

- **Class**: execute (write, async). Runs a query scoped to an ontology.
- **Preconditions**: an ontology you can query.
- **Effect**: starts an ontology-scoped query; may directly return results.
- **Inputs**: ontology context + query string.
- **Success**: a query id/results; check status.

### sql_query.get_results

- **Class**: read (Arrow download). Downloads a finished query's results.
- **Preconditions**: the query reached a finished status.
- **Effect**: downloads Arrow result bytes via the binary handler;
  `--output` destination. This operation has no `--format` rendering of the
  binary itself.
- **Inputs**: positional `query_id`; `--output`.
- **Success**: the saved Arrow file (bounded download).
- **Failure**: exit 4 if query not finished/missing; exit 8 if read blocked.
- **Example**: `pal-found-sql-queries query get-results <QUERY_ID> --output out.arrow`.

### sql_query.get_status

- **Class**: read (async status). Returns a query's execution status.
- **Preconditions**: can read the query.
- **Effect**: returns the query status (running/succeeded/failed).
- **Inputs**: positional `query_id`.
- **Success**: the status record.
- **Failure**: exit 4 if query missing.

## Evidence and review

Reviewed against the installed `pal-found-sql-queries` parser and pinned SDK
sources (commit `2da67907`). `execute`/`execute_ontology` start compute; a zero
exit means the query was accepted, not finished. Use `get_status`, then
`get_results` only after success (AC-D-013-05). No unsupported operation is
documented as callable.
