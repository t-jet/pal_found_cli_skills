# foundry_sdk.v2.aip_agents.models.SessionExchange


Represents an individual exchange between a user and an Agent in a conversation session.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| user_input | userInput | UserTextInput | required; no default | The user message that initiated the exchange. |
| contexts | contexts | typing.Optional[SessionExchangeContexts] | None | Additional retrieved context that was included in the prompt to the Agent.<br>    This may include context that was passed by the client with the user input, or relevant context that was automatically retrieved and added based on available data sources configured on the Agent.<br>    Empty if no additional context was included in the prompt. |
| result | result | SessionExchangeResult | required; no default | The final result for the exchange. |

```python
class SessionExchange(core.ModelBase):
    """Represents an individual exchange between a user and an Agent in a conversation session."""

    user_input: UserTextInput = pydantic.Field(alias=str("userInput"))  # type: ignore[literal-required]
    """The user message that initiated the exchange."""

    contexts: typing.Optional[SessionExchangeContexts] = None
    """
    Additional retrieved context that was included in the prompt to the Agent.
    This may include context that was passed by the client with the user input, or relevant context that was automatically retrieved and added based on available data sources configured on the Agent.
    Empty if no additional context was included in the prompt.
    """

    result: SessionExchangeResult
    """The final result for the exchange."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.SessionExchangeContexts](SessionExchangeContexts.md)
- [foundry_sdk.v2.aip_agents.models.SessionExchangeResult](SessionExchangeResult.md)
- [foundry_sdk.v2.aip_agents.models.UserTextInput](UserTextInput.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SessionExchange.md)
