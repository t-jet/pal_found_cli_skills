---
name: pal-found-connectivity
description: Offline entry point for Foundry Connectivity API v2 CLI. Documents 20 Connection, FileImport, TableImport, and VirtualTable operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Connectivity CLI

## Capability and source

Foundry Data Connection provides a controlled path from external files,
databases, and warehouses into Foundry. A connection identifies the source,
its runtime, and credentials. A file import selects files and writes them to
a dataset; a table import, also called a batch sync, copies tabular data with
a schema into a dataset. The import definition can be created, inspected,
replaced, and executed. Execution is separate from defining the import and
updates the output dataset only after the sync finishes.

Virtual tables are different: for supported sources, Foundry can query the
remote table without first storing a copy in a dataset. Read [Data Connection
concepts](https://www.palantir.com/docs/foundry/data-connection/core-concepts),
[file syncs](https://www.palantir.com/docs/foundry/data-connection/file-based-syncs/),
and [virtual tables](https://www.palantir.com/docs/foundry/data-integration/virtual-tables/index.html).
The CLI exposes 20 connection, import, and virtual-table operations.

Source: [Palantir Data Connection concepts](https://www.palantir.com/docs/foundry/data-connection/core-concepts).

20 Foundry Connectivity API v2 operations are available through the installed `pal-found-connectivity` command.

## Usage

```bash
pal-found-connectivity <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--all`, `--max-pages` (for import lists).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Connection operations](references/01-connection.md) | `connection` | 7 |
| [File and table import operations](references/02-imports.md) | `file_import`, `table_import`, `virtual_table` | 13 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--all` and `--max-pages`. JSON payloads use `--configuration-json`,
`--filters-json`, `--config-json`, and `--secrets-json` where help shows them.
`file-import create` takes positional `connection_rid` plus required
`--dataset-rid`, `--display-name`, `--filters-json`, and `--import-mode`.
`table-import create` takes a connection RID, output dataset RID, name,
import mode, and `--config-json`.
`upload_custom_jdbc_drivers` reads a bounded JDBC `.jar` file via `--file`.
Secret values passed through `--secrets-json` are command-line arguments;
handle them according to your shell and environment's secret-handling rules.

## Install requirement

`pal-found-connectivity` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```
