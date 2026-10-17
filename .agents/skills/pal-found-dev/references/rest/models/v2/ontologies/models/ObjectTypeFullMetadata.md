# foundry_sdk.v2.ontologies.models.ObjectTypeFullMetadata


ObjectTypeFullMetadata

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_type | objectType | ObjectTypeV2 | required; no default | No additional field description in SDK source. |
| link_types | linkTypes | typing.List[LinkTypeSideV2] | required; no default | No additional field description in SDK source. |
| implements_interfaces | implementsInterfaces | typing.List[InterfaceTypeApiName] | required; no default | A list of interfaces that this object type implements. |
| implements_interfaces2 | implementsInterfaces2 | typing.Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementation] | required; no default | A list of interfaces that this object type implements and how it implements them. |
| shared_property_type_mapping | sharedPropertyTypeMapping | typing.Dict[SharedPropertyTypeApiName, PropertyApiName] | required; no default | A map from shared property type API name to backing local property API name for the shared property types <br>    present on this object type. |

```python
class ObjectTypeFullMetadata(core.ModelBase):
    """ObjectTypeFullMetadata"""

    object_type: ObjectTypeV2 = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    link_types: typing.List[LinkTypeSideV2] = pydantic.Field(alias=str("linkTypes"))  # type: ignore[literal-required]
    implements_interfaces: typing.List[InterfaceTypeApiName] = pydantic.Field(alias=str("implementsInterfaces"))  # type: ignore[literal-required]
    """A list of interfaces that this object type implements."""

    implements_interfaces2: typing.Dict[InterfaceTypeApiName, ObjectTypeInterfaceImplementation] = pydantic.Field(alias=str("implementsInterfaces2"))  # type: ignore[literal-required]
    """A list of interfaces that this object type implements and how it implements them."""

    shared_property_type_mapping: typing.Dict[SharedPropertyTypeApiName, PropertyApiName] = pydantic.Field(alias=str("sharedPropertyTypeMapping"))  # type: ignore[literal-required]
    """
    A map from shared property type API name to backing local property API name for the shared property types 
    present on this object type.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeSideV2](LinkTypeSideV2.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeInterfaceImplementation](ObjectTypeInterfaceImplementation.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeV2](ObjectTypeV2.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeApiName](SharedPropertyTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeFullMetadata.md)
