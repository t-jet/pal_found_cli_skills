# foundry_sdk.v2.language_models.models.AnthropicToolResult


AnthropicToolResult

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| tool_use_id | toolUseId | str | required; no default | No additional field description in SDK source. |
| content | content | typing.Optional[typing.List[AnthropicToolResultContent]] | None | No additional field description in SDK source. |
| is_error | isError | typing.Optional[bool] | default None | No additional field description in SDK source. |
| cache_control | cacheControl | typing.Optional[AnthropicCacheControl] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['toolResult'] | 'toolResult' | No additional field description in SDK source. |

```python
class AnthropicToolResult(core.ModelBase):
    """AnthropicToolResult"""

    tool_use_id: str = pydantic.Field(alias=str("toolUseId"))  # type: ignore[literal-required]
    content: typing.Optional[typing.List[AnthropicToolResultContent]] = None
    is_error: typing.Optional[bool] = pydantic.Field(alias=str("isError"), default=None)  # type: ignore[literal-required]
    cache_control: typing.Optional[AnthropicCacheControl] = pydantic.Field(alias=str("cacheControl"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["toolResult"] = "toolResult"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.language_models.models.AnthropicCacheControl](AnthropicCacheControl.md)
- [foundry_sdk.v2.language_models.models.AnthropicToolResultContent](AnthropicToolResultContent.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnthropicToolResult.md)
