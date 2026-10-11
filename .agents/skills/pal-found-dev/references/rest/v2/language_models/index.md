# v2.language_models resources and operations


Select a model exposed by the permitted enrollment and use its operation-specific request and response format. Model availability, token limits and streaming behavior are operation dependent; test with a bounded prompt and handle rejected or partial responses explicitly. Read the selected operation contract before invocation; stage, API version and result lifetime remain operation-specific.

| Operation | Stage |
| --- | --- |
| [v2.language_models.AnthropicModel.messages](../../contracts/v2/language_models/AnthropicModel/messages.md) | Private Beta |
| [v2.language_models.OpenAiModel.embeddings](../../contracts/v2/language_models/OpenAiModel/embeddings.md) | Private Beta |

[All services](../../catalog.md) | [SDK handling](../../client-behavior.md)

[Part 1](index.md)
