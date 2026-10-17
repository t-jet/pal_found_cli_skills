# foundry_sdk.v2.aip_agents.errors.InvalidParameterTypeParameters


The provided value does not match the expected type for the application variable configured on the Agent for this session.
Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Chatbot Studio.
The Agent version used for the session can be checked through the API with `getSession`.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| agentRid | agentRid | aip_agents_models.AgentRid | TypedDict key required | No additional field description in SDK source. |
| sessionRid | sessionRid | aip_agents_models.SessionRid | TypedDict key required | No additional field description in SDK source. |
| parameter | parameter | aip_agents_models.ParameterId | TypedDict key required | No additional field description in SDK source. |
| expectedType | expectedType | str | TypedDict key required | No additional field description in SDK source. |
| receivedType | receivedType | str | TypedDict key required | No additional field description in SDK source. |

```python
class InvalidParameterTypeParameters(typing_extensions.TypedDict):
    """
    The provided value does not match the expected type for the application variable configured on the Agent for this session.
    Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Chatbot Studio.
    The Agent version used for the session can be checked through the API with `getSession`.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    parameter: aip_agents_models.ParameterId
    expectedType: str
    receivedType: str
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.AgentRid](../models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.ParameterId](../models/ParameterId.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../models/SessionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InvalidParameterTypeParameters.md)
