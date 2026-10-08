# foundry_sdk.v2.aip_agents.models.Agent


Agent

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | AgentRid | required; no default | An RID identifying an Agent created in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/). |
| version | version | AgentVersionString | required; no default | The version of this instance of the Agent. |
| metadata | metadata | AgentMetadata | required; no default | No additional field description in SDK source. |
| parameters | parameters | typing.Dict[ParameterId, Parameter] | required; no default | The types and names of variables configured for the Agent in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/) in the [application state](https://palantir.com/docs/foundry/chatbot-studio/application-state/).<br>    These variables can be used to send custom values in prompts sent to an Agent to customize and control the Agent's behavior. |

```python
class Agent(core.ModelBase):
    """Agent"""

    rid: AgentRid
    """An RID identifying an Agent created in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/)."""

    version: AgentVersionString
    """The version of this instance of the Agent."""

    metadata: AgentMetadata
    parameters: typing.Dict[ParameterId, Parameter]
    """
    The types and names of variables configured for the Agent in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/) in the [application state](https://palantir.com/docs/foundry/chatbot-studio/application-state/).
    These variables can be used to send custom values in prompts sent to an Agent to customize and control the Agent's behavior.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.AgentMetadata](AgentMetadata.md)
- [foundry_sdk.v2.aip_agents.models.AgentRid](AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersionString](AgentVersionString.md)
- [foundry_sdk.v2.aip_agents.models.Parameter](Parameter.md)
- [foundry_sdk.v2.aip_agents.models.ParameterId](ParameterId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Agent.md)
