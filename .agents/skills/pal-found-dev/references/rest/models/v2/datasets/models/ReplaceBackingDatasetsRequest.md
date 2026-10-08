# foundry_sdk.v2.datasets.models.ReplaceBackingDatasetsRequest


ReplaceBackingDatasetsRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| branch | branch | typing.Optional[core_models.BranchName] | None | No additional field description in SDK source. |
| backing_datasets | backingDatasets | typing.List[ViewBackingDataset] | required; no default | No additional field description in SDK source. |

```python
class ReplaceBackingDatasetsRequest(core.ModelBase):
    """ReplaceBackingDatasetsRequest"""

    branch: typing.Optional[core_models.BranchName] = None
    backing_datasets: typing.List[ViewBackingDataset] = pydantic.Field(alias=str("backingDatasets"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.datasets.models.ViewBackingDataset](ViewBackingDataset.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceBackingDatasetsRequest.md)
