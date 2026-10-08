# foundry_sdk.v2.language_models.models.AnthropicMessagesRequest


AnthropicMessagesRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| messages | messages | typing.List[AnthropicMessage] | required; no default | Input messages to the model. This can include a single user-role message or multiple messages with<br>    alternating user and assistant roles. |
| max_tokens | maxTokens | int | required; no default | The maximum number of tokens to generate before stopping. |
| stop_sequences | stopSequences | typing.Optional[typing.List[str]] | default None | Custom text sequences that will cause the model to stop generating. |
| system | system | typing.Optional[typing.List[AnthropicSystemMessage]] | None | A system prompt is a way of providing context and instructions to Claude, such as specifying a <br>    particular goal or role. As of now, sending multiple system prompts is not supported. |
| temperature | temperature | typing.Optional[float] | None | Amount of randomness injected into the response. Ranges from 0.0 to 1.0. Note that even with <br>    temperature of 0.0, the results will not be fully deterministic. Defaults to 1.0 |
| thinking | thinking | typing.Optional[AnthropicThinkingConfig] | None | Configuration for enabling Claude's extended thinking. |
| tool_choice | toolChoice | typing.Optional[AnthropicToolChoice] | default None | How the model should use the provided tools. |
| tools | tools | typing.Optional[typing.List[AnthropicTool]] | None | Definitions of tools that the model may use. |
| top_k | topK | typing.Optional[int] | default None | Only sample from the top K options for each subsequent token. |
| top_p | topP | typing.Optional[float] | default None | Use nucleus sampling. You should either alter temperature or top_p, but not both |
| output_config | outputConfig | typing.Optional[AnthropicOutputConfig] | default None | Configuration to control the shape of the model's output |

```python
class AnthropicMessagesRequest(core.ModelBase):
    """AnthropicMessagesRequest"""

    messages: typing.List[AnthropicMessage]
    """
    Input messages to the model. This can include a single user-role message or multiple messages with
    alternating user and assistant roles.
    """

    max_tokens: int = pydantic.Field(alias=str("maxTokens"))  # type: ignore[literal-required]
    """The maximum number of tokens to generate before stopping."""

    stop_sequences: typing.Optional[typing.List[str]] = pydantic.Field(alias=str("stopSequences"), default=None)  # type: ignore[literal-required]
    """Custom text sequences that will cause the model to stop generating."""

    system: typing.Optional[typing.List[AnthropicSystemMessage]] = None
    """
    A system prompt is a way of providing context and instructions to Claude, such as specifying a 
    particular goal or role. As of now, sending multiple system prompts is not supported.
    """

    temperature: typing.Optional[float] = None
    """
    Amount of randomness injected into the response. Ranges from 0.0 to 1.0. Note that even with 
    temperature of 0.0, the results will not be fully deterministic. Defaults to 1.0
    """

    thinking: typing.Optional[AnthropicThinkingConfig] = None
    """Configuration for enabling Claude's extended thinking."""

    tool_choice: typing.Optional[AnthropicToolChoice] = pydantic.Field(alias=str("toolChoice"), default=None)  # type: ignore[literal-required]
    """How the model should use the provided tools."""

    tools: typing.Optional[typing.List[AnthropicTool]] = None
    """Definitions of tools that the model may use."""

    top_k: typing.Optional[int] = pydantic.Field(alias=str("topK"), default=None)  # type: ignore[literal-required]
    """Only sample from the top K options for each subsequent token."""

    top_p: typing.Optional[float] = pydantic.Field(alias=str("topP"), default=None)  # type: ignore[literal-required]
    """Use nucleus sampling. You should either alter temperature or top_p, but not both"""

    output_config: typing.Optional[AnthropicOutputConfig] = pydantic.Field(alias=str("outputConfig"), default=None)  # type: ignore[literal-required]
    """Configuration to control the shape of the model's output"""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.language_models.models.AnthropicMessage](AnthropicMessage.md)
- [foundry_sdk.v2.language_models.models.AnthropicOutputConfig](AnthropicOutputConfig.md)
- [foundry_sdk.v2.language_models.models.AnthropicSystemMessage](AnthropicSystemMessage.md)
- [foundry_sdk.v2.language_models.models.AnthropicThinkingConfig](AnthropicThinkingConfig.md)
- [foundry_sdk.v2.language_models.models.AnthropicTool](AnthropicTool.md)
- [foundry_sdk.v2.language_models.models.AnthropicToolChoice](AnthropicToolChoice.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnthropicMessagesRequest.md)
