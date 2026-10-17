# foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsFilter


Search criteria for checkpoint records.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SearchCheckpointRecordsFilter: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "SearchCheckpointRecordsNotFilter",
        "SearchCheckpointRecordsOrFilter",
        "SearchCheckpointRecordsTextSearchFilter",
        "SearchCheckpointRecordsAndFilter",
        "SearchCheckpointRecordsLtFilter",
        "SearchCheckpointRecordsGteFilter",
        "SearchCheckpointRecordsEqualsFilter",
        "SearchCheckpointRecordsCheckpointedItemIdFilter",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsAndFilter](SearchCheckpointRecordsAndFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsCheckpointedItemIdFilter](SearchCheckpointRecordsCheckpointedItemIdFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsEqualsFilter](SearchCheckpointRecordsEqualsFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsGteFilter](SearchCheckpointRecordsGteFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsLtFilter](SearchCheckpointRecordsLtFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsNotFilter](SearchCheckpointRecordsNotFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsOrFilter](SearchCheckpointRecordsOrFilter.md)
- [foundry_sdk.v2.checkpoints.models.SearchCheckpointRecordsTextSearchFilter](SearchCheckpointRecordsTextSearchFilter.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchCheckpointRecordsFilter.md)
