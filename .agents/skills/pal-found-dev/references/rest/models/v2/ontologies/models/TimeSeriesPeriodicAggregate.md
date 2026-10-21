# foundry_sdk.v2.ontologies.models.TimeSeriesPeriodicAggregate


Aggregates values over discrete, periodic windows for a given time series.

A periodic window divides the time series into windows of fixed durations.
For each window, an aggregate function is applied to the points within that window. The result is a time series
with values representing the aggregate for each window. Windows with no data points are not included
in the output.

Periodic aggregation is useful for downsampling a continuous stream of data to larger granularities such as
hourly, daily, monthly.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| window_size | windowSize | PreciseDuration | required; no default | No additional field description in SDK source. |
| alignment_timestamp | alignmentTimestamp | typing.Optional[core.AwareDatetime] | default None | The timestamp used to align the result, such that ticks in the result time series will lie at integer<br>    multiples of the window duration from the alignment timestamp.<br><br>    Default is the first epoch timestamp (January 1, 1970, 00:00:00 UTC) so that all aggregated points have<br>    timestamps at midnight UTC at the start of each window duration.<br><br>    For example, for a weekly aggregate with alignment timestamp 5 January, 8:33PM, <br>    each aggregated timestamp will lie on the 7 day intervals at 8:33PM starting at 5 January. |
| window_type | windowType | TimeSeriesWindowType | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['periodic'] | 'periodic' | No additional field description in SDK source. |

```python
class TimeSeriesPeriodicAggregate(core.ModelBase):
    """
    Aggregates values over discrete, periodic windows for a given time series.

    A periodic window divides the time series into windows of fixed durations.
    For each window, an aggregate function is applied to the points within that window. The result is a time series
    with values representing the aggregate for each window. Windows with no data points are not included
    in the output.

    Periodic aggregation is useful for downsampling a continuous stream of data to larger granularities such as
    hourly, daily, monthly.
    """

    window_size: PreciseDuration = pydantic.Field(alias=str("windowSize"))  # type: ignore[literal-required]
    alignment_timestamp: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("alignmentTimestamp"), default=None)  # type: ignore[literal-required]
    """
    The timestamp used to align the result, such that ticks in the result time series will lie at integer
    multiples of the window duration from the alignment timestamp.

    Default is the first epoch timestamp (January 1, 1970, 00:00:00 UTC) so that all aggregated points have
    timestamps at midnight UTC at the start of each window duration.

    For example, for a weekly aggregate with alignment timestamp 5 January, 8:33PM, 
    each aggregated timestamp will lie on the 7 day intervals at 8:33PM starting at 5 January.
    """

    window_type: TimeSeriesWindowType = pydantic.Field(alias=str("windowType"))  # type: ignore[literal-required]
    type: typing.Literal["periodic"] = "periodic"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk.v2.ontologies.models.PreciseDuration](PreciseDuration.md)
- [foundry_sdk.v2.ontologies.models.TimeSeriesWindowType](TimeSeriesWindowType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TimeSeriesPeriodicAggregate.md)
