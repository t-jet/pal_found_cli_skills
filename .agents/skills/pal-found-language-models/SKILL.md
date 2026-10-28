---
name: pal-found-language-models
description: Understand Foundry language-model inference and use two API v2 CLI operations for Anthropic messages and OpenAI-style embeddings.
---

# Foundry Language Models CLI

## Capability and source

Foundry's Language Model Service gives applications a common way to invoke
supported models while managing provider integration in the platform. A
message model produces a response from conversation messages and generation
settings. An embedding model turns input text into numeric vectors used for
similarity and retrieval. These are inference calls, so results depend on the
selected model and inputs and can consume model usage. Model availability
depends on the enrollment. Optional sources: Palantir's
[platform overview](https://www.palantir.com/docs/foundry/platform-overview/overview)
and [supported LLMs](https://www.palantir.com/docs/foundry/aip/supported-llms).
The operation records below explain supported request shapes.

The two CLI commands are provider-shaped endpoints: `anthropic-model messages`
accepts a model API name, messages, and `--max-tokens`; `open-ai-model
embeddings` accepts a model API name and input text array. Inspect the model's
supported features before supplying tools, thinking, or other optional
generation settings. Read the local [Anthropic operation record](references/anthropic-model.md),
[embedding operation record](references/open-ai-model.md), and
[inference inputs](references/inputs.md) for supported request and response shapes.

2 Foundry Language Models API v2 operations are exposed by `pal-found-language-models`.

## Usage

```bash
pal-found-language-models <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`.

`--timeout` sets the request timeout in seconds. `--format` accepts `json`,
`toon`, or `auto`. Both inference endpoints return top-level objects, so the
formatter emits JSON even when `--format toon` is requested; TOON encoding
requires a nonempty uniform array of objects. `--pretty` indents JSON output.

The CLI uses the shared config loader, access control guard, retry handler,
structured error serializer, output formatter, and
SDK-native B3 tracing scope.

## Operation index

| Part | Resource clients | Operations |
| --- | --- | ---: |
| [Inference operations](references/01-inference.md) | `anthropic_model`, `open_ai_model` | 2 |

## Parameters and JSON

Read [inference inputs](references/inputs.md) for model names, message
shapes, and embedding text arrays.

Every operation accepts `--timeout`, `--format json|toon|auto`, and
`--pretty`. Inference payloads use `--messages-json`, `--tools-json`, and
`--input-json` where help shows them.
