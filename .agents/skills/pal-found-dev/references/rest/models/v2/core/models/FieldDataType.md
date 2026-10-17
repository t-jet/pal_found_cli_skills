# foundry_sdk.v2.core.models.FieldDataType


FieldDataType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
FieldDataType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "StructFieldType",
        "DateType",
        "StringType",
        "ByteType",
        "DoubleType",
        "IntegerType",
        "FloatType",
        "LongType",
        "BooleanType",
        "ArrayFieldType",
        "BinaryType",
        "ShortType",
        "DecimalType",
        "MapFieldType",
        "TimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.ArrayFieldType](ArrayFieldType.md)
- [foundry_sdk.v2.core.models.BinaryType](BinaryType.md)
- [foundry_sdk.v2.core.models.BooleanType](BooleanType.md)
- [foundry_sdk.v2.core.models.ByteType](ByteType.md)
- [foundry_sdk.v2.core.models.DateType](DateType.md)
- [foundry_sdk.v2.core.models.DecimalType](DecimalType.md)
- [foundry_sdk.v2.core.models.DoubleType](DoubleType.md)
- [foundry_sdk.v2.core.models.FloatType](FloatType.md)
- [foundry_sdk.v2.core.models.IntegerType](IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](LongType.md)
- [foundry_sdk.v2.core.models.MapFieldType](MapFieldType.md)
- [foundry_sdk.v2.core.models.ShortType](ShortType.md)
- [foundry_sdk.v2.core.models.StringType](StringType.md)
- [foundry_sdk.v2.core.models.StructFieldType](StructFieldType.md)
- [foundry_sdk.v2.core.models.TimestampType](TimestampType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FieldDataType.md)
