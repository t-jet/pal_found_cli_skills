# foundry_sdk.v2.ontologies.models.ObjectTypeInterfaceImplementation


ObjectTypeInterfaceImplementation

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| api_name | apiName | typing.Optional[InterfaceTypeApiName] | default None | No additional field description in SDK source. |
| rid | rid | typing.Optional[InterfaceTypeRid] | None | No additional field description in SDK source. |
| properties | properties | typing.Dict[SharedPropertyTypeApiName, PropertyApiName] | required; no default | No additional field description in SDK source. |
| properties_v2 | propertiesV2 | typing.Dict[InterfacePropertyApiName, InterfacePropertyTypeImplementation] | required; no default | No additional field description in SDK source. |
| links | links | typing.Dict[InterfaceLinkTypeApiName, typing.List[LinkTypeApiName]] | required; no default | No additional field description in SDK source. |

```python
class ObjectTypeInterfaceImplementation(core.ModelBase):
    """ObjectTypeInterfaceImplementation"""

    api_name: typing.Optional[InterfaceTypeApiName] = pydantic.Field(alias=str("apiName"), default=None)  # type: ignore[literal-required]
    rid: typing.Optional[InterfaceTypeRid] = None
    properties: typing.Dict[SharedPropertyTypeApiName, PropertyApiName]
    properties_v2: typing.Dict[InterfacePropertyApiName, InterfacePropertyTypeImplementation] = pydantic.Field(alias=str("propertiesV2"))  # type: ignore[literal-required]
    links: typing.Dict[InterfaceLinkTypeApiName, typing.List[LinkTypeApiName]]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeApiName](InterfaceLinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyApiName](InterfacePropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyTypeImplementation](InterfacePropertyTypeImplementation.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeRid](InterfaceTypeRid.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeApiName](SharedPropertyTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectTypeInterfaceImplementation.md)
