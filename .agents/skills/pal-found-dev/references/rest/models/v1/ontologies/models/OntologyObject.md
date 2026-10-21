# foundry_sdk.v1.ontologies.models.OntologyObject


Represents an object in the Ontology.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| properties | properties | typing.Dict[PropertyApiName, typing.Optional[PropertyValue]] | required; no default | A map of the property values of the object. |
| rid | rid | ObjectRid | required; no default | No additional field description in SDK source. |

```python
class OntologyObject(core.ModelBase):
    """Represents an object in the Ontology."""

    properties: typing.Dict[PropertyApiName, typing.Optional[PropertyValue]]
    """A map of the property values of the object."""

    rid: ObjectRid
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.ontologies.models.ObjectRid](ObjectRid.md)
- [foundry_sdk.v1.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v1.ontologies.models.PropertyValue](PropertyValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyObject.md)
