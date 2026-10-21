# foundry_sdk.v2.ontologies.models.ObjectSetWithPropertiesType


ObjectSet which returns objects with additional derived properties.

This feature is experimental and not yet generally available.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_set | objectSet | ObjectSet | required; no default | No additional field description in SDK source. |
| derived_properties | derivedProperties | typing.Dict[DerivedPropertyApiName, DerivedPropertyDefinition] | required; no default | Map of the name of the derived property to return and its definition |
| type | type | typing.Literal['withProperties'] | 'withProperties' | No additional field description in SDK source. |

```python
class ObjectSetWithPropertiesType(core.ModelBase):
    """
    ObjectSet which returns objects with additional derived properties.

    This feature is experimental and not yet generally available.
    """

    object_set: ObjectSet = pydantic.Field(alias=str("objectSet"))  # type: ignore[literal-required]
    derived_properties: typing.Dict[DerivedPropertyApiName, DerivedPropertyDefinition] = pydantic.Field(alias=str("derivedProperties"))  # type: ignore[literal-required]
    """Map of the name of the derived property to return and its definition"""

    type: typing.Literal["withProperties"] = "withProperties"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.DerivedPropertyApiName](DerivedPropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.DerivedPropertyDefinition](DerivedPropertyDefinition.md)
- [foundry_sdk.v2.ontologies.models.ObjectSet](ObjectSet.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectSetWithPropertiesType.md)
