# foundry_sdk.v2.ontologies.models.TimeSeriesRollingAggregateWindow



A rolling window is a moving subset of data points that ends at the current timestamp (inclusive)
and spans a specified duration (window size). As new data points are added, old points fall out of the
window if they are outside the specified duration.

Rolling windows are commonly used for smoothing data, detecting trends, and reducing noise
in time series analysis.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
TimeSeriesRollingAggregateWindow: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["PreciseDuration", "RollingAggregateWindowPoints"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.PreciseDuration](PreciseDuration.md)
- [foundry_sdk.v2.ontologies.models.RollingAggregateWindowPoints](RollingAggregateWindowPoints.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TimeSeriesRollingAggregateWindow.md)
