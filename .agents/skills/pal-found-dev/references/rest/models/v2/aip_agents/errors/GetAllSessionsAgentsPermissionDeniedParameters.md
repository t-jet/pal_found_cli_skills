# foundry_sdk.v2.aip_agents.errors.GetAllSessionsAgentsPermissionDeniedParameters


The calling user does not have permission to list all sessions across all Agents.
Listing all sessions across all agents requires the `api:aip-agents-write` scope.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
class GetAllSessionsAgentsPermissionDeniedParameters(typing_extensions.TypedDict):
    """
    The calling user does not have permission to list all sessions across all Agents.
    Listing all sessions across all agents requires the `api:aip-agents-write` scope.
    """

    __pydantic_config__ = {"extra": "allow"}
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetAllSessionsAgentsPermissionDeniedParameters.md)
