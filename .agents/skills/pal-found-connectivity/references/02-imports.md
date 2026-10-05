# File, table import, and virtual table operations

A connection stores how Foundry reaches an external source. A file import selects source files and
writes them to a dataset; a table import syncs tabular source data into a dataset. The import
definition is separate from an execution. A virtual table lets supported sources be queried without
first copying them into a Foundry dataset.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-connection/core-concepts). The behavior
below describes the installed CLI commands and their behavior.
Replace example identifiers and configuration values with values from your Foundry enrollment.

## Operation records

### file_import.create

- **Behavior:** Defines a file import on this connection. Its ordered filters choose source files;
  its import mode decides whether later executions replace, append, or update files in the
  destination dataset. Creation does not start a sync.
- **Before use:** The connection must exist; the output dataset must be writable and compatible with
  the chosen import mode.
- **Inputs:** positional `connection_rid`; required `--dataset-rid`, `--display-name`,
  `--filters-json`, `--import-mode`; optional `--branch-name`, `--subfolder`. `dataset_rid`: The RID
  of the output dataset. Can not be modified after the file import is created.
  `file_import_filters`: Use filters to limit which files should be imported. Filters are applied in
  the order they are defined. A different ordering of filters may lead to a more optimized import.
  Learn more about optimizing file imports. `branch_name`: The branch name in the output dataset
  that will contain the imported data. Defaults to `master` for most enrollments. Can not be
  modified after the file import is created.
- **Parameter notes:** `--branch-name` chooses the destination dataset branch and is fixed after creation. `--subfolder` limits import to that external source folder; omission uses the source root.
- **Result:** `FileImport`.
- **Failure or follow-up:** An invalid configuration or insufficient permission rejects file import
  creation; use the returned RID for later calls.
- **Example:** `pal-found-connectivity file-import create CONNECTION_RID --dataset-rid DATASET_RID --display-name Orders --filters-json '[{"type":"pathMatchesFilter","regex":".*[.]csv"}]' --import-mode SNAPSHOT`

### file_import.delete

- **Behavior:** Delete the FileImport with the specified RID. Deleting the file import does not
  delete the destination dataset but the dataset will no longer be updated by this import.
- **Before use:** The connection and import must exist; the caller needs permission to change or run
  the import.
- **Inputs:** positional `connection_rid`, `file_import_rid`; required none; optional none.
- **Result:** `None`.
- **Failure or follow-up:** A missing file import, invalid target, or insufficient permission
  rejects the removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-connectivity file-import delete CONNECTION_RID FILE_IMPORT_RID`

### file_import.execute

- **Behavior:** Executes the FileImport, which runs asynchronously as a Foundry Build. The returned
  BuildRid can be used to check the status via the Orchestration API.
- **Before use:** The connection and import must exist; the caller needs permission to change or run
  the import.
- **Inputs:** positional `connection_rid`, `file_import_rid`; required none; optional none.
- **Result:** `BuildRid`.
- **Failure or follow-up:** A successful request starts a sync; inspect the output dataset and
  subsequent transaction/build status for completion.
- **Example:** `pal-found-connectivity file-import execute CONNECTION_RID FILE_IMPORT_RID`

### file_import.get

- **Behavior:** Get the FileImport with the specified rid.
- **Before use:** The connection and requested import must be readable.
- **Inputs:** positional `connection_rid`, `file_import_rid`; required none; optional none.
- **Result:** `FileImport`.
- **Failure or follow-up:** A missing or inaccessible file import returns an error, except where the
  SDK declares an optional result.
- **Example:** `pal-found-connectivity file-import get CONNECTION_RID FILE_IMPORT_RID`

### file_import.list

- **Behavior:** Lists all file imports defined for this connection. Only file imports that the user
  has permissions to view will be returned.
- **Before use:** The connection and requested import must be readable.
- **Inputs:** positional `connection_rid`; required none; optional none.
- **Result:** `ListFileImportsResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-connectivity file-import list CONNECTION_RID`

### file_import.replace

- **Behavior:** Replaces the file import's editable definition, including name, source filters,
  import mode, and optional source subfolder. The output dataset and branch chosen at creation
  remain fixed. Replacement does not execute the import.
- **Before use:** The connection and import must exist; the caller needs permission to change or run
  the import.
- **Inputs:** positional `connection_rid`, `file_import_rid`; required `--display-name`,
  `--filters-json`, `--import-mode`; optional `--subfolder`. `file_import_filters`: Use filters to
  limit which files should be imported. Filters are applied in the order they are defined. A
  different ordering of filters may lead to a more optimized import. Learn more about optimizing
  file imports. `subfolder`: A subfolder in the external system that will be imported. If not
  specified, defaults to the root folder of the external system.
- **Parameter notes:** `--subfolder` selects an external source folder for the import; omission uses the source root.
- **Result:** `FileImport`.
- **Failure or follow-up:** An invalid replacement payload or insufficient permission leaves the
  file import unchanged; read it again after success.
- **Example:** `pal-found-connectivity file-import replace CONNECTION_RID FILE_IMPORT_RID --display-name Orders --filters-json '[{"type":"pathMatchesFilter","regex":".*[.]csv"}]' --import-mode SNAPSHOT`

### table_import.create

- **Behavior:** Defines a table import on this connection. `--config-json` identifies the source
  table or query; the import mode controls how each execution updates the output dataset.
  Creation saves the definition but does not run it.
- **Before use:** The connection must exist; the output dataset must be writable and compatible with
  the chosen import mode.
- **Inputs:** positional `connection_rid`; required `--config-json`, `--dataset-rid`,
  `--display-name`, `--import-mode`; optional `--allow-schema-changes`, `--branch-name`.
  `dataset_rid`: The RID of the output dataset. Can not be modified after the table import is
  created. `allow_schema_changes`: Allow the TableImport to succeed if the schema of imported rows
  does not match the existing dataset's schema. Defaults to false for new table imports.
  `branch_name`: The branch name in the output dataset that will contain the imported data. Defaults
  to `master` for most enrollments. Can not be modified after the table import is created.
- **Parameter notes:** `--allow-schema-changes` lets a sync succeed if imported rows differ from the existing dataset schema; default is false. `--branch-name` chooses the fixed destination branch.
- **Result:** `TableImport`.
- **Failure or follow-up:** An unsupported source config, inaccessible output dataset, or invalid
  import mode rejects creation. Use the returned import RID with `table-import execute`.
- **Example:** `pal-found-connectivity table-import create CONNECTION_RID --config-json '{"type":"jdbcImportConfig","query":"SELECT * FROM table"}' --dataset-rid DATASET_RID --display-name Orders --import-mode SNAPSHOT`

### table_import.delete

- **Behavior:** Delete the TableImport with the specified RID. Deleting the table import does not
  delete the destination dataset but the dataset will no longer be updated by this import.
- **Before use:** The connection and import must exist; the caller needs permission to change or run
  the import.
- **Inputs:** positional `connection_rid`, `table_import_rid`; required none; optional none.
- **Result:** `None`.
- **Failure or follow-up:** A missing table import, invalid target, or insufficient permission
  rejects the removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-connectivity table-import delete CONNECTION_RID TABLE_IMPORT_RID`

