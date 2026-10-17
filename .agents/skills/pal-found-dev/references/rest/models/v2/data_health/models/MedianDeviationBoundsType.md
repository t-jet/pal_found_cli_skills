# foundry_sdk.v2.data_health.models.MedianDeviationBoundsType


The three types of median deviations a bounds type can have: - LOWER_BOUND – Tests for significant deviations below the median value, - UPPER_BOUND – Tests for significant deviations above the median value, - TWO_TAILED – Tests for significant deviations in either direction from the median value.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
MedianDeviationBoundsType: typing_extensions.TypeAlias = typing.Literal[
    "LOWER_BOUND", "UPPER_BOUND", "TWO_TAILED"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MedianDeviationBoundsType.md)
