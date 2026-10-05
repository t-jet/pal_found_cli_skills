---
name: pal-found-sql-queries
description: Run SELECT queries over Foundry datasets, query Ontology data, inspect execution, and retrieve Arrow results.
---

# Foundry SQL Queries CLI

## Capability and source

Foundry SQL Queries lets authorized users analyze datasets with SELECT-only
Spark SQL. Dataset queries run asynchronously: submission returns status and
an ID, status can be polled, and results are downloaded as Apache Arrow.
Ontology SQL is a separate private-beta path that returns Arrow bytes
synchronously. The CLI exposes both paths through five `query` operations.

Source: [Palantir SQL access to Foundry datasets](https://www.palantir.com/docs/foundry/analytics-connectivity/odbc-jdbc-drivers/#use-sql-to-query-foundry-datasets).

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
`--pretty`. Both execution commands require `--query`. Dataset execution
accepts `--fallback-branch-ids-json`; Ontology execution accepts
`--dry-run`, `--parameters-json`, and `--row-limit`.
`get-results` accepts `--output`.

`--timeout` limits a request in seconds; `--format json|toon|auto` chooses
metadata encoding; `--pretty` indents structured output. `--query` is the SQL
text. `--fallback-branch-ids-json` gives an ordered JSON array of dataset
branch names. For Ontology SQL, `--dry-run` validates a query, `--row-limit`
caps returned rows, and `--parameters-json` supplies typed query values.
`--output` names the saved Arrow file within the configured download directory.

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
