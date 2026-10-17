# foundry_sdk.v2.aip_agents.models.StringParameter


StringParameter

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| default_value | defaultValue | typing.Optional[str] | default None | The default value to use for this variable. |
| type | type | typing.Literal['string'] | 'string' | No additional field description in SDK source. |

```python
class StringParameter(core.ModelBase):
    """StringParameter"""

    default_value: typing.Optional[str] = pydantic.Field(alias=str("defaultValue"), default=None)  # type: ignore[literal-required]
    """The default value to use for this variable."""

    type: typing.Literal["string"] = "string"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StringParameter.md)
