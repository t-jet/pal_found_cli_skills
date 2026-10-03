# View operations

This part documents the `view` resource client (6 operations). A view is a
derived dataset backed by one or more source datasets; its primary key defines
the identifying column(s). Read the [Datasets entry](SKILL.md) first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/datasets/scripts/pal_found_datasets_cli.py`;
SDK `foundry_sdk/v2/datasets/view.py` at pinned commit `2da67907`. Reviewer
architect (CODEREVIEW-044), 2026-10-03. QA baseline TESTCASE-003.

## Workflow

1. `view.create` the view dataset.
2. Add backing datasets (`view.add_backing_datasets`) and set the primary key
   (`view.add_primary_key`).
3. Read `view.get`; update backing with `replace_backing_datasets` or remove
   with `remove_backing_datasets` as needed.

## Operation records

### view.add_backing_datasets

- **Class**: change. Adds backing datasets to a view.
- **Preconditions**: can write the view.
- **Effect**: registers additional source datasets behind the view.
- **Inputs**: positional `view_dataset_rid`; `--backing-datasets` JSON list.
- **Success**: returns the updated view.
- **Example**: `pal-found-datasets view add-backing-datasets <VIEW_RID> --backing-datasets '["ri.foundry.main.dataset.s1"]'`.

### view.add_primary_key

- **Class**: change. Sets the primary key on a view.
- **Preconditions**: can write the view.
- **Effect**: defines which column(s) make rows unique in the view.
- **Inputs**: positional `view_dataset_rid`; `--primary-key` (list).
- **Success**: returns the updated view.
- **Example**: `pal-found-datasets view add-primary-key <VIEW_RID> --primary-key '["order_id"]'`.

### view.create

- **Class**: create. Creates a view dataset.
- **Preconditions**: a parent folder and a derived name.
- **Effect**: creates a view; returns its RID.
- **Inputs**: required `--name`, `--parent-folder-rid`; `--backing-datasets`,
  `--primary-key` as needed.
- **Success**: the created view dataset.
- **Failure**: exit 1 invalid input; exit 8 readonly block.
- **Example**: `pal-found-datasets view create --name "OrderView" --parent-folder-rid ri.foundry.main.folder.f1 --backing-datasets '["ri.foundry.main.dataset.s1"]' --primary-key '["order_id"]'`.

### view.get

- **Class**: read. Returns a view dataset.
- **Preconditions**: can read the view.
- **Effect**: returns the view record and its backing/primary key metadata.
- **Inputs**: positional `view_dataset_rid`.
- **Success**: the view record.
- **Failure**: exit 4 if missing.
- **Example**: `pal-found-datasets view get <VIEW_RID>`.

### view.remove_backing_datasets

- **Class**: change. Removes backing datasets from a view.
- **Preconditions**: can write the view.
- **Effect**: unregisters source datasets from the view.
- **Inputs**: positional `view_dataset_rid`; `--backing-datasets` JSON list.
- **Success**: returns the updated view.
- **Example**: `pal-found-datasets view remove-backing-datasets <VIEW_RID> --backing-datasets '["ri.foundry.main.dataset.s1"]'`.

### view.replace_backing_datasets

- **Class**: change. Replaces the full set of backing datasets.
- **Preconditions**: can write the view.
- **Effect**: replaces backing with the provided set; sources no longer listed
  are removed.
- **Inputs**: positional `view_dataset_rid`; `--backing-datasets` JSON list.
- **Success**: returns the updated view.
- **Example**: `pal-found-datasets view replace-backing-datasets <VIEW_RID> --backing-datasets '["ri.foundry.main.dataset.s2"]'`.

## Evidence and review

Reviewed against the installed `pal-found-datasets` parser and pinned SDK
sources (commit `2da67907`). `create` and the backing/primary-key writes change
the view; `get` is a read. `replace_backing_datasets` is destructive to the
listed-but-removed sources' view membership. No unsupported operation is
documented as callable.
