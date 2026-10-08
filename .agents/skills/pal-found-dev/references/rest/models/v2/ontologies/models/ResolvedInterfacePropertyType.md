# foundry_sdk.v2.ontologies.models.ResolvedInterfacePropertyType


An interface property type with additional fields to indicate constraints that need to be satisfied by
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
| description | description | typing.Optional[str] | None | A short text that describes the InterfacePropertyType. |
| data_type | dataType | ObjectPropertyType | required; no default | No additional field description in SDK source. |
| value_type_api_name | valueTypeApiName | typing.Optional[ValueTypeApiName] | default None | No additional field description in SDK source. |
| value_formatting | valueFormatting | typing.Optional[PropertyValueFormattingRule] | default None | No additional field description in SDK source. |
| require_implementation | requireImplementation | bool | required; no default | Whether each implementing object type must declare an implementation for this property. |

```python
class ResolvedInterfacePropertyType(core.ModelBase):
    """
    An interface property type with additional fields to indicate constraints that need to be satisfied by
    implementing object property types.
    """

    rid: InterfacePropertyTypeRid
    api_name: InterfacePropertyApiName = pydantic.Field(alias=str("apiName"))  # type: ignore[literal-required]
    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    """A short text that describes the InterfacePropertyType."""

    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    value_type_api_name: typing.Optional[ValueTypeApiName] = pydantic.Field(alias=str("valueTypeApiName"), default=None)  # type: ignore[literal-required]
    value_formatting: typing.Optional[PropertyValueFormattingRule] = pydantic.Field(alias=str("valueFormatting"), default=None)  # type: ignore[literal-required]
    require_implementation: bool = pydantic.Field(alias=str("requireImplementation"))  # type: ignore[literal-required]
    """Whether each implementing object type must declare an implementation for this property."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyApiName](InterfacePropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyTypeRid](InterfacePropertyTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectPropertyType](ObjectPropertyType.md)
- [foundry_sdk.v2.ontologies.models.PropertyValueFormattingRule](PropertyValueFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeApiName](ValueTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ResolvedInterfacePropertyType.md)
