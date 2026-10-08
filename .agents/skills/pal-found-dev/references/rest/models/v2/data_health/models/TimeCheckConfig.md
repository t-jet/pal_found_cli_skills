# foundry_sdk.v2.data_health.models.TimeCheckConfig


TimeCheckConfig

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| time_bounds | timeBounds | typing.Optional[TimeBoundsConfig] | default None | No additional field description in SDK source. |
| median_deviation | medianDeviation | typing.Optional[MedianDeviationConfig] | default None | No additional field description in SDK source. |

```python
class TimeCheckConfig(core.ModelBase):
    """TimeCheckConfig"""

    time_bounds: typing.Optional[TimeBoundsConfig] = pydantic.Field(alias=str("timeBounds"), default=None)  # type: ignore[literal-required]
    median_deviation: typing.Optional[MedianDeviationConfig] = pydantic.Field(alias=str("medianDeviation"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.MedianDeviationConfig](MedianDeviationConfig.md)
- [foundry_sdk.v2.data_health.models.TimeBoundsConfig](TimeBoundsConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TimeCheckConfig.md)
