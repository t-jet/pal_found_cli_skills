# foundry_sdk.v2.ontologies.models.CreateObjectLogicRule


CreateObjectLogicRule

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| object_type_api_name | objectTypeApiName | ObjectTypeApiName | required; no default | No additional field description in SDK source. |
| property_arguments | propertyArguments | typing.Dict[PropertyApiName, LogicRuleArgument] | required; no default | No additional field description in SDK source. |
| struct_property_arguments | structPropertyArguments | typing.Dict[PropertyApiName, typing.Dict[StructFieldApiName, StructFieldArgument]] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['createObject'] | 'createObject' | No additional field description in SDK source. |

```python
class CreateObjectLogicRule(core.ModelBase):
    """CreateObjectLogicRule"""

    object_type_api_name: ObjectTypeApiName = pydantic.Field(alias=str("objectTypeApiName"))  # type: ignore[literal-required]
    property_arguments: typing.Dict[PropertyApiName, LogicRuleArgument] = pydantic.Field(alias=str("propertyArguments"))  # type: ignore[literal-required]
    struct_property_arguments: typing.Dict[PropertyApiName, typing.Dict[StructFieldApiName, StructFieldArgument]] = pydantic.Field(alias=str("structPropertyArguments"))  # type: ignore[literal-required]
    type: typing.Literal["createObject"] = "createObject"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.LogicRuleArgument](LogicRuleArgument.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](StructFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldArgument](StructFieldArgument.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateObjectLogicRule.md)
