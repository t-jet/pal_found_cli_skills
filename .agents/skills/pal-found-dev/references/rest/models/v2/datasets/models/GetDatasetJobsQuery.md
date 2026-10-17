# foundry_sdk.v2.datasets.models.GetDatasetJobsQuery


Query for getting jobs on given dataset.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
GetDatasetJobsQuery: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["GetDatasetJobsOrFilter", "GetDatasetJobsAndFilter", "GetDatasetJobsTimeFilter"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.datasets.models.GetDatasetJobsAndFilter](GetDatasetJobsAndFilter.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsOrFilter](GetDatasetJobsOrFilter.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsTimeFilter](GetDatasetJobsTimeFilter.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetDatasetJobsQuery.md)
