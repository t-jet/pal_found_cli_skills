# foundry_sdk.v2.ontologies.models.ModifyEdit


ModifyEdit

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| includes_all_previous_values | includesAllPreviousValues | typing.Optional[bool] | default None | No additional field description in SDK source. |
| previous_properties | previousProperties | typing.Dict[PropertyApiName, PropertyValue] | required; no default | The property values before the modification.<br>    Only includes properties that were changed.<br>    Maps property API names to their previous values. |
| properties | properties | typing.Dict[PropertyApiName, PropertyValue] | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['modifyEdit'] | 'modifyEdit' | No additional field description in SDK source. |

```python
class ModifyEdit(core.ModelBase):
    """ModifyEdit"""

    includes_all_previous_values: typing.Optional[bool] = pydantic.Field(alias=str("includesAllPreviousValues"), default=None)  # type: ignore[literal-required]
    previous_properties: typing.Dict[PropertyApiName, PropertyValue] = pydantic.Field(alias=str("previousProperties"))  # type: ignore[literal-required]
    """
    The property values before the modification.
    Only includes properties that were changed.
    Maps property API names to their previous values.
    """

    properties: typing.Dict[PropertyApiName, PropertyValue]
    type: typing.Literal["modifyEdit"] = "modifyEdit"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](PropertyValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModifyEdit.md)
