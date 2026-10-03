---
name: pal-found-connectivity
description: Offline entry point for Foundry Connectivity API v2 CLI. Documents 20 Connection, FileImport, TableImport, and VirtualTable operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Connectivity CLI

## Capability and source

Foundry Connectivity manages external data sources: connections, file and
table imports from them, virtual tables, and JDBC driver uploads. The
`pal-found-connectivity` command exposes 20 Connection, FileImport,
TableImport, and VirtualTable operations.

Source: [Palantir data integration](https://www.palantir.com/docs/foundry/data-integration); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

20 Foundry Connectivity API v2 operations are available through the installed `pal-found-connectivity` command.

## Usage

```bash
pal-found-connectivity <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (where paging applies).

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
`--batch-pages`. JSON payloads use `--configuration-json`,
`--file-import-filters-json`, and `--secrets-json` where help shows them.
`upload_custom_jdbc_drivers` reads a bounded JDBC `.jar` file via `--file`.
Secrets are supplied only as JSON flags and are never echoed in output or
logs.

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

## File layout

```
.agents/skills/pal-found-connectivity/
├── SKILL.md
└── references/
    ├── 01-connection.md
    └── 02-imports.md
```

Copy the entire `pal-found-connectivity` folder, including `references/`, so
the relative links above resolve offline.
