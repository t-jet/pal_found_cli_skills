# foundry_sdk.v2.ontologies.models.InterfacePropertyStructFieldImplementation


An implementation of an interface property via the field of a local struct property.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| struct_field_of_property | structFieldOfProperty | StructFieldOfPropertyImplementation | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['structFieldImplementation'] | 'structFieldImplementation' | No additional field description in SDK source. |

```python
class InterfacePropertyStructFieldImplementation(core.ModelBase):
    """An implementation of an interface property via the field of a local struct property."""

    struct_field_of_property: StructFieldOfPropertyImplementation = pydantic.Field(alias=str("structFieldOfProperty"))  # type: ignore[literal-required]
    type: typing.Literal["structFieldImplementation"] = "structFieldImplementation"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.StructFieldOfPropertyImplementation](StructFieldOfPropertyImplementation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfacePropertyStructFieldImplementation.md)
