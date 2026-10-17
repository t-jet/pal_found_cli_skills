# foundry_sdk.v2.ontologies.models.ObjectSet


Represents the definition of an `ObjectSet` in the `Ontology`.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ObjectSet: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ObjectSetSearchAroundType",
        "ObjectSetStaticType",
        "ObjectSetIntersectionType",
        "ObjectSetWithPropertiesType",
        "ObjectSetInterfaceLinkSearchAroundType",
        "ObjectSetSubtractType",
        "ObjectSetNearestNeighborsType",
        "ObjectSetUnionType",
        "ObjectSetAsTypeType",
        "ObjectSetMethodInputType",
        "ObjectSetReferenceType",
        "ObjectSetFilterType",
        "ObjectSetInterfaceBaseType",
        "ObjectSetAsBaseObjectTypesType",
        "ObjectSetBaseType",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ObjectSetAsBaseObjectTypesType](ObjectSetAsBaseObjectTypesType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetAsTypeType](ObjectSetAsTypeType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetBaseType](ObjectSetBaseType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetFilterType](ObjectSetFilterType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetInterfaceBaseType](ObjectSetInterfaceBaseType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetInterfaceLinkSearchAroundType](ObjectSetInterfaceLinkSearchAroundType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetIntersectionType](ObjectSetIntersectionType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetMethodInputType](ObjectSetMethodInputType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetNearestNeighborsType](ObjectSetNearestNeighborsType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetReferenceType](ObjectSetReferenceType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetSearchAroundType](ObjectSetSearchAroundType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetStaticType](ObjectSetStaticType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetSubtractType](ObjectSetSubtractType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetUnionType](ObjectSetUnionType.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetWithPropertiesType](ObjectSetWithPropertiesType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectSet.md)
