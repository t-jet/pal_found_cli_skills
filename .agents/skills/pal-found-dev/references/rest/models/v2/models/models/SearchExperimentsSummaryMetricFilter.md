# foundry_sdk.v2.models.models.SearchExperimentsSummaryMetricFilter


Filter that atomically binds a series name and aggregation type to a value comparison,
ensuring all conditions are evaluated on the same summary metric.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| series_name | seriesName | SeriesName | required; no default | The name of the series this metric belongs to. |
| aggregation | aggregation | SummaryMetricAggregation | required; no default | The aggregation type (MIN, MAX, LAST). |
| operator | operator | SearchExperimentsNumericFilterOperator | required; no default | The comparison operator (EQ, GT, or LT). |
| value | value | typing.Any | required; no default | The value to compare against. |
| type | type | typing.Literal['summaryMetricFilter'] | 'summaryMetricFilter' | No additional field description in SDK source. |

```python
class SearchExperimentsSummaryMetricFilter(core.ModelBase):
    """
    Filter that atomically binds a series name and aggregation type to a value comparison,
    ensuring all conditions are evaluated on the same summary metric.
    """

    series_name: SeriesName = pydantic.Field(alias=str("seriesName"))  # type: ignore[literal-required]
    """The name of the series this metric belongs to."""

    aggregation: SummaryMetricAggregation
    """The aggregation type (MIN, MAX, LAST)."""

    operator: SearchExperimentsNumericFilterOperator
    """The comparison operator (EQ, GT, or LT)."""

    value: typing.Any
    """The value to compare against."""

    type: typing.Literal["summaryMetricFilter"] = "summaryMetricFilter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.SearchExperimentsNumericFilterOperator](SearchExperimentsNumericFilterOperator.md)
- [foundry_sdk.v2.models.models.SeriesName](SeriesName.md)
- [foundry_sdk.v2.models.models.SummaryMetricAggregation](SummaryMetricAggregation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchExperimentsSummaryMetricFilter.md)
