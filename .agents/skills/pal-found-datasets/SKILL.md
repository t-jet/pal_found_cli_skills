---
name: pal-found-datasets
description: Offline entry point for Foundry Datasets API v2 CLI. Documents 33 Dataset, Branch, File, Transaction, and View operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Datasets CLI

## Capability and source

Foundry Datasets stores tabular data with branches, transactions, schemas,
files, and derived views. The `pal-found-datasets` command exposes 33 Dataset,
Branch, File, Transaction, and View operations for those lifecycle and read
paths.

Source: [Palantir data integration](https://www.palantir.com/docs/foundry/data-integration/application-reference); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

33 Foundry Datasets API v2 operations are available through the installed `pal-found-datasets` command.

## Usage

```bash
pal-found-datasets <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (where paging applies).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. Its parser is built from `_add_operation` loops;
per-operation records cite the CLI and SDK source locators.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Dataset operations](references/01-dataset.md) | `dataset` | 11 |
| [Branch operations](references/02-branch.md) | `branch` | 5 |
| [File operations](references/03-file.md) | `file` | 5 |
| [Transaction operations](references/04-transaction.md) | `transaction` | 6 |
| [View operations](references/05-view.md) | `view` | 6 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--batch-pages`. Dataset, branch, file, transaction, and view commands use a
positional `dataset_rid` where shown. Batch dataset IDs use required
`--dataset-r` (a JSON list). Required scalar variants include `--name`,
`--parent-folder-rid`, `--branch-name`, `--file-path`, `--transaction-rid`,
`--view-dataset-rid`, and `--primary-key`. JSON or list payloads use
`--schema`, `--backing-datasets`, and `--primary-key` in operation-specific
forms; `--branch` selects a view or table branch. File content variants accept
`--start-transaction-rid` and `--end-transaction-rid`. The exact flag set is
per-operation; read the record before invoking.

## Install requirement

`pal-found-datasets` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```

## File layout

```
.agents/skills/pal-found-datasets/
├── SKILL.md
└── references/
    ├── 01-dataset.md
    ├── 02-branch.md
    ├── 03-file.md
    ├── 04-transaction.md
    └── 05-view.md
```

Copy the entire `pal-found-datasets` folder, including `references/`, so the
relative links above resolve offline.
