# Dataset operations

Datasets hold versioned files, with an optional schema for tabular reads. A transaction changes a
branch view; a branch is a pointer to transaction history. A View is a separate resource that reads
a union of backing datasets without storing their files. Most enrollments use `master` as the
default branch, but omit the branch flag to use the enrollment default.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-integration/datasets). The behavior below
describes the installed CLI commands. Replace
example identifiers and configuration values with values from your Foundry enrollment.

## Operation records

### dataset.create

- **Behavior:** Creates a new Dataset. A default branch - `master` for most enrollments - will be
  created on the Dataset.
- **Before use:** Choose an existing parent folder in which you can create datasets.
- **Inputs:** positional none; required `--name`, `--parent-folder-rid`; optional none.
- **Result:** `Dataset`.
- **Failure or follow-up:** An invalid configuration or insufficient permission rejects dataset
  creation; use the returned RID for later calls.
- **Example:** `pal-found-datasets dataset create --name Orders --parent-folder-rid PARENT_FOLDER_RID`

### dataset.get

- **Behavior:** Reads dataset metadata by RID, including its name and parent folder. This does not
  read files or table rows; use `file list` or `dataset read-table` for content.
- **Before use:** The dataset must exist and be readable.
- **Inputs:** positional `dataset_rid`; required none; optional none.
- **Result:** `Dataset`.
- **Failure or follow-up:** A missing or inaccessible dataset returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-datasets dataset get DATASET_RID`

### dataset.get_health_check_reports

- **Behavior:** Get the most recent Data Health Check report for each check configured on the given
  Dataset. Returns one report per check, representing the current health status of the dataset. To
  get the list of checks configured on a Dataset, use Get Dataset Health Checks. For the full report
  history of a specific check, use Get Latest Check Reports.
- **Before use:** The dataset must exist and be readable.
- **Inputs:** positional `dataset_rid`; required none; optional `--branch-name`. `branch_name`: The
  name of the Branch. If none is provided, the default Branch name - `master` for most enrollments -
  will be used.
- **Parameter notes:** `--branch-name` selects the dataset branch whose configured checks are reported; omit it for the default branch.
- **Result:** `GetHealthCheckReportsResponse`.
- **Failure or follow-up:** Invalid input or insufficient access to the dataset is returned through
  the CLI error envelope.
- **Example:** `pal-found-datasets dataset get-health-check-reports DATASET_RID`

### dataset.get_health_checks

- **Behavior:** Get the RIDs of the Data Health Checks that are configured for the given Dataset.
- **Before use:** The dataset must exist and be readable.
- **Inputs:** positional `dataset_rid`; required none; optional `--branch-name`. `branch_name`: The
  name of the Branch. If none is provided, the default Branch name - `master` for most enrollments -
  will be used.
- **Parameter notes:** `--branch-name` selects the dataset branch whose check RIDs are listed; omit it for the default branch.
- **Result:** `ListHealthChecksResponse`.
- **Failure or follow-up:** Invalid input or insufficient access to the dataset is returned through
  the CLI error envelope.
- **Example:** `pal-found-datasets dataset get-health-checks DATASET_RID`

### dataset.get_schedules

- **Behavior:** Get the RIDs of the Schedules that target the given Dataset. Note: It may take up to
  an hour for recent changes to schedules to be reflected in this response, especially for schedules
  managed by Marketplace. This operation will return outdated results in the meantime.
- **Before use:** The dataset must exist and be readable.
- **Inputs:** positional `dataset_rid`; required none; optional `--branch-name`. `branch_name`: The
  name of the Branch. If none is provided, the default Branch name - `master` for most enrollments -
  will be used.
- **Parameter notes:** `--branch-name` selects the branch whose targeting schedules are listed; omit it for the default branch.
- **Result:** `ListSchedulesResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-datasets dataset get-schedules DATASET_RID`

### dataset.get_schema

- **Behavior:** Reads the schema associated with the selected branch's latest committed version.
  The SDK also supports an end transaction, but this CLI operation exposes only `--branch-name`.
- **Before use:** The dataset must exist and be readable.
- **Inputs:** positional `dataset_rid`; required none; optional `--branch-name`.
- **Result:** `GetDatasetSchemaResponse`.
- **Failure or follow-up:** A missing or inaccessible dataset returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-datasets dataset get-schema DATASET_RID`

