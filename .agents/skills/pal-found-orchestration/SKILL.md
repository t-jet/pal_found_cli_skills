---
name: pal-found-orchestration
description: Offline entry point for Foundry Orchestration API v2 CLI. Documents 20 Build, Job, Schedule, and ScheduleVersion operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Orchestration CLI

## Capability and source

Foundry builds compute new versions of datasets. A build coordinates jobs;
each job runs a defined unit of work and can write one or more output
datasets. A one-time `build create` starts a build from its target and branch
configuration. Inspect the build and its jobs for progress, failures, and
output rather than treating a successful start request as completed work.

Schedules repeat builds when their trigger conditions are met. The trigger
can depend on time, changed data, changed logic, or a combination. A schedule
run records whether it started a build, was ignored because there was no
work, or failed; a successful run still does not mean its build succeeded.
Scope matters: a user-scoped schedule's buildable outputs depend on the
user's current permissions. Read [build concepts](https://www.palantir.com/docs/foundry/data-integration/builds)
and [schedule concepts](https://www.palantir.com/docs/foundry/data-integration/schedules).
The CLI exposes 20 build, job, schedule, and schedule-version operations.

Source: [Palantir build concepts](https://www.palantir.com/docs/foundry/data-integration/builds).

20 Foundry Orchestration API v2 operations are available through the installed `pal-found-orchestration` command.

## Usage

```bash
pal-found-orchestration <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--all`, `--max-pages` (where paging applies).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Build and job operations](references/01-build-job.md) | `build`, `job` | 8 |
| [Schedule operations](references/02-schedule.md) | `schedule`, `schedule_version` | 12 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--all` and `--max-pages`. JSON payloads use `--target-json`,
`--fallback-branches-json`, `--action-json`, `--trigger-json`,
`--scope-mode-json`, and search filters such as `--where-json`. For
`build create`, the target and fallback branches are required. For schedule
create or replace, action, trigger, and scope mode are required. Read the
operation record for the other flags and the returned status.

## Install requirement

`pal-found-orchestration` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```
