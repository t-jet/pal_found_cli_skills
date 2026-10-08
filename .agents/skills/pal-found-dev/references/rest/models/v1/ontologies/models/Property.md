# foundry_sdk.v1.ontologies.models.Property


Details about some property of an object.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| display_name | displayName | typing.Optional[core_models.DisplayName] | default None | No additional field description in SDK source. |
| base_type | baseType | ValueType | required; no default | No additional field description in SDK source. |
| legacy_property_id | legacyPropertyId | typing.Optional[LegacyPropertyId] | default None | No additional field description in SDK source. |

```python
class Property(core.ModelBase):
    """Details about some property of an object."""

    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    base_type: ValueType = pydantic.Field(alias=str("baseType"))  # type: ignore[literal-required]
    legacy_property_id: typing.Optional[LegacyPropertyId] = pydantic.Field(alias=str("legacyPropertyId"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v1.ontologies.models.LegacyPropertyId](LegacyPropertyId.md)
- [foundry_sdk.v1.ontologies.models.ValueType](ValueType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Property.md)
