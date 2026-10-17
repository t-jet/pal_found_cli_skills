# foundry_sdk.v2.ontologies.models.PropertyV2


Details about some property of an object.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| display_name | displayName | typing.Optional[core_models.DisplayName] | default None | No additional field description in SDK source. |
| data_type | dataType | ObjectPropertyType | required; no default | No additional field description in SDK source. |
| rid | rid | PropertyTypeRid | required; no default | No additional field description in SDK source. |
| status | status | typing.Optional[PropertyTypeStatus] | None | No additional field description in SDK source. |
| visibility | visibility | typing.Optional[PropertyTypeVisibility] | None | No additional field description in SDK source. |
| value_type_api_name | valueTypeApiName | typing.Optional[ValueTypeApiName] | default None | No additional field description in SDK source. |
| value_formatting | valueFormatting | typing.Optional[PropertyValueFormattingRule] | default None | No additional field description in SDK source. |
| type_classes | typeClasses | typing.Optional[typing.List[TypeClass]] | default None | No additional field description in SDK source. |

```python
class PropertyV2(core.ModelBase):
    """Details about some property of an object."""

    description: typing.Optional[str] = None
    display_name: typing.Optional[core_models.DisplayName] = pydantic.Field(alias=str("displayName"), default=None)  # type: ignore[literal-required]
    data_type: ObjectPropertyType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    rid: PropertyTypeRid
    status: typing.Optional[PropertyTypeStatus] = None
    visibility: typing.Optional[PropertyTypeVisibility] = None
    value_type_api_name: typing.Optional[ValueTypeApiName] = pydantic.Field(alias=str("valueTypeApiName"), default=None)  # type: ignore[literal-required]
    value_formatting: typing.Optional[PropertyValueFormattingRule] = pydantic.Field(alias=str("valueFormatting"), default=None)  # type: ignore[literal-required]
    type_classes: typing.Optional[typing.List[TypeClass]] = pydantic.Field(alias=str("typeClasses"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.ontologies.models.ObjectPropertyType](ObjectPropertyType.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeRid](PropertyTypeRid.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeStatus](PropertyTypeStatus.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeVisibility](PropertyTypeVisibility.md)
- [foundry_sdk.v2.ontologies.models.PropertyValueFormattingRule](PropertyValueFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.TypeClass](TypeClass.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeApiName](ValueTypeApiName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PropertyV2.md)
