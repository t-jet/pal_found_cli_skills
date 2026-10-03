---
name: pal-found-third-party-applications
description: Offline entry point for Foundry Third-Party Applications API v2 CLI. Documents 9 ThirdPartyApplication, Website, and WebsiteVersion operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Third-Party Applications CLI

## Capability and source

Foundry Third-Party Applications manage websites, their versions, and
deployments. The `pal-found-third-party-applications` command exposes 9
ThirdPartyApplication, Website, and Version operations.

Source: [Palantir third-party applications](https://www.palantir.com/docs/foundry/third-party-applications); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

9 Foundry Third-Party Applications API v2 operations are available through the installed `pal-found-third-party-applications` command.

## Usage

```bash
pal-found-third-party-applications <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (where paging applies).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. Version uploads are bounded zip reads.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Application, website, and version operations](references/01-applications.md) | `third_party_application`, `website`, `version` | 9 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--batch-pages`. Binary uploads use `--file` (bounded 16 MiB zip).

## Install requirement

`pal-found-third-party-applications` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found-third-party-applications/
├── SKILL.md
└── references/
    └── 01-applications.md
```

Copy the entire `pal-found-third-party-applications` folder, including
`references/`, so the relative links above resolve offline.
