# foundry_sdk.v2.aip_agents.errors.SessionTraceIdAlreadyExistsParameters


The provided trace ID already exists for the session and cannot be reused.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| agentRid | agentRid | aip_agents_models.AgentRid | TypedDict key required | No additional field description in SDK source. |
| sessionRid | sessionRid | aip_agents_models.SessionRid | TypedDict key required | No additional field description in SDK source. |
| sessionTraceId | sessionTraceId | aip_agents_models.SessionTraceId | TypedDict key required | No additional field description in SDK source. |

```python
class SessionTraceIdAlreadyExistsParameters(typing_extensions.TypedDict):
    """The provided trace ID already exists for the session and cannot be reused."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    sessionTraceId: aip_agents_models.SessionTraceId
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.AgentRid](../models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../models/SessionRid.md)
- [foundry_sdk.v2.aip_agents.models.SessionTraceId](../models/SessionTraceId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SessionTraceIdAlreadyExistsParameters.md)
