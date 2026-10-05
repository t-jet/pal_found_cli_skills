# Transaction operations

Datasets hold versioned files, with an optional schema for tabular reads. A transaction changes a
branch view; a branch is a pointer to transaction history. A View is a separate resource that reads
a union of backing datasets without storing their files. Most enrollments use `master` as the
default branch, but omit the branch flag to use the enrollment default.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-integration/datasets). The behavior below
describes the installed CLI commands. Replace
example identifiers and configuration values with values from your Foundry enrollment.

## Operation records

### transaction.abort

- **Behavior:** Aborts an open Transaction. File modifications made on this Transaction are not
  preserved and the Branch is not updated.
- **Before use:** The transaction must be open and belong to the specified dataset.
- **Inputs:** positional `dataset_rid`; required `--transaction-rid`; optional none.
- **Result:** `Transaction`.
- **Failure or follow-up:** The transaction must still be open; a state conflict or missing
  transaction is returned as a CLI error.
- **Example:** `pal-found-datasets transaction abort DATASET_RID --transaction-rid TRANSACTION_RID`

### transaction.build

- **Behavior:** Get the Build that computed the given Transaction. Not all Transactions have an
  associated Build. For example, if a Dataset is updated by a User uploading a CSV file into the
  browser, no Build will be tied to the Transaction.
- **Before use:** The dataset and transaction must be readable.
- **Inputs:** positional `dataset_rid`; required `--transaction-rid`; optional none.
- **Result:** `Optional[BuildRid]`. This is a read: it returns the build associated with a
  transaction when one exists; it does not start a build.
- **Failure or follow-up:** A missing or inaccessible transaction returns an error, except where the
  SDK declares an optional result.
- **Example:** `pal-found-datasets transaction build DATASET_RID --transaction-rid TRANSACTION_RID`

### transaction.commit

- **Behavior:** Commits an open Transaction. File modifications made on this Transaction are
  preserved and the Branch is updated to point to the Transaction.
- **Before use:** The transaction must be open and belong to the specified dataset.
- **Inputs:** positional `dataset_rid`; required `--transaction-rid`; optional none.
- **Result:** `Transaction`.
- **Failure or follow-up:** The transaction must still be open; a state conflict or missing
  transaction is returned as a CLI error.
- **Example:** `pal-found-datasets transaction commit DATASET_RID --transaction-rid TRANSACTION_RID`

### transaction.get

- **Behavior:** Gets a Transaction of a Dataset.
- **Before use:** The dataset and transaction must be readable.
- **Inputs:** positional `dataset_rid`; required `--transaction-rid`; optional none.
- **Result:** `Transaction`.
- **Failure or follow-up:** A missing or inaccessible transaction returns an error, except where the
  SDK declares an optional result.
- **Example:** `pal-found-datasets transaction get DATASET_RID --transaction-rid TRANSACTION_RID`

### transaction.job

- **Behavior:** Get the Job that computed the given Transaction. Not all Transactions have an
  associated Job. For example, if a Dataset is updated by a User uploading a CSV file into the
  browser, no Job will be tied to the Transaction.
- **Before use:** The dataset and transaction must be readable.
- **Inputs:** positional `dataset_rid`; required `--transaction-rid`; optional none.
- **Result:** `Optional[JobRid]`.
- **Failure or follow-up:** A missing or inaccessible transaction returns an error, except where the
  SDK declares an optional result.
- **Example:** `pal-found-datasets transaction job DATASET_RID --transaction-rid TRANSACTION_RID`

### transaction.create

- **Behavior:** Creates a Transaction on a Branch of a Dataset.
- **Before use:** The dataset branch must exist, be writable, and have no other open transaction.
- **Inputs:** positional `dataset_rid`; required `--transaction-type`; optional `--branch-name`.
  Choose `SNAPSHOT`, `APPEND`, `UPDATE`, or `DELETE` according to how this transaction should change
  the dataset view. The branch defaults to `master` for most enrollments.
- **Result:** `Transaction`.
- **Failure or follow-up:** An invalid configuration or insufficient permission rejects transaction
  creation; use the returned RID for later calls.
- **Example:** `pal-found-datasets transaction create DATASET_RID --transaction-type APPEND --branch-name master`
