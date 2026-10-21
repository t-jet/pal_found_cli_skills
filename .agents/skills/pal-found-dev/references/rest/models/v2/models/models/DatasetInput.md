# foundry_sdk.v2.models.models.DatasetInput


Dataset input configuration.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | core_models.DatasetRid | required; no default | The RID of the input dataset. |
| column_mapping | columnMapping | typing.Dict[ColumnTypeSpecId, typing.List[core_models.ColumnName]] | required; no default | Mapping of column type spec IDs to column names. |
| ignore_columns | ignoreColumns | typing.List[core_models.ColumnName] | required; no default | Columns to ignore from the dataset. |
| select_columns | selectColumns | typing.List[core_models.ColumnName] | required; no default | Columns to select from the dataset. If empty, all columns not in ignoreColumns will be used. |
| type | type | typing.Literal['dataset'] | 'dataset' | No additional field description in SDK source. |

```python
class DatasetInput(core.ModelBase):
    """Dataset input configuration."""

    rid: core_models.DatasetRid
    """The RID of the input dataset."""

    column_mapping: typing.Dict[ColumnTypeSpecId, typing.List[core_models.ColumnName]] = pydantic.Field(alias=str("columnMapping"))  # type: ignore[literal-required]
    """Mapping of column type spec IDs to column names."""

    ignore_columns: typing.List[core_models.ColumnName] = pydantic.Field(alias=str("ignoreColumns"))  # type: ignore[literal-required]
    """Columns to ignore from the dataset."""

    select_columns: typing.List[core_models.ColumnName] = pydantic.Field(alias=str("selectColumns"))  # type: ignore[literal-required]
    """Columns to select from the dataset. If empty, all columns not in ignoreColumns will be used."""

    type: typing.Literal["dataset"] = "dataset"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.ColumnName](../../core/models/ColumnName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)
- [foundry_sdk.v2.models.models.ColumnTypeSpecId](ColumnTypeSpecId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DatasetInput.md)
