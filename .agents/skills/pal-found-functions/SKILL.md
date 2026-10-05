---
name: pal-found-functions
description: Understand Foundry Functions and use seven Functions API v2 CLI operations to inspect and execute published queries and inspect value types.
---

# Foundry Functions CLI

## Capability and source

Foundry Functions run authored logic on the server in an isolated environment
for applications and operational workflows. A function can inspect Ontology
objects, follow links, compute a metric, or produce an Ontology edit when
authored for that purpose. Query functions expose typed inputs and outputs
through the API gateway. The CLI here executes published queries and reads
query or value-type definitions; it does not author or publish functions.
See Palantir's [Functions overview](https://www.palantir.com/docs/foundry/functions/overview)
and [query API guide](https://www.palantir.com/docs/foundry/functions/query-functions/).

Source: Palantir's Functions overview and query API guide linked above; method
the operation records below explain each supported command.

Use a query's API name for `execute`, `streaming_execute`, and `get`; use a RID
only for `get_by_rid` and `get_by_rid_batch`. Execution defaults to the latest
query version unless `--version` is supplied. The SDK marks `execute` as a
backward-compatibility endpoint and recommends `streaming_execute` for new
callers. That endpoint returns NDJSON, including a single line for a
nonstreaming function. Query execution can consume compute; inspecting query
or value-type metadata does not run the query.

7 Foundry Functions API v2 operations are exposed by `pal-found-functions`.

## Usage

```bash
pal-found-functions <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`.

`--timeout` sets the request timeout in seconds. `--format` selects JSON,
TOON, or automatic structured output; `--pretty` indents it.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Query, value type, and version id operations](references/01-query.md) | `query`, `value_type`, `version_id` | 7 |

## Parameters and JSON

Read [function identifiers and parameters](references/inputs.md) for query
API names, RIDs, and JSON payload shapes.

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`. Query execution uses JSON parameter payloads.

## Install requirement

`pal-found-functions` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```
