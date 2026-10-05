# View operations

Datasets hold versioned files, with an optional schema for tabular reads. A transaction changes a
branch view; a branch is a pointer to transaction history. A View is a separate resource that reads
a union of backing datasets without storing their files. Most enrollments use `master` as the
default branch, but omit the branch flag to use the enrollment default.

Platform context: [Palantir
documentation](https://www.palantir.com/docs/foundry/data-integration/datasets). The behavior below
describes the installed CLI commands. Replace
example identifiers and configuration values with values from your Foundry enrollment.

## Operation records

### view.add_backing_datasets

- **Behavior:** Adds one or more backing datasets to a View. Any duplicates with the same dataset
  RID and branch name are ignored.
- **Before use:** The View must be writable. Each backing dataset must be accessible, have a schema,
  and live in the View's project or be added there as a project reference.
- **Inputs:** positional none; required `--view-dataset-rid`, `--backing-datasets`; optional
  `--branch`. `view_dataset_rid`: The rid of the View.
- **Parameter notes:** `--branch` selects the View branch whose backing dataset list changes.
- **Result:** `View`.
- **Failure or follow-up:** Invalid identifiers or insufficient permission reject the change; read
  the view afterward to verify its state.
- **Example:** `pal-found-datasets view add-backing-datasets --view-dataset-rid VIEW_DATASET_RID --backing-datasets '[{"datasetRid":"ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da","stopPropagatingMarkingIds":["18212f9a-0e63-4b79-96a0-aae04df23336"],"branch":"master"}]'`

### view.remove_backing_datasets

- **Behavior:** Removes specified backing datasets from a View. Removing a dataset triggers a
  SNAPSHOT transaction on the next update. If a specified dataset does not exist, no error is
  thrown.
- **Before use:** The View must be writable; identify the exact backing dataset RID and branch to
  remove. A dataset not currently backing the View is ignored.
- **Inputs:** positional none; required `--view-dataset-rid`, `--backing-datasets`; optional
  `--branch`. `view_dataset_rid`: The rid of the View.
- **Parameter notes:** `--branch` selects the View branch from which the listed backing datasets are removed.
- **Result:** `View`.
- **Failure or follow-up:** A missing view, invalid target, or insufficient permission rejects the
  removal. Confirm the resulting state with a read operation.
- **Example:** `pal-found-datasets view remove-backing-datasets --view-dataset-rid VIEW_DATASET_RID --backing-datasets '[{"datasetRid":"ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da","stopPropagatingMarkingIds":["18212f9a-0e63-4b79-96a0-aae04df23336"],"branch":"master"}]'`

### view.replace_backing_datasets

- **Behavior:** Replaces the backing datasets for a View. Removing any backing dataset triggers a
  SNAPSHOT transaction the next time the View is updated.
- **Before use:** The View must be writable. New backing datasets need schemas and must be in the
  View's project or added there as project references.
- **Inputs:** positional none; required `--view-dataset-rid`, `--backing-datasets`; optional
  `--branch`. `view_dataset_rid`: The rid of the View.
- **Parameter notes:** `--branch` selects the View branch whose full backing dataset list is replaced.
- **Result:** `View`.
- **Failure or follow-up:** Invalid input or insufficient access to the view is returned through the
  CLI error envelope.
- **Example:** `pal-found-datasets view replace-backing-datasets --view-dataset-rid VIEW_DATASET_RID --backing-datasets '[{"datasetRid":"ri.foundry.main.dataset.c26f11c8-cdb3-4f44-9f5d-9816ea1c82da","stopPropagatingMarkingIds":["18212f9a-0e63-4b79-96a0-aae04df23336"],"branch":"master"}]'`

### view.add_primary_key

- **Behavior:** Adds a primary key to a View that does not already have one. Primary keys are
  treated as guarantees provided by the creator of the dataset.
- **Before use:** The View must be writable and must not already have a primary key. Choose columns
  present in its backing datasets and a resolution rule that fits the data.
- **Inputs:** positional none; required `--view-dataset-rid`, `--primary-key`; optional `--branch`.
  `view_dataset_rid`: The rid of the View.
- **Parameter notes:** `--branch` selects the View branch on which to add the primary key.
- **Result:** `View`.
- **Failure or follow-up:** Invalid identifiers or insufficient permission reject the change; read
  the view afterward to verify its state.
- **Example:** `pal-found-datasets view add-primary-key --view-dataset-rid VIEW_DATASET_RID --primary-key '{"columns":["colA"],"resolution":{"type":"duplicate","deletionColumn":"deletionCol","resolutionStrategy":{"type":"latestWins","columns":["colB","colC"]}}}'`

### view.create

- **Behavior:** Create a new View.
- **Before use:** Choose a writable parent folder and backing datasets with compatible schemas.
- **Inputs:** positional none; required `--view-name`, `--parent-folder-rid`, and
  `--backing-datasets` as a JSON array of dataset RID and branch selections. Optional
  `--branch` selects the view branch and `--primary-key` supplies key configuration.
- **Parameter notes:** `--branch` names the initial View branch; `--primary-key` gives key columns and a duplicate-resolution rule for the new View.
- **Result:** `View`.
- **Failure or follow-up:** An invalid configuration or insufficient permission rejects view
  creation; use the returned RID for later calls.
- **Example:** `pal-found-datasets view create --view-name Orders --parent-folder-rid PARENT_FOLDER_RID --backing-datasets '[{"datasetRid":"DATASET_RID","branch":"master"}]'`

### view.get

- **Behavior:** Get metadata for a View.
- **Before use:** The View must exist and be readable.
- **Inputs:** positional none; required `--view-dataset-rid`; optional `--branch`.
  `view_dataset_rid`: The rid of the View.
- **Parameter notes:** `--branch` selects the View branch whose metadata is read.
- **Result:** `View`.
- **Failure or follow-up:** A missing or inaccessible view returns an error, except where the SDK
  declares an optional result.
- **Example:** `pal-found-datasets view get --view-dataset-rid VIEW_DATASET_RID`
