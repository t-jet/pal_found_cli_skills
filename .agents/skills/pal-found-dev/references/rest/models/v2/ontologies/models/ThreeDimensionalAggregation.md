# foundry_sdk.v2.ontologies.models.ThreeDimensionalAggregation


ThreeDimensionalAggregation

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| key_type | keyType | QueryAggregationKeyType | required; no default | No additional field description in SDK source. |
| value_type | valueType | TwoDimensionalAggregation | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['threeDimensionalAggregation'] | 'threeDimensionalAggregation' | No additional field description in SDK source. |

```python
class ThreeDimensionalAggregation(core.ModelBase):
    """ThreeDimensionalAggregation"""

    key_type: QueryAggregationKeyType = pydantic.Field(alias=str("keyType"))  # type: ignore[literal-required]
    value_type: TwoDimensionalAggregation = pydantic.Field(alias=str("valueType"))  # type: ignore[literal-required]
    type: typing.Literal["threeDimensionalAggregation"] = "threeDimensionalAggregation"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.QueryAggregationKeyType](QueryAggregationKeyType.md)
- [foundry_sdk.v2.ontologies.models.TwoDimensionalAggregation](TwoDimensionalAggregation.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ThreeDimensionalAggregation.md)
