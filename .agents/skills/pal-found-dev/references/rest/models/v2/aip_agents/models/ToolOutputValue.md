# foundry_sdk.v2.aip_agents.models.ToolOutputValue


A tool output value, which can be either a string or a Resource Identifier (RID).

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ToolOutputValue: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["StringToolOutputValue", "RidToolOutputValue"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.RidToolOutputValue](RidToolOutputValue.md)
- [foundry_sdk.v2.aip_agents.models.StringToolOutputValue](StringToolOutputValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ToolOutputValue.md)
