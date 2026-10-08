# foundry_sdk.v2.orchestration.models.SearchBuildsFilter


SearchBuildsFilter

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SearchBuildsFilter: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "SearchBuildsNotFilter",
        "SearchBuildsOrFilter",
        "SearchBuildsAndFilter",
        "SearchBuildsLtFilter",
        "SearchBuildsGteFilter",
        "SearchBuildsEqualsFilter",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.orchestration.models.SearchBuildsAndFilter](SearchBuildsAndFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsEqualsFilter](SearchBuildsEqualsFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsGteFilter](SearchBuildsGteFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsLtFilter](SearchBuildsLtFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsNotFilter](SearchBuildsNotFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsOrFilter](SearchBuildsOrFilter.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchBuildsFilter.md)
