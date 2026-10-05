---
name: pal-found-models
description: Understand Foundry model lifecycle and use 23 Models API v2 CLI operations for versions, experiments, Model Studio, and live inference.
---

# Foundry Models CLI

## Capability and source

Foundry models are versioned artifacts that package machine learning logic.
Teams can train in Foundry or integrate existing artifacts, containers, and
external services. Model versions preserve distinct implementations. An
experiment records training runs and their metrics or artifacts; a live
deployment accepts inputs and returns inference results. Modeling Objectives
support evaluation, review, release, and deployment across that lifecycle.
See Palantir's [model integration overview](https://www.palantir.com/docs/foundry/model-integration/overview).

Source: Palantir's model integration and Model Studio overviews linked in this
section; the operation records below explain each supported command.

Model Studio is Foundry's no-code model development tool. Users choose a
trainer, provide datasets, set configuration, and launch a training job. A
run records progress and results, and a successful trained model can be used
for inference in other Foundry workflows. The CLI exposes Model Studio
resources, configuration versions, trainers, and runs. `launch` starts work;
its response is not proof that training finished. See Palantir's
[Model Studio overview](https://www.palantir.com/docs/foundry/model-studio/overview).

23 Foundry Models API v2 operations are exposed by `pal-found-models`. Model creation and version
promotion change resources; artifact reads can transfer substantial data;
live deployment transforms run inference.

## Usage

```bash
pal-found-models <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--all`, and `--max-pages` (where paging applies).

`--timeout` sets the request timeout in seconds. `--format` selects JSON,
TOON, or automatic structured output; `--pretty` indents it. For paged
operations, `--page-size` requests entries per page and `--page-token`
resumes from a returned cursor. `--all` retrieves up to the CLI page cap;
`--max-pages` sets a smaller page cap.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. Artifact and series reads download streamed data.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Model and experiment operations](references/01-models.md) | `model`, `model_version`, `experiment`, `experiment_artifact_table`, `experiment_series`, `live_deployment` | 13 |
| [Model Studio operations](references/02-model-studio.md) | `model_studio`, `model_studio_config_version`, `model_studio_run`, `model_studio_trainer` | 10 |

## Parameters and JSON

Read [model identifiers and JSON inputs](references/inputs.md) for model API,
trainer configuration, experiment, and deployment payloads.

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--all` or `--max-pages`. JSON payloads use `--model-api-json` and `--where-json`
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
