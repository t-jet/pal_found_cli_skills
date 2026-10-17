# foundry_sdk.v2.ontologies.models.LinkTypeSideV2


`foreignKeyPropertyApiName` is the API name of the foreign key on this object type. If absent, the link is
either a m2m link or the linked object has the foreign key and this object type has the primary key.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| api_name | apiName | LinkTypeApiName | required; no default | No additional field description in SDK source. |
| display_name | displayName | core_models.DisplayName | required; no default | No additional field description in SDK source. |
| status | status | core_models.ReleaseStatus | required; no default | No additional field description in SDK source. |
| object_type_api_name | objectTypeApiName | ObjectTypeApiName | required; no default | No additional field description in SDK source. |
| cardinality | cardinality | LinkTypeSideCardinality | required; no default | No additional field description in SDK source. |
| foreign_key_property_api_name | foreignKeyPropertyApiName | typing.Optional[PropertyApiName] | default None | No additional field description in SDK source. |
| link_type_rid | linkTypeRid | LinkTypeRid | required; no default | No additional field description in SDK source. |

```python
class LinkTypeSideV2(core.ModelBase):
    """
    `foreignKeyPropertyApiName` is the API name of the foreign key on this object type. If absent, the link is
    either a m2m link or the linked object has the foreign key and this object type has the primary key.
    """

    api_name: LinkTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    cardinality: LinkTypeSideCardinality
    foreign_key_property_api_name: typing.Optional[PropertyApiName] = pydantic.Field(alias=str("foreignKeyPropertyApiName"), default=None)  # type: ignore[literal-required]
    link_type_rid: LinkTypeRid = pydantic.Field(alias=str("linkTypeRid"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.ReleaseStatus](../../core/models/ReleaseStatus.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeRid](LinkTypeRid.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeSideCardinality](LinkTypeSideCardinality.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LinkTypeSideV2.md)
