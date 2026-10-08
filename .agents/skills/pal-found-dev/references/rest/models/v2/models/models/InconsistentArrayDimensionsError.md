# foundry_sdk.v2.models.models.InconsistentArrayDimensionsError


Array elements have inconsistent dimensions.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| first_element_shape | firstElementShape | typing.List[int] | required; no default | The shape of the first array element |
| conflicting_element_shape | conflictingElementShape | typing.List[int] | required; no default | The shape of the conflicting array element |
| type | type | typing.Literal['inconsistentArrayDimensions'] | 'inconsistentArrayDimensions' | No additional field description in SDK source. |

```python
class InconsistentArrayDimensionsError(core.ModelBase):
    """Array elements have inconsistent dimensions."""

    first_element_shape: typing.List[int] = pydantic.Field(alias=str("firstElementShape"))  # type: ignore[literal-required]
    """The shape of the first array element"""

    conflicting_element_shape: typing.List[int] = pydantic.Field(alias=str("conflictingElementShape"))  # type: ignore[literal-required]
    """The shape of the conflicting array element"""

    type: typing.Literal["inconsistentArrayDimensions"] = "inconsistentArrayDimensions"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InconsistentArrayDimensionsError.md)
