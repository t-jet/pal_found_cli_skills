# foundry_sdk.v1.ontologies.models.OntologyDataType


A union of all the primitive types used by Palantir's Ontology-based products.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
OntologyDataType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "OntologyStructType",
        "OntologySetType",
        core_models.StringType,
        core_models.ByteType,
        core_models.DoubleType,
        core_models.IntegerType,
        core_models.FloatType,
        core_models.AnyType,
        core_models.LongType,
        core_models.BooleanType,
        core_models.CipherTextType,
        core_models.MarkingType,
        core_models.UnsupportedType,
        core_models.MediaReferenceType,
        "OntologyArrayType",
        "OntologyObjectSetType",
        core_models.BinaryType,
        core_models.ShortType,
        core_models.DecimalType,
        "OntologyMapType",
        core_models.TimestampType,
        "OntologyObjectType",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v1.core.models.AnyType](../../core/models/AnyType.md)
- [foundry_sdk.v1.core.models.BinaryType](../../core/models/BinaryType.md)
- [foundry_sdk.v1.core.models.BooleanType](../../core/models/BooleanType.md)
- [foundry_sdk.v1.core.models.ByteType](../../core/models/ByteType.md)
- [foundry_sdk.v1.core.models.CipherTextType](../../core/models/CipherTextType.md)
- [foundry_sdk.v1.core.models.DateType](../../core/models/DateType.md)
- [foundry_sdk.v1.core.models.DecimalType](../../core/models/DecimalType.md)
- [foundry_sdk.v1.core.models.DoubleType](../../core/models/DoubleType.md)
- [foundry_sdk.v1.core.models.FloatType](../../core/models/FloatType.md)
- [foundry_sdk.v1.core.models.IntegerType](../../core/models/IntegerType.md)
- [foundry_sdk.v1.core.models.LongType](../../core/models/LongType.md)
- [foundry_sdk.v1.core.models.MarkingType](../../core/models/MarkingType.md)
- [foundry_sdk.v1.core.models.MediaReferenceType](../../core/models/MediaReferenceType.md)
- [foundry_sdk.v1.core.models.ShortType](../../core/models/ShortType.md)
- [foundry_sdk.v1.core.models.StringType](../../core/models/StringType.md)
- [foundry_sdk.v1.core.models.TimestampType](../../core/models/TimestampType.md)
- [foundry_sdk.v1.core.models.UnsupportedType](../../core/models/UnsupportedType.md)
- [foundry_sdk.v1.ontologies.models.OntologyArrayType](OntologyArrayType.md)
- [foundry_sdk.v1.ontologies.models.OntologyMapType](OntologyMapType.md)
- [foundry_sdk.v1.ontologies.models.OntologyObjectSetType](OntologyObjectSetType.md)
- [foundry_sdk.v1.ontologies.models.OntologyObjectType](OntologyObjectType.md)
- [foundry_sdk.v1.ontologies.models.OntologySetType](OntologySetType.md)
- [foundry_sdk.v1.ontologies.models.OntologyStructType](OntologyStructType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyDataType.md)
