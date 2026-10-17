# foundry_sdk.v2.language_models.models.AnthropicToolUse


AnthropicToolUse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| id | id | str | required; no default | No additional field description in SDK source. |
| input | input | typing.Any | required; no default | No additional field description in SDK source. |
| name | name | str | required; no default | No additional field description in SDK source. |
| cache_control | cacheControl | typing.Optional[AnthropicCacheControl] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['toolUse'] | 'toolUse' | No additional field description in SDK source. |

```python
class AnthropicToolUse(core.ModelBase):
    """AnthropicToolUse"""

    id: str
    input: typing.Any
    name: str
    cache_control: typing.Optional[AnthropicCacheControl] = pydantic.Field(alias=str("cacheControl"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["toolUse"] = "toolUse"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.language_models.models.AnthropicCacheControl](AnthropicCacheControl.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnthropicToolUse.md)
