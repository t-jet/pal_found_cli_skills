# foundry_sdk.v2.ontologies.models.ActionParameterV2


Details about a parameter of an action.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| display_name | displayName | core_models.DisplayName | required; no default | No additional field description in SDK source. |
| description | description | typing.Optional[str] | None | No additional field description in SDK source. |
| data_type | dataType | ActionParameterType | required; no default | No additional field description in SDK source. |
| required | required | bool | required; no default | No additional field description in SDK source. |
| type_classes | typeClasses | typing.Optional[typing.List[TypeClass]] | default None | No additional field description in SDK source. |

```python
class ActionParameterV2(core.ModelBase):
    """Details about a parameter of an action."""

    display_name: core_models.DisplayName = pydantic.Field(alias=str("displayName"))  # type: ignore[literal-required]
    description: typing.Optional[str] = None
    data_type: ActionParameterType = pydantic.Field(alias=str("dataType"))  # type: ignore[literal-required]
    required: bool
    type_classes: typing.Optional[typing.List[TypeClass]] = pydantic.Field(alias=str("typeClasses"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.DisplayName](../../core/models/DisplayName.md)
- [foundry_sdk.v2.ontologies.models.ActionParameterType](ActionParameterType.md)
- [foundry_sdk.v2.ontologies.models.TypeClass](TypeClass.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ActionParameterV2.md)
