# foundry_sdk.v2.language_models.models.AnthropicText


AnthropicText

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| text | text | str | required; no default | No additional field description in SDK source. |
| citations | citations | typing.Optional[typing.List[AnthropicCompletionCitation]] | None | No additional field description in SDK source. |
| cache_control | cacheControl | typing.Optional[AnthropicCacheControl] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['text'] | 'text' | No additional field description in SDK source. |

```python
class AnthropicText(core.ModelBase):
    """AnthropicText"""

    text: str
    citations: typing.Optional[typing.List[AnthropicCompletionCitation]] = None
    cache_control: typing.Optional[AnthropicCacheControl] = pydantic.Field(alias=str("cacheControl"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["text"] = "text"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.language_models.models.AnthropicCacheControl](AnthropicCacheControl.md)
- [foundry_sdk.v2.language_models.models.AnthropicCompletionCitation](AnthropicCompletionCitation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnthropicText.md)
