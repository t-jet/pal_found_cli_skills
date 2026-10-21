# foundry_sdk.v2.ontologies.models.ObjectTypeV2


Represents an object type in the Ontology.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| api_name | apiName | ObjectTypeApiName | required; no default | No additional field description in SDK source. |
| display_name | displayName | core_models.DisplayName | required; no default | No additional field description in SDK source. |
| status | status | core_models.ReleaseStatus | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | The description of the object type. |
| plural_display_name | pluralDisplayName | str | required; no default | The plural display name of the object type. |
| icon | icon | Icon | required; no default | No additional field description in SDK source. |
| primary_key | primaryKey | PropertyApiName | required; no default | No additional field description in SDK source. |
| properties | properties | typing.Dict[PropertyApiName, PropertyV2] | required; no default | A map of the properties of the object type. |
| rid | rid | ObjectTypeRid | required; no default | No additional field description in SDK source. |
| title_property | titleProperty | PropertyApiName | required; no default | No additional field description in SDK source. |
| visibility | visibility | typing.Optional[ObjectTypeVisibility] | None | No additional field description in SDK source. |
| aliases | aliases | typing.Optional[typing.List[str]] | None | Alternative names (synonyms) for the object type, usable as search terms. This field is only populated on<br>    the get-by-RID read paths (e.g. `getObjectTypeV2`); it is always empty on the `listObjectTypesV2` endpoint. |
| datasources | datasources | typing.Optional[typing.List[ObjectTypeDatasource]] | None | The datasources backing this object type which the user has access to see. Only populated when the request<br>    specifies `includeDatasources=true`. This list may be empty if the user doesn't have access to any<br>    datasources. |

```python
class ObjectTypeV2(core.ModelBase):
    """Represents an object type in the Ontology."""

    api_name: ObjectTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    status: core_models.ReleaseStatus
    description: typing.Optional[str] = None
    """The description of the object type."""

    plural_display_name: str = pydantic.Field(alias=str("pluralDisplayName"))  # type: ignore[literal-required]
    """The plural display name of the object type."""

    icon: Icon
    primary_key: PropertyApiName = pydantic.Field(alias=str("primaryKey"))  # type: ignore[literal-required]
    properties: typing.Dict[PropertyApiName, PropertyV2]
    """A map of the properties of the object type."""

    rid: ObjectTypeRid
    title_property: PropertyApiName = pydantic.Field(alias=str("titleProperty"))  # type: ignore[literal-required]
    visibility: typing.Optional[ObjectTypeVisibility] = None
    aliases: typing.Optional[typing.List[str]] = None
    """
    Alternative names (synonyms) for the object type, usable as search terms. This field is only populated on
    the get-by-RID read paths (e.g. `getObjectTypeV2`); it is always empty on the `listObjectTypesV2` endpoint.
    """

    datasources: typing.Optional[typing.List[ObjectTypeDatasource]] = None
    """
    The datasources backing this object type which the user has access to see. Only populated when the request
    specifies `includeDatasources=true`. This list may be empty if the user doesn't have access to any
    datasources.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.ReleaseStatus](../../core/models/ReleaseStatus.md)
- [foundry_sdk.v2.ontologies.models.Icon](Icon.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeDatasource](ObjectTypeDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeRid](ObjectTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeVisibility](ObjectTypeVisibility.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyV2](PropertyV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeV2.md)
