# foundry_sdk.v2.aip_agents.errors.RetryDeadlineExceededParameters


Failed to generate a response after retrying up to the configured retry deadline. Clients should wait and retry.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| agentRid | agentRid | aip_agents_models.AgentRid | TypedDict key required | No additional field description in SDK source. |
| sessionRid | sessionRid | aip_agents_models.SessionRid | TypedDict key required | No additional field description in SDK source. |
| details | details | str | TypedDict key required | Any additional details provided for the error. |

```python
class RetryDeadlineExceededParameters(typing_extensions.TypedDict):
    """Failed to generate a response after retrying up to the configured retry deadline. Clients should wait and retry."""

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: aip_agents_models.SessionRid
    details: str
    """Any additional details provided for the error."""
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.AgentRid](../models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../models/SessionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RetryDeadlineExceededParameters.md)
