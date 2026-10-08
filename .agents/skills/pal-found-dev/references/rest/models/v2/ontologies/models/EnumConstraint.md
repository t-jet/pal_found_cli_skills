# foundry_sdk.v2.ontologies.models.EnumConstraint


EnumConstraint

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| options | options | typing.List[typing.Optional[PropertyValue]] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['enum'] | 'enum' | No additional field description in SDK source. |

```python
class EnumConstraint(core.ModelBase):
    """EnumConstraint"""

    options: typing.List[typing.Optional[PropertyValue]]
    type: typing.Literal["enum"] = "enum"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](PropertyValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](EnumConstraint.md)
