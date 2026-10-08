# foundry_sdk.v2.ontologies.models.SelectedPropertyOperation


Operation on a selected property, can be an aggregation function or retrieval of a single selected property

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SelectedPropertyOperation: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "SelectedPropertyApproximateDistinctAggregation",
        "SelectedPropertyMinAggregation",
        "SelectedPropertyAvgAggregation",
        "SelectedPropertyMaxAggregation",
        "SelectedPropertyApproximatePercentileAggregation",
        "GetSelectedPropertyOperation",
        "SelectedPropertyCountAggregation",
        "SelectedPropertySumAggregation",
        "SelectedPropertyCollectListAggregation",
        "SelectedPropertyExactDistinctAggregation",
        "SelectedPropertyCollectSetAggregation",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.GetSelectedPropertyOperation](GetSelectedPropertyOperation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyApproximateDistinctAggregation](SelectedPropertyApproximateDistinctAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyApproximatePercentileAggregation](SelectedPropertyApproximatePercentileAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyAvgAggregation](SelectedPropertyAvgAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyCollectListAggregation](SelectedPropertyCollectListAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyCollectSetAggregation](SelectedPropertyCollectSetAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyCountAggregation](SelectedPropertyCountAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyExactDistinctAggregation](SelectedPropertyExactDistinctAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyMaxAggregation](SelectedPropertyMaxAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertyMinAggregation](SelectedPropertyMinAggregation.md)
- [foundry_sdk.v2.ontologies.models.SelectedPropertySumAggregation](SelectedPropertySumAggregation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SelectedPropertyOperation.md)
