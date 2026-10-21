# foundry_sdk.v2.functions.models.ArrayConstraint


ArrayConstraint

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| minimum_size | minimumSize | typing.Optional[int] | default None | No additional field description in SDK source. |
| maximum_size | maximumSize | typing.Optional[int] | default None | No additional field description in SDK source. |
| unique_values | uniqueValues | bool | required; no default | No additional field description in SDK source. |
| value_constraint | valueConstraint | typing.Optional[ValueTypeConstraint] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['array'] | 'array' | No additional field description in SDK source. |

```python
class ArrayConstraint(core.ModelBase):
    """ArrayConstraint"""

    minimum_size: typing.Optional[int] = pydantic.Field(alias=str("minimumSize"), default=None)  # type: ignore[literal-required]
    maximum_size: typing.Optional[int] = pydantic.Field(alias=str("maximumSize"), default=None)  # type: ignore[literal-required]
    unique_values: bool = pydantic.Field(alias=str("uniqueValues"))  # type: ignore[literal-required]
    value_constraint: typing.Optional[ValueTypeConstraint] = pydantic.Field(alias=str("valueConstraint"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["array"] = "array"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.functions.models.ValueTypeConstraint](ValueTypeConstraint.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ArrayConstraint.md)
