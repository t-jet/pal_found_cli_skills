# foundry_sdk.v2.data_health.models.ColumnTypeConfig


Configuration for column type validation with severity settings.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| column_name | columnName | ColumnName | required; no default | No additional field description in SDK source. |
| expected_type | expectedType | typing.Optional[core_models.SchemaFieldType] | default None | No additional field description in SDK source. |
| severity | severity | SeverityLevel | required; no default | No additional field description in SDK source. |

```python
class ColumnTypeConfig(core.ModelBase):
    """Configuration for column type validation with severity settings."""

    column_name: ColumnName = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    expected_type: typing.Optional[core_models.SchemaFieldType] = pydantic.Field(alias=str("expectedType"), default=None)  # type: ignore[literal-required]
    severity: SeverityLevel
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.SchemaFieldType](../../core/models/SchemaFieldType.md)
- [foundry_sdk.v2.data_health.models.ColumnName](ColumnName.md)
- [foundry_sdk.v2.data_health.models.SeverityLevel](SeverityLevel.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ColumnTypeConfig.md)
