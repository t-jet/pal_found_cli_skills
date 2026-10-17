# foundry_sdk.v2.media_sets.models.ChatLlmSpec


Standard chat-based LLM specification with system and user prompts.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| model_locator | modelLocator | LanguageModelLocator | required; no default | No additional field description in SDK source. |
| system_prompt | systemPrompt | str | required; no default | System prompt for the LLM. |
| user_prompt | userPrompt | str | required; no default | User prompt for the LLM. |
| max_tokens | maxTokens | typing.Optional[int] | default None | Maximum number of tokens per request to generate. |

```python
class ChatLlmSpec(core.ModelBase):
    """Standard chat-based LLM specification with system and user prompts."""

    model_locator: LanguageModelLocator = pydantic.Field(alias=str("modelLocator"))  # type: ignore[literal-required]
    system_prompt: str = pydantic.Field(alias=str("systemPrompt"))  # type: ignore[literal-required]
    """System prompt for the LLM."""

    user_prompt: str = pydantic.Field(alias=str("userPrompt"))  # type: ignore[literal-required]
    """User prompt for the LLM."""

    max_tokens: typing.Optional[int] = pydantic.Field(alias=str("maxTokens"), default=None)  # type: ignore[literal-required]
    """Maximum number of tokens per request to generate."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.LanguageModelLocator](LanguageModelLocator.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ChatLlmSpec.md)
