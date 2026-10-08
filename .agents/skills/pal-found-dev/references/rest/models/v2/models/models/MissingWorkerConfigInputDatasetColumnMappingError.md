# foundry_sdk.v2.models.models.MissingWorkerConfigInputDatasetColumnMappingError


The provided worker config input dataset is missing a column mapping required by the trainer.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| dataset_rid | datasetRid | core_models.DatasetRid | required; no default | The RID of the dataset with the missing column mapping. |
| column_type_spec_id | columnTypeSpecId | ColumnTypeSpecId | required; no default | The column type spec ID for the missing column. |
| type | type | typing.Literal['missingWorkerConfigInputDatasetColumnMapping'] | 'missingWorkerConfigInputDatasetColumnMapping' | No additional field description in SDK source. |

```python
class MissingWorkerConfigInputDatasetColumnMappingError(core.ModelBase):
    """The provided worker config input dataset is missing a column mapping required by the trainer."""

    dataset_rid: core_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    """The RID of the dataset with the missing column mapping."""

    column_type_spec_id: ColumnTypeSpecId = pydantic.Field(alias=str("columnTypeSpecId"))  # type: ignore[literal-required]
    """The column type spec ID for the missing column."""

    type: typing.Literal["missingWorkerConfigInputDatasetColumnMapping"] = (
        "missingWorkerConfigInputDatasetColumnMapping"
    )
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)
- [foundry_sdk.v2.models.models.ColumnTypeSpecId](ColumnTypeSpecId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MissingWorkerConfigInputDatasetColumnMappingError.md)
