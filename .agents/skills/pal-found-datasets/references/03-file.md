# File operations

This part documents the `file` resource client (5 operations). Files are named
binary blobs stored inside a dataset's branch, and are read or written within
a transaction when applicable. Read the [Datasets entry](SKILL.md) first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/datasets/scripts/pal_found_datasets_cli.py`;
SDK `foundry_sdk/v2/datasets/file.py` at pinned commit `2da67907`. Reviewer
architect (CODEREVIEW-044), 2026-10-03. QA baseline TESTCASE-003.

## Operation records

### file.content

- **Class**: read (binary download). Returns a file's bytes into a saved blob.
- **Preconditions**: can read the file and the dataset.
- **Effect**: streams the file content through the binary download handler and
  returns a metadata envelope (file path, size, checksums). Does not write the
  dataset.
- **Inputs**: positional `dataset_rid`, `file_path`; `--output`; optional
  `--start-transaction-rid`/`--end-transaction-rid` to bound the view.
- **Success**: metadata envelope; download bound applies.
- **Failure**: exit 4 if file missing; exit 8 if content read blocked.
- **Example**: `pal-found-datasets file content <DATASET_RID> path/to/data.csv --output data.csv`.

### file.delete

- **Class**: delete. Deletes a file from a branch.
- **Preconditions**: can write the dataset and its transaction.
- **Effect**: deletes the file; the deletion is part of a transaction.
- **Inputs**: positional `dataset_rid`, `file_path`; transaction and branch
  context.
- **Success**: returns the deleted file reference.
- **Failure**: exit 8 readonly block.
- **Example**: `pal-found-datasets file delete <DATASET_RID> path/to/data.csv`.

### file.get

- **Class**: read. Returns file metadata.
- **Preconditions**: can read the file.
- **Effect**: returns the file record (path, size, time).
- **Inputs**: positional `dataset_rid`, `file_path`; optional branch/transaction.
- **Success**: the file metadata record.
- **Failure**: exit 4 if file missing.
- **Example**: `pal-found-datasets file get <DATASET_RID> path/to/data.csv`.

### file.list

- **Class**: read. Lists files in a dataset branch (optionally a logical path).
- **Preconditions**: can read the dataset.
- **Effect**: returns a page of files.
- **Inputs**: positional `dataset_rid`; `--path`/branch, paging options.
- **Success**: files; empty if none.
- **Example**: `pal-found-datasets file list <DATASET_RID> --branch-name main`.

### file.upload

- **Class**: create. Uploads a file into a dataset branch.
- **Preconditions**: can write the dataset and its open transaction.
- **Effect**: writes the file bytes into the branch as part of a transaction.
- **Inputs**: positional `dataset_rid`; `--file-path` (local file) and target
  `--path`; transaction and branch context. Upload bound 16 MiB applies.
- **Success**: returns the created file record.
- **Failure**: exit 1 file too large/absent; exit 8 readonly block.
- **Example**: `pal-found-datasets file upload <DATASET_RID> --file-path ./data.csv --branch-name main`.

## Evidence and review

Reviewed against the installed `pal-found-datasets` parser and pinned SDK
sources (commit `2da67907`). `content` is a binary read; `upload` and `delete`
write within a transaction. Binary upload/download size bounds apply (AC-D-013-09).
No unsupported operation is documented as callable.
