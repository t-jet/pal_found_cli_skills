# foundry_sdk.v2.ontologies.models.SearchObjectsForInterfaceRequest


SearchObjectsForInterfaceRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| where | where | typing.Optional[SearchJsonQueryV2] | None | No additional field description in SDK source. |
| order_by | orderBy | typing.Optional[SearchOrderByV2] | default None | No additional field description in SDK source. |
| augmented_properties | augmentedProperties | typing.Dict[ObjectTypeApiName, typing.List[PropertyApiName]] | required; no default | A map from object type API name to a list of property type API names. For each returned object, if the <br>    object’s object type is a key in the map, then we augment the response for that object type with the list <br>    of properties specified in the value. |
| augmented_shared_property_types | augmentedSharedPropertyTypes | typing.Dict[InterfaceTypeApiName, typing.List[SharedPropertyTypeApiName]] | required; no default | A map from interface type API name to a list of shared property type API names. For each returned object, if<br>    the object implements an interface that is a key in the map, then we augment the response for that object <br>    type with the list of properties specified in the value. |
| augmented_interface_property_types | augmentedInterfacePropertyTypes | typing.Dict[InterfaceTypeApiName, typing.List[InterfacePropertyApiName]] | required; no default | A map from interface type API name to a list of interface property type API names. For each returned object, <br>    if the object implements an interface that is a key in the map, then we augment the response for that object <br>    type with the list of properties specified in the value. |
| selected_shared_property_types | selectedSharedPropertyTypes | typing.List[SharedPropertyTypeApiName] | required; no default | A list of shared property type API names of the interface type that should be included in the response. <br>    Omit this parameter to include all properties of the interface type in the response. |
| selected_interface_property_types | selectedInterfacePropertyTypes | typing.List[InterfacePropertyApiName] | required; no default | A list of interface property type API names of the interface type that should be included in the response. <br>    Omit this parameter to include all properties of the interface type in the response. |
| selected_object_types | selectedObjectTypes | typing.List[ObjectTypeApiName] | required; no default | A list of object type API names that should be included in the response. If non-empty, object types that are<br>    not mentioned will not be included in the response even if they implement the specified interface. Omit the <br>    parameter to include all object types. |
| other_interface_types | otherInterfaceTypes | typing.List[InterfaceTypeApiName] | required; no default | A list of interface type API names. Object types must implement all the mentioned interfaces in order to be <br>    included in the response. |
| page_size | pageSize | typing.Optional[core_models.PageSize] | default None | No additional field description in SDK source. |
| page_token | pageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |

```python
class SearchObjectsForInterfaceRequest(core.ModelBase):
    """SearchObjectsForInterfaceRequest"""

    where: typing.Optional[SearchJsonQueryV2] = None
    order_by: typing.Optional[SearchOrderByV2] = pydantic.Field(alias=str("orderBy"), default=None)  # type: ignore[literal-required]
    augmented_properties: typing.Dict[ObjectTypeApiName, typing.List[PropertyApiName]] = pydantic.Field(alias=str("augmentedProperties"))  # type: ignore[literal-required]
    """
    A map from object type API name to a list of property type API names. For each returned object, if the 
    object’s object type is a key in the map, then we augment the response for that object type with the list 
    of properties specified in the value.
    """

    augmented_shared_property_types: typing.Dict[InterfaceTypeApiName, typing.List[SharedPropertyTypeApiName]] = pydantic.Field(alias=str("augmentedSharedPropertyTypes"))  # type: ignore[literal-required]
    """
    A map from interface type API name to a list of shared property type API names. For each returned object, if
    the object implements an interface that is a key in the map, then we augment the response for that object 
    type with the list of properties specified in the value.
    """

    augmented_interface_property_types: typing.Dict[InterfaceTypeApiName, typing.List[InterfacePropertyApiName]] = pydantic.Field(alias=str("augmentedInterfacePropertyTypes"))  # type: ignore[literal-required]
    """
    A map from interface type API name to a list of interface property type API names. For each returned object, 
    if the object implements an interface that is a key in the map, then we augment the response for that object 
    type with the list of properties specified in the value.
    """

    selected_shared_property_types: typing.List[SharedPropertyTypeApiName] = pydantic.Field(alias=str("selectedSharedPropertyTypes"))  # type: ignore[literal-required]
    """
    A list of shared property type API names of the interface type that should be included in the response. 
    Omit this parameter to include all properties of the interface type in the response.
    """

    selected_interface_property_types: typing.List[InterfacePropertyApiName] = pydantic.Field(alias=str("selectedInterfacePropertyTypes"))  # type: ignore[literal-required]
    """
    A list of interface property type API names of the interface type that should be included in the response. 
    Omit this parameter to include all properties of the interface type in the response.
    """

    selected_object_types: typing.List[ObjectTypeApiName] = pydantic.Field(alias=str("selectedObjectTypes"))  # type: ignore[literal-required]
    """
    A list of object type API names that should be included in the response. If non-empty, object types that are
    not mentioned will not be included in the response even if they implement the specified interface. Omit the 
    parameter to include all object types.
    """

    other_interface_types: typing.List[InterfaceTypeApiName] = pydantic.Field(alias=str("otherInterfaceTypes"))  # type: ignore[literal-required]
    """
    A list of interface type API names. Object types must implement all the mentioned interfaces in order to be 
    included in the response.
    """

    page_size: typing.Optional[core_models.PageSize] = pydantic.Field(alias=str("pageSize"), default=None)  # type: ignore[literal-required]
    page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("pageToken"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.PageSize](../../core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyApiName](InterfacePropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.SearchJsonQueryV2](SearchJsonQueryV2.md)
- [foundry_sdk.v2.ontologies.models.SearchOrderByV2](SearchOrderByV2.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeApiName](SharedPropertyTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SearchObjectsForInterfaceRequest.md)
