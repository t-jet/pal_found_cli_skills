# foundry_sdk.v2.ontologies.models.RangesConstraint


RangesConstraint

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| minimum_value | minimumValue | typing.Optional[PropertyValue] | default None | No additional field description in SDK source. |
| maximum_value | maximumValue | typing.Optional[PropertyValue] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['range'] | 'range' | No additional field description in SDK source. |

```python
class RangesConstraint(core.ModelBase):
    """RangesConstraint"""

    minimum_value: typing.Optional[PropertyValue] = pydantic.Field(alias=str("minimumValue"), default=None)  # type: ignore[literal-required]
    maximum_value: typing.Optional[PropertyValue] = pydantic.Field(alias=str("maximumValue"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["range"] = "range"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](PropertyValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](RangesConstraint.md)