### dataset.read_table

- **Behavior:** Gets the content of a dataset as a table in the specified format. This endpoint
  currently does not support views (virtual datasets composed of other datasets).
- **Before use:** The dataset must have readable tabular data and a schema on the selected branch.
- **Inputs:** positional `dataset_rid`; required `--table-format ARROW|CSV`; optional `--output`,
  `--branch-name`, `--columns-json`, `--row-limit`, `--start-transaction-rid`, and
  `--end-transaction-rid`. `--columns-json` is an array of column names. Row order is not guaranteed.
- **Parameter notes:** `--branch-name` selects the branch to export. `--columns-json` is a JSON array of columns to include. `--start-transaction-rid` and `--end-transaction-rid` bound the transaction view read by the export.
- **Result:** Saves the table export under the configured download root and prints JSON metadata
  with the saved path, byte count, checksums, and MIME type. `--output` sets a basename, not a path;
  omitting it lets the download handler choose a filename.
- **Failure or follow-up:** An invalid column list, format, or missing dataset fails. Large exports
  may exceed the configured download size limit; use `--row-limit` or select fewer columns.
- **Example:** `pal-found-datasets dataset read-table DATASET_RID --table-format CSV --row-limit 100 --output orders.csv`

### dataset.get_schema_batch

- **Behavior:** Fetch schemas for multiple datasets in a single request. Datasets not found or
  inaccessible to the user will be omitted from the response. The maximum batch size for this
  endpoint is 1000.
- **Before use:** Supply readable dataset RIDs; missing or inaccessible RIDs are omitted from the
  batch response.
- **Inputs:** positional none; required `--body-json` containing an array of up to 1000 objects,
  each with a `datasetRid`; optional none. The response includes schemas for accessible datasets.
- **Result:** `GetSchemaDatasetsBatchResponse`.
- **Failure or follow-up:** Check the returned entries: batch endpoints may omit missing or
  inaccessible resources, so compare the result with requested RIDs.
- **Example:** `pal-found-datasets dataset get-schema-batch --body-json '[{"datasetRid":"DATASET_RID"}]'`

### dataset.jobs

- **Behavior:** Lists jobs that wrote the dataset. By default, jobs appear in descending start-time
  order; inspect a job through Orchestration for its status and build details.
- **Before use:** The dataset must exist and be readable.
- **Inputs:** positional `dataset_rid`; required none; optional none.
- **Result:** A page of job details and a continuation token when more jobs exist.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-datasets dataset jobs DATASET_RID`

### dataset.put_schema

- **Behavior:** Sets the dataset schema for the selected branch so Foundry can interpret its files
  as typed table columns. The supplied schema describes columns; it does not upload data.
- **Before use:** The dataset and selected branch must exist and be writable; supply a schema
  matching the intended data.
- **Inputs:** positional `dataset_rid`; required `--schema`; optional `--branch-name`. `schema`: The
  schema that will be added.
- **Parameter notes:** `--branch-name` selects the branch on which to write the schema; omit it for the default branch.
- **Result:** `GetDatasetSchemaResponse`.
- **Failure or follow-up:** An invalid replacement payload or insufficient permission leaves the
  dataset unchanged; read it again after success.
- **Example:** `pal-found-datasets dataset put-schema DATASET_RID --schema '{"fieldSchemaList":[{"name":"id","type":"LONG","nullable":false,"customMetadata":{"description":"Primary key"}},{"name":"event_time","type":"TIMESTAMP","nullable":false},{"name":"price","type":"DECIMAL","precision":10,"scale":2,"nullable":true},{"name":"tags","type":"ARRAY","nullable":true,"arraySubtype":{"type":"STRING","nullable":false}},{"name":"metrics","type":"STRUCT","nullable":true,"subSchemas":[{"name":"temperature","type":"DOUBLE","nullable":true},{"name":"humidity","type":"DOUBLE","nullable":true}]}]}'`

### dataset.transactions

- **Behavior:** Lists transactions for the dataset across branches in reverse chronological order.
  Use `branch transactions` to inspect history for one branch.
- **Before use:** The dataset must exist and be readable.
- **Inputs:** positional `dataset_rid`; required none; optional none.
- **Result:** `ListTransactionsOfDatasetResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-datasets dataset transactions DATASET_RID`
