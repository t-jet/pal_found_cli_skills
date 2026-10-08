# foundry_sdk.v2.aip_agents.models.CreateSessionRequest


CreateSessionRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| agent_version | agentVersion | typing.Optional[AgentVersionString] | default None | The version of the Agent associated with the session.<br>    This can be set by clients on session creation.<br>    If not specified, defaults to use the latest published version of the Agent at session creation time. |

```python
class CreateSessionRequest(core.ModelBase):
    """CreateSessionRequest"""

    agent_version: typing.Optional[AgentVersionString] = pydantic.Field(alias=str("agentVersion"), default=None)  # type: ignore[literal-required]
    """
    The version of the Agent associated with the session.
    This can be set by clients on session creation.
    If not specified, defaults to use the latest published version of the Agent at session creation time.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersionString](AgentVersionString.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateSessionRequest.md)