### table_import.execute

- **Behavior:** Executes the TableImport, which runs asynchronously as a Foundry Build. The returned
  BuildRid can be used to check the status via the Orchestration API.
- **Before use:** The connection and import must exist; the caller needs permission to change or run
  the import.
- **Inputs:** positional `connection_rid`, `table_import_rid`; required none; optional none.
- **Result:** `BuildRid`.
- **Failure or follow-up:** A successful request starts a sync; inspect the output dataset and
  subsequent transaction/build status for completion.
- **Example:** `pal-found-connectivity table-import execute CONNECTION_RID TABLE_IMPORT_RID`

### table_import.get

- **Behavior:** Get the TableImport with the specified rid.
- **Before use:** The connection and requested import must be readable.
- **Inputs:** positional `connection_rid`, `table_import_rid`; required none; optional none.
- **Result:** `TableImport`.
- **Failure or follow-up:** A missing or inaccessible table import returns an error, except where
  the SDK declares an optional result.
- **Example:** `pal-found-connectivity table-import get CONNECTION_RID TABLE_IMPORT_RID`

### table_import.list

- **Behavior:** Lists all table imports defined for this connection. Only table imports that the
  user has permissions to view will be returned.
- **Before use:** The connection and requested import must be readable.
- **Inputs:** positional `connection_rid`; required none; optional none.
- **Result:** `ListTableImportsResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-connectivity table-import list CONNECTION_RID`

### table_import.replace

- **Behavior:** Replaces the table import's editable definition: name, source query/configuration,
  import mode, and schema-change policy. Its output dataset and branch remain those chosen at
  creation. Replacement does not execute the import.
- **Before use:** The connection and import must exist; the caller needs permission to change or run
  the import.
- **Inputs:** positional `connection_rid`, `table_import_rid`; required `--config-json`,
  `--display-name`, `--import-mode`; optional `--allow-schema-changes`. `allow_schema_changes`:
  Allow the TableImport to succeed if the schema of imported rows does not match the existing
  dataset's schema. Defaults to false for new table imports.
- **Parameter notes:** `--allow-schema-changes` lets subsequent syncs succeed when source row schema differs from the output dataset schema.
- **Result:** `TableImport`.
- **Failure or follow-up:** An invalid replacement payload or insufficient permission leaves the
  table import unchanged; read it again after success.
- **Example:** `pal-found-connectivity table-import replace CONNECTION_RID TABLE_IMPORT_RID --config-json '{"type":"jdbcImportConfig","query":"SELECT * FROM table"}' --display-name Orders --import-mode SNAPSHOT`

### virtual_table.create

- **Behavior:** Creates a virtual table in the parent folder from an upstream table described by
  `--config-json`. Queries read through the connection; creation does not copy that source table
  into a versioned Foundry dataset.
- **Before use:** Use an accessible supported connection and a writable parent folder for the
  virtual table.
- **Inputs:** positional `connection_rid`; required `--config-json`, `--name`, `--parent-rid`;
  optional `--markings-json`.
- **Parameter notes:** `--markings-json` is a JSON list of security markings to apply to the new virtual table.
- **Result:** `VirtualTable`.
- **Failure or follow-up:** An invalid configuration or insufficient permission rejects virtual
  table creation; use the returned RID for later calls.
- **Example:** `pal-found-connectivity virtual-table create CONNECTION_RID --config-json '{"type":"snowflake","database":"ANALYTICS","schema":"PUBLIC","table":"ORDERS"}' --name Orders --parent-rid PARENT_RID`
