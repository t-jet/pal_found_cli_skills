# foundry_sdk.v2.data_health.models.TimeBoundsConfig


Configuration for time bounds check with severity settings.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| time_bounds | timeBounds | TimeBounds | required; no default | No additional field description in SDK source. |
| severity | severity | SeverityLevel | required; no default | No additional field description in SDK source. |

```python
class TimeBoundsConfig(core.ModelBase):
    """Configuration for time bounds check with severity settings."""

    time_bounds: TimeBounds = pydantic.Field(alias=str("timeBounds"))  # type: ignore[literal-required]
    severity: SeverityLevel
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.SeverityLevel](SeverityLevel.md)
- [foundry_sdk.v2.data_health.models.TimeBounds](TimeBounds.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](TimeBoundsConfig.md)
