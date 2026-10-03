---
name: pal-found-widgets
description: Offline entry point for Foundry Widgets API v2 CLI. Documents 8 DevModeSettings, Release, Repository, and WidgetSet operations, and records 4 legacy design-catalogue operations as unsupported (negative checks only).
---

# Foundry Widgets CLI

## Capability and source

Foundry Widgets manage widget-set repositories, their releases, and dev-mode
settings. The `pal-found-widgets` command exposes 8 operations on the
installed runtime surface (DevModeSettings 2, Release 3, Repository 2,
WidgetSet 1).

Source: [Palantir Widgets](https://www.palantir.com/docs/foundry/widgets); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

8 Foundry Widgets API v2 operations are available through the installed `pal-found-widgets` command.

## Usage

```bash
pal-found-widgets <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (where paging applies).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. `repository.publish` reads a bounded zip.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Widget repository and settings operations](references/01-repository.md) | `dev_mode_settings`, `release`, `repository`, `widget_set` | 8 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--batch-pages`. `set_widget_set_by_id` uses `--settings-json`.

## Install requirement

`pal-found-widgets` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```

## Unsupported legacy operations

The older Widgets design catalogue contained these operations, which the
installed runtime does **not** expose. They are unsupported and must not be
invoked or presented as callable:

- `dev-mode-settings disable`
- `dev-mode-settings get`
- `dev-mode-settings pause`
- `dev-mode-settings set-widget-set`

These are negative checks only (SA-DES-012 section 4, AC-D-013-08). If a task
names one of them, stop and report that it is not supported by the installed
CLI.

## File layout

```
.agents/skills/pal-found-widgets/
├── SKILL.md
└── references/
    └── 01-repository.md
```

Copy the entire `pal-found-widgets` folder, including `references/`, so the
relative links above resolve offline.
