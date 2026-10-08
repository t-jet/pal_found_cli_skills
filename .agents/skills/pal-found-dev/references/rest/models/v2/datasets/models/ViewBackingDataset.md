# foundry_sdk.v2.datasets.models.ViewBackingDataset


One of the Datasets backing a View.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| branch | branch | typing.Optional[core_models.BranchName] | None | The branch of the backing dataset. If not specified, defaults to the branch of the View. |
| dataset_rid | datasetRid | core_models.DatasetRid | required; no default | No additional field description in SDK source. |
| stop_propagating_marking_ids | stopPropagatingMarkingIds | typing.List[core_models.MarkingId] | required; no default | Markings listed here will not be inherited from this backing dataset. The caller must have the DECLASSIFY <br>    permission on each marking listed here. If multiple backing datasets have the same marking applied,<br>    the marking must be listed for each backing dataset or it will still be inherited. |

```python
class ViewBackingDataset(core.ModelBase):
    """One of the Datasets backing a View."""

    branch: typing.Optional[core_models.BranchName] = None
    """The branch of the backing dataset. If not specified, defaults to the branch of the View."""

    dataset_rid: core_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    stop_propagating_marking_ids: typing.List[core_models.MarkingId] = pydantic.Field(alias=str("stopPropagatingMarkingIds"))  # type: ignore[literal-required]
    """
    Markings listed here will not be inherited from this backing dataset. The caller must have the DECLASSIFY 
    permission on each marking listed here. If multiple backing datasets have the same marking applied,
    the marking must be listed for each backing dataset or it will still be inherited.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.MarkingId](../../core/models/MarkingId.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ViewBackingDataset.md)
