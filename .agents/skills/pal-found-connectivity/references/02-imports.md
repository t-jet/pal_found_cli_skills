# File, table import, and virtual table operations

A connection stores how Foundry reaches an external source. A file import selects source files and
writes them to a dataset; a table import syncs tabular source data into a dataset. The import
definition is separate from an execution. A virtual table lets supported sources be queried without
first copying them into a Foundry dataset.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-connection/core-concepts). The behavior
below describes the installed CLI commands and their behavior.
Replace example identifiers and configuration values with values from your Foundry enrollment.

## Choose an import mode

Set `--import-mode` on create or replace; the selected mode takes effect when the import executes.

| Resource / SDK type | Mode | Effect of an execution |
|---|---|---|
| File import / `FileImportMode` | `SNAPSHOT` | New dataset state contains only files from this execution. |
| File import / `FileImportMode` | `APPEND` | Keeps files from earlier executions and adds new files. |
| File import / `FileImportMode` | `UPDATE` | Replaces files from earlier executions by matching file names. |
| Table import / `TableImportMode` | `SNAPSHOT` | New dataset state contains only data from this execution. |
| Table import / `TableImportMode` | `APPEND` | Keeps data from earlier executions and adds new data. |

Choose snapshot when each execution supplies the complete desired state; omitted files/data are
absent from that new state. Choose append for additive inputs. Choose file update when repeated file
names should replace earlier files. Table imports do not accept `UPDATE`; file update does not imply
row-key merging. Re-executing an additive import can add data again; reconcile uncertain executions
before starting another.

## Observe an execution

Prerequisites: preinstalled, configured `pal-found-orchestration`, an authorized identity able to read
the build and its jobs, and the destination dataset RID/branch from the import definition. The commands
and decisions needed here are given below; no additional skill folder is required.

1. Run `file-import execute` or `table-import execute` once and retain its returned JSON string
   `BuildRid` as `BUILD_RID` (without JSON quotes). This acknowledges asynchronous work.
2. Run `pal-found-orchestration build get BUILD_RID --format json --timeout 30`. Check `rid`,
   `branchName`, `status`, `jobRids`, and `finishedTime`; verify the branch matches the import.
3. While `status` is `RUNNING`, wait at least 10 seconds between reads. Use at most 12 build reads
   and a 5-minute overall observation budget, whichever ends first. These are reader limits, not
   server completion guarantees. A read error consumes an attempt. On authentication/permission
   failure, stop and obtain authorized access; missing/inaccessible data does not establish failure.
4. `SUCCEEDED` is terminal build success. `FAILED` and `CANCELED` are terminal unsuccessful outcomes.
   In each terminal case, inspect jobs with
   `pal-found-orchestration build jobs BUILD_RID --format json --max-pages 2 --timeout 30`.
   Jobs expose `rid`, `buildRid`, `jobStatus`, `outputs`, and optional `finishedTime`. `WAITING` and
   `RUNNING` are nonterminal; `SUCCEEDED`, `FAILED`, `CANCELED`, and `DID_NOT_RUN` are terminal job
   states. A failed, canceled, or unrun job does not prove successful output publication.
5. In job `outputs`, match `type: "datasetJobOutput"` and `datasetRid` to the intended destination.
   Record its `outputTransactionRid` when present. Build success plus the expected dataset/branch
   and output evidence establishes execution success; checking expected content/schema still requires
   authorized dataset inspection. An absent transaction RID or omitted output is insufficient evidence
   of dataset publication. Job outputs omit unsupported resource types.

For job paging, stdout contains items and stderr metadata contains `next_page_token`. Within the same
5-minute budget, resume with `--page-token TOKEN`, allowing at most 4 job pages in total. Stop on a
repeated token. A remaining cursor means partial observation, even when stdout is empty. Budget
exhaustion, unknown status, inconsistent build/job states, or missing expected output means unresolved:
retain build/import/dataset RIDs and last states for the connection owner; do not execute again to poll.
For failed builds, the owner checks source connectivity, configuration and destination permissions
before correcting the cause and deciding whether a new execution is appropriate.

