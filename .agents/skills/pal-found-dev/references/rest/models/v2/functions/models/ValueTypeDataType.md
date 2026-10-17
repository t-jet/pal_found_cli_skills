# foundry_sdk.v2.functions.models.ValueTypeDataType


The underlying base type of a value type.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ValueTypeDataType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ValueTypeDataTypeDateType",
        "ValueTypeDataTypeStructType",
        "ValueTypeDataTypeStringType",
        "ValueTypeDataTypeByteType",
        "ValueTypeDataTypeDoubleType",
        "ValueTypeDataTypeOptionalType",
        "ValueTypeDataTypeIntegerType",
        "ValueTypeDataTypeUnionType",
        "ValueTypeDataTypeFloatType",
        "ValueTypeDataTypeLongType",
        "ValueTypeDataTypeBooleanType",
        "ValueTypeDataTypeArrayType",
        "ValueTypeDataTypeBinaryType",
        "ValueTypeDataTypeValueTypeReference",
        "ValueTypeDataTypeShortType",
        "ValueTypeDataTypeDecimalType",
        "ValueTypeDataTypeMapType",
        "ValueTypeDataTypeTimestampType",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.functions.models.ValueTypeDataTypeArrayType](ValueTypeDataTypeArrayType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeBinaryType](ValueTypeDataTypeBinaryType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeBooleanType](ValueTypeDataTypeBooleanType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeByteType](ValueTypeDataTypeByteType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeDateType](ValueTypeDataTypeDateType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeDecimalType](ValueTypeDataTypeDecimalType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeDoubleType](ValueTypeDataTypeDoubleType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeFloatType](ValueTypeDataTypeFloatType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeIntegerType](ValueTypeDataTypeIntegerType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeLongType](ValueTypeDataTypeLongType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeMapType](ValueTypeDataTypeMapType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeOptionalType](ValueTypeDataTypeOptionalType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeShortType](ValueTypeDataTypeShortType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeStringType](ValueTypeDataTypeStringType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeStructType](ValueTypeDataTypeStructType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeTimestampType](ValueTypeDataTypeTimestampType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeUnionType](ValueTypeDataTypeUnionType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeValueTypeReference](ValueTypeDataTypeValueTypeReference.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ValueTypeDataType.md)
