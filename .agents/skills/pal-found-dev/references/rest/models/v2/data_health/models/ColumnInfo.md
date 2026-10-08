# foundry_sdk.v2.data_health.models.ColumnInfo


Information about a column including its name and type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | ColumnName | required; no default | No additional field description in SDK source. |
| column_type | columnType | typing.Optional[core_models.SchemaFieldType] | default None | No additional field description in SDK source. |

```python
class ColumnInfo(core.ModelBase):
    """Information about a column including its name and type."""

    name: ColumnName
    column_type: typing.Optional[core_models.SchemaFieldType] = pydantic.Field(alias=str("columnType"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.SchemaFieldType](../../core/models/SchemaFieldType.md)
- [foundry_sdk.v2.data_health.models.ColumnName](ColumnName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ColumnInfo.md)
