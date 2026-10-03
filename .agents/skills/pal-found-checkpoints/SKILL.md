---
name: pal-found-checkpoints
description: Offline entry point for Foundry Checkpoints API v2 CLI. Documents 3 Record operations (get, get_batch, search) with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Checkpoints CLI

## Capability and source

Foundry Checkpoints stores named records that hold external system state for
coordination between jobs. The `pal-found-checkpoints` command exposes 3
`record` operations.

Source: [Palantir Foundry checkpoints](https://www.palantir.com/docs/foundry/data-integration); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

3 Foundry Checkpoints API v2 operations are available through the installed `pal-found-checkpoints` command.

## Usage

```bash
pal-found-checkpoints record <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (on paged search).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

| Part | Resource client | Operations |
| --- | --- | ---: |
| [Record operations](references/01-record.md) | `record` | 3 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`. JSON payloads use `--records-json` (batch RIDs) and `--where-json`
(search criteria).

## Install requirement

`pal-found-checkpoints` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found-checkpoints/
├── SKILL.md
└── references/
    └── 01-record.md
```

Copy the entire `pal-found-checkpoints` folder, including `references/`, so
the relative links above resolve offline.
