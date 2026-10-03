# Branch operations

This part documents the `branch` resource client (5 operations). A branch is a
named line of a dataset's history; most datasets have a default branch (for
example `main`). Read the [Datasets entry](SKILL.md) first.

Source/pins: CLI parser
`pal_found_cli_tool/src/pal_found_cli/datasets/scripts/pal_found_datasets_cli.py`;
SDK `foundry_sdk/v2/datasets/branch.py` at pinned commit `2da67907`. Reviewer
architect (CODEREVIEW-044), 2026-10-03. QA baseline TESTCASE-003.

## Operation records

### branch.create

- **Class**: create. Creates a new branch on a dataset.
- **Preconditions**: can write the dataset; the branch name is not already used.
- **Effect**: creates a branch (optionally from an existing branch's content).
- **Inputs**: positional `dataset_rid`; `--branch-name`, `--name`; optional
  `--fork-branch`/`--transaction-rid` to start from existing content.
- **Success**: the created branch record.
- **Failure**: exit 1 duplicate branch name; exit 8 readonly block.
- **Example**: `pal-found-datasets branch create <DATASET_RID> --name dev`.

### branch.delete

- **Class**: delete. Deletes a branch.
- **Preconditions**: can write the dataset; confirm the branch's work is not
  needed (deleting a branch can remove its open transactions).
- **Effect**: deletes the branch.
- **Inputs**: positional `dataset_rid`, `branch_id` (branch name).
- **Success**: returns the deleted branch.
- **Failure**: exit 4 if branch not found.
- **Example**: `pal-found-datasets branch delete <DATASET_RID> dev`.

### branch.get

- **Class**: read. Returns a single branch.
- **Preconditions**: can read the dataset.
- **Effect**: returns the branch record.
- **Inputs**: positional `dataset_rid`, `branch_id`.
- **Success**: the branch record.
- **Failure**: exit 4 if branch missing.
- **Example**: `pal-found-datasets branch get <DATASET_RID> main`.

### branch.list

- **Class**: read. Lists a dataset's branches.
- **Preconditions**: can read the dataset.
- **Effect**: returns a page of branches.
- **Inputs**: positional `dataset_rid`; paging options.
- **Success**: branches; empty if none.
- **Example**: `pal-found-datasets branch list <DATASET_RID> --page-size 50`.

### branch.transactions

- **Class**: read. Lists transactions on a branch.
- **Preconditions**: can read the dataset.
- **Effect**: returns transactions on the branch, paged.
- **Inputs**: positional `dataset_rid`, `branch_id`; paging options.
- **Success**: transactions; empty if none.
- **Example**: `pal-found-datasets branch transactions <DATASET_RID> main`.

## Evidence and review

Reviewed against the installed `pal-found-datasets` parser and pinned SDK
sources (commit `2da67907`). `create` and `delete` write; the rest are reads.
Deleting a branch with open transactions is destructive; confirm before
invoking. No unsupported operation is documented as callable.
