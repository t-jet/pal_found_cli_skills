# OpenAiModel: language models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

The embeddings API converts supplied text into vectors through an enabled model. Validate the model and input batch before using vectors in a downstream index or search.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Operations

### embeddings

Submit text inputs for embedding, then check each vector index and dimension against the request before persisting downstream references.

Read the [exact SDK/HTTP contract](../../contracts/v2/language_models/OpenAiModel/embeddings.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/language_models/OpenAiModel/embeddings.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
