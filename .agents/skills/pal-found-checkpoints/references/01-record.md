# Record operations

This part documents the `record` resource client (3 operations). A checkpoint
record holds arbitrary state identified by a RID, searchable by criteria.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/checkpoints/scripts/pal_found_checkpoints_cli.py`;
SDK `foundry_sdk/v2/checkpoints/record.py` at pinned commit `2da67907`.
Reviewer architect (CODEREVIEW-048), 2026-10-03. QA baseline TESTCASE-019.

## Operation records

### record.get

- **Class**: read. Returns a single checkpoint record.
- **Preconditions**: can read the record.
- **Effect**: returns the record's value/state.
- **Inputs**: positional `record_rid`.
- **Success**: the record.
- **Failure**: exit 4 if RID missing.
- **Example**: `pal-found-checkpoints record get <RECORD_RID>`.

### record.get_batch

- **Class**: read. Returns several records.
- **Preconditions**: can read each.
- **Effect**: returns a batch of records.
- **Inputs**: `--records-json` (list of record RIDs).
- **Success**: list of records.
- **Example**: `pal-found-checkpoints record get-batch --records-json '["r1","r2"]'`.

### record.search

- **Class**: read/query. Searches records by criteria.
- **Preconditions**: can read records.
- **Effect**: returns records matching the search criteria, paged.
- **Inputs**: `--where-json` (search criteria); paging options.
- **Success**: matching records; empty if none.
- **Example**: `pal-found-checkpoints record search --where-json '{"branchId":"main"}'`.

## Evidence and review

All three records are read-class. Reviewed against the installed
`pal-found-checkpoints` parser and pinned SDK sources (commit `2da67907`).
Reads never write. No unsupported operation is documented as callable.
