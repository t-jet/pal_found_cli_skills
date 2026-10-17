# foundry_sdk.v2.language_models.models.AnthropicMessagesResponse


AnthropicMessagesResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| content | content | typing.List[AnthropicCompletionContent] | required; no default | No additional field description in SDK source. |
| id | id | str | required; no default | No additional field description in SDK source. |
| model | model | str | required; no default | No additional field description in SDK source. |
| role | role | AnthropicMessageRole | required; no default | No additional field description in SDK source. |
| stop_reason | stopReason | typing.Optional[str] | default None | No additional field description in SDK source. |
| stop_sequence | stopSequence | typing.Optional[str] | default None | No additional field description in SDK source. |
| usage | usage | AnthropicTokenUsage | required; no default | No additional field description in SDK source. |

```python
class AnthropicMessagesResponse(core.ModelBase):
    """AnthropicMessagesResponse"""

    content: typing.List[AnthropicCompletionContent]
    id: str
    model: str
    role: AnthropicMessageRole
    stop_reason: typing.Optional[str] = pydantic.Field(alias=str("stopReason"), default=None)  # type: ignore[literal-required]
    stop_sequence: typing.Optional[str] = pydantic.Field(alias=str("stopSequence"), default=None)  # type: ignore[literal-required]
    usage: AnthropicTokenUsage
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.language_models.models.AnthropicCompletionContent](AnthropicCompletionContent.md)
- [foundry_sdk.v2.language_models.models.AnthropicMessageRole](AnthropicMessageRole.md)
- [foundry_sdk.v2.language_models.models.AnthropicTokenUsage](AnthropicTokenUsage.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnthropicMessagesResponse.md)
