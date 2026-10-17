# foundry_sdk.v2.models.models.MultiplePropertiesNotAllowedForTrainerError


Multiple properties were mapped but the trainer only allows a single property for this spec.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_set_rid | objectSetRid | core.RID | required; no default | The RID of the object set with multiple properties mapped. |
| property_type_spec_id | propertyTypeSpecId | str | required; no default | The property type spec ID that does not allow multiple properties. |
| type | type | typing.Literal['multiplePropertiesNotAllowedForTrainer'] | 'multiplePropertiesNotAllowedForTrainer' | No additional field description in SDK source. |

```python
class MultiplePropertiesNotAllowedForTrainerError(core.ModelBase):
    """Multiple properties were mapped but the trainer only allows a single property for this spec."""

    object_set_rid: core.RID = pydantic.Field(alias=str("objectSetRid"))  # type: ignore[literal-required]
    """The RID of the object set with multiple properties mapped."""

    property_type_spec_id: str = pydantic.Field(alias=str("propertyTypeSpecId"))  # type: ignore[literal-required]
    """The property type spec ID that does not allow multiple properties."""

    type: typing.Literal["multiplePropertiesNotAllowedForTrainer"] = (
        "multiplePropertiesNotAllowedForTrainer"
    )
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../_core/RID.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MultiplePropertiesNotAllowedForTrainerError.md)
