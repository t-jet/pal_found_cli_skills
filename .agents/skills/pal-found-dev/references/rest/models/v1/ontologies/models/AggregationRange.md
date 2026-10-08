# foundry_sdk.v1.ontologies.models.AggregationRange


Specifies a date range from an inclusive start date to an exclusive end date.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| lt | lt | typing.Optional[typing.Any] | None | Exclusive end date. |
| lte | lte | typing.Optional[typing.Any] | None | Inclusive end date. |
| gt | gt | typing.Optional[typing.Any] | None | Exclusive start date. |
| gte | gte | typing.Optional[typing.Any] | None | Inclusive start date. |

```python
class AggregationRange(core.ModelBase):
    """Specifies a date range from an inclusive start date to an exclusive end date."""

    lt: typing.Optional[typing.Any] = None
    """Exclusive end date."""

    lte: typing.Optional[typing.Any] = None
    """Inclusive end date."""

    gt: typing.Optional[typing.Any] = None
    """Exclusive start date."""

    gte: typing.Optional[typing.Any] = None
    """Inclusive start date."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregationRange.md)
