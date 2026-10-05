---
name: pal-found-widgets
description: Inspect widget sets and releases, publish widget builds, and manage user dev mode through 8 CLI operations.
---

# Foundry Widgets CLI

## Capability and source

Custom widgets extend Workshop with frontend components such as tailored
charts or object views. A widget set is a permissioned resource containing
multiple widgets and versioned code from a repository. Publishing a build
creates a release; host applications choose which release to use. Dev mode
previews unpublished assets for the token's user only, so other users retain
the published version. `release` operations use a **widget set RID** and
semantic release version, while `repository` operations use a repository RID.
Dev mode expires after 24 hours. New widgets can be previewed in playground
or Code Workspaces before release; Workshop can select them only after first
publication. An inactive dev mode session displays published assets when the
development server supplies no override for a viewed widget.

Source: [Custom widgets](https://www.palantir.com/docs/foundry/custom-widgets/overview),
[core concepts](https://www.palantir.com/docs/foundry/custom-widgets/core-concepts),
[development](https://www.palantir.com/docs/foundry/custom-widgets/development).
Operation details: SDK `docs/v2/Widgets/` used to author this skill.

8 Foundry Widgets API v2 operations are available through the installed `pal-found-widgets` command.

## Usage

```bash
pal-found-widgets <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`; release
listing also accepts `--page-size`, `--page-token`, `--all`, `--max-pages`.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. `repository.publish` reads a bounded zip.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Widget repository and settings operations](references/01-repository.md) | `dev_mode_settings`, `release`, `repository`, `widget_set` | 8 |

## Parameters and JSON

`set-widget-set-by-id` requires `--widget-set-rid` and `--settings-json`.
`repository publish` requires `--repository-version` and a bounded zip file.

`--timeout` limits a request in seconds; `--format json|toon|auto` chooses
output encoding; `--pretty` indents it. Release listing accepts `--page-size`
as the requested number of releases, `--page-token` to resume from a returned
token, and `--all --max-pages` for bounded automatic traversal.
`--widget-set-rid` identifies the widget set whose dev overrides change;
`--settings-json` is its JSON override map. Publishing uses
`--repository-version` as the build version and `--file` as the local zip path.

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

- `dev-mode-settings disable` (operation `disable`)
- `dev-mode-settings get` (operation `get`)
- `dev-mode-settings pause` (operation `pause`)
- `dev-mode-settings set-widget-set` (operation `set-widget-set`)

Each is a negative check only: operations `disable`, `get`, `pause`, and
`set-widget-set` are unsupported. If a task
names one of them, stop and report that it is not supported by the installed
CLI.
