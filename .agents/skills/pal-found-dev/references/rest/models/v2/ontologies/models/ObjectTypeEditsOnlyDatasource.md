# foundry_sdk.v2.ontologies.models.ObjectTypeEditsOnlyDatasource


An object type datasource that is not backed by any external Foundry resource. All properties on the object type
can only be populated via Actions. Other datasources have edit only *properties*, which are permissioned to the
backing tabular datasource. This datasource has no backing tabular datasource and is a true edit only object
type. Note that this datasource type is incompatible with any other datasource and all the properties on the
object type are backed by it.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| type | type | typing.Literal['editsOnly'] | 'editsOnly' | No additional field description in SDK source. |

```python
class ObjectTypeEditsOnlyDatasource(core.ModelBase):
    """
    An object type datasource that is not backed by any external Foundry resource. All properties on the object type
    can only be populated via Actions. Other datasources have edit only *properties*, which are permissioned to the
    backing tabular datasource. This datasource has no backing tabular datasource and is a true edit only object
    type. Note that this datasource type is incompatible with any other datasource and all the properties on the
    object type are backed by it.
    """

    type: typing.Literal["editsOnly"] = "editsOnly"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeEditsOnlyDatasource.md)
