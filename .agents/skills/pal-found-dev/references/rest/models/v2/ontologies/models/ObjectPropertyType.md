# foundry_sdk.v2.ontologies.models.ObjectPropertyType


A union of all the types supported by Ontology Object properties.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ObjectPropertyType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "StructType",
        core_models.StringType,
        core_models.ByteType,
        core_models.DoubleType,
        core_models.GeoPointType,
        core_models.GeotimeSeriesReferenceType,
        core_models.IntegerType,
        core_models.FloatType,
        core_models.GeoShapeType,
        core_models.LongType,
        core_models.BooleanType,
        core_models.CipherTextType,
        core_models.MarkingType,
        core_models.AttachmentType,
        core_models.MediaReferenceType,
        core_models.TimeseriesType,
        "OntologyObjectArrayType",
        core_models.ShortType,
        core_models.VectorType,
        core_models.DecimalType,
        core_models.TimestampType,
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.core.models.AttachmentType](../../core/models/AttachmentType.md)
- [foundry_sdk.v2.core.models.BooleanType](../../core/models/BooleanType.md)
- [foundry_sdk.v2.core.models.ByteType](../../core/models/ByteType.md)
- [foundry_sdk.v2.core.models.CipherTextType](../../core/models/CipherTextType.md)
- [foundry_sdk.v2.core.models.DateType](../../core/models/DateType.md)
- [foundry_sdk.v2.core.models.DecimalType](../../core/models/DecimalType.md)
- [foundry_sdk.v2.core.models.DoubleType](../../core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.FloatType](../../core/models/FloatType.md)
- [foundry_sdk.v2.core.models.GeoPointType](../../core/models/GeoPointType.md)
- [foundry_sdk.v2.core.models.GeoShapeType](../../core/models/GeoShapeType.md)
- [foundry_sdk.v2.core.models.GeotimeSeriesReferenceType](../../core/models/GeotimeSeriesReferenceType.md)
- [foundry_sdk.v2.core.models.IntegerType](../../core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../core/models/LongType.md)
- [foundry_sdk.v2.core.models.MarkingType](../../core/models/MarkingType.md)
- [foundry_sdk.v2.core.models.MediaReferenceType](../../core/models/MediaReferenceType.md)
- [foundry_sdk.v2.core.models.ShortType](../../core/models/ShortType.md)
- [foundry_sdk.v2.core.models.StringType](../../core/models/StringType.md)
- [foundry_sdk.v2.core.models.TimeseriesType](../../core/models/TimeseriesType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.VectorType](../../core/models/VectorType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectArrayType](OntologyObjectArrayType.md)
- [foundry_sdk.v2.ontologies.models.StructType](StructType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectPropertyType.md)
