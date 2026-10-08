# foundry_sdk.v2.aip_agents.errors.FunctionLocatorNotFoundParameters


The specified function locator is configured for use by the Agent but could not be found.
The function type or version may not exist or the client token does not have access.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| agentRid | agentRid | aip_agents_models.AgentRid | TypedDict key required | No additional field description in SDK source. |
| sessionRid | sessionRid | typing_extensions.NotRequired[aip_agents_models.SessionRid] | TypedDict key may be omitted | The session RID where the error occurred. This is omitted if the error occurred during session creation. |
| functionRid | functionRid | core.RID | TypedDict key required | No additional field description in SDK source. |
| functionVersion | functionVersion | str | TypedDict key required | No additional field description in SDK source. |

```python
class FunctionLocatorNotFoundParameters(typing_extensions.TypedDict):
    """
    The specified function locator is configured for use by the Agent but could not be found.
    The function type or version may not exist or the client token does not have access.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    agentRid: aip_agents_models.AgentRid
    sessionRid: typing_extensions.NotRequired[aip_agents_models.SessionRid]
    """The session RID where the error occurred. This is omitted if the error occurred during session creation."""

    functionRid: core.RID
    functionVersion: str
```

## Referenced definitions

- [foundry_sdk._core.utils.RID](../../../_core/RID.md)
- [foundry_sdk.v2.aip_agents.models.AgentRid](../models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../models/SessionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FunctionLocatorNotFoundParameters.md)
