# foundry_sdk.v1.ontologies.models.AggregationDurationGrouping


Divides objects into groups according to an interval. Note that this grouping applies only on date types.
The interval uses the ISO 8601 notation. For example, "PT1H2M34S" represents a duration of 3754 seconds.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| field | field | FieldNameV1 | required; no default | No additional field description in SDK source. |
| duration | duration | Duration | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['duration'] | 'duration' | No additional field description in SDK source. |

```python
class AggregationDurationGrouping(core.ModelBase):
    """
    Divides objects into groups according to an interval. Note that this grouping applies only on date types.
    The interval uses the ISO 8601 notation. For example, "PT1H2M34S" represents a duration of 3754 seconds.
    """

    field: FieldNameV1
    duration: Duration
    type: typing.Literal["duration"] = "duration"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.ontologies.models.Duration](Duration.md)
- [foundry_sdk.v1.ontologies.models.FieldNameV1](FieldNameV1.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregationDurationGrouping.md)
