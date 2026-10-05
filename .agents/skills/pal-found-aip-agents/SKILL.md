---
name: pal-found-aip-agents
description: Understand AIP Chatbot Studio agents and use 15 AIP Agents API v2 CLI operations for versions, conversations, context, content, and traces.
---

# Foundry AIP Agents CLI

## Capability and source

AIP Chatbot Studio, formerly AIP Agent Studio, creates assistants that combine
a language model with enterprise information and configured tools. An agent
defines its behavior and available context. A session records a user's
conversation with an agent; each continue call adds an exchange and generates
a response. Agent versions let callers select a specific published behavior.
Source: Palantir's [AIP Chatbot Studio overview](https://www.palantir.com/docs/foundry/chatbot-studio/overview)
and [core concepts](https://www.palantir.com/docs/foundry/chatbot-studio/core-concepts).

This CLI binds a local `--alias` to the server session RID when creating a
session. Use that alias for subsequent session, content, and trace commands.
Continue calls require both `--parameter-inputs-json` for application
variables and `--user-input-json` with the user's text. By default the agent
retrieves context from its configured sources; `--contexts-override-json`
supplies explicit context instead. Do not send concurrent continue requests
to the same session. Cancel applies to an in-progress streamed exchange and
needs its message ID; cancellation does not close the client stream. Session
content and traces can expose user data and internal execution details.
The `streaming-continue` CLI command saves the SDK response to a file and
returns download metadata after the call; it does not display live tokens.

15 Foundry AIP Agents API v2 operations are exposed by `pal-found-aip-agents`.

## Usage

```bash
pal-found-aip-agents <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (where paging applies).

`--timeout` sets the request timeout in seconds. `--format` selects JSON,
TOON, or automatic structured output; `--pretty` indents it. For paged
operations, `--page-size` requests entries per page, `--page-token` resumes
from a returned cursor, and `--batch-pages` bounds how many pages this call
fetches.

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

Read [agent identifiers and conversation inputs](references/inputs.md) for
alias binding, application variables, and continue payloads.

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
