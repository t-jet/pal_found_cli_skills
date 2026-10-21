# foundry_sdk.v2.sql_queries.models.ParameterValue


A typed parameter value for SQL query execution.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ParameterValue: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ParameterDateValue",
        "ParameterStructValue",
        "ParameterStringValue",
        "ParameterDoubleValue",
        "ParameterIntegerValue",
        "ParameterFloatValue",
        "ParameterListValue",
        "ParameterAnyValue",
        "ParameterLongValue",
        "ParameterBooleanValue",
        "ParameterNullValue",
        "ParameterShortValue",
        "ParameterDecimalValue",
        "ParameterMapValue",
        "ParameterTimestampValue",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.sql_queries.models.ParameterAnyValue](ParameterAnyValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterBooleanValue](ParameterBooleanValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterDateValue](ParameterDateValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterDecimalValue](ParameterDecimalValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterDoubleValue](ParameterDoubleValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterFloatValue](ParameterFloatValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterIntegerValue](ParameterIntegerValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterListValue](ParameterListValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterLongValue](ParameterLongValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterMapValue](ParameterMapValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterNullValue](ParameterNullValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterShortValue](ParameterShortValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterStringValue](ParameterStringValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterStructValue](ParameterStructValue.md)
- [foundry_sdk.v2.sql_queries.models.ParameterTimestampValue](ParameterTimestampValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParameterValue.md)
