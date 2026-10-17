# foundry_sdk.v2.ontologies.models.ObjectTypeDatasource


A datasource that supplies property values for an object type. Each object type can have one or more
datasources; together they back all of the object type's properties. The `definition` carries the RID of the
backing Foundry resource (for example, the dataset RID for a dataset-backed object type), enabling callers to
navigate from an object type to its backing data.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | DatasourceRid | required; no default | No additional field description in SDK source. |
| definition | definition | ObjectTypeDatasourceDefinition | required; no default | No additional field description in SDK source. |

```python
class ObjectTypeDatasource(core.ModelBase):
    """
    A datasource that supplies property values for an object type. Each object type can have one or more
    datasources; together they back all of the object type's properties. The `definition` carries the RID of the
    backing Foundry resource (for example, the dataset RID for a dataset-backed object type), enabling callers to
    navigate from an object type to its backing data.
    """

    rid: DatasourceRid
    definition: ObjectTypeDatasourceDefinition
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.DatasourceRid](DatasourceRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeDatasourceDefinition](ObjectTypeDatasourceDefinition.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeDatasource.md)
