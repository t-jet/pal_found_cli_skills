# foundry_sdk.v2.ontologies.models.InterfaceType


Represents an interface type in the Ontology.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | InterfaceTypeRid | required; no default | No additional field description in SDK source. |
| api_name | apiName | InterfaceTypeApiName | required; no default | No additional field description in SDK source. |
| display_name | displayName | core_models.DisplayName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | The description of the interface. |
| properties | properties | typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType] | required; no default | A map from a shared property type API name to the corresponding shared property type. The map describes the <br>    set of properties the interface has. A shared property type must be unique across all of the properties.<br>    This field only includes properties on the interface that are backed by shared property types. |
| all_properties | allProperties | typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType] | required; no default | A map from a shared property type API name to the corresponding shared property type. The map describes the <br>    set of properties the interface has, including properties from all directly and indirectly extended <br>    interfaces.<br>    This field only includes properties on the interface that are backed by shared property types. |
| properties_v2 | propertiesV2 | typing.Dict[InterfacePropertyApiName, InterfacePropertyType] | required; no default | A map from a interface property type API name to the corresponding interface property type. The map<br>    describes the set of properties the interface has. An interface property can either be backed by a shared<br>    property or it can be defined directly on the interface. |
| all_properties_v2 | allPropertiesV2 | typing.Dict[InterfacePropertyApiName, ResolvedInterfacePropertyType] | required; no default | A map from a interface property type API name to the corresponding interface property type. The map<br>    describes the set of properties the interface has, including properties from all directly and indirectly<br>    extended interfaces. |
| extends_interfaces | extendsInterfaces | typing.List[InterfaceTypeApiName] | required; no default | A list of interface API names that this interface extends. An interface can extend other interfaces to <br>    inherit their properties. |
| all_extends_interfaces | allExtendsInterfaces | typing.List[InterfaceTypeApiName] | required; no default | A list of interface API names that this interface extends, both directly and indirectly. |
| implemented_by_object_types | implementedByObjectTypes | typing.List[ObjectTypeApiName] | required; no default | A list of object API names that implement this interface. |
| links | links | typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkType] | required; no default | A map from an interface link type API name to the corresponding interface link type. The map describes the<br>    set of link types the interface has. |
| all_links | allLinks | typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkType] | required; no default | A map from an interface link type API name to the corresponding interface link type. The map describes the<br>    set of link types the interface has, including links from all directly and indirectly extended interfaces. |

```python
class InterfaceType(core.ModelBase):
    """Represents an interface type in the Ontology."""

    rid: InterfaceTypeRid
    api_name: InterfaceTypeApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description of the interface."""

    properties: typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType]
    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has. A shared property type must be unique across all of the properties.
    This field only includes properties on the interface that are backed by shared property types.
    """

    all_properties: typing.Dict[SharedPropertyTypeApiName, InterfaceSharedPropertyType] = pydantic.Field(alias=str("allProperties"))  # type: ignore[literal-required]
    """
    A map from a shared property type API name to the corresponding shared property type. The map describes the 
    set of properties the interface has, including properties from all directly and indirectly extended 
    interfaces.
    This field only includes properties on the interface that are backed by shared property types.
    """

    properties_v2: typing.Dict[InterfacePropertyApiName, InterfacePropertyType] = pydantic.Field(alias=str("propertiesV2"))  # type: ignore[literal-required]
    """
    A map from a interface property type API name to the corresponding interface property type. The map
    describes the set of properties the interface has. An interface property can either be backed by a shared
    property or it can be defined directly on the interface.
    """

    all_properties_v2: typing.Dict[InterfacePropertyApiName, ResolvedInterfacePropertyType] = pydantic.Field(alias=str("allPropertiesV2"))  # type: ignore[literal-required]
    """
    A map from a interface property type API name to the corresponding interface property type. The map
    describes the set of properties the interface has, including properties from all directly and indirectly
    extended interfaces.
    """

    extends_interfaces: typing.List[InterfaceTypeApiName] = pydantic.Field(alias=str("extendsInterfaces"))  # type: ignore[literal-required]
    """
    A list of interface API names that this interface extends. An interface can extend other interfaces to 
    inherit their properties.
    """

    all_extends_interfaces: typing.List[InterfaceTypeApiName] = pydantic.Field(alias=str("allExtendsInterfaces"))  # type: ignore[literal-required]
    """A list of interface API names that this interface extends, both directly and indirectly."""

    implemented_by_object_types: typing.List[ObjectTypeApiName] = pydantic.Field(alias=str("implementedByObjectTypes"))  # type: ignore[literal-required]
    """A list of object API names that implement this interface."""

    links: typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkType]
    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has.
    """

    all_links: typing.Dict[InterfaceLinkTypeApiName, InterfaceLinkType] = pydantic.Field(alias=str("allLinks"))  # type: ignore[literal-required]
    """
    A map from an interface link type API name to the corresponding interface link type. The map describes the
    set of link types the interface has, including links from all directly and indirectly extended interfaces.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkType](InterfaceLinkType.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeApiName](InterfaceLinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyApiName](InterfacePropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyType](InterfacePropertyType.md)
- [foundry_sdk.v2.ontologies.models.InterfaceSharedPropertyType](InterfaceSharedPropertyType.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeRid](InterfaceTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ResolvedInterfacePropertyType](ResolvedInterfacePropertyType.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeApiName](SharedPropertyTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfaceType.md)
