# foundry_sdk.v2.models.models.SearchExperimentsOrderByField


Fields to order experiment search results by.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
SearchExperimentsOrderByField: typing_extensions.TypeAlias = typing.Literal[
    "EXPERIMENT_NAME", "CREATED_TIME"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchExperimentsOrderByField.md)
