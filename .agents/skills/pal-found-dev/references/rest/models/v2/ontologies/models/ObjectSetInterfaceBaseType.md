# foundry_sdk.v2.ontologies.models.ObjectSetInterfaceBaseType


ObjectSetInterfaceBaseType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| interface_type | interfaceType | str | required; no default | An object set with objects that implement the interface with the given interface API name. The objects in <br>    the object set will only have properties that implement properties of the given interface, unless you set the includeAllBaseObjectProperties flag. |
| include_all_base_object_properties | includeAllBaseObjectProperties | typing.Optional[bool] | default None | A flag that will return all of the underlying object properties for the objects that implement the interface. <br>    This includes properties that don't explicitly implement an SPT on the interface. |
| type | type | typing.Literal['interfaceBase'] | 'interfaceBase' | No additional field description in SDK source. |

```python
class ObjectSetInterfaceBaseType(core.ModelBase):
    """ObjectSetInterfaceBaseType"""

    interface_type: str = pydantic.Field(alias=str("interfaceType"))  # type: ignore[literal-required]
    """
    An object set with objects that implement the interface with the given interface API name. The objects in 
    the object set will only have properties that implement properties of the given interface, unless you set the includeAllBaseObjectProperties flag.
    """

    include_all_base_object_properties: typing.Optional[bool] = pydantic.Field(alias=str("includeAllBaseObjectProperties"), default=None)  # type: ignore[literal-required]
    """
    A flag that will return all of the underlying object properties for the objects that implement the interface. 
    This includes properties that don't explicitly implement an SPT on the interface.
    """

    type: typing.Literal["interfaceBase"] = "interfaceBase"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ObjectSetInterfaceBaseType.md)
