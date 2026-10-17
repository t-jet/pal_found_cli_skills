# foundry_sdk.v2.models.models.SummaryMetricAggregation


The type of aggregation computed for a summary metric.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SummaryMetricAggregation: typing_extensions.TypeAlias = typing.Literal["MIN", "MAX", "LAST"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SummaryMetricAggregation.md)
