# foundry_sdk.v2.language_models.models.AnthropicTokenUsage


AnthropicTokenUsage

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| cache_creation_input_tokens | cacheCreationInputTokens | typing.Optional[int] | default None | No additional field description in SDK source. |
| cache_read_input_tokens | cacheReadInputTokens | typing.Optional[int] | default None | No additional field description in SDK source. |
| input_tokens | inputTokens | int | required; no default | No additional field description in SDK source. |
| output_tokens | outputTokens | int | required; no default | No additional field description in SDK source. |

```python
class AnthropicTokenUsage(core.ModelBase):
    """AnthropicTokenUsage"""

    cache_creation_input_tokens: typing.Optional[int] = pydantic.Field(alias=str("cacheCreationInputTokens"), default=None)  # type: ignore[literal-required]
    cache_read_input_tokens: typing.Optional[int] = pydantic.Field(alias=str("cacheReadInputTokens"), default=None)  # type: ignore[literal-required]
    input_tokens: int = pydantic.Field(alias=str("inputTokens"))  # type: ignore[literal-required]
    output_tokens: int = pydantic.Field(alias=str("outputTokens"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnthropicTokenUsage.md)
