# Open ai model operations

These records describe the `open_ai_model` commands in `pal-found-language-models`. Each record gives inputs, behavior, results, and examples.

### open_ai_model.embeddings

- **Purpose and behavior:** Converts each input text into a numeric vector for semantic search or similarity comparison. The selected model determines the vector space; use the same model when comparing vectors.
- **CLI inputs:** positionals `model_id`; required `--input-json`; optional `--dimensions`, `--encoding-format`.
- **Input meaning:** `--input-json`: JSON array of text strings to embed. `model_id`: Language model API name available in this enrollment. `--dimensions`: Requested output vector length, if the model supports it. `--encoding-format`: Vector representation in the response.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The model API name is available in this enrollment and the caller may invoke it with the supported request shape.
- **Result:** Returns `OpenAiEmbeddingsResponse` with one indexed embedding vector per input item and model usage information.
- **Failure:** Unavailable model, malformed inference input, or denied access returns a structured error. A timeout leaves usage and response status uncertain.
- **Example:** `pal-found-language-models open-ai-model embeddings <MODEL_ID> --input-json '["Order shipped yesterday"]'`
