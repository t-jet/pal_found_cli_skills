# foundry_sdk.v2.ontologies.models.CreateInterfaceLogicRule


CreateInterfaceLogicRule

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| interface_type_api_name | interfaceTypeApiName | InterfaceTypeApiName | required; no default | No additional field description in SDK source. |
| object_type | objectType | ParameterId | required; no default | No additional field description in SDK source. |
| shared_property_arguments | sharedPropertyArguments | typing.Dict[SharedPropertyTypeApiName, LogicRuleArgument] | required; no default | No additional field description in SDK source. |
| struct_property_arguments | structPropertyArguments | typing.Dict[SharedPropertyTypeApiName, typing.Dict[StructFieldApiName, StructFieldArgument]] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['createInterface'] | 'createInterface' | No additional field description in SDK source. |

```python
class CreateInterfaceLogicRule(core.ModelBase):
    """CreateInterfaceLogicRule"""

    interface_type_api_name: InterfaceTypeApiName = pydantic.Field(alias=str("interfaceTypeApiName"))  # type: ignore[literal-required]
    object_type: ParameterId = pydantic.Field(alias=str("objectType"))  # type: ignore[literal-required]
    shared_property_arguments: typing.Dict[SharedPropertyTypeApiName, LogicRuleArgument] = pydantic.Field(alias=str("sharedPropertyArguments"))  # type: ignore[literal-required]
    struct_property_arguments: typing.Dict[SharedPropertyTypeApiName, typing.Dict[StructFieldApiName, StructFieldArgument]] = pydantic.Field(alias=str("structPropertyArguments"))  # type: ignore[literal-required]
    type: typing.Literal["createInterface"] = "createInterface"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LogicRuleArgument](LogicRuleArgument.md)
- [foundry_sdk.v2.ontologies.models.ParameterId](ParameterId.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeApiName](SharedPropertyTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](StructFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldArgument](StructFieldArgument.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateInterfaceLogicRule.md)
