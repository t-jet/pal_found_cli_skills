# foundry_sdk.v2.ontologies.models.OntologyFullMetadata


OntologyFullMetadata

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| ontology | ontology | OntologyV2 | required; no default | No additional field description in SDK source. |
| object_types | objectTypes | typing.Dict[ObjectTypeApiName, ObjectTypeFullMetadata] | required; no default | No additional field description in SDK source. |
| action_types | actionTypes | typing.Dict[ActionTypeApiName, ActionTypeV2] | required; no default | No additional field description in SDK source. |
| query_types | queryTypes | typing.Dict[VersionedQueryTypeApiName, QueryTypeV2] | required; no default | No additional field description in SDK source. |
| interface_types | interfaceTypes | typing.Dict[InterfaceTypeApiName, InterfaceType] | required; no default | No additional field description in SDK source. |
| shared_property_types | sharedPropertyTypes | typing.Dict[SharedPropertyTypeApiName, SharedPropertyType] | required; no default | No additional field description in SDK source. |
| branch | branch | typing.Optional[core_models.BranchMetadata] | None | No additional field description in SDK source. |
| value_types | valueTypes | typing.Dict[ValueTypeApiName, OntologyValueType] | required; no default | No additional field description in SDK source. |

```python
class OntologyFullMetadata(core.ModelBase):
    """OntologyFullMetadata"""

    ontology: OntologyV2
    object_types: typing.Dict[ObjectTypeApiName, ObjectTypeFullMetadata] = pydantic.Field(alias=str("objectTypes"))  # type: ignore[literal-required]
    action_types: typing.Dict[ActionTypeApiName, ActionTypeV2] = pydantic.Field(alias=str("actionTypes"))  # type: ignore[literal-required]
    query_types: typing.Dict[VersionedQueryTypeApiName, QueryTypeV2] = pydantic.Field(alias=str("queryTypes"))  # type: ignore[literal-required]
    interface_types: typing.Dict[InterfaceTypeApiName, InterfaceType] = pydantic.Field(alias=str("interfaceTypes"))  # type: ignore[literal-required]
    shared_property_types: typing.Dict[SharedPropertyTypeApiName, SharedPropertyType] = pydantic.Field(alias=str("sharedPropertyTypes"))  # type: ignore[literal-required]
    branch: typing.Optional[core_models.BranchMetadata] = None
    value_types: typing.Dict[ValueTypeApiName, OntologyValueType] = pydantic.Field(alias=str("valueTypes"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchMetadata](../../core/models/BranchMetadata.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeApiName](ActionTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeV2](ActionTypeV2.md)
- [foundry_sdk.v2.ontologies.models.InterfaceType](InterfaceType.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeFullMetadata](ObjectTypeFullMetadata.md)
- [foundry_sdk.v2.ontologies.models.OntologyV2](OntologyV2.md)
- [foundry_sdk.v2.ontologies.models.OntologyValueType](OntologyValueType.md)
- [foundry_sdk.v2.ontologies.models.QueryTypeV2](QueryTypeV2.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyType](SharedPropertyType.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeApiName](SharedPropertyTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeApiName](ValueTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.VersionedQueryTypeApiName](VersionedQueryTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](OntologyFullMetadata.md)
