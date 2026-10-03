# Transaction operations

This part documents the `transaction` resource client (6 operations). A
transaction groups a set of changes to a dataset branch: it is created, edits
are applied, then it is `commit`ed or `abort`ed. Read the [Datasets
entry](SKILL.md) first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/datasets/scripts/pal_found_datasets_cli.py`;
SDK `foundry_sdk/v2/datasets/transaction.py` at pinned commit `2da67907`.
Reviewer architect (CODEREVIEW-044), 2026-10-03. QA baseline TESTCASE-003.

## Workflow

1. `transaction.create` an open (open) transaction on a branch.
2. Apply edits such as `file.upload`/`file.delete` against it.
3. `transaction.commit` to make the changes visible, or `transaction.abort` to
   discard them.
4. Read status with `transaction.get` and build output with `transaction.job`.

## Operation records

### transaction.abort

- **Class**: change. Discards an open transaction's changes.
- **Preconditions**: an open transaction on a branch you can write.
- **Effect**: aborts the transaction; its changes are not applied.
- **Inputs**: positional `dataset_rid`, `transaction_rid`; `--branch-name`.
- **Success**: returns the aborted transaction.
- **Failure**: exit 1 if the transaction is not open.
- **Example**: `pal-found-datasets transaction abort <DATASET_RID> <TXN_RID> --branch-name main`.

### transaction.build

- **Class**: execute (async). Builds the dataset from the transaction.
- **Preconditions**: write access; branch wants build-on-commit-compatible state.
- **Effect**: triggers a build/job for the transaction; acceptance is not proof
  the build finished.
- **Inputs**: positional `dataset_rid`, `transaction_rid`; branch options.
- **Success**: returns a build reference; check `transaction.job` for status.
- **Failure**: exit 1 invalid state; exit 3 permission.
- **Example**: `pal-found-datasets transaction build <DATASET_RID> <TXN_RID> --branch-name main`.

### transaction.commit

- **Class**: change. Commits an open transaction, making its changes visible.
- **Preconditions**: an open transaction on a writable branch.
- **Effect**: applies the transaction's changes to the branch.
- **Inputs**: positional `dataset_rid`, `transaction_rid`; `--branch-name`.
- **Success**: returns the committed transaction.
- **Failure**: exit 1 invalid state (already committed/aborted); exit 8 block.
- **Example**: `pal-found-datasets transaction commit <DATASET_RID> <TXN_RID> --branch-name main`.

### transaction.create

- **Class**: create. Opens a new transaction on a branch.
- **Preconditions**: can write the branch.
- **Effect**: creates an open transaction to group edits.
- **Inputs**: positional `dataset_rid`, `branch_id`; `--transaction-type`
  (e.g. SNAPSHOT/APPEND/UPDATE).
- **Success**: the created open transaction, including its RID.
- **Failure**: exit 1 invalid type; exit 8 readonly block.
- **Example**: `pal-found-datasets transaction create <DATASET_RID> main --transaction-type SNAPSHOT`.

### transaction.get

- **Class**: read. Returns a transaction's status and summary.
- **Preconditions**: can read the branch.
- **Effect**: returns transaction metadata.
- **Inputs**: positional `dataset_rid`, `transaction_rid`; `--branch-name`.
- **Success**: the transaction record and its status.
- **Failure**: exit 4 if missing.
- **Example**: `pal-found-datasets transaction get <DATASET_RID> <TXN_RID> --branch-name main`.

### transaction.job

- **Class**: read (async status). Returns the build job for a transaction.
- **Preconditions**: a transaction that had a build.
- **Effect**: returns the job/build status.
- **Inputs**: positional `dataset_rid`, `transaction_rid`.
- **Success**: the job record, showing whether the build succeeded/pending.
- **Failure**: exit 4 if no job for the transaction.
- **Example**: `pal-found-datasets transaction job <DATASET_RID> <TXN_RID>`.

## Evidence and review

Reviewed against the installed `pal-found-datasets` parser and pinned SDK
sources (commit `2da67907`). `commit`/`abort`/`build` change branch state;
`create` opens a transaction; `get`/`job` are reads. Async build work requires a
follow-up `get`/`job`; a zero exit does not prove the build finished
(AC-D-013-04/05). No unsupported operation is documented as callable.
