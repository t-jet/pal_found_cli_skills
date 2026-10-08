# foundry_sdk.v1.ontologies.models.ObjectType


Represents an object type in the Ontology.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| api_name | apiName | ObjectTypeApiName | required; no default | No additional field description in SDK source. |
| legacy_object_type_id | legacyObjectTypeId | typing.Optional[LegacyObjectTypeId] | default None | No additional field description in SDK source. |
| display_name | displayName | typing.Optional[core_models.DisplayName] | default None | No additional field description in SDK source. |
| status | status | core_models.ReleaseStatus | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | The description of the object type. |
| visibility | visibility | typing.Optional[ObjectTypeVisibility] | None | No additional field description in SDK source. |
| primary_key | primaryKey | typing.List[PropertyApiName] | required; no default | The primary key of the object. This is a list of properties that can be used to uniquely identify the object. |
| properties | properties | typing.Dict[PropertyApiName, Property] | required; no default | A map of the properties of the object type. |
| rid | rid | ObjectTypeRid | required; no default | No additional field description in SDK source. |

```python
class ObjectType(core.ModelBase):
    """Represents an object type in the Ontology."""

    api_name: ObjectTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    legacy_object_type_id: typing.Optional[LegacyObjectTypeId] = pydantic.Field(alias=str("legacyObjectTypeId"), default=None)  # type: ignore[literal-required]
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    description: typing.Optional[str] = None
    """The description of the object type."""

    visibility: typing.Optional[ObjectTypeVisibility] = None
    primary_key: typing.List[PropertyApiName] = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    """The primary key of the object. This is a list of properties that can be used to uniquely identify the object."""

    properties: typing.Dict[PropertyApiName, Property]
    """A map of the properties of the object type."""

    rid: ObjectTypeRid
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v1.core.models.ReleaseStatus](../../core/models/ReleaseStatus.md)
- [foundry_sdk.v1.ontologies.models.LegacyObjectTypeId](LegacyObjectTypeId.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeRid](ObjectTypeRid.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeVisibility](ObjectTypeVisibility.md)
- [foundry_sdk.v1.ontologies.models.Property](Property.md)
- [foundry_sdk.v1.ontologies.models.PropertyApiName](PropertyApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectType.md)
