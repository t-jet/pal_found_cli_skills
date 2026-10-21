# foundry_sdk.v2.data_health.models.MedianDeviation


The number of thresholds the build's duration differs from the median.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| bounds_type | boundsType | typing.Optional[MedianDeviationBoundsType] | default None | No additional field description in SDK source. |
| data_points | dataPoints | int | required; no default | No additional field description in SDK source. |
| deviation_threshold | deviationThreshold | float | required; no default | No additional field description in SDK source. |

```python
class MedianDeviation(core.ModelBase):
    """The number of thresholds the build's duration differs from the median."""

    bounds_type: typing.Optional[MedianDeviationBoundsType] = pydantic.Field(alias=str("boundsType"), default=None)  # type: ignore[literal-required]
    data_points: int = pydantic.Field(alias=str("dataPoints"))  # type: ignore[literal-required]
    deviation_threshold: float = pydantic.Field(alias=str("deviationThreshold"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.MedianDeviationBoundsType](MedianDeviationBoundsType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MedianDeviation.md)
