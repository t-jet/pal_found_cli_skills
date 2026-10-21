# foundry_sdk.v2.models.models.FieldValidationError


A dataset column type is not compatible with the trainer's supported column types.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| dataset_rid | datasetRid | core_models.DatasetRid | required; no default | The RID of the dataset containing the invalid field. |
| field_name | fieldName | typing.Optional[str] | default None | The name of the dataset column or field that failed validation. |
| field_type | fieldType | str | required; no default | The type of the dataset field. |
| type | type | typing.Literal['fieldValidationFailure'] | 'fieldValidationFailure' | No additional field description in SDK source. |

```python
class FieldValidationError(core.ModelBase):
    """A dataset column type is not compatible with the trainer's supported column types."""

    dataset_rid: core_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset containing the invalid field."""

    field_name: typing.Optional[str] = pydantic.Field(alias=str("fieldName"), default=None)  # type: ignore[literal-required]
    """The name of the dataset column or field that failed validation."""

    field_type: str = pydantic.Field(alias=str("fieldType"))  # type: ignore[literal-required]
    """The type of the dataset field."""

    type: typing.Literal["fieldValidationFailure"] = "fieldValidationFailure"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FieldValidationError.md)
