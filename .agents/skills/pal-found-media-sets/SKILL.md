---
name: pal-found-media-sets
description: Offline entry point for Foundry Media Sets API v2 CLI. Documents 19 MediaSet operations for the media lifecycle and bounded binary uploads/downloads with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Media Sets CLI

## Capability and source

Foundry Media Sets store unstructured binary media with a transaction
lifecycle. The `pal-found-media-sets` command exposes 19 operations on the
single `media_set` resource client, including four bounded binary downloads
and two binary uploads.

Source: [Palantir media sets](https://www.palantir.com/docs/foundry/media-sets); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

19 Foundry Media Sets API v2 operations are available through the installed `pal-found-media-sets` command.

## Usage

```bash
pal-found-media-sets media-set <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`.

Downloads use the shared `BinaryDownloadHandler` and return a JSON/TOON
metadata envelope (file path, size, checksums); the download bound applies.
Uploads read a bounded file (16 MiB).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. Attribution is applied per FR-ATTR-4.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Media set lifecycle](references/01-lifecycle.md) | `media_set` | 10 |
| [Media content operations](references/02-content.md) | `media_set` | 9 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`. Binary variants use `--file`, `--filename`, `--output`,
`--media-item-path`, `--media-item-rid`, `--transaction-id`, `--branch-name`,
`--branch-rid`, `--view-rid`, `--token`, `--read-token`, `--physical-item-name`,
and `--transformation-json` where help shows them.

## Install requirement

`pal-found-media-sets` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found-media-sets/
├── SKILL.md
└── references/
    ├── 01-lifecycle.md
    └── 02-content.md
```

Copy the entire `pal-found-media-sets` folder, including `references/`, so the
relative links above resolve offline.
