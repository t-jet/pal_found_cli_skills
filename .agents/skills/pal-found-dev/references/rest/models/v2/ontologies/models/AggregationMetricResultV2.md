# foundry_sdk.v2.ontologies.models.AggregationMetricResultV2


AggregationMetricResultV2

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | str | required; no default | No additional field description in SDK source. |
| value | value | typing.Optional[typing.Any] | None | The value of the metric. This will be a double in the case of<br>    a numeric metric, or a date string in the case of a date metric. |

```python
class AggregationMetricResultV2(core.ModelBase):
    """AggregationMetricResultV2"""

    name: str
    value: typing.Optional[typing.Any] = None
    """
    The value of the metric. This will be a double in the case of
    a numeric metric, or a date string in the case of a date metric.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregationMetricResultV2.md)
