# Anthropic model operations

These records describe the `anthropic_model` commands in `pal-found-language-models`. Each record gives inputs, behavior, results, and examples.

### anthropic_model.messages

- **Purpose and behavior:** Sends conversation turns to an Anthropic model and generates an assistant reply. The request can also set a system instruction, generation limits, sampling controls, stop sequences, and tool use.
- **CLI inputs:** positionals `model_id`; required `--max-tokens`, `--messages-json`; optional `--output-config-json`, `--stop-sequences-json`, `--system-json`, `--temperature`, `--thinking-json`, `--tool-choice-json`, `--tools-json`, `--top-k`, `--top-p`.
- **Input meaning:** `--max-tokens`: The maximum number of tokens to generate before stopping. `--messages-json`: Ordered JSON array of user and assistant turns, each with a role and typed content blocks. `model_id`: Language model API name available in this enrollment. `--system-json`: System instruction; `--temperature`, `--top-k`, and `--top-p` control sampling. `--tools-json` defines available tools and `--tool-choice-json` controls whether the model uses them. `--output-config-json` configures the shape of the generated model output; `--stop-sequences-json` lists text sequences that stop model generation; `--thinking-json` configures the model's supported extended thinking mode.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model API name is available in this enrollment and the caller may invoke it with the supported request shape.
- **Result:** Returns `AnthropicMessagesResponse`, including generated message content and usage reported by the model.
- **Failure:** Unavailable model, malformed inference input, or denied access returns a structured error. A timeout leaves usage and response status uncertain.
- **Example:** `pal-found-language-models anthropic-model messages <MODEL_ID> --max-tokens 256 --messages-json '[{"role":"USER","content":[{"type":"text","text":"Summarize this order."}]}]'`
