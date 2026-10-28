# Inference inputs

The positional `model_id` is the language model API name available in the
current Foundry enrollment. It is not a model artifact RID. The SDK uses
`anthropic_model_model_id` and `open_ai_model_model_id` for the same CLI
position. Availability and supported settings vary by model.

`anthropic-model messages` needs `--max-tokens` and `--messages-json`. The
message value is an array of objects with `role` (`USER` or `ASSISTANT`) and
`content`, an array of typed blocks. A simple text block is
`{"type":"text","text":"Summarize this order."}`. Optional JSON flags
configure tools, system instructions, tool choice, and thinking only when
the selected model supports them. `--system-json` takes an array containing
at most one text block, for example
`[{"type":"text","text":"Answer concisely."}]`; multiple system prompts
are unsupported in SDK 1.101.0. `--temperature` ranges from 0 to 1 in the
SDK; a zero value does not guarantee deterministic output. When tuning
sampling, change either `--temperature` or `--top-p`, as the SDK documentation
recommends, rather than both.

Optional message payloads use the following SDK 1.101.0 shapes. Pass each
JSON value as one quoted CLI argument, and combine settings only when the
selected model supports them.

| Flag | Example JSON value | Meaning |
| --- | --- | --- |
| `--stop-sequences-json` | `["END"]` | Stop generation when a listed sequence is produced. |
| `--tools-json` | `[{"type":"custom","name":"lookup_order","inputSchema":{"type":"object","properties":{}}}]` | Declare a custom tool and its input schema. Add the fields required by the actual tool. |
| `--tool-choice-json` | `{"type":"auto"}` | Let the model choose whether to use a declared tool. Other variants are `{"type":"none"}`, `{"type":"any"}`, and `{"type":"tool","name":"lookup_order"}`; the named tool must match a declaration. |
| `--thinking-json` | `{"type":"disabled"}` | Disable extended thinking. To enable it, use `{"type":"enabled","budgetTokens":2048}`; the SDK documents a budget greater than 1024. |
| `--output-config-json` | `{"format":{"type":"jsonSchema","schema":{"type":"object","properties":{"answer":{"type":"string"}},"required":["answer"]}},"effort":"HIGH"}` | Request a JSON-schema output shape and supported effort. Effort values are `LOW`, `MEDIUM`, `HIGH`, or `MAX`; format and effort are optional. |

`open-ai-model embeddings --input-json` takes a JSON array of input strings,
for example `["Order shipped yesterday"]`. SDK 1.101.0 documents a maximum
of 8192 tokens per input. Check the selected model's availability and input
limits in the enrollment before live use. `--dimensions` is supported only
by text-embedding-3 and later models. `--encoding-format` selects `FLOAT` or
`BASE64`.
