# foundry_sdk.v2.orchestration.models.NewLogicTrigger


Trigger whenever a new JobSpec is put on the dataset and on
that branch.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| branch_name | branchName | core_models.BranchName | required; no default | No additional field description in SDK source. |
| dataset_rid | datasetRid | core_models.DatasetRid | required; no default | No additional field description in SDK source. |
| type | type | typing.Literal['newLogic'] | 'newLogic' | No additional field description in SDK source. |

```python
class NewLogicTrigger(core.ModelBase):
    """
    Trigger whenever a new JobSpec is put on the dataset and on
    that branch.
    """

    branch_name: core_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    dataset_rid: core_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    type: typing.Literal["newLogic"] = "newLogic"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](NewLogicTrigger.md)
