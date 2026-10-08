# foundry_sdk.v2.models.models.SeriesAggregations


Series with precomputed aggregation values.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | SeriesName | required; no default | The series name |
| length | length | typing.Optional[core.Long] | None | Number of values in the series. This field may be absent when series aggregations are derived from summary metrics rather than the full series data. |
| value | value | SeriesAggregationsValue | required; no default | Aggregated values for this series |

```python
class SeriesAggregations(core.ModelBase):
    """Series with precomputed aggregation values."""

    name: SeriesName
    """The series name"""

    length: typing.Optional[core.Long] = None
    """Number of values in the series. This field may be absent when series aggregations are derived from summary metrics rather than the full series data."""

    value: SeriesAggregationsValue
    """Aggregated values for this series"""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../_core/Long.md)
- [foundry_sdk.v2.models.models.SeriesAggregationsValue](SeriesAggregationsValue.md)
- [foundry_sdk.v2.models.models.SeriesName](SeriesName.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SeriesAggregations.md)
