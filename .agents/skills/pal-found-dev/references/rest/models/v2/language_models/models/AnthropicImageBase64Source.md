# foundry_sdk.v2.language_models.models.AnthropicImageBase64Source


AnthropicImageBase64Source

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | str | required; no default | No additional field description in SDK source. |
| media_type | mediaType | AnthropicMediaType | required; no default | This can include image/jpeg, image/png, image/gif or image/webp. |
| type | type | typing.Literal['base64'] | 'base64' | No additional field description in SDK source. |

```python
class AnthropicImageBase64Source(core.ModelBase):
    """AnthropicImageBase64Source"""

    data: str
    media_type: AnthropicMediaType = pydantic.Field(alias=str("mediaType"))  # type: ignore[literal-required]
    """This can include image/jpeg, image/png, image/gif or image/webp."""

    type: typing.Literal["base64"] = "base64"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.language_models.models.AnthropicMediaType](AnthropicMediaType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnthropicImageBase64Source.md)
