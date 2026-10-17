# foundry_sdk.v2.functions.models.QueryDataType


A union of all the types supported by Query parameters or outputs.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
QueryDataType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "QueryStructType",
        "QuerySetType",
        core_models.VoidType,
        core_models.StringType,
        core_models.DoubleType,
        core_models.IntegerType,
        "ThreeDimensionalAggregation",
        "QueryUnionType",
        core_models.FloatType,
        core_models.LongType,
        core_models.BooleanType,
        core_models.UnsupportedType,
        core_models.AttachmentType,
        core_models.MediaReferenceType,
        core_models.NullType,
        "QueryArrayType",
        "TwoDimensionalAggregation",
        "ValueTypeReference",
        "QueryTypeReferenceType",
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.AttachmentType](../../core/models/AttachmentType.md)
- [foundry_sdk.v2.core.models.BooleanType](../../core/models/BooleanType.md)
- [foundry_sdk.v2.core.models.DateType](../../core/models/DateType.md)
- [foundry_sdk.v2.core.models.DoubleType](../../core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.FloatType](../../core/models/FloatType.md)
- [foundry_sdk.v2.core.models.IntegerType](../../core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../core/models/LongType.md)
- [foundry_sdk.v2.core.models.MediaReferenceType](../../core/models/MediaReferenceType.md)
- [foundry_sdk.v2.core.models.NullType](../../core/models/NullType.md)
- [foundry_sdk.v2.core.models.StringType](../../core/models/StringType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.UnsupportedType](../../core/models/UnsupportedType.md)
- [foundry_sdk.v2.core.models.VoidType](../../core/models/VoidType.md)
- [foundry_sdk.v2.functions.models.QueryArrayType](QueryArrayType.md)
- [foundry_sdk.v2.functions.models.QuerySetType](QuerySetType.md)
- [foundry_sdk.v2.functions.models.QueryStructType](QueryStructType.md)
- [foundry_sdk.v2.functions.models.QueryTypeReferenceType](QueryTypeReferenceType.md)
- [foundry_sdk.v2.functions.models.QueryUnionType](QueryUnionType.md)
- [foundry_sdk.v2.functions.models.ThreeDimensionalAggregation](ThreeDimensionalAggregation.md)
- [foundry_sdk.v2.functions.models.TwoDimensionalAggregation](TwoDimensionalAggregation.md)
- [foundry_sdk.v2.functions.models.ValueTypeReference](ValueTypeReference.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](QueryDataType.md)
