# foundry_sdk.v2.ontologies.models.ListScenarioEditedEntityTypesResponse


The object types and link types that have been modified within a scenario.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_types | objectTypes | typing.List[ObjectTypeApiName] | required; no default | The list of object type API names that have been modified within the scenario. |
| link_types | linkTypes | typing.List[ObjectTypeLinkTypeApiNameMapping] | required; no default | The list of edited link types grouped by source object type.<br><br>    Note that only many-to-many link types are returned. One-to-many link type edits are surfaced as object<br>    edits on the object type that owns the foreign key property. |

```python
class ListScenarioEditedEntityTypesResponse(core.ModelBase):
    """The object types and link types that have been modified within a scenario."""

    object_types: typing.List[ObjectTypeApiName] = pydantic.Field(alias=str("objectTypes"))  # type: ignore[literal-required]
    """The list of object type API names that have been modified within the scenario."""

    link_types: typing.List[ObjectTypeLinkTypeApiNameMapping] = pydantic.Field(alias=str("linkTypes"))  # type: ignore[literal-required]
    """
    The list of edited link types grouped by source object type.

    Note that only many-to-many link types are returned. One-to-many link type edits are surfaced as object
    edits on the object type that owns the foreign key property.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeLinkTypeApiNameMapping](ObjectTypeLinkTypeApiNameMapping.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ListScenarioEditedEntityTypesResponse.md)
