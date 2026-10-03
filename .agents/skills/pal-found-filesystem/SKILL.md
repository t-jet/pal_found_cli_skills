---
name: pal-found-filesystem
description: Offline entry point for Foundry Filesystem API v2 CLI. Documents 31 Folder, Project, Resource, ResourceRole, and Space operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Filesystem CLI

## Capability and source

Foundry Filesystem organizes projects, folders, resources, spaces, markings,
and resource roles. The `pal-found-filesystem` command exposes 31 operations
across those five resource clients, including create, lookup, access metadata,
restore, and deletion.

Source: [Palantir Foundry overview](https://www.palantir.com/docs/foundry/getting-started/overview); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

31 Foundry Filesystem API v2 operations are available through the installed `pal-found-filesystem` command.

## Usage

```bash
pal-found-filesystem <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (where paging applies).

Paginated operations are folder `children`, project `organizations`, resource
`markings`, resource-role `list`, and space `list`.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Folder and project operations](references/01-folder-project.md) | `folder`, `project` | 12 |
| [Resource operations](references/02-resource.md) | `resource` | 11 |
| [Resource role and space operations](references/03-resource-role-space.md) | `resource_role`, `space` | 8 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--batch-pages`. JSON payloads use a positional `body` for batch and
replacement bodies, plus `--organizations`, `--organization-rids`, `--roles`,
`--role-grants`, `--default-roles`, `--deletion-policy-organizations`, and
`--variable-values` where command help shows them. Other variants include
required `--enrollment-rid`, `--parent-folder-rid`, `--template-rid`,
`--project-description`, `--display-name`, `--path`, `--marking-ids`,
`--space-rid`, and `--file-system-id`, with `--preview` and
`--include-inherited` as booleans. Additional scalar variants are
`--default-role-set-id`, `--description`,
`--resource-level-role-grants-allowed`, and `--usage-account-rid`.

## Install requirement

`pal-found-filesystem` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found-filesystem/
├── SKILL.md
└── references/
    ├── 01-folder-project.md
    ├── 02-resource.md
    └── 03-resource-role-space.md
```

Copy the entire `pal-found-filesystem` folder, including `references/`, so the
relative links above resolve offline.
