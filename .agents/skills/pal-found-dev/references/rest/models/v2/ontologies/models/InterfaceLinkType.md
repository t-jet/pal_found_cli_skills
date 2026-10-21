# foundry_sdk.v2.ontologies.models.InterfaceLinkType


A link type constraint defined at the interface level where the implementation of the links is provided
by the implementing object types.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | InterfaceLinkTypeRid | required; no default | No additional field description in SDK source. |
| api_name | apiName | InterfaceLinkTypeApiName | required; no default | No additional field description in SDK source. |
| display_name | displayName | core_models.DisplayName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | The description of the interface link type. |
| linked_entity_api_name | linkedEntityApiName | InterfaceLinkTypeLinkedEntityApiName | required; no default | No additional field description in SDK source. |
| cardinality | cardinality | InterfaceLinkTypeCardinality | required; no default | No additional field description in SDK source. |
| required | required | bool | required; no default | Whether each implementing object type must declare at least one implementation of this link. |

```python
class InterfaceLinkType(core.ModelBase):
    """
    A link type constraint defined at the interface level where the implementation of the links is provided
    by the implementing object types.
    """

    rid: InterfaceLinkTypeRid
    api_name: InterfaceLinkTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description of the interface link type."""

    linked_entity_api_name: InterfaceLinkTypeLinkedEntityApiName = pydantic.Field(alias=str("linkedEntityApiName"))  # type: ignore[literal-required]
    cardinality: InterfaceLinkTypeCardinality
    required: bool
    """Whether each implementing object type must declare at least one implementation of this link."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeApiName](InterfaceLinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeCardinality](InterfaceLinkTypeCardinality.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeLinkedEntityApiName](InterfaceLinkTypeLinkedEntityApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeRid](InterfaceLinkTypeRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfaceLinkType.md)
