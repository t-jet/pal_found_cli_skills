# Branch operations

Datasets hold versioned files, with an optional schema for tabular reads. A transaction changes a
branch view; a branch is a pointer to transaction history. A View is a separate resource that reads
a union of backing datasets without storing their files. Most enrollments use `master` as the
default branch, but omit the branch flag to use the enrollment default.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-integration/datasets). The behavior below
describes the installed CLI commands. Replace
example identifiers and configuration values with values from your Foundry enrollment.

## Operation records

### branch.create

- **Behavior:** Creates a named branch on an existing dataset. With `--transaction-rid`, its head
  points to that dataset's specified open or committed transaction; an aborted transaction cannot
  be the head. Without the flag, Foundry creates the branch without a supplied head transaction.
- **Before use:** The dataset must exist and be writable. A supplied transaction must belong to
  that dataset and be open or committed.
- **Inputs:** positional `dataset_rid`; required `--name`; optional `--transaction-rid`.
  `transaction_rid`: The most recent OPEN or COMMITTED transaction on the branch. This will never be
  an ABORTED transaction.
- **Result:** `Branch`.
- **Failure or follow-up:** A duplicate branch name, invalid transaction, or insufficient permission
  rejects creation. Later calls identify the branch by name alongside the dataset RID.
- **Example:** `pal-found-datasets branch create DATASET_RID --name experiment --transaction-rid TRANSACTION_RID`

### branch.delete

- **Behavior:** Deletes the named branch pointer. It does not delete the dataset itself.
- **Before use:** The named branch must exist and you must be able to change the dataset.
- **Inputs:** positional `dataset_rid`; required `--branch-name`; optional none.
- **Result:** `None`.
- **Failure or follow-up:** A missing branch, invalid target, or insufficient permission rejects the
  removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-datasets branch delete DATASET_RID --branch-name experiment`

### branch.get

- **Behavior:** Gets the named branch and its current transaction head. Without `--branch-name`,
  Foundry selects the dataset's default branch (`master` in most enrollments).
- **Before use:** The dataset and selected branch must be readable.
- **Inputs:** positional `dataset_rid`; required none; optional `--branch-name`.
- **Result:** `Branch`.
- **Failure or follow-up:** A missing or inaccessible branch returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-datasets branch get DATASET_RID`

### branch.list

- **Behavior:** Lists the names and transaction heads of branches visible on the dataset.
- **Before use:** The dataset must be readable.
- **Inputs:** positional `dataset_rid`; required none; optional none.
- **Result:** `ListBranchesResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-datasets branch list DATASET_RID`

### branch.transactions

- **Behavior:** Get the Transaction history for the given Dataset. When requesting all transactions,
  the endpoint returns them in reverse chronological order.
- **Before use:** The dataset and selected branch must be readable.
- **Inputs:** positional `dataset_rid`; required none; optional `--branch-name`.
- **Parameter notes:** `--branch-name` selects the branch whose transaction history is returned; omit it for the default branch.
- **Result:** `ListTransactionsResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-datasets branch transactions DATASET_RID`
