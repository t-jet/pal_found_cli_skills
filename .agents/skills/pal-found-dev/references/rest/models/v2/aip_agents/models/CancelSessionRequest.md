# foundry_sdk.v2.aip_agents.models.CancelSessionRequest


CancelSessionRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| message_id | messageId | MessageId | required; no default | The identifier for the in-progress exchange to cancel.<br>    This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`. |
| response | response | typing.Optional[AgentMarkdownResponse] | None | When specified, the exchange is added to the session with the client-provided response as the result.<br>    When omitted, the exchange is not added to the session. |

```python
class CancelSessionRequest(core.ModelBase):
    """CancelSessionRequest"""

    message_id: MessageId = pydantic.Field(alias=str("messageId"))  # type: ignore[literal-required]
    """
    The identifier for the in-progress exchange to cancel.
    This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`.
    """

    response: typing.Optional[AgentMarkdownResponse] = None
    """
    When specified, the exchange is added to the session with the client-provided response as the result.
    When omitted, the exchange is not added to the session.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.AgentMarkdownResponse](AgentMarkdownResponse.md)
- [foundry_sdk.v2.aip_agents.models.MessageId](MessageId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CancelSessionRequest.md)
