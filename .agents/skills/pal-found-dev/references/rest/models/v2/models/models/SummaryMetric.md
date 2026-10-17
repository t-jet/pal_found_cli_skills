# foundry_sdk.v2.models.models.SummaryMetric


A summary metric with series name, aggregation type, and computed value.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| series_name | seriesName | SeriesName | required; no default | Name of the series this metric belongs to |
| aggregation | aggregation | SummaryMetricAggregation | required; no default | Type of aggregation (MIN, MAX, LAST) |
| value | value | float | required; no default | The computed value |

```python
class SummaryMetric(core.ModelBase):
    """A summary metric with series name, aggregation type, and computed value."""

    series_name: SeriesName = pydantic.Field(alias=str("seriesName"))  # type: ignore[literal-required]
    """Name of the series this metric belongs to"""

    aggregation: SummaryMetricAggregation
    """Type of aggregation (MIN, MAX, LAST)"""

    value: float
    """The computed value"""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.SeriesName](SeriesName.md)
- [foundry_sdk.v2.models.models.SummaryMetricAggregation](SummaryMetricAggregation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SummaryMetric.md)
