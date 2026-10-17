# foundry_sdk.v2.data_health.models.ReplaceNumericColumnRangeCheckConfig


ReplaceNumericColumnRangeCheckConfig

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| numeric_bounds_config | numericBoundsConfig | NumericBoundsConfig | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['numericColumnRange'] | 'numericColumnRange' | No additional field description in SDK source. |

```python
class ReplaceNumericColumnRangeCheckConfig(core.ModelBase):
    """ReplaceNumericColumnRangeCheckConfig"""

    numeric_bounds_config: NumericBoundsConfig = pydantic.Field(alias=str("numericBoundsConfig"))  # type: ignore[literal-required]
    type: typing.Literal["numericColumnRange"] = "numericColumnRange"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.NumericBoundsConfig](NumericBoundsConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceNumericColumnRangeCheckConfig.md)
