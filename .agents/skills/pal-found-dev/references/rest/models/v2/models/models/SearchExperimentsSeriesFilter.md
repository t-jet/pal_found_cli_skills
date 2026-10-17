# foundry_sdk.v2.models.models.SearchExperimentsSeriesFilter


Filter that atomically binds a series name to a metric comparison,
ensuring all conditions are evaluated on the same series.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| series_name | seriesName | SeriesName | required; no default | The name of the series to filter on. |
| field | field | SearchExperimentsSeriesFilterField | required; no default | The series metric to compare. |
| operator | operator | SearchExperimentsNumericFilterOperator | required; no default | The comparison operator (EQ, GT, or LT). |
| value | value | typing.Any | required; no default | The value to compare against. |
| type | type | typing.Literal['seriesFilter'] | 'seriesFilter' | No additional field description in SDK source. |

```python
class SearchExperimentsSeriesFilter(core.ModelBase):
    """
    Filter that atomically binds a series name to a metric comparison,
    ensuring all conditions are evaluated on the same series.
    """

    series_name: SeriesName = pydantic.Field(alias=str("seriesName"))  # type: ignore[literal-required]
    """The name of the series to filter on."""

    field: SearchExperimentsSeriesFilterField
    """The series metric to compare."""

    operator: SearchExperimentsNumericFilterOperator
    """The comparison operator (EQ, GT, or LT)."""

    value: typing.Any
    """The value to compare against."""

    type: typing.Literal["seriesFilter"] = "seriesFilter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.models.models.SearchExperimentsNumericFilterOperator](SearchExperimentsNumericFilterOperator.md)
- [foundry_sdk.v2.models.models.SearchExperimentsSeriesFilterField](SearchExperimentsSeriesFilterField.md)
- [foundry_sdk.v2.models.models.SeriesName](SeriesName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchExperimentsSeriesFilter.md)
