# foundry_sdk.v2.aip_agents.errors.AgentVersionNotFoundParameters


The given AgentVersion could not be found.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| agentRid | agentRid | aip_agents_models.AgentRid | TypedDict key required | An RID identifying an Agent created in AIP Chatbot Studio. |
| agentVersionString | agentVersionString | aip_agents_models.AgentVersionString | TypedDict key required | The semantic version of the Agent, formatted as "majorVersion.minorVersion". |

```python
class AgentVersionNotFoundParameters(typing_extensions.TypedDict):
    """The given AgentVersion could not be found."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    """An RID identifying an Agent created in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/)."""

    agentVersionString: aip_agents_models.AgentVersionString
    """The semantic version of the Agent, formatted as "majorVersion.minorVersion"."""
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.AgentRid](../models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersionString](../models/AgentVersionString.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AgentVersionNotFoundParameters.md)
