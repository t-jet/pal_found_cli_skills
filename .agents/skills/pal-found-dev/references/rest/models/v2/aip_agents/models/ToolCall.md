# foundry_sdk.v2.aip_agents.models.ToolCall


A tool call with its input and output.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| tool_metadata | toolMetadata | ToolMetadata | required; no default | Details about the tool that was called, including the name and type of the tool. |
| input | input | ToolCallInput | required; no default | No additional field description in SDK source. |
| output | output | typing.Optional[ToolCallOutput] | None | Empty if the tool call is in progress. |

```python
class ToolCall(core.ModelBase):
    """A tool call with its input and output."""

    tool_metadata: ToolMetadata = pydantic.Field(alias=str("toolMetadata"))  # type: ignore[literal-required]
    """Details about the tool that was called, including the name and type of the tool."""

    input: ToolCallInput
    output: typing.Optional[ToolCallOutput] = None
    """Empty if the tool call is in progress."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.ToolCallInput](ToolCallInput.md)
- [foundry_sdk.v2.aip_agents.models.ToolCallOutput](ToolCallOutput.md)
- [foundry_sdk.v2.aip_agents.models.ToolMetadata](ToolMetadata.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ToolCall.md)
