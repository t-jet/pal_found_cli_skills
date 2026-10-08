# foundry_sdk.v2.aip_agents.models.ToolCallOutput


The output of a tool call.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ToolCallOutput: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["SuccessToolCallOutput", "FailureToolCallOutput"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.FailureToolCallOutput](FailureToolCallOutput.md)
- [foundry_sdk.v2.aip_agents.models.SuccessToolCallOutput](SuccessToolCallOutput.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ToolCallOutput.md)
