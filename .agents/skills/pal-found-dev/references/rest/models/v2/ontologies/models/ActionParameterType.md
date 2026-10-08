# foundry_sdk.v2.ontologies.models.ActionParameterType


A union of all the types supported by Ontology Action parameters.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ActionParameterType: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        core_models.DateType,
        "OntologyInterfaceObjectType",
        "OntologyStructType",
        core_models.StringType,
        core_models.DoubleType,
        core_models.IntegerType,
        core_models.GeoShapeType,
        core_models.LongType,
        "OntologyObjectTypeReferenceType",
        core_models.BooleanType,
        core_models.MarkingType,
        core_models.ScenarioReferenceType,
        core_models.AttachmentType,
        core_models.MediaReferenceType,
        "ActionParameterArrayType",
        "OntologyObjectSetType",
        core_models.GeohashType,
        core_models.VectorType,
        "OntologyObjectType",
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
- [foundry_sdk.v2.core.models.GeoShapeType](../../core/models/GeoShapeType.md)
- [foundry_sdk.v2.core.models.GeohashType](../../core/models/GeohashType.md)
- [foundry_sdk.v2.core.models.IntegerType](../../core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../core/models/LongType.md)
- [foundry_sdk.v2.core.models.MarkingType](../../core/models/MarkingType.md)
- [foundry_sdk.v2.core.models.MediaReferenceType](../../core/models/MediaReferenceType.md)
- [foundry_sdk.v2.core.models.ScenarioReferenceType](../../core/models/ScenarioReferenceType.md)
- [foundry_sdk.v2.core.models.StringType](../../core/models/StringType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.VectorType](../../core/models/VectorType.md)
- [foundry_sdk.v2.ontologies.models.ActionParameterArrayType](ActionParameterArrayType.md)
- [foundry_sdk.v2.ontologies.models.OntologyInterfaceObjectType](OntologyInterfaceObjectType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectSetType](OntologyObjectSetType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectType](OntologyObjectType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectTypeReferenceType](OntologyObjectTypeReferenceType.md)
- [foundry_sdk.v2.ontologies.models.OntologyStructType](OntologyStructType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ActionParameterType.md)
