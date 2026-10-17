# foundry_sdk.v2.aip_agents.models.ObjectContext


Details of relevant retrieved object instances for a user's message to include as additional context in the prompt to the Agent.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_rids | objectRids | typing.List[ontologies_models.ObjectRid] | required; no default | The RIDs of the relevant object instances to include in the prompt. |
| property_type_rids | propertyTypeRids | typing.List[ontologies_models.PropertyTypeRid] | required; no default | The RIDs of the property types for the given objects to include in the prompt. |
| type | type | typing.Literal['objectContext'] | 'objectContext' | No additional field description in SDK source. |

```python
class ObjectContext(core.ModelBase):
    """Details of relevant retrieved object instances for a user's message to include as additional context in the prompt to the Agent."""

    object_rids: typing.List[ontologies_models.ObjectRid] = pydantic.Field(alias=str("objectRids"))  # type: ignore[literal-required]
    """The RIDs of the relevant object instances to include in the prompt."""

    property_type_rids: typing.List[ontologies_models.PropertyTypeRid] = pydantic.Field(alias=str("propertyTypeRids"))  # type: ignore[literal-required]
    """The RIDs of the property types for the given objects to include in the prompt."""

    type: typing.Literal["objectContext"] = "objectContext"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ObjectRid](../../ontologies/models/ObjectRid.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeRid](../../ontologies/models/PropertyTypeRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectContext.md)
