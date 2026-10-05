---
name: pal-found-datasets
description: Offline entry point for Foundry Datasets API v2 CLI. Documents 33 Dataset, Branch, File, Transaction, and View operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Datasets CLI

## Capability and source

Foundry datasets hold versioned collections of files. They can contain
tabular data with a schema, or unstructured files without one. A branch
points to transaction history. Committing a transaction updates the visible
files on that branch: `SNAPSHOT` replaces the current view, `APPEND` adds
files, `UPDATE` may replace files, and `DELETE` removes them. Transaction type
matters to downstream incremental pipelines.

Branches let engineers work on separate versions of data; Foundry does not
merge dataset branches. Most enrollments name the default branch `master`.
The `view` client manages a different resource: a union of backing datasets
that stores no files of its own. It can deduplicate on a primary key and can
be used as a transform input, but not as a transform output.

Read [dataset concepts](https://www.palantir.com/docs/foundry/data-integration/datasets),
[branching](https://www.palantir.com/docs/foundry/data-integration/branching),
and [Views](https://www.palantir.com/docs/foundry/data-integration/views)
for platform behavior. The 33 CLI operations below cover dataset metadata,
schemas, table reads, branch and file access, transactions, and Views.

Source: [Palantir dataset concepts](https://www.palantir.com/docs/foundry/data-integration/datasets).

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
per-operation records give inputs, behavior, results, and examples.

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
`--batch-pages`. Dataset RIDs are positional for most dataset, branch, file,
and transaction commands. Transaction RIDs use `--transaction-rid`; they are
not positional. `dataset get-schema-batch` takes a JSON list through
`--body-json` as an array of objects with `datasetRid`. Schema and View payloads are JSON values passed to the named
flags shown in their operation records. `file upload --file-path` opens a
local file and uses the same path as its dataset path; verify that path before
uploading. `transaction create` requires `--transaction-type` so Foundry knows
whether to replace, add, update, or delete files in the branch view.
`dataset read-table` requires `--table-format ARROW|CSV`; it and `file content`
save bytes under the configured download root, then print download metadata.
For both, `--output` is an optional filename only, not a full path.

### Parameter meanings

All positional `dataset_rid` values identify the dataset to read or change.
`--timeout` limits request duration; `--format` selects JSON, TOON, or automatic
output; `--pretty` indents structured output. On paged calls, `--page-size`
requests a page length, `--page-token` resumes from a returned token, and
`--batch-pages` caps pages fetched in one CLI call. A page may be short even
when another token exists.

| Parameter | Meaning |
| --- | --- |
| `--name`, `--view-name` | Name of a new dataset or View in its parent folder. |
| `--parent-folder-rid` | Existing folder in which to create the dataset or View. |
| `--branch-name`, `--branch` | Dataset branch to use, or View branch for View operations; omit to use the enrollment default. |
| `--transaction-rid` | Existing transaction to inspect, commit, abort, or use for a file change. |
| `--transaction-type` | How a new transaction changes the branch's file view: `SNAPSHOT`, `APPEND`, `UPDATE`, or `DELETE`. |
| `--start-transaction-rid`, `--end-transaction-rid` | Bounds of a historical dataset view for file or table reads. |
| `--file-path` | Dataset file path; for upload the CLI reads that same path locally. |
| `--path-prefix` | Limit listed dataset files to paths with this prefix. |
| `--schema` | JSON column schema to put on a dataset branch. |
| `--body-json` | JSON array of dataset RID objects for batch schema lookup. |
| `--table-format` | Byte format of a table download: `ARROW` or `CSV`. |
| `--columns-json`, `--row-limit` | Column names to project and maximum rows in a table download. |
| `--output` | Saved download filename, resolved under the configured download root. |
| `--view-dataset-rid` | RID of the View to inspect or change. |
| `--backing-datasets` | JSON array of dataset RID and branch pairs feeding a View; entries may also control marking propagation. |
| `--primary-key` | JSON key columns and duplicate-resolution rule for a View. |

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
