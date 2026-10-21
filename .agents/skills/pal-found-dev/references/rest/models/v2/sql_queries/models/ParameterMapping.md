# foundry_sdk.v2.sql_queries.models.ParameterMapping


A mapping of named parameters to their values.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ParameterMapping: typing_extensions.TypeAlias = typing.Dict["ParameterName", "ParameterValue"]
```

## Referenced definitions

- [foundry_sdk.v2.sql_queries.models.ParameterName](ParameterName.md)
- [foundry_sdk.v2.sql_queries.models.ParameterValue](ParameterValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParameterMapping.md)
