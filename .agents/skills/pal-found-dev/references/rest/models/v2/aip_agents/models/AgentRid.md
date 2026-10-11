# foundry_sdk.v2.aip_agents.models.AgentRid


An RID identifying an Agent created in AIP Chatbot Studio. Obtain an existing Agent RID from the authorized Studio or application configuration, or use a supplied synthetic RID in an offline fixture. The frozen SDK Agent client has `get` and session methods but no Agent list operation; `get` already requires the RID.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
AgentRid: typing_extensions.TypeAlias = core.RID
```

## Referenced definitions

- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AgentRid.md)
