# foundry_sdk.v2.aip_agents.errors.CancelSessionFailedMessageNotInProgressParameters


Unable to cancel the requested session exchange as no in-progress exchange was found
for the provided message identifier.
This is expected if no exchange was initiated with the provided message identifier
through a `streamingContinue` request, or if the exchange for this identifier has already completed
and cannot be canceled, or if the exchange has already been canceled.
This error can also occur if the cancellation was requested immediately after requesting the exchange
through a `streamingContinue` request, and the exchange has not started yet.
Clients should handle these errors gracefully, and can reload the session content to get the latest
conversation state.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| messageId | messageId | aip_agents_models.MessageId | TypedDict key required | The message identifier that was requested for cancellation. |
| agentRid | agentRid | aip_agents_models.AgentRid | TypedDict key required | No additional field description in SDK source. |
| sessionRid | sessionRid | aip_agents_models.SessionRid | TypedDict key required | No additional field description in SDK source. |

```python
class CancelSessionFailedMessageNotInProgressParameters(typing_extensions.TypedDict):
    """
    Unable to cancel the requested session exchange as no in-progress exchange was found
    for the provided message identifier.
    This is expected if no exchange was initiated with the provided message identifier
    through a `streamingContinue` request, or if the exchange for this identifier has already completed
    and cannot be canceled, or if the exchange has already been canceled.
    This error can also occur if the cancellation was requested immediately after requesting the exchange
    through a `streamingContinue` request, and the exchange has not started yet.
    Clients should handle these errors gracefully, and can reload the session content to get the latest
    conversation state.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    messageId: aip_agents_models.MessageId
    """The message identifier that was requested for cancellation."""

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.AgentRid](../models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.MessageId](../models/MessageId.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../models/SessionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CancelSessionFailedMessageNotInProgressParameters.md)
