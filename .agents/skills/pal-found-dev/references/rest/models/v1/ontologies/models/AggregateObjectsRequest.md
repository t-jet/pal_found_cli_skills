# foundry_sdk.v1.ontologies.models.AggregateObjectsRequest


AggregateObjectsRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| aggregation | aggregation | typing.List[Aggregation] | required; no default | No additional field description in SDK source. |
| query | query | typing.Optional[SearchJsonQuery] | None | No additional field description in SDK source. |
| group_by | groupBy | typing.List[AggregationGroupBy] | required; no default | No additional field description in SDK source. |

```python
class AggregateObjectsRequest(core.ModelBase):
    """AggregateObjectsRequest"""

    aggregation: typing.List[Aggregation]
    query: typing.Optional[SearchJsonQuery] = None
    group_by: typing.List[AggregationGroupBy] = pydantic.Field(alias=str("groupBy"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.ontologies.models.Aggregation](Aggregation.md)
- [foundry_sdk.v1.ontologies.models.AggregationGroupBy](AggregationGroupBy.md)
- [foundry_sdk.v1.ontologies.models.SearchJsonQuery](SearchJsonQuery.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregateObjectsRequest.md)
