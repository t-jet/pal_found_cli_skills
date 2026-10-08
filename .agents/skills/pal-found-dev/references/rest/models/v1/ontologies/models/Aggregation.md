# foundry_sdk.v1.ontologies.models.Aggregation


Specifies an aggregation function.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
Aggregation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ApproximateDistinctAggregation",
        "MinAggregation",
        "AvgAggregation",
        "MaxAggregation",
        "CountAggregation",
        "SumAggregation",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v1.ontologies.models.ApproximateDistinctAggregation](ApproximateDistinctAggregation.md)
- [foundry_sdk.v1.ontologies.models.AvgAggregation](AvgAggregation.md)
- [foundry_sdk.v1.ontologies.models.CountAggregation](CountAggregation.md)
- [foundry_sdk.v1.ontologies.models.MaxAggregation](MaxAggregation.md)
- [foundry_sdk.v1.ontologies.models.MinAggregation](MinAggregation.md)
- [foundry_sdk.v1.ontologies.models.SumAggregation](SumAggregation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Aggregation.md)
