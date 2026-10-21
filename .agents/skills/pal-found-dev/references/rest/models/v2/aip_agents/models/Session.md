# foundry_sdk.v2.aip_agents.models.Session


Session

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | SessionRid | required; no default | The Resource Identifier (RID) of the conversation session. |
| metadata | metadata | SessionMetadata | required; no default | Metadata about the session. |
| agent_rid | agentRid | AgentRid | required; no default | The Resource Identifier (RID) of the Agent associated with the session. |
| agent_version | agentVersion | AgentVersionString | required; no default | The version of the Agent associated with the session.<br>    This can be set by clients on session creation.<br>    If not specified, defaults to use the latest published version of the Agent at session creation time. |

```python
class Session(core.ModelBase):
    """Session"""

    rid: SessionRid
    """The Resource Identifier (RID) of the conversation session."""

    metadata: SessionMetadata
    """Metadata about the session."""

    agent_rid: AgentRid = pydantic.Field(alias=str("agentRid"))  # type: ignore[literal-required]
    """The Resource Identifier (RID) of the Agent associated with the session."""

    agent_version: AgentVersionString = pydantic.Field(alias=str("agentVersion"))  # type: ignore[literal-required]
    """
    The version of the Agent associated with the session.
    This can be set by clients on session creation.
    If not specified, defaults to use the latest published version of the Agent at session creation time.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.AgentRid](AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersionString](AgentVersionString.md)
- [foundry_sdk.v2.aip_agents.models.SessionMetadata](SessionMetadata.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](SessionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Session.md)
