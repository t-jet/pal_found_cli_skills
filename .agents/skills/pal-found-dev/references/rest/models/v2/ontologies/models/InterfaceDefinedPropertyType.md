# foundry_sdk.v2.ontologies.models.InterfaceDefinedPropertyType


An interface property type with an additional field to indicate constraints that need to be satisfied by
implementing object property types.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | InterfacePropertyTypeRid | required; no default | No additional field description in SDK source. |
| api_name | apiName | InterfacePropertyApiName | required; no default | No additional field description in SDK source. |
| display_name | displayName | core_models.DisplayName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | The description of the interface property type. |
| data_type | dataType | ObjectPropertyType | required; no default | No additional field description in SDK source. |
| value_type_api_name | valueTypeApiName | typing.Optional[ValueTypeApiName] | default None | No additional field description in SDK source. |
| require_implementation | requireImplementation | bool | required; no default | Whether each implementing object type must declare an implementation for this property. |
| type_classes | typeClasses | typing.Optional[typing.List[TypeClass]] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['interfaceDefinedPropertyType'] | 'interfaceDefinedPropertyType' | No additional field description in SDK source. |

```python
class InterfaceDefinedPropertyType(core.ModelBase):
    """
    An interface property type with an additional field to indicate constraints that need to be satisfied by
    implementing object property types.
    """

    rid: InterfacePropertyTypeRid
    api_name: InterfacePropertyApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """The description of the interface property type."""

    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    value_type_api_name: typing.Optional[ValueTypeApiName] = pydantic.Field(alias=str("valueTypeApiName"), default=None)  # type: ignore[literal-required]
    require_implementation: bool = pydantic.Field(alias=str("requireImplementation"))  # type: ignore[literal-required]
    """Whether each implementing object type must declare an implementation for this property."""

    type_classes: typing.Optional[typing.List[TypeClass]] = pydantic.Field(alias=str("typeClasses"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["interfaceDefinedPropertyType"] = "interfaceDefinedPropertyType"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyApiName](InterfacePropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyTypeRid](InterfacePropertyTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectPropertyType](ObjectPropertyType.md)
- [foundry_sdk.v2.ontologies.models.TypeClass](TypeClass.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeApiName](ValueTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InterfaceDefinedPropertyType.md)
