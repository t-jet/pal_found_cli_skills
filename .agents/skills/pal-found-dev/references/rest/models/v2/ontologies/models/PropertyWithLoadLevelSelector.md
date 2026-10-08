# foundry_sdk.v2.ontologies.models.PropertyWithLoadLevelSelector


A combination of a property identifier and the load level to apply to the property. You can select a reduced
value for arrays and the main value for structs. If the provided load level cannot be applied to the property
type, then it will be ignored. This selector is experimental and may not work in filters or sorts.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| property_identifier | propertyIdentifier | PropertyIdentifier | required; no default | No additional field description in SDK source. |
| load_level | loadLevel | PropertyLoadLevel | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['propertyWithLoadLevel'] | 'propertyWithLoadLevel' | No additional field description in SDK source. |

```python
class PropertyWithLoadLevelSelector(core.ModelBase):
    """
    A combination of a property identifier and the load level to apply to the property. You can select a reduced
    value for arrays and the main value for structs. If the provided load level cannot be applied to the property
    type, then it will be ignored. This selector is experimental and may not work in filters or sorts.
    """

    property_identifier: PropertyIdentifier = pydantic.Field(alias=str("propertyIdentifier"))  # type: ignore[literal-required]
    load_level: PropertyLoadLevel = pydantic.Field(alias=str("loadLevel"))  # type: ignore[literal-required]
    type: typing.Literal["propertyWithLoadLevel"] = "propertyWithLoadLevel"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyIdentifier](PropertyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.PropertyLoadLevel](PropertyLoadLevel.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyWithLoadLevelSelector.md)
