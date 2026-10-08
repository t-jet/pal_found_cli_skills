# foundry_sdk.v2.models.models.SearchExperimentsFilter



Filter for searching experiments using operator-based composition.
Supports equality, text matching, boolean combination operators, and compound filters
that atomically bind a name to a value comparison.

Example filters:
- Simple status: {"eq": {"field": "STATUS", "value": "RUNNING"}}
- Branch match: {"eq": {"field": "BRANCH", "value": "master"}}
- Parameter filter: {"parameterFilter": {"parameterName": "learning_rate", "operator": "GT", "value": 0.01}}
- Combined: {"and": {"filters": [
    {"eq": {"field": "STATUS", "value": "SUCCEEDED"}},
    {"parameterFilter": {"parameterName": "learning_rate", "operator": "GT", "value": 0.5}}
  ]}}


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SearchExperimentsFilter: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "SearchExperimentsSeriesFilter",
        "SearchExperimentsContainsFilter",
        "SearchExperimentsNotFilter",
        "SearchExperimentsOrFilter",
        "SearchExperimentsAndFilter",
        "SearchExperimentsParameterFilter",
        "SearchExperimentsSummaryMetricFilter",
        "SearchExperimentsEqualsFilter",
        "SearchExperimentsStartsWithFilter",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.models.models.SearchExperimentsAndFilter](SearchExperimentsAndFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsContainsFilter](SearchExperimentsContainsFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsEqualsFilter](SearchExperimentsEqualsFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsNotFilter](SearchExperimentsNotFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsOrFilter](SearchExperimentsOrFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsParameterFilter](SearchExperimentsParameterFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsSeriesFilter](SearchExperimentsSeriesFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsStartsWithFilter](SearchExperimentsStartsWithFilter.md)
- [foundry_sdk.v2.models.models.SearchExperimentsSummaryMetricFilter](SearchExperimentsSummaryMetricFilter.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchExperimentsFilter.md)
