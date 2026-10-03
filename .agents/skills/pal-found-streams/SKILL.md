---
name: pal-found-streams
description: Offline entry point for Foundry Streams API v2 CLI. Documents 15 Dataset, Stream, and Subscriber operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Streams CLI

## Capability and source

Foundry Streams are time-ordered record streams; subscribers consume records
at committed offsets. The `pal-found-streams` command exposes 15 Dataset,
Stream, and Subscriber operations.

Source: [Palantir Streams](https://www.palantir.com/docs/foundry/streams); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

15 Foundry Streams API v2 operations are available through the installed `pal-found-streams` command.

## Usage

```bash
pal-found-streams <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (where paging applies).

Long-lived record connections use `FOUNDRY_AGENTIC_CLI_STREAMS_TIMEOUT_S`
(default 120 s). The CLI uses the shared config loader, access control guard,
retry handler, pagination helper, structured error serializer, output
formatter, and SDK-native B3 tracing scope.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Stream operations](references/01-stream.md) | `dataset`, `stream` | 9 |
| [Subscriber operations](references/02-subscriber.md) | `subscriber` | 6 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--batch-pages`. JSON payloads use `--schema-json`, `--records-json`, and
`--offsets-json` where help shows them. Reads honor `--max-records`.

## Install requirement

`pal-found-streams` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found-streams/
├── SKILL.md
└── references/
    ├── 01-stream.md
    └── 02-subscriber.md
```

Copy the entire `pal-found-streams` folder, including `references/`, so the
relative links above resolve offline.
