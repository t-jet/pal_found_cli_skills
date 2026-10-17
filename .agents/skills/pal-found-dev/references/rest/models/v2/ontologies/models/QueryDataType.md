# foundry_sdk.v2.ontologies.models.QueryDataType


A union of all the types supported by Ontology Query parameters or outputs.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
QueryDataType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "OntologyInterfaceObjectType",
        "QueryStructType",
        core_models.StringType,
        core_models.IntegerType,
        "ThreeDimensionalAggregation",
        core_models.FloatType,
        core_models.LongType,
        core_models.UnsupportedType,
        core_models.AttachmentType,
        "QueryArrayType",
        "OntologyObjectSetType",
        "TwoDimensionalAggregation",
        "QueryTypeReferenceType",
        core_models.TimestampType,
        "QuerySetType",
        core_models.VoidType,
        "EntrySetType",
        core_models.DoubleType,
        "QueryUnionType",
        core_models.BooleanType,
        core_models.MediaReferenceType,
        core_models.NullType,
        "OntologyInterfaceObjectSetType",
        "OntologyObjectType",
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
- [foundry_sdk.v2.ontologies.models.EntrySetType](EntrySetType.md)
- [foundry_sdk.v2.ontologies.models.OntologyInterfaceObjectSetType](OntologyInterfaceObjectSetType.md)
- [foundry_sdk.v2.ontologies.models.OntologyInterfaceObjectType](OntologyInterfaceObjectType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectSetType](OntologyObjectSetType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectType](OntologyObjectType.md)
- [foundry_sdk.v2.ontologies.models.QueryArrayType](QueryArrayType.md)
- [foundry_sdk.v2.ontologies.models.QuerySetType](QuerySetType.md)
- [foundry_sdk.v2.ontologies.models.QueryStructType](QueryStructType.md)
- [foundry_sdk.v2.ontologies.models.QueryTypeReferenceType](QueryTypeReferenceType.md)
- [foundry_sdk.v2.ontologies.models.QueryUnionType](QueryUnionType.md)
- [foundry_sdk.v2.ontologies.models.ThreeDimensionalAggregation](ThreeDimensionalAggregation.md)
- [foundry_sdk.v2.ontologies.models.TwoDimensionalAggregation](TwoDimensionalAggregation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](QueryDataType.md)
