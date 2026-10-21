# foundry_sdk.v2.data_health.models.PercentageBounds


The configuration for the range of percentage values between which the health check is expected to succeed.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| lower_bound_percentage | lowerBoundPercentage | typing.Optional[PercentageValue] | default None | No additional field description in SDK source. |
| upper_bound_percentage | upperBoundPercentage | typing.Optional[PercentageValue] | default None | No additional field description in SDK source. |

```python
class PercentageBounds(core.ModelBase):
    """The configuration for the range of percentage values between which the health check is expected to succeed."""

    lower_bound_percentage: typing.Optional[PercentageValue] = pydantic.Field(alias=str("lowerBoundPercentage"), default=None)  # type: ignore[literal-required]
    upper_bound_percentage: typing.Optional[PercentageValue] = pydantic.Field(alias=str("upperBoundPercentage"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.data_health.models.PercentageValue](PercentageValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PercentageBounds.md)