## Reconcile uncertain writes

A timeout, transport loss, or exhausted retries can follow an accepted write. Preserve the intended
connection/import/dataset/branch, payload, request time, and returned RIDs or CLI `call_id`; a client
error alone does not establish whether Foundry changed anything.

- If execute returned a build RID, follow the bounded observation procedure above. If the RID was
  lost, search visible builds on the known branch with
  `pal-found-orchestration build search --where-json '{"type":"eq","field":"BRANCH_NAME","value":"BRANCH_NAME"}' --format json --max-pages 2 --timeout 30`,
  replacing the JSON value with the actual branch. Compare `createdTime`, `createdBy`, and `branchName`
  with the request context, then inspect candidate jobs for the expected `datasetRid`. Limit this
  recovery to 5 minutes, 2 search pages and 10 candidates, with at most 2 job pages per candidate.
  Stop on a repeated cursor. Matches are candidates, not proof of which import request ran. If the
  result is partial, absent, or ambiguous, ask the connection owner to correlate the request and
  build history before any replay. These commands provide no import-execution lookup by request ID.
- For create without a returned RID, use the matching `file-import list` or `table-import list` on
  the original connection with `--max-pages 2`; compare name, dataset, branch, filters/configuration
  and mode, then `get` a candidate RID. Allow at most 4 pages total, resuming with `--page-token`,
  within 5 minutes; stop on repeated tokens. Names need not establish unique identity. For virtual
  table create, these commands provide no virtual-table get/list reconciliation; retain request
  context for the connection owner to inspect the parent folder through authorized tooling.
- For replace or delete of a known import RID, use the matching import `get` to compare the current
  definition with the intended change. Allow at most 3 reads, at least 10 seconds apart, within
  2 minutes. A missing/inaccessible result alone cannot distinguish deletion from loss of access.
  Stop unresolved when access, concurrent edits, or resource identity prevents reconciliation.

Keep unresolved outcomes explicit and stop writes when a budget expires. Resume observation or replay
only after the owner establishes the prior effect and confirms a further write is appropriate; none
of these read procedures proves server authorization, source reachability, or live completion offline.

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
- **Failure or follow-up:** Follow [Observe an execution](#observe-an-execution) for completion;
  use [Reconcile uncertain writes](#reconcile-uncertain-writes) after a lost or uncertain response.
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
- **Inputs:** positional `connection_rid`; required none; optional `--page-size`, `--page-token`,
  `--all`, `--max-pages`.
- **Parameter notes:** `--page-size` sets items requested per server page. `--page-token` starts
  after a previous page. `--max-pages` fetches at most that many pages; `--all` requests bounded
  automatic paging.
- **Result:** List of `FileImport` items on stdout in the selected output format. The CLI writes `pages_fetched`,
  `total_items`, and any `next_page_token` as JSON metadata on stderr.
- **Failure or follow-up:** The default call fetches one page. An empty item array can still have a
  `next_page_token`; pass it with `--page-token` to continue, or use `--all` for bounded automatic
  paging.
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
- **Failure or follow-up:** Follow [Observe an execution](#observe-an-execution) for completion;
  use [Reconcile uncertain writes](#reconcile-uncertain-writes) after a lost or uncertain response.
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
- **Inputs:** positional `connection_rid`; required none; optional `--page-size`, `--page-token`,
  `--all`, `--max-pages`.
- **Parameter notes:** `--page-size` sets items requested per server page. `--page-token` starts
  after a previous page. `--max-pages` fetches at most that many pages; `--all` requests bounded
  automatic paging.
- **Result:** List of `TableImport` items on stdout in the selected output format. The CLI writes `pages_fetched`,
  `total_items`, and any `next_page_token` as JSON metadata on stderr.
- **Failure or follow-up:** The default call fetches one page. An empty item array can still have a
  `next_page_token`; pass it with `--page-token` to continue, or use `--all` for bounded automatic
  paging.
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
