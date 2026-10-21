# foundry_sdk.v2.ontologies.models.ValueTypeFieldType


ValueTypeFieldType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ValueTypeFieldType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "ValueTypeStructType",
        core_models.StringType,
        core_models.ByteType,
        core_models.DoubleType,
        "ValueTypeOptionalType",
        core_models.IntegerType,
        "ValueTypeUnionType",
        core_models.FloatType,
        core_models.LongType,
        "ValueTypeReferenceType",
        core_models.BooleanType,
        "ValueTypeArrayType",
        core_models.BinaryType,
        core_models.ShortType,
        "ValueTypeDecimalType",
        "ValueTypeMapType",
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.BinaryType](../../core/models/BinaryType.md)
- [foundry_sdk.v2.core.models.BooleanType](../../core/models/BooleanType.md)
- [foundry_sdk.v2.core.models.ByteType](../../core/models/ByteType.md)
- [foundry_sdk.v2.core.models.DateType](../../core/models/DateType.md)
- [foundry_sdk.v2.core.models.DoubleType](../../core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.FloatType](../../core/models/FloatType.md)
- [foundry_sdk.v2.core.models.IntegerType](../../core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../core/models/LongType.md)
- [foundry_sdk.v2.core.models.ShortType](../../core/models/ShortType.md)
- [foundry_sdk.v2.core.models.StringType](../../core/models/StringType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../core/models/TimestampType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeArrayType](ValueTypeArrayType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeDecimalType](ValueTypeDecimalType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeMapType](ValueTypeMapType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeOptionalType](ValueTypeOptionalType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeReferenceType](ValueTypeReferenceType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeStructType](ValueTypeStructType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeUnionType](ValueTypeUnionType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ValueTypeFieldType.md)
