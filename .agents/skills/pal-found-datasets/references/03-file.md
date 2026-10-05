# File operations

Datasets hold versioned files, with an optional schema for tabular reads. A transaction changes a
branch view; a branch is a pointer to transaction history. A View is a separate resource that reads
a union of backing datasets without storing their files. Most enrollments use `master` as the
default branch, but omit the branch flag to use the enrollment default.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-integration/datasets). The behavior below
describes the installed CLI commands. Replace
example identifiers and configuration values with values from your Foundry enrollment.

## Operation records

### file.content

- **Behavior:** Reads the bytes of a dataset file. With no branch or transaction range, Foundry
  resolves the latest view of the default branch. `--branch-name` chooses another branch;
  transaction RIDs narrow the historical view being read.
- **Before use:** The dataset and requested file or transaction view must be readable.
- **Inputs:** positional `dataset_rid`; required `--file-path`; optional `--output`, `--branch-name`,
  `--start-transaction-rid`, `--end-transaction-rid`. `branch_name`: The name of the Branch that
  contains the File. Defaults to `master` for most enrollments. `start_transaction_rid`: The
  Resource Identifier (RID) of the start Transaction. `end_transaction_rid`: The Resource Identifier
  (RID) of the end Transaction.
- **Parameter notes:** `--start-transaction-rid` and `--end-transaction-rid` select the historical transaction range whose file bytes are read.
- **Result:** Saves the file bytes under the configured download root and prints JSON metadata with
  the saved path, byte count, checksums, and MIME type. `--output` sets a basename, not a path;
  omitting it lets the download handler choose a filename.
- **Failure or follow-up:** A missing or inaccessible file returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-datasets file content DATASET_RID --file-path orders.csv --output orders.csv`

### file.delete

- **Behavior:** Removes a file from the latest dataset view while leaving historical views intact.
  By default Foundry opens and commits a delete transaction on the default branch. With
  `--transaction-rid`, it writes the deletion into an already open `DELETE` transaction, which the
  caller must later commit or abort.
- **Before use:** The file path must exist in the dataset view; a supplied transaction RID must
  identify an open DELETE transaction.
- **Inputs:** positional `dataset_rid`; required `--file-path`; optional `--transaction-rid`.
  `transaction_rid`: The Resource Identifier (RID) of the open delete Transaction on which to delete
  the File.
- **Result:** `None`.
- **Failure or follow-up:** A missing file, invalid target, or insufficient permission rejects the
  removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-datasets file delete DATASET_RID --file-path orders.csv`

### file.get

- **Behavior:** Reads a file's metadata, rather than its content, from the selected branch or
  transaction range. Without selectors it uses the latest view of the default branch.
- **Before use:** The dataset and requested file or transaction view must be readable.
- **Inputs:** positional `dataset_rid`; required `--file-path`; optional `--branch-name`,
  `--start-transaction-rid`, and `--end-transaction-rid` to select the dataset view.
- **Parameter notes:** `--branch-name` selects the branch. `--start-transaction-rid` and `--end-transaction-rid` select the historical view whose file metadata is read.
- **Result:** `File`.
- **Failure or follow-up:** A missing or inaccessible file returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-datasets file get DATASET_RID --file-path orders.csv`

### file.list

- **Behavior:** Lists file metadata for the resolved dataset view in pages. By default the SDK uses
  the latest view of the default branch; branch and transaction range flags select another view.
- **Before use:** The dataset and requested file or transaction view must be readable.
- **Inputs:** positional `dataset_rid`; required none; optional `--branch-name`,
  `--path-prefix`, `--start-transaction-rid`, and `--end-transaction-rid`.
- **Parameter notes:** `--branch-name` selects the branch; `--path-prefix` filters listed file paths. `--start-transaction-rid` and `--end-transaction-rid` select a historical transaction range.
- **Result:** `ListFilesResponse`.
- **Failure or follow-up:** An empty page is not proof there are no more results; follow the
  returned page token when present.
- **Example:** `pal-found-datasets file list DATASET_RID`

### file.upload

- **Behavior:** Reads a local file and uploads its bytes into the dataset. Without
  `--transaction-rid`, Foundry creates and commits a transaction on the default branch. With an open
  transaction RID, the upload is part of that transaction and becomes visible after commit.
  Uploading an existing dataset path makes the latest version visible in the new view.
- **Before use:** The local file must exist. The dataset must be writable; a supplied transaction
  RID must identify an open compatible transaction.
- **Inputs:** positional `dataset_rid`; required `--file-path`; optional `--transaction-rid`.
  `transaction_rid`: The Resource Identifier (RID) of the open Transaction on which to upload the
  File.
- **Result:** `File`. `--file-path` names a local file that the CLI reads and passes to the SDK
  under the same dataset path.
- **Failure or follow-up:** A missing local file, upload size limit, incompatible open transaction,
  or missing dataset write permission fails the upload. After a manual transaction, commit it to
  make the file visible on the branch.
- **Example:** `pal-found-datasets file upload DATASET_RID --file-path orders.csv`
