# foundry_sdk.v2.models.models.MissingWorkerConfigInputObjectSetPropertyMappingError


The provided worker config input object set is missing a property mapping required by the trainer.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_set_rid | objectSetRid | core.RID | required; no default | The RID of the object set with the missing property mapping. |
| property_type_spec_id | propertyTypeSpecId | str | required; no default | The property type spec ID for the missing property. |
| type | type | typing.Literal['missingWorkerConfigInputObjectSetPropertyMapping'] | 'missingWorkerConfigInputObjectSetPropertyMapping' | No additional field description in SDK source. |

```python
class MissingWorkerConfigInputObjectSetPropertyMappingError(core.ModelBase):
    """The provided worker config input object set is missing a property mapping required by the trainer."""

    object_set_rid: core.RID = pydantic.Field(alias=str("objectSetRid"))  # type: ignore[literal-required]
    """The RID of the object set with the missing property mapping."""

    property_type_spec_id: str = pydantic.Field(alias=str("propertyTypeSpecId"))  # type: ignore[literal-required]
    """The property type spec ID for the missing property."""

    type: typing.Literal["missingWorkerConfigInputObjectSetPropertyMapping"] = (
        "missingWorkerConfigInputObjectSetPropertyMapping"
    )
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MissingWorkerConfigInputObjectSetPropertyMappingError.md)
