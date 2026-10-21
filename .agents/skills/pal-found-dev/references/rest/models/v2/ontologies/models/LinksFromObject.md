# foundry_sdk.v2.ontologies.models.LinksFromObject


The Ontology Objects in this response will only ever have the `__primaryKey` and `__apiName`
fields present, thus functioning as object locators rather than full objects.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| source_object | sourceObject | typing.Optional[OntologyObjectV2] | default None | No additional field description in SDK source. |
| linked_objects | linkedObjects | typing.List[LinkedObjectLocator] | required; no default | No additional field description in SDK source. |

```python
class LinksFromObject(core.ModelBase):
    """
    The Ontology Objects in this response will only ever have the `__primaryKey` and `__apiName`
    fields present, thus functioning as object locators rather than full objects.
    """

    source_object: typing.Optional[OntologyObjectV2] = pydantic.Field(alias=str("sourceObject"), default=None)  # type: ignore[literal-required]
    linked_objects: typing.List[LinkedObjectLocator] = pydantic.Field(alias=str("linkedObjects"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.LinkedObjectLocator](LinkedObjectLocator.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectV2](OntologyObjectV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LinksFromObject.md)
