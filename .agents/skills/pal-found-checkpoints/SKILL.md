---
name: pal-found-checkpoints
description: Investigate Foundry checkpoint justifications with get, batch retrieval, and filtered record search.
---

# Foundry Checkpoints CLI

## Capability and source

Foundry Checkpoints is a governance capability. A checkpoint prompts a user
to justify a sensitive interaction, such as an export. Its configuration
determines who sees the prompt and what justification is required. Submission
creates a record of the user, time, justification, checkpoint type, and
associated data. Users can review their own submitted justifications;
authorized administrators can review records across their scope. This CLI
exposes three read operations for records; it does not configure prompts.

Source: [Palantir Checkpoints overview](https://www.palantir.com/docs/foundry/checkpoints/overview) and SDK `docs/v2/Checkpoints/Record.md`.

3 Foundry Checkpoints API v2 operations are available through the installed `pal-found-checkpoints` command.

## Usage

```bash
pal-found-checkpoints record <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`,
`--page-size`, `--page-token`, `--batch-pages` (on paged search).

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

| Part | Resource client | Operations |
| --- | --- | ---: |
| [Record operations](references/01-record.md) | `record` | 3 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`. `get-batch` uses `--records-json` (array of RIDs, at most 100).
`search` uses `--where-json` (typed filter), `--page-size`, `--page-token`,
and `--sort-direction ASC|DESC`. Read the [record guide](references/01-record.md)
for the visibility rule: batch retrieval omits missing and inaccessible records.

`--timeout` limits a request in seconds; `--format` selects output encoding;
`--pretty` indents it. On search, `--page-size` requests records per page,
`--page-token` resumes at a returned continuation token, and `--batch-pages`
caps automatic traversal. `--sort-direction` controls creation-time order.

## Install requirement

`pal-found-checkpoints` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

```bash
# conda (t-jet channel)
conda install -c t-jet pal_found_cli

# PyPI / pip
pip install pal_found_cli

# uv
uv tool install pal_found_cli
```
