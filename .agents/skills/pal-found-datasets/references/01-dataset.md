# Dataset operations

This part documents the `dataset` resource client (11 operations). Read the
[Datasets entry](SKILL.md) and the general [platform
concepts](../pal-found/references/01-platform-concepts.md) part first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/datasets/scripts/pal_found_datasets_cli.py`;
SDK `foundry_sdk/v2/datasets/*.py` at pinned commit `2da67907`. Reviewer
architect (CODEREVIEW-044), 2026-10-03. QA baseline TESTCASE-003.

## Workflow

1. Create a dataset (`dataset.create`) in a parent folder.
2. Set its schema (`dataset.put_schema`) and read it back
   (`dataset.get_schema`, `dataset.get_schema_batch`).
3. Read data (`dataset.read_table`), health and schedules
   (`get_health_checks`, `get_health_check_reports`, `get_schedules`), and
   transaction status (`dataset.transactions`, `dataset.jobs`).

## Operation records

### dataset.create

- **Class**: create. Stores a new dataset in a parent folder.
- **Preconditions**: a parent folder you can write into; a display name.
- **Effect**: creates the dataset and returns it, including its RID.
- **Inputs**: required `--parent-folder-rid`, `--name`; optional `--description`.
- **Success**: the created dataset; a branch (`branch`) is typically created
  for it.
- **Failure**: exit 1 invalid input; exit 8 readonly block; exit 3 permission.
- **Example**: `pal-found-datasets dataset create --parent-folder-rid ri.foundry.main.folder.f1 --name "Orders"`.

### dataset.get

- **Class**: read. Returns a dataset by RID.
- **Preconditions**: can read the dataset.
- **Effect**: returns dataset metadata (RID, file-system-path).
- **Inputs**: positional `dataset_rid`.
- **Success**: the dataset record.
- **Failure**: exit 4 if RID wrong.
- **Example**: `pal-found-datasets dataset get <DATASET_RID>`.

### dataset.get_health_checks

- **Class**: read. Returns configured data health checks for a dataset.
- **Preconditions**: can read the dataset's checks.
- **Effect**: returns health checks.
- **Inputs**: positional `dataset_rid`.
- **Success**: health checks; empty if none configured.

### dataset.get_health_check_reports

- **Class**: read. Returns check reports for a dataset.
- **Preconditions**: can read the dataset's check reports.
- **Effect**: returns reports.
- **Inputs**: positional `dataset_rid`.

### dataset.get_schedules

- **Class**: read. Returns the build/transform schedules on a dataset.
- **Preconditions**: can read the dataset's schedules.
- **Effect**: returns schedules.
- **Inputs**: positional `dataset_rid`.

### dataset.get_schema

- **Class**: read. Returns a branch's schema.
- **Preconditions**: the dataset and branch exist.
- **Effect**: returns the schema for the selected branch; does not write.
- **Inputs**: positional `dataset_rid`; `--branch-name` (default branch if
  omitted).
- **Success**: schema information for that branch. An absent schema must be
  interpreted from the observed CLI/SDK response, not guessed.
- **Failure**: exit 4 if dataset/branch missing.
- **Example**: `pal-found-datasets dataset get-schema <DATASET_RID> --branch-name main`.

### dataset.get_schema_batch

- **Class**: read. Returns schemas for several datasets in one call.
- **Preconditions**: can read each dataset.
- **Effect**: returns a batch of schemas.
- **Inputs**: required `--dataset-r` (JSON list of dataset RIDs).
- **Success**: a list of schemas for the requested RIDs.

### dataset.jobs

- **Class**: read (async status). Returns jobs that built the dataset.
- **Preconditions**: can read the dataset.
- **Effect**: returns build/job records for the dataset.
- **Inputs**: positional `dataset_rid`; paging options.
- **Success**: job records; empty if none. Use `transaction.job` for a single
  build status.

### dataset.put_schema

- **Class**: change. Sets or replaces a dataset's schema.
- **Preconditions**: can write the dataset and its branch.
- **Effect**: writes the schema for the branch; the dataset now advertises it.
- **Inputs**: positional `dataset_rid`; `--schema` JSON; `--branch-name`.
- **Success**: returns the updated dataset.
- **Failure**: exit 1 invalid schema JSON; exit 8 readonly block.
- **Example**: `pal-found-datasets dataset put-schema <DATASET_RID> --branch-name main --schema '{"schema_type":"STRUCT","fieldSchemaList":[]}'`.

### dataset.read_table

- **Class**: read. Reads tabular data from a dataset branch.
- **Preconditions**: can read the dataset; the branch holds a transaction.
- **Effect**: returns rows from the branch (respecting format/paging).
- **Inputs**: positional `dataset_rid`; `--branch-name`; format/row options.
- **Success**: the returned rows; may be a full or bounded set depending on the
  parser.
- **Failure**: exit 5 on timeout for large reads; consider rows limit.
- **Example**: `pal-found-datasets dataset read-table <DATASET_RID> --branch-name main`.

### dataset.transactions

- **Class**: read. Lists transactions on a dataset branch.
- **Preconditions**: can read the dataset.
- **Effect**: returns transactions, paged.
- **Inputs**: positional `dataset_rid`; `--branch-name`; paging options.
- **Success**: transactions; empty if none.
- **Example**: `pal-found-datasets dataset transactions <DATASET_RID> --branch-name main`.

## Evidence and review

Each record was reviewed against the installed `pal-found-datasets` parser
and pinned SDK sources (commit `2da67907`). Reads never write; `create` and
`put_schema` are the write operations here. Data-volume and row-limit cues
apply to `read_table` (AC-D-013-09). No unsupported operation is documented as
callable.
