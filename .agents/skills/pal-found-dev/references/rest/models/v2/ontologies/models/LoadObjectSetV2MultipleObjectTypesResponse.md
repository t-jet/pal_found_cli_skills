# foundry_sdk.v2.ontologies.models.LoadObjectSetV2MultipleObjectTypesResponse


Represents the API response when loading an `ObjectSet`. An `interfaceToObjectTypeMappings` field is
optionally returned if the type scope of the returned object set includes any interfaces. The "type scope"
of an object set refers to whether objects contain all their properties (object-type type scope) or just the
properties that implement interface properties (interface type scope). There can be multiple type scopes in a
single object set- some objects may have all their properties and some may only have interface properties.

The `interfaceToObjectTypeMappings` field contains mappings from `SharedPropertyTypeApiName`s on the interface(s) to
`PropertyApiName` for properties on the object(s).

The `interfaceToObjectTypeMappingsV2` field contains mappings from `InterfacePropertyApiName`s on the
interface(s) to `InterfacePropertyTypeImplementation` for properties on the object(s). This therefore includes
implementations of both properties backed by SharedPropertyTypes as well as properties defined on the interface.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| data | data | typing.List[OntologyObjectV2] | required; no default | The list of objects in the current page. |
| next_page_token | nextPageToken | typing.Optional[core_models.PageToken] | default None | No additional field description in SDK source. |
| total_count | totalCount | core_models.TotalCount | required; no default | No additional field description in SDK source. |
| interface_to_object_type_mappings | interfaceToObjectTypeMappings | typing.Dict[InterfaceTypeApiName, InterfaceToObjectTypeMappings] | required; no default | No additional field description in SDK source. |
| interface_to_object_type_mappings_v2 | interfaceToObjectTypeMappingsV2 | typing.Dict[InterfaceTypeApiName, InterfaceToObjectTypeMappingsV2] | required; no default | No additional field description in SDK source. |
| compute_usage | computeUsage | typing.Optional[core_models.ComputeSeconds] | default None | No additional field description in SDK source. |
| property_securities | propertySecurities | typing.Optional[typing.List[PropertySecurities]] | default None | No additional field description in SDK source. |

```python
class LoadObjectSetV2MultipleObjectTypesResponse(core.ModelBase):
    """
    Represents the API response when loading an `ObjectSet`. An `interfaceToObjectTypeMappings` field is
    optionally returned if the type scope of the returned object set includes any interfaces. The "type scope"
    of an object set refers to whether objects contain all their properties (object-type type scope) or just the
    properties that implement interface properties (interface type scope). There can be multiple type scopes in a
    single object set- some objects may have all their properties and some may only have interface properties.

    The `interfaceToObjectTypeMappings` field contains mappings from `SharedPropertyTypeApiName`s on the interface(s) to
    `PropertyApiName` for properties on the object(s).

    The `interfaceToObjectTypeMappingsV2` field contains mappings from `InterfacePropertyApiName`s on the
    interface(s) to `InterfacePropertyTypeImplementation` for properties on the object(s). This therefore includes
    implementations of both properties backed by SharedPropertyTypes as well as properties defined on the interface.
    """

    data: typing.List[OntologyObjectV2]
    """The list of objects in the current page."""

    next_page_token: typing.Optional[core_models.PageToken] = pydantic.Field(alias=str("nextPageToken"), default=None)  # type: ignore[literal-required]
    total_count: core_models.TotalCount = pydantic.Field(alias=str("totalCount"))  # type: ignore[literal-required]
    interface_to_object_type_mappings: typing.Dict[InterfaceTypeApiName, InterfaceToObjectTypeMappings] = pydantic.Field(alias=str("interfaceToObjectTypeMappings"))  # type: ignore[literal-required]
    interface_to_object_type_mappings_v2: typing.Dict[InterfaceTypeApiName, InterfaceToObjectTypeMappingsV2] = pydantic.Field(alias=str("interfaceToObjectTypeMappingsV2"))  # type: ignore[literal-required]
    compute_usage: typing.Optional[core_models.ComputeSeconds] = pydantic.Field(alias=str("computeUsage"), default=None)  # type: ignore[literal-required]
    property_securities: typing.Optional[typing.List[PropertySecurities]] = pydantic.Field(alias=str("propertySecurities"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.ComputeSeconds](../../core/models/ComputeSeconds.md)
- [foundry_sdk.v2.core.models.PageToken](../../core/models/PageToken.md)
- [foundry_sdk.v2.core.models.TotalCount](../../core/models/TotalCount.md)
- [foundry_sdk.v2.ontologies.models.InterfaceToObjectTypeMappings](InterfaceToObjectTypeMappings.md)
- [foundry_sdk.v2.ontologies.models.InterfaceToObjectTypeMappingsV2](InterfaceToObjectTypeMappingsV2.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectV2](OntologyObjectV2.md)
- [foundry_sdk.v2.ontologies.models.PropertySecurities](PropertySecurities.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](LoadObjectSetV2MultipleObjectTypesResponse.md)
