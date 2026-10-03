---
name: pal-found-data-health
description: Offline entry point for Foundry Data Health API v2 CLI. Documents 6 Check and CheckReport operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Data Health CLI

## Capability and source

Foundry Data Health runs checks that report on data quality and a dataset's
readiness. The `pal-found-data-health` command exposes 6 Check and
CheckReport operations.

Source: [Palantir data health](https://www.palantir.com/docs/foundry/data-health); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

6 Foundry Data Health API v2 operations are available through the installed `pal-found-data-health` command.

## Usage

```bash
pal-found-data-health <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Check and check-report operations](references/01-check-report.md) | `check`, `check_report` | 6 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`. Check payloads use JSON flags for the check definition.

## Install requirement

`pal-found-data-health` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found-data-health/
├── SKILL.md
└── references/
    └── 01-check-report.md
```

Copy the entire `pal-found-data-health` folder, including `references/`, so
the relative links above resolve offline.
