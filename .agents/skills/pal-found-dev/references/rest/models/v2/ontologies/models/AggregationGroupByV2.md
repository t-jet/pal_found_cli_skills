# foundry_sdk.v2.ontologies.models.AggregationGroupByV2


Specifies a grouping for aggregation results.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
AggregationGroupByV2: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "AggregationDurationGroupingV2",
        "AggregationFixedWidthGroupingV2",
        "AggregationRangesGroupingV2",
        "AggregationExactGroupingV2",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.AggregationDurationGroupingV2](AggregationDurationGroupingV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationExactGroupingV2](AggregationExactGroupingV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationFixedWidthGroupingV2](AggregationFixedWidthGroupingV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationRangesGroupingV2](AggregationRangesGroupingV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregationGroupByV2.md)
