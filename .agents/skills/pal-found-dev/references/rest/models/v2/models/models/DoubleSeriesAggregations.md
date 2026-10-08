# foundry_sdk.v2.models.models.DoubleSeriesAggregations


Aggregated statistics for numeric series.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| min | min | typing.Optional[float] | None | Minimum value in the series. Absent if the metric has not been computed. |
| max | max | typing.Optional[float] | None | Maximum value in the series. Absent if the metric has not been computed. |
| last | last | typing.Optional[float] | None | Most recent value in the series. Absent if the metric has not been computed. |
| type | type | typing.Literal['double'] | 'double' | No additional field description in SDK source. |

```python
class DoubleSeriesAggregations(core.ModelBase):
    """Aggregated statistics for numeric series."""

    min: typing.Optional[float] = None
    """Minimum value in the series. Absent if the metric has not been computed."""

    max: typing.Optional[float] = None
    """Maximum value in the series. Absent if the metric has not been computed."""

    last: typing.Optional[float] = None
    """Most recent value in the series. Absent if the metric has not been computed."""

    type: typing.Literal["double"] = "double"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DoubleSeriesAggregations.md)
