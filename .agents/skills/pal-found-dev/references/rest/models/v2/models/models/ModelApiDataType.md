# foundry_sdk.v2.models.models.ModelApiDataType


ModelApiDataType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ModelApiDataType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        core_models.BooleanType,
        core_models.UnsupportedType,
        core_models.StringType,
        "ModelApiArrayType",
        core_models.DoubleType,
        core_models.IntegerType,
        core_models.FloatType,
        "ModelApiAnyType",
        "ModelApiMapType",
        core_models.LongType,
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.BooleanType](../../core/models/BooleanType.md)
- [foundry_sdk.v2.core.models.DateType](../../core/models/DateType.md)
- [foundry_sdk.v2.core.models.DoubleType](../../core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.FloatType](../../core/models/FloatType.md)
- [foundry_sdk.v2.core.models.IntegerType](../../core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../core/models/LongType.md)
- [foundry_sdk.v2.core.models.StringType](../../core/models/StringType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.UnsupportedType](../../core/models/UnsupportedType.md)
- [foundry_sdk.v2.models.models.ModelApiAnyType](ModelApiAnyType.md)
- [foundry_sdk.v2.models.models.ModelApiArrayType](ModelApiArrayType.md)
- [foundry_sdk.v2.models.models.ModelApiMapType](ModelApiMapType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelApiDataType.md)
