# foundry_sdk.v2.ontologies.models.ObjectTypeDatasourceDefinition



The definition of an object type datasource, identifying the kind of Foundry resource that backs the object
type.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ObjectTypeDatasourceDefinition: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "ObjectTypeTimeSeriesDatasource",
        "ObjectTypeUnsupportedDatasource",
        "ObjectTypeRestrictedViewDatasource",
        "ObjectTypeStreamDatasource",
        "ObjectTypeMediaSetViewDatasource",
        "ObjectTypeDirectDatasource",
        "ObjectTypeGeotimeSeriesDatasource",
        "ObjectTypeEditsOnlyDatasource",
        "ObjectTypeDatasetDatasource",
        "ObjectTypeTableDatasource",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.ontologies.models.ObjectTypeDatasetDatasource](ObjectTypeDatasetDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeDirectDatasource](ObjectTypeDirectDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeEditsOnlyDatasource](ObjectTypeEditsOnlyDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeGeotimeSeriesDatasource](ObjectTypeGeotimeSeriesDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeMediaSetViewDatasource](ObjectTypeMediaSetViewDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeRestrictedViewDatasource](ObjectTypeRestrictedViewDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeStreamDatasource](ObjectTypeStreamDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeTableDatasource](ObjectTypeTableDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeTimeSeriesDatasource](ObjectTypeTimeSeriesDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeUnsupportedDatasource](ObjectTypeUnsupportedDatasource.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeDatasourceDefinition.md)
