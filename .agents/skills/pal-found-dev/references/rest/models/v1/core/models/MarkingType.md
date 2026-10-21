# foundry_sdk.v1.core.models.MarkingType


MarkingType

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| marking_type | markingType | typing.Optional[MarkingTypeValue] | default None | No additional field description in SDK source. |
| type | type | typing.Literal['marking'] | 'marking' | No additional field description in SDK source. |

```python
class MarkingType(core.ModelBase):
    """MarkingType"""

    marking_type: typing.Optional[MarkingTypeValue] = pydantic.Field(alias=str("markingType"), default=None)  # type: ignore[literal-required]
    type: typing.Literal["marking"] = "marking"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.core.models.MarkingTypeValue](MarkingTypeValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](MarkingType.md)
