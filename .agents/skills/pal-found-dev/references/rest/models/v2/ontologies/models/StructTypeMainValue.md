# foundry_sdk.v2.ontologies.models.StructTypeMainValue


StructTypeMainValue

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| main_value_type | mainValueType | ObjectPropertyType | required; no default | No additional field description in SDK source. |
| fields | fields | typing.List[StructFieldApiName] | required; no default | The fields which comprise the main value of the struct. |

```python
class StructTypeMainValue(core.ModelBase):
    """StructTypeMainValue"""

    main_value_type: ObjectPropertyType = pydantic.Field(alias=str("mainValueType"))  # type: ignore[literal-required]
    fields: typing.List[StructFieldApiName]
    """The fields which comprise the main value of the struct."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectPropertyType](ObjectPropertyType.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](StructFieldApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StructTypeMainValue.md)
