# foundry_sdk.v2.aip_agents.errors.ActionTypeNotFoundParameters


An action tool configured on the Agent references an action type that could not be found.
This can surface at runtime if the action type was deleted or is not accessible to the calling token.
Verify the action type exists and is accessible, then review the Agent's tools in AIP Chatbot Studio.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| agentRid | agentRid | aip_agents_models.AgentRid | TypedDict key required | No additional field description in SDK source. |
| sessionRid | sessionRid | typing_extensions.NotRequired[aip_agents_models.SessionRid] | TypedDict key may be omitted | The session RID where the error occurred. This is omitted if the error occurred during session creation. |
| actionRid | actionRid | ontologies_models.ActionTypeRid | TypedDict key required | No additional field description in SDK source. |

```python
class ActionTypeNotFoundParameters(typing_extensions.TypedDict):
    """
    An action tool configured on the Agent references an action type that could not be found.
    This can surface at runtime if the action type was deleted or is not accessible to the calling token.
    Verify the action type exists and is accessible, then review the Agent's tools in AIP Chatbot Studio.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: typing_extensions.NotRequired[aip_agents_models.SessionRid]
    """The session RID where the error occurred. This is omitted if the error occurred during session creation."""

    actionRid: ontologies_models.ActionTypeRid
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.AgentRid](../models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../models/SessionRid.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeRid](../../ontologies/models/ActionTypeRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ActionTypeNotFoundParameters.md)
