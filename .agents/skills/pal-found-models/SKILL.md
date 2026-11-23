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
Optional source: Palantir's [model integration overview](https://www.palantir.com/docs/foundry/model-integration/overview).
The operation records below explain each supported command.

Model Studio is Foundry's no-code model development tool. Users choose a
trainer, provide datasets, set configuration, and launch a training job. A
run records progress and results, and a successful trained model can be used
for inference in other Foundry workflows. The CLI exposes Model Studio
resources, configuration versions, trainers, and runs. `launch` starts work;
its response is not proof that training finished. Optional source: Palantir's
[Model Studio overview](https://www.palantir.com/docs/foundry/model-studio/overview).

23 Foundry Models API v2 operations are exposed by `pal-found-models`. Model creation and version
promotion change resources; artifact reads can transfer substantial data;
live deployment transforms run inference.

## Usage

The CLI and this skill must already be provisioned. Set `FOUNDRY_TOKEN` to an
authorized user token and `FOUNDRY_HOSTNAME` to your enrollment hostname before
running commands. Supply credentials through your environment's secret handling;
do not paste tokens into commands, examples, or logs. Missing or blank credentials
fail before a request. This CLI uses `UserTokenAuth`; it does not perform OAuth
login or create service users. For automation, obtain an approved token identity
and resource grants from your enrollment administrator. A service user must have
the same required resource access; having a token alone does not grant it.

Use an existing accessible parent folder to create models or studios. Training
also needs readable input datasets with schemas, existing writable output models,
an available trainer, and compute allowed by the project's resource queue. These
commands do not provision datasets, repositories, folders, queues, deployments,
or credentials. Obtain their RIDs and any required grants before starting.
Model-version creation also requires actual compatible serialized model code,
accessible backing repositories, and resolvable Conda requirements. Inference
requires a pre-existing live deployment and its model API.

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

Use `--format json` for predictable machine parsing. JSON request keys below use
SDK aliases such as `workerConfig`; typed response fields use SDK aliases
such as `workerConfig`. `--format toon` can fall back to JSON, including
typed results containing values the formatter cannot serialize to TOON. Inspect
actual output for your route; the requested format does not guarantee TOON.
Download commands print metadata and save bytes separately. Failed commands
return structured errors; check exit status before consuming output.

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
