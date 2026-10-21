# foundry_sdk.v2.language_models.models.AnthropicCharacterLocationCitation


AnthropicCharacterLocationCitation

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| cited_text | citedText | str | required; no default | No additional field description in SDK source. |
| document_index | documentIndex | int | required; no default | No additional field description in SDK source. |
| document_title | documentTitle | typing.Optional[str] | default None | No additional field description in SDK source. |
| start_char_index | startCharIndex | int | required; no default | No additional field description in SDK source. |
| end_char_index | endCharIndex | int | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['charLocation'] | 'charLocation' | No additional field description in SDK source. |

```python
class AnthropicCharacterLocationCitation(core.ModelBase):
    """AnthropicCharacterLocationCitation"""

    cited_text: str = pydantic.Field(alias=str("citedText"))  # type: ignore[literal-required]
    document_index: int = pydantic.Field(alias=str("documentIndex"))  # type: ignore[literal-required]
    document_title: typing.Optional[str] = pydantic.Field(alias=str("documentTitle"), default=None)  # type: ignore[literal-required]
    start_char_index: int = pydantic.Field(alias=str("startCharIndex"))  # type: ignore[literal-required]
    end_char_index: int = pydantic.Field(alias=str("endCharIndex"))  # type: ignore[literal-required]
    type: typing.Literal["charLocation"] = "charLocation"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnthropicCharacterLocationCitation.md)
