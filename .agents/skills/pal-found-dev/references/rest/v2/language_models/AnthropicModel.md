# AnthropicModel: language models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

The messages API sends an Anthropic-format request to an enabled language model. Supply a supported model identifier and bounded output, then inspect response content and usage.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Operations

### messages

Send a bounded messages request with an authorized model identifier. Verify response stop reason, output blocks and usage before storing or displaying content.

Read the [exact SDK/HTTP contract](../../contracts/v2/language_models/AnthropicModel/messages.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/language_models/AnthropicModel/messages.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
