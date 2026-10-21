# foundry_sdk.v2.data_health.models.NumericColumnMeanCheckConfig


Checks the mean value of a numeric column.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| subject | subject | DatasetSubject | required; no default | No additional field description in SDK source. |
| numeric_column_check_config | numericColumnCheckConfig | NumericColumnCheckConfig | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['numericColumnMean'] | 'numericColumnMean' | No additional field description in SDK source. |

```python
class NumericColumnMeanCheckConfig(core.ModelBase):
    """Checks the mean value of a numeric column."""

    subject: DatasetSubject
    numeric_column_check_config: NumericColumnCheckConfig = pydantic.Field(alias=str("numericColumnCheckConfig"))  # type: ignore[literal-required]
    type: typing.Literal["numericColumnMean"] = "numericColumnMean"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.DatasetSubject](DatasetSubject.md)
- [foundry_sdk.v2.data_health.models.NumericColumnCheckConfig](NumericColumnCheckConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumericColumnMeanCheckConfig.md)
