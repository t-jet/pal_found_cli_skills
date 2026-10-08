# foundry_sdk.v2.ontologies.models.AggregateObjectsResponseV2


AggregateObjectsResponseV2

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| excluded_items | excludedItems | typing.Optional[int] | default None | No additional field description in SDK source. |
| accuracy | accuracy | AggregationAccuracy | required; no default | No additional field description in SDK source. |
| data | data | typing.List[AggregateObjectsResponseItemV2] | required; no default | No additional field description in SDK source. |
| compute_usage | computeUsage | typing.Optional[core_models.ComputeSeconds] | default None | No additional field description in SDK source. |

```python
class AggregateObjectsResponseV2(core.ModelBase):
    """AggregateObjectsResponseV2"""

    excluded_items: typing.Optional[int] = pydantic.Field(alias=str("excludedItems"), default=None)  # type: ignore[literal-required]
    accuracy: AggregationAccuracy
    data: typing.List[AggregateObjectsResponseItemV2]
    compute_usage: typing.Optional[core_models.ComputeSeconds] = pydantic.Field(alias=str("computeUsage"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.ComputeSeconds](../../core/models/ComputeSeconds.md)
- [foundry_sdk.v2.ontologies.models.AggregateObjectsResponseItemV2](AggregateObjectsResponseItemV2.md)
- [foundry_sdk.v2.ontologies.models.AggregationAccuracy](AggregationAccuracy.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AggregateObjectsResponseV2.md)
