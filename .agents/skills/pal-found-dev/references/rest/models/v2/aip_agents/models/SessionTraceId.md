# foundry_sdk.v2.aip_agents.models.SessionTraceId



The unique identifier for a trace. The trace lists the sequence of steps that an Agent took to arrive at an
answer. For example, a trace may include steps such as context retrieval and tool calls.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SessionTraceId: typing_extensions.TypeAlias = core.UUID
```

## Referenced definitions

- [foundry_sdk._core.utils.UUID](../../../_core/UUID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SessionTraceId.md)
