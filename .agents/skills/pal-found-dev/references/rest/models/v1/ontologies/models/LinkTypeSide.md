# foundry_sdk.v1.ontologies.models.LinkTypeSide


LinkTypeSide

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

```python
class LinkTypeSide(core.ModelBase):
    """LinkTypeSide"""

    api_name: LinkTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    cardinality: LinkTypeSideCardinality
    foreign_key_property_api_name: typing.Optional[PropertyApiName] = pydantic.Field(alias=str("foreignKeyPropertyApiName"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v1.core.models.ReleaseStatus](../../core/models/ReleaseStatus.md)
- [foundry_sdk.v1.ontologies.models.LinkTypeApiName](LinkTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.LinkTypeSideCardinality](LinkTypeSideCardinality.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.PropertyApiName](PropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LinkTypeSide.md)
