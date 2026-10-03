---
name: pal-found-orchestration
description: Offline entry point for Foundry Orchestration API v2 CLI. Documents 20 Build, Job, Schedule, and ScheduleVersion operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Orchestration CLI

## Capability and source

Foundry Orchestration manages scheduled builds, jobs, and schedules. The
`pal-found-orchestration` command exposes 20 Build, Job, Schedule, and
ScheduleVersion operations.

Source: [Palantir Orchestration](https://www.palantir.com/docs/foundry/orchestration); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

20 Foundry Orchestration API v2 operations are available through the installed `pal-found-orchestration` command.

## Usage

```bash
pal-found-orchestration <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (where paging applies).

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
`--batch-pages`. JSON payloads use `--target-json` and `--where-json` where
help shows them.

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

## File layout

```
.agents/skills/pal-found-orchestration/
├── SKILL.md
└── references/
    ├── 01-build-job.md
    └── 02-schedule.md
```

Copy the entire `pal-found-orchestration` folder, including `references/`, so
the relative links above resolve offline.
