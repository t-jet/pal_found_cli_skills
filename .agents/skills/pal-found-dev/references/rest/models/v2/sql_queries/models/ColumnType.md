# foundry_sdk.v2.sql_queries.models.ColumnType


The type of a column in a SQL query result or parameter.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ColumnType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "StructColumnType",
        core_models.StringType,
        core_models.DoubleType,
        core_models.IntegerType,
        core_models.FloatType,
        "ListColumnType",
        "AnyColumnType",
        core_models.LongType,
        core_models.BooleanType,
        core_models.BinaryType,
        core_models.ShortType,
        "DecimalColumnType",
        "MapColumnType",
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.BinaryType](../../core/models/BinaryType.md)
- [foundry_sdk.v2.core.models.BooleanType](../../core/models/BooleanType.md)
- [foundry_sdk.v2.core.models.DateType](../../core/models/DateType.md)
- [foundry_sdk.v2.core.models.DoubleType](../../core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.FloatType](../../core/models/FloatType.md)
- [foundry_sdk.v2.core.models.IntegerType](../../core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../core/models/LongType.md)
- [foundry_sdk.v2.core.models.ShortType](../../core/models/ShortType.md)
- [foundry_sdk.v2.core.models.StringType](../../core/models/StringType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../core/models/TimestampType.md)
- [foundry_sdk.v2.sql_queries.models.AnyColumnType](AnyColumnType.md)
- [foundry_sdk.v2.sql_queries.models.DecimalColumnType](DecimalColumnType.md)
- [foundry_sdk.v2.sql_queries.models.ListColumnType](ListColumnType.md)
- [foundry_sdk.v2.sql_queries.models.MapColumnType](MapColumnType.md)
- [foundry_sdk.v2.sql_queries.models.StructColumnType](StructColumnType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ColumnType.md)
