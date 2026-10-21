# foundry_sdk.v2.aip_agents.models.ToolMetadata


Details about the used tool.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | str | required; no default | The name of the tool that was called, as configured on the Agent. |
| type | type | ToolType | required; no default | The type of the tool that was called. |

```python
class ToolMetadata(core.ModelBase):
    """Details about the used tool."""

    name: str
    """The name of the tool that was called, as configured on the Agent."""

    type: ToolType
    """The type of the tool that was called."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.ToolType](ToolType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ToolMetadata.md)
