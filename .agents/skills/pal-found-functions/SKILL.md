---
name: pal-found-functions
description: Offline entry point for Foundry Functions API v2 CLI. Documents 7 Query, ValueType, and VersionId operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Functions CLI

## Capability and source

Foundry Functions are server-side queries callable from the CLI. The
`pal-found-functions` command exposes 7 Query, ValueType, and VersionId
operations.

Source: [Palantir Functions](https://www.palantir.com/docs/foundry/functions); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

7 Foundry Functions API v2 operations are available through the installed `pal-found-functions` command.

## Usage

```bash
pal-found-functions <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Query, value type, and version id operations](references/01-query.md) | `query`, `value_type`, `version_id` | 7 |

## Parameters and JSON

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

## File layout

```
.agents/skills/pal-found-functions/
├── SKILL.md
└── references/
    └── 01-query.md
```

Copy the entire `pal-found-functions` folder, including `references/`, so the
relative links above resolve offline.
