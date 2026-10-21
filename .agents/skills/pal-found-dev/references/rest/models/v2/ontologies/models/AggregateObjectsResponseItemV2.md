# foundry_sdk.v2.ontologies.models.AggregateObjectsResponseItemV2


AggregateObjectsResponseItemV2

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| group | group | typing.Dict[AggregationGroupKeyV2, typing.Optional[AggregationGroupValueV2]] | required; no default | No additional field description in SDK source. |
| metrics | metrics | typing.List[AggregationMetricResultV2] | required; no default | No additional field description in SDK source. |

```python
class AggregateObjectsResponseItemV2(core.ModelBase):
    """AggregateObjectsResponseItemV2"""

    group: typing.Dict[AggregationGroupKeyV2, typing.Optional[AggregationGroupValueV2]]
    metrics: typing.List[AggregationMetricResultV2]
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.AggregationGroupKeyV2](AggregationGroupKeyV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationGroupValueV2](AggregationGroupValueV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationMetricResultV2](AggregationMetricResultV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregateObjectsResponseItemV2.md)
