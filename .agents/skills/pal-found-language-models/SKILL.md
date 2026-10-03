---
name: pal-found-language-models
description: Offline entry point for Foundry Language Models API v2 CLI. Documents 2 AnthropicModel messages and OpenAiModel embeddings operations with preconditions, effect, inputs, result, and failure offline.
---

# Foundry Language Models CLI

## Capability and source

Foundry Language Models exposes inference endpoints. The
`pal-found-language-models` command exposes 2 operations: Anthropic messages
and OpenAI embeddings.

Source: [Palantir Foundry documentation](https://www.palantir.com/docs/foundry); reviewed 2026-08-13. This source link is maintenance evidence for maintainers; it is not needed to use the skill offline.

2 Foundry Language Models API v2 operations are available through the installed `pal-found-language-models` command.

## Usage

```bash
pal-found-language-models <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Inference operations](references/01-inference.md) | `anthropic_model`, `open_ai_model` | 2 |

## Parameters and JSON

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`. Inference payloads use `--messages-json`, `--tools-json`, and
`--input-json` where help shows them.

## Install requirement

`pal-found-language-models` is provided by the `pal_found_cli` Python package. Install it with your preferred package manager:

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
.agents/skills/pal-found-language-models/
├── SKILL.md
└── references/
    └── 01-inference.md
```

Copy the entire `pal-found-language-models` folder, including `references/`,
so the relative links above resolve offline.
