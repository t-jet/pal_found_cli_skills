# foundry_sdk.v1.ontologies.models.ArraySizeConstraint


The parameter expects an array of values and the size of the array must fall within the defined range.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| lt | lt | typing.Optional[typing.Any] | None | Less than |
| lte | lte | typing.Optional[typing.Any] | None | Less than or equal |
| gt | gt | typing.Optional[typing.Any] | None | Greater than |
| gte | gte | typing.Optional[typing.Any] | None | Greater than or equal |
| type | type | typing.Literal['arraySize'] | 'arraySize' | No additional field description in SDK source. |

```python
class ArraySizeConstraint(core.ModelBase):
    """The parameter expects an array of values and the size of the array must fall within the defined range."""

    lt: typing.Optional[typing.Any] = None
    """Less than"""

    lte: typing.Optional[typing.Any] = None
    """Less than or equal"""

    gt: typing.Optional[typing.Any] = None
    """Greater than"""

    gte: typing.Optional[typing.Any] = None
    """Greater than or equal"""

    type: typing.Literal["arraySize"] = "arraySize"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ArraySizeConstraint.md)
