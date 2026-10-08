# foundry_sdk.v2.ontologies.models.LinkedObjectLocator


Does not contain information about the source object. Should be used in a nested type that provides information about source objects.
The `targetObject` Ontology Object in this response will only ever have the `__primaryKey` and `__apiName`
fields present, thus functioning as object locators rather than full objects.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| target_object | targetObject | typing.Optional[OntologyObjectV2] | default None | No additional field description in SDK source. |
| link_type | linkType | typing.Optional[LinkTypeApiName] | default None | No additional field description in SDK source. |

```python
class LinkedObjectLocator(core.ModelBase):
    """
    Does not contain information about the source object. Should be used in a nested type that provides information about source objects.
    The `targetObject` Ontology Object in this response will only ever have the `__primaryKey` and `__apiName`
    fields present, thus functioning as object locators rather than full objects.
    """

    target_object: typing.Optional[OntologyObjectV2] = pydantic.Field(alias=str("targetObject"), default=None)  # type: ignore[literal-required]
    link_type: typing.Optional[LinkTypeApiName] = pydantic.Field(alias=str("linkType"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectV2](OntologyObjectV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LinkedObjectLocator.md)
