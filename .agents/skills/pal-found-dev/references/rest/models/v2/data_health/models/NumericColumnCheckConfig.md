# foundry_sdk.v2.data_health.models.NumericColumnCheckConfig


Configuration for numeric column-based checks (such as mean or median). At least one of numericBounds or trend must be specified. Both may be provided to validate both the absolute value range and the trend behavior over time.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| column_name | columnName | ColumnName | required; no default | No additional field description in SDK source. |
| numeric_bounds | numericBounds | typing.Optional[NumericBoundsConfig] | default None | No additional field description in SDK source. |
| trend | trend | typing.Optional[TrendConfig] | None | No additional field description in SDK source. |

```python
class NumericColumnCheckConfig(core.ModelBase):
    """Configuration for numeric column-based checks (such as mean or median). At least one of numericBounds or trend must be specified. Both may be provided to validate both the absolute value range and the trend behavior over time."""

    column_name: ColumnName = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    numeric_bounds: typing.Optional[NumericBoundsConfig] = pydantic.Field(alias=str("numericBounds"), default=None)  # type: ignore[literal-required]
    trend: typing.Optional[TrendConfig] = None
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.ColumnName](ColumnName.md)
- [foundry_sdk.v2.data_health.models.NumericBoundsConfig](NumericBoundsConfig.md)
- [foundry_sdk.v2.data_health.models.TrendConfig](TrendConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumericColumnCheckConfig.md)
