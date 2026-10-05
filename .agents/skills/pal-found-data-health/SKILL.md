---
name: pal-found-data-health
description: Define dataset health checks and read evaluation reports through the Foundry Data Health API.
---

# Foundry Data Health CLI

## Capability and source

Foundry Data Health monitors resources for operational and data-quality
problems. Monitoring views apply rules across a project, folder, or resource;
their coverage can grow as resources are added. Health checks validate an
individual resource in detail, including dataset content and schema. A check
stores a rule; each evaluation creates a report with the result and a snapshot
of that rule. Time-based checks can evaluate when a dataset updates or passes
a configured threshold, or on a regular manual schedule. Creating a check
therefore need not create a report immediately. Both monitoring views and
health checks can generate alerts.
Users can receive alerts in Foundry, email digests, or configured external
systems. This CLI covers six check and report operations. It does not manage
monitoring views, alert subscriptions, or notification integrations.

Source: [Data Health overview](https://www.palantir.com/docs/foundry/observability/data-health), [check evaluation](https://www.palantir.com/docs/foundry/health-checks/check-evaluation), and SDK `docs/v2/DataHealth/{Check,CheckReport}.md`.

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
`--pretty`. `create` and `replace` require `--config-json`, a typed check
configuration. `get-latest` accepts `--limit` (default 10, maximum 100).
Read [check and report operations](references/01-check-report.md) before
replacing a rule: its type cannot change after creation.

`--timeout` limits a request in seconds; `--format json|toon|auto` selects
output encoding; `--pretty` indents structured output. For check creation,
`--config-json` defines the rule and its subject, while `--intent` records why
it exists. For replacement, the configuration changes the existing rule but
does not change its subject. `--limit` on `get-latest` caps returned reports.

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
