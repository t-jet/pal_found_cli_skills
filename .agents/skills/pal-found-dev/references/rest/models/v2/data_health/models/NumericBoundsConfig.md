# foundry_sdk.v2.data_health.models.NumericBoundsConfig


Configuration for numeric bounds check with severity settings.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| numeric_bounds | numericBounds | NumericBounds | required; no default | No additional field description in SDK source. |
| severity | severity | SeverityLevel | required; no default | No additional field description in SDK source. |

```python
class NumericBoundsConfig(core.ModelBase):
    """Configuration for numeric bounds check with severity settings."""

    numeric_bounds: NumericBounds = pydantic.Field(alias=str("numericBounds"))  # type: ignore[literal-required]
    severity: SeverityLevel
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.NumericBounds](NumericBounds.md)
- [foundry_sdk.v2.data_health.models.SeverityLevel](SeverityLevel.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NumericBoundsConfig.md)
