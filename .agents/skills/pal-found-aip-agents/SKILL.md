---
name: pal-found-aip-agents
description: Offline entry point for Foundry AIP Agents API v2 CLI. Documents 15 Agent, AgentVersion, Content, Session, and SessionTrace operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry AIP Agents CLI

## Capability and source

Foundry AIP Agents are conversational Foundry agents. The `pal-found-aip-agents`
command exposes 15 Agent, AgentVersion, Content, Session, and SessionTrace
operations for agent and session lifecycle and conversation continuation.

Source: [Palantir AIP Agents](https://www.palantir.com/docs/foundry/aip-agents); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

15 Foundry AIP Agents API v2 operations are available through the installed `pal-found-aip-agents` command.

## Usage

```bash
pal-found-aip-agents <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (where paging applies).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope. Session content and traces are never written to
logs.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Agent and session operations](references/01-agents-sessions.md) | `agent`, `agent_version`, `session` | 13 |
| [Session content and trace operations](references/02-content-trace.md) | `content`, `session_trace` | 2 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`; paged operations add `--page-size`, `--page-token`, and
`--batch-pages`. JSON payloads use `--parameter-inputs-json`,
`--user-input-json`, and `--contexts-override-json` where help shows them.

## Install requirement

`pal-found-aip-agents` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found-aip-agents/
├── SKILL.md
└── references/
    ├── 01-agents-sessions.md
    └── 02-content-trace.md
```

Copy the entire `pal-found-aip-agents` folder, including `references/`, so the
relative links above resolve offline.
