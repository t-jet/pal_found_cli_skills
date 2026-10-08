# foundry_sdk.v2.data_health.models.DateBounds


The range of date values a check is expected to be within.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| lower_bound | lowerBound | typing.Optional[core.AwareDatetime] | default None | No additional field description in SDK source. |
| upper_bound | upperBound | typing.Optional[core.AwareDatetime] | default None | No additional field description in SDK source. |

```python
class DateBounds(core.ModelBase):
    """The range of date values a check is expected to be within."""

    lower_bound: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("lowerBound"), default=None)  # type: ignore[literal-required]
    upper_bound: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("upperBound"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DateBounds.md)
