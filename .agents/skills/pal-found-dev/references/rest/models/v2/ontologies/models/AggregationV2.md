# foundry_sdk.v2.ontologies.models.AggregationV2


Specifies an aggregation function.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
AggregationV2: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ApproximateDistinctAggregationV2",
        "MinAggregationV2",
        "AvgAggregationV2",
        "MaxAggregationV2",
        "ApproximatePercentileAggregationV2",
        "CountAggregationV2",
        "SumAggregationV2",
        "ExactDistinctAggregationV2",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ApproximateDistinctAggregationV2](ApproximateDistinctAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.ApproximatePercentileAggregationV2](ApproximatePercentileAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.AvgAggregationV2](AvgAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.CountAggregationV2](CountAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.ExactDistinctAggregationV2](ExactDistinctAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.MaxAggregationV2](MaxAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.MinAggregationV2](MinAggregationV2.md)
- [foundry_sdk.v2.ontologies.models.SumAggregationV2](SumAggregationV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregationV2.md)
