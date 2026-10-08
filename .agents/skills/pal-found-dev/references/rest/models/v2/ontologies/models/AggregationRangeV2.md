# foundry_sdk.v2.ontologies.models.AggregationRangeV2


Specifies a range from an inclusive start value to an exclusive end value.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| start_value | startValue | typing.Any | required; no default | Inclusive start. |
| end_value | endValue | typing.Any | required; no default | Exclusive end. |

```python
class AggregationRangeV2(core.ModelBase):
    """Specifies a range from an inclusive start value to an exclusive end value."""

    start_value: typing.Any = pydantic.Field(alias=str("startValue"))  # type: ignore[literal-required]
    """Inclusive start."""

    end_value: typing.Any = pydantic.Field(alias=str("endValue"))  # type: ignore[literal-required]
    """Exclusive end."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregationRangeV2.md)
