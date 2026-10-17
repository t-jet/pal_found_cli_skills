# foundry_sdk.v2.ontologies.models.TimeSeriesAggregationStrategy



CUMULATIVE aggregates all points up to the current point.
ROLLING aggregates all points in a rolling window whose size is either the specified number of points or
time duration.
PERIODIC aggregates all points in specified time windows.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
TimeSeriesAggregationStrategy: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "TimeSeriesRollingAggregate", "TimeSeriesPeriodicAggregate", "TimeSeriesCumulativeAggregate"
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.TimeSeriesCumulativeAggregate](TimeSeriesCumulativeAggregate.md)
- [foundry_sdk.v2.ontologies.models.TimeSeriesPeriodicAggregate](TimeSeriesPeriodicAggregate.md)
- [foundry_sdk.v2.ontologies.models.TimeSeriesRollingAggregate](TimeSeriesRollingAggregate.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TimeSeriesAggregationStrategy.md)
