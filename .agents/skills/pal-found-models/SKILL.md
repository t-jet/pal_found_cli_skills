---
name: pal-found-models
description: Offline entry point for Foundry Models API v2 CLI. Documents 23 Model, ModelVersion, Experiment, ModelStudio, LiveDeployment operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Models CLI

## Capability and source

Foundry Models manages ML model artifacts, their versions, live deployments,
experiments, and Model Studio resources. The `pal-found-models` command
exposes 23 operations across those resource clients.

Source: [Palantir Models](https://www.palantir.com/docs/foundry/model-integration); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

23 Foundry Models API v2 operations are available through the installed `pal-found-models` command.

## Usage

```bash
pal-found-models <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (where paging applies).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. Artifact and series reads download streamed data.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Model and experiment operations](references/01-models.md) | `model`, `model_version`, `experiment`, `experiment_artifact_table`, `experiment_series`, `live_deployment` | 13 |
| [Model Studio operations](references/02-model-studio.md) | `model_studio`, `model_studio_config_version`, `model_studio_run`, `model_studio_trainer` | 10 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--batch-pages`. JSON payloads use `--model-api-json` and `--where-json`
where help shows them.

## Install requirement

`pal-found-models` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found-models/
├── SKILL.md
└── references/
    ├── 01-models.md
    └── 02-model-studio.md
```

Copy the entire `pal-found-models` folder, including `references/`, so the
relative links above resolve offline.
