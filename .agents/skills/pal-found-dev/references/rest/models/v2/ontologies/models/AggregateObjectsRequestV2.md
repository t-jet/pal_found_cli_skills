# foundry_sdk.v2.ontologies.models.AggregateObjectsRequestV2


AggregateObjectsRequestV2

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| aggregation | aggregation | typing.List[AggregationV2] | required; no default | No additional field description in SDK source. |
| where | where | typing.Optional[SearchJsonQueryV2] | None | No additional field description in SDK source. |
| group_by | groupBy | typing.List[AggregationGroupByV2] | required; no default | No additional field description in SDK source. |
| accuracy | accuracy | typing.Optional[AggregationAccuracyRequest] | None | No additional field description in SDK source. |

```python
class AggregateObjectsRequestV2(core.ModelBase):
    """AggregateObjectsRequestV2"""

    aggregation: typing.List[AggregationV2]
    where: typing.Optional[SearchJsonQueryV2] = None
    group_by: typing.List[AggregationGroupByV2] = pydantic.Field(alias=str("groupBy"))  # type: ignore[literal-required]
    accuracy: typing.Optional[AggregationAccuracyRequest] = None
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.ontologies.models.AggregationAccuracyRequest](AggregationAccuracyRequest.md)
- [foundry_sdk.v2.ontologies.models.AggregationGroupByV2](AggregationGroupByV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationV2](AggregationV2.md)
- [foundry_sdk.v2.ontologies.models.SearchJsonQueryV2](SearchJsonQueryV2.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregateObjectsRequestV2.md)
