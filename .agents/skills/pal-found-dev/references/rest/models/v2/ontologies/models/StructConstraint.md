# foundry_sdk.v2.ontologies.models.StructConstraint


StructConstraint

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| properties | properties | typing.Dict[PropertyApiName, ValueTypeApiName] | required; no default | A map of the properties of the struct type to the value type applied to that property. |
| type | type | typing.Literal['struct'] | 'struct' | No additional field description in SDK source. |

```python
class StructConstraint(core.ModelBase):
    """StructConstraint"""

    properties: typing.Dict[PropertyApiName, ValueTypeApiName]
    """A map of the properties of the struct type to the value type applied to that property."""

    type: typing.Literal["struct"] = "struct"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeApiName](ValueTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StructConstraint.md)
