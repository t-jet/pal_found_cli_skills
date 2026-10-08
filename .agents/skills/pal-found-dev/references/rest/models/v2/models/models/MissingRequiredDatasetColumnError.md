# foundry_sdk.v2.models.models.MissingRequiredDatasetColumnError


The user-provided dataset is missing a column required by the trainer.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| dataset_rid | datasetRid | core_models.DatasetRid | required; no default | The RID of the dataset missing the required column. |
| column_type_spec_id | columnTypeSpecId | ColumnTypeSpecId | required; no default | The trainer column type spec ID for the required column. |
| column_names | columnNames | typing.List[core_models.ColumnName] | required; no default | The valid dataset column names that could map to this trainer column. |
| type | type | typing.Literal['missingRequiredDatasetColumn'] | 'missingRequiredDatasetColumn' | No additional field description in SDK source. |

```python
class MissingRequiredDatasetColumnError(core.ModelBase):
    """The user-provided dataset is missing a column required by the trainer."""

    dataset_rid: core_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset missing the required column."""

    column_type_spec_id: ColumnTypeSpecId = pydantic.Field(alias=str("columnTypeSpecId"))  # type: ignore[literal-required]
    """The trainer column type spec ID for the required column."""

    column_names: typing.List[core_models.ColumnName] = pydantic.Field(alias=str("columnNames"))  # type: ignore[literal-required]
    """The valid dataset column names that could map to this trainer column."""

    type: typing.Literal["missingRequiredDatasetColumn"] = "missingRequiredDatasetColumn"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.ColumnName](../../core/models/ColumnName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)
- [foundry_sdk.v2.models.models.ColumnTypeSpecId](ColumnTypeSpecId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MissingRequiredDatasetColumnError.md)
