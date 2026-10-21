# AnthropicModel: language models operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

The messages API sends an Anthropic-format request to an enabled language model. Supply a supported model identifier and bounded output, then inspect response content and usage.

Prepare SDK 1.101.0 and access to the exact tenant resource. Check operation stage and endpoint restrictions in its contract. For uncertain writes, read the exact resulting RID/state before repeating the request. A fake-transport fixture proves SDK serialization, not tenant capability or model execution.

## Python client route

With a configured `FoundryClient` named `client`, use `client.language_models.AnthropicModel` for this resource. Each operation below is a method on that resource client; `with_raw_response` and `with_streaming_response` are wrappers available where the linked contract lists them. The offline fixture constructs the resource client directly so it can replace HTTP transport without tenant access.

## Operations

### messages

Send a bounded messages request with an authorized model identifier. Verify response stop reason, output blocks and usage before storing or displaying content.

For a text-only request, `client.language_models.AnthropicModel.messages`
accepts one USER message whose content contains a `type="text"` block. In
the synthetic fixture the request asks for a greeting with `max_tokens=16`;
the decoded response has `role="ASSISTANT"`, a text block, `stop_reason`
and token usage. Applications should select the enabled model ID, bound the
token budget, and inspect response block types before reading `.text`:

```python
reply = client.language_models.AnthropicModel.messages(
    anthropic_model_model_id=model_id,
    max_tokens=16,
    messages=[{"role": "USER", "content": [
        {"type": "text", "text": "Reply with one short greeting."},
    ]}],
    request_timeout=30,
)
assert reply.role == "ASSISTANT"
text_blocks = [block.text for block in reply.content if block.type == "text"]
assert text_blocks, "Inspect non-text output or refusal before using result"
assert reply.usage.output_tokens >= 0
```

The fixture uses only valid text content; image requests require actual image
bytes encoded according to the selected media type. Do not label arbitrary
text as base64 image data.

Read the [exact SDK/HTTP contract](../../contracts/v2/language_models/AnthropicModel/messages.md) for parameters, models, return mode and named errors. Run the [offline SDK fixture](../../../../examples/rest/087/v2/language_models/AnthropicModel/messages.py) from the skill root. It checks the synthetic request, result and declared errors without contacting Foundry.
