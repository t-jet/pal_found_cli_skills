# File, table import, and virtual table operations

This part documents the `file_import` (6), `table_import` (6), and
`virtual_table` (1) resource clients (13 operations). Imports pull data from a
connection into Foundry.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/connectivity/scripts/pal_found_connectivity_cli.py`;
SDK `foundry_sdk/v2/connectivity/{file_import,table_import,virtual_table}.py`
at pinned commit `2da67907`. Reviewer architect (CODEREVIEW-048), 2026-10-03.
QA baseline TESTCASE-017.

## Operation records

### file_import.create

- **Class**: create (write). Creates a file import config.
- **Preconditions**: a connection and filters are valid.
- **Effect**: defines an import of matched files from the source.
- **Inputs**: `--display-name`, `--connection-rid`, `--file-import-filters-json`,
  `--output-dataset-rid`, `--branch-name`.
- **Success**: the created import, including its RID.
- **Failure**: exit 1 invalid filters; exit 8 readonly block.

### file_import.delete

- **Class**: delete (write). Deletes a file import.
- **Preconditions**: can delete the import.
- **Effect**: removes the import definition.
- **Inputs**: positional `file_import_rid`.
- **Success**: returns the deleted import.

### file_import.execute

- **Class**: execute (write, async). Runs the file import now.
- **Preconditions**: the import exists.
- **Effect**: triggers an import run; acceptance is not proof the run finished.
- **Inputs**: positional `file_import_rid`; maybe a config/branch.
- **Success**: a run reference; check output dataset/status for completion.

### file_import.get

- **Class**: read. Returns a file import.
- **Preconditions**: can read the import.
- **Effect**: returns the import definition.
- **Inputs**: positional `file_import_rid`.
- **Success**: the import record.
- **Failure**: exit 4 if missing.

### file_import.list

- **Class**: read. Lists file imports.
- **Preconditions**: can read imports.
- **Effect**: returns imports, paged.
- **Inputs**: paging options.
- **Success**: imports; empty if none.

### file_import.replace

- **Class**: change (write). Replaces a file import definition.
- **Preconditions**: can write the import.
- **Effect**: replaces the import's filters/target.
- **Inputs**: positional `file_import_rid`; replacement fields.
- **Success**: the updated import.

### table_import.create / delete / execute / get / list / replace

- **Class**: same shape as `file_import` but targets tables.
- **Preconditions**: a connection and table config.
- **Effect**: defines/deletes/runs/reads/replaces a table import.
- **Inputs**: `--display-name`, `--connection-rid`,
  `--table-import-configuration-json`, `--output-dataset-rid`,
  `--branch-name`; positional `table_import_rid` where used.
- **Success**: the import definition or run reference.
- **Failure**: exit 1 invalid table config; exit 8 readonly block.
- **Note**: `execute` is async; check the output dataset for completion.

### virtual_table.create

- **Class**: create (write). Creates a virtual table.
- **Preconditions**: can create virtual tables in the target space/folder.
- **Effect**: creates a virtual table backed by a configured source.
- **Inputs**: display name, parent folder/space, source configuration.
- **Success**: the created virtual table (RID).
- **Failure**: exit 1 invalid config; exit 8 readonly block.

## Evidence and review

Reviewed against the installed `pal-found-connectivity` parser and pinned SDK
sources (commit `2da67907`). Import `execute` operations start asynchronous
work: a zero exit confirms acceptance, not completion; check the output
dataset or import status. Creates/deletes/replaces write state. No unsupported
operation is documented as callable.
