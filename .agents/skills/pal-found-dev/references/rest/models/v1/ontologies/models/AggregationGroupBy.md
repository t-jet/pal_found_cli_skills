# foundry_sdk.v1.ontologies.models.AggregationGroupBy


Specifies a grouping for aggregation results.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
AggregationGroupBy: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "AggregationDurationGrouping",
        "AggregationFixedWidthGrouping",
        "AggregationRangesGrouping",
        "AggregationExactGrouping",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v1.ontologies.models.AggregationDurationGrouping](AggregationDurationGrouping.md)
- [foundry_sdk.v1.ontologies.models.AggregationExactGrouping](AggregationExactGrouping.md)
- [foundry_sdk.v1.ontologies.models.AggregationFixedWidthGrouping](AggregationFixedWidthGrouping.md)
- [foundry_sdk.v1.ontologies.models.AggregationRangesGrouping](AggregationRangesGrouping.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregationGroupBy.md)
