# Dataset metadata and table exports

[Operation catalog](../../catalog.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A Dataset identifies tabular or file data in Foundry. Branches and transactions
select data versions. Metadata, schema, health checks and execution history are
different views of that resource; reading metadata does not prove that the
caller can export its contents. Views are virtual datasets with separate APIs.

## Export a bounded table

1. Resolve the dataset RID and intended branch. Inspect the schema to choose
   columns and verify that the application can handle their types.
2. Call [read_table](../../contracts/v2/datasets/Dataset/read_table.md) with
   `format="CSV"` or `format="ARROW"`. Set `row_limit` when only a sample is
   needed. Row order is nondeterministic, so the limit does not select a stable
   prefix of the data. Select `columns` explicitly when exporting a subset.
3. Choose start/end transaction RIDs only when a transaction-bounded export is
   intended. Validate their relationship with the branch; individually valid
   parameters can form an invalid combination.
4. Retain the returned bytes and parse them according to the chosen format.
   Check required column names and application-level row constraints before
   using results. Close raw responses, including when decoding fails.

Run from the skill directory:

```bash
python -B examples/rest/074/v2/datasets/Dataset/read_table.py
```

The actual SDK sends a CSV request with a two-row limit to a synthetic transport.
The response contains the CSV header `asset_id,status` and one example row. The
example checks the request query, decoded byte content and all eight declared
errors. Byte equality proves transport decoding; a live application must also
parse the table and validate its own schema. ARROW exports require an Arrow IPC
reader already present in the environment. CSV bytes must not be passed to an
Arrow-only conversion method.

This endpoint does not support views. `DatasetReadNotSupported` requires choosing
a supported dataset or an application workflow that understands the view's
backing datasets. `ColumnTypesNotSupported` requires checking exportable columns
and schema. `SchemaNotFound` can mean missing schema or missing access; verify
both for the selected branch. `ReadTableDatasetPermissionDenied` requires
resource access review. `ReadTableRowLimitExceeded` applies a one-million-row
limit to datasets not stored as Parquet; Parquet datasets have no such documented
row limit. Reduce the export when appropriate instead of retrying unchanged.
For `ReadTableTimeout` or `ReadTableError`, retain request bounds and error
details, then choose a smaller export or investigate the service failure.

## Execution boundary

SDK source gives no universal scope string for table export. Verify configured
application grants, dataset read access and enrollment enablement before live
execution. Offline fixtures require prepared SDK/httpx only and do not establish
tenant data access.
