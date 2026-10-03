---
name: pal-found-sql-queries
description: Offline entry point for Foundry SQL Queries API v2 CLI. Documents 5 SqlQuery operations (cancel, execute, execute_ontology, get_results, get_status) with preconditions, effect, inputs, result, and failure offline.
---

# Foundry SQL Queries CLI

## Capability and source

Foundry SQL Queries runs ad-hoc SQL against Foundry data and returns Arrow
result bytes. The `pal-found-sql-queries` command exposes 5 `sql_query`
operations. The CLI resource subcommand is `query`.

Source: [Palantir SQL queries](https://www.palantir.com/docs/foundry/sql); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

5 Foundry SQL Queries API v2 operations are available through the installed `pal-found-sql-queries` command.

## Usage

```bash
pal-found-sql-queries query <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. Arrow result bytes are downloaded via the shared
binary handler.

## Operation index

| Part | Resource client | Operations |
| --- | --- | ---: |
| [SQL query lifecycle](references/01-query.md) | `sql_query` (CLI `query`) | 5 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`. Query execution uses `--query-string` and `--parameters-json`,
`--fallback-branch-ids-json` where shown.

## Install requirement

`pal-found-sql-queries` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found-sql-queries/
├── SKILL.md
└── references/
    └── 01-query.md
```

Copy the entire `pal-found-sql-queries` folder, including `references/`, so
the relative links above resolve offline.
