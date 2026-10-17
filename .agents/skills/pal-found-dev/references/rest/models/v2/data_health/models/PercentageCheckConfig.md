# foundry_sdk.v2.data_health.models.PercentageCheckConfig


Configuration for percentage-based checks (such as null percentage).

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| column_name | columnName | ColumnName | required; no default | No additional field description in SDK source. |
| percentage_bounds | percentageBounds | typing.Optional[PercentageBoundsConfig] | default None | No additional field description in SDK source. |
| median_deviation | medianDeviation | typing.Optional[MedianDeviationConfig] | default None | No additional field description in SDK source. |

```python
class PercentageCheckConfig(core.ModelBase):
    """Configuration for percentage-based checks (such as null percentage)."""

    column_name: ColumnName = pydantic.Field(alias=str("columnName"))  # type: ignore[literal-required]
    percentage_bounds: typing.Optional[PercentageBoundsConfig] = pydantic.Field(alias=str("percentageBounds"), default=None)  # type: ignore[literal-required]
    median_deviation: typing.Optional[MedianDeviationConfig] = pydantic.Field(alias=str("medianDeviation"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.ColumnName](ColumnName.md)
- [foundry_sdk.v2.data_health.models.MedianDeviationConfig](MedianDeviationConfig.md)
- [foundry_sdk.v2.data_health.models.PercentageBoundsConfig](PercentageBoundsConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PercentageCheckConfig.md)
