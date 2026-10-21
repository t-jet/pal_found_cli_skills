# foundry_sdk.v2.datasets.models.GetDatasetJobsRequest


GetDatasetJobsRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| where | where | typing.Optional[GetDatasetJobsQuery] | None | No additional field description in SDK source. |
| order_by | orderBy | typing.List[GetDatasetJobsSort] | required; no default | No additional field description in SDK source. |

```python
class GetDatasetJobsRequest(core.ModelBase):
    """GetDatasetJobsRequest"""

    where: typing.Optional[GetDatasetJobsQuery] = None
    order_by: typing.List[GetDatasetJobsSort] = pydantic.Field(alias=str("orderBy"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsQuery](GetDatasetJobsQuery.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsSort](GetDatasetJobsSort.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetDatasetJobsRequest.md)
