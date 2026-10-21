# foundry_sdk.v2.sql_queries.models.Parameters



Parameters for SQL query execution. Can be either unnamed positional parameters
or named parameter mappings.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
Parameters: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["UnnamedParameterValues", "NamedParameterMapping"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.sql_queries.models.NamedParameterMapping](NamedParameterMapping.md)
- [foundry_sdk.v2.sql_queries.models.UnnamedParameterValues](UnnamedParameterValues.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Parameters.md)
