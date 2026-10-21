# foundry_sdk.v2.data_health.models.AllowedColumnValuesCheckConfig


Checks that values in a column are within an allowed set of values.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| subject | subject | DatasetSubject | required; no default | No additional field description in SDK source. |
| column_name | columnName | ColumnName | required; no default | No additional field description in SDK source. |
| allowed_values | allowedValues | typing.List[ColumnValue] | required; no default | No additional field description in SDK source. |
| allow_null | allowNull | typing.Optional[bool] | default None | No additional field description in SDK source. |
| severity | severity | SeverityLevel | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['allowedColumnValues'] | 'allowedColumnValues' | No additional field description in SDK source. |

```python
class AllowedColumnValuesCheckConfig(core.ModelBase):
    """Checks that values in a column are within an allowed set of values."""

    subject: DatasetSubject
    column_name: ColumnName = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    allowed_values: typing.List[ColumnValue] = pydantic.Field(alias=str("allowedValues"))  # type: ignore[literal-required]
    allow_null: typing.Optional[bool] = pydantic.Field(alias=str("allowNull"), default=None)  # type: ignore[literal-required]
    severity: SeverityLevel
    type: typing.Literal["allowedColumnValues"] = "allowedColumnValues"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.ColumnName](ColumnName.md)
- [foundry_sdk.v2.data_health.models.ColumnValue](ColumnValue.md)
- [foundry_sdk.v2.data_health.models.DatasetSubject](DatasetSubject.md)
- [foundry_sdk.v2.data_health.models.SeverityLevel](SeverityLevel.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AllowedColumnValuesCheckConfig.md)
