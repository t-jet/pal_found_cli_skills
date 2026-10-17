# foundry_sdk.v2.ontologies.models.LoadOntologyMetadataRequest


The Ontology metadata (i.e., object, link, action, query, and interface types) to load.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_types | objectTypes | typing.List[ObjectTypeApiName] | required; no default | No additional field description in SDK source. |
| link_types | linkTypes | typing.List[LinkTypeApiName] | required; no default | No additional field description in SDK source. |
| action_types | actionTypes | typing.List[ActionTypeApiName] | required; no default | No additional field description in SDK source. |
| query_types | queryTypes | typing.List[VersionedQueryTypeApiName] | required; no default | No additional field description in SDK source. |
| interface_types | interfaceTypes | typing.List[InterfaceTypeApiName] | required; no default | No additional field description in SDK source. |

```python
class LoadOntologyMetadataRequest(core.ModelBase):
    """The Ontology metadata (i.e., object, link, action, query, and interface types) to load."""

    object_types: typing.List[ObjectTypeApiName] = pydantic.Field(alias=str("objectTypes"))  # type: ignore[literal-required]
    link_types: typing.List[LinkTypeApiName] = pydantic.Field(alias=str("linkTypes"))  # type: ignore[literal-required]
    action_types: typing.List[ActionTypeApiName] = pydantic.Field(alias=str("actionTypes"))  # type: ignore[literal-required]
    query_types: typing.List[VersionedQueryTypeApiName] = pydantic.Field(alias=str("queryTypes"))  # type: ignore[literal-required]
    interface_types: typing.List[InterfaceTypeApiName] = pydantic.Field(alias=str("interfaceTypes"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeApiName](ActionTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.VersionedQueryTypeApiName](VersionedQueryTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LoadOntologyMetadataRequest.md)
