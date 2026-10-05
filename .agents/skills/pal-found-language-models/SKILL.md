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
depends on the enrollment. See Palantir's [platform overview](https://www.palantir.com/docs/foundry/platform-overview/overview)
and [supported LLMs](https://www.palantir.com/docs/foundry/aip/supported-llms).

Source: Palantir's platform overview and supported LLMs pages linked above;
the operation records below explain supported request shapes.
documentation.

The two CLI commands are provider-shaped endpoints: `anthropic-model messages`
accepts a model API name, messages, and `--max-tokens`; `open-ai-model
embeddings` accepts a model API name and input text array. Inspect the model's
supported features before supplying tools, thinking, or other optional
generation settings. The SDK method documentation defines the request and
response shapes in `LanguageModels/AnthropicModel.md` and `OpenAiModel.md`.

2 Foundry Language Models API v2 operations are exposed by `pal-found-language-models`.

## Usage

```bash
pal-found-language-models <resource> <operation> [options]
```

Common options: `--timeout`, `--format json|toon|auto`, `--pretty`.

`--timeout` sets the request timeout in seconds. `--format` selects JSON,
TOON, or automatic structured output; `--pretty` indents it.

The CLI uses the shared config loader, access control guard, retry handler,
pagination helper, structured error serializer, output formatter, and
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
