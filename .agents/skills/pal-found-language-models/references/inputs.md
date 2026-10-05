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
the selected model supports them. `--temperature` ranges from 0 to 1 in the
SDK; a zero value does not guarantee deterministic output.

`open-ai-model embeddings --input-json` takes a JSON array of input strings,
for example `["Order shipped yesterday"]`. Each input must stay within the
model's token limit. `--dimensions` is available only for compatible
embedding models, and `--encoding-format` selects `FLOAT` or `BASE64`.
