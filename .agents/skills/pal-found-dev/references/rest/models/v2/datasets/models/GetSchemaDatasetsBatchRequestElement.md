# foundry_sdk.v2.datasets.models.GetSchemaDatasetsBatchRequestElement


GetSchemaDatasetsBatchRequestElement

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| end_transaction_rid | endTransactionRid | typing.Optional[TransactionRid] | default None | The Resource Identifier (RID) of the end Transaction. If a user does not provide a value, the RID of the latest committed transaction will be used. |
| dataset_rid | datasetRid | core_models.DatasetRid | required; no default | No additional field description in SDK source. |
| version_id | versionId | typing.Optional[core_models.VersionId] | default None | The schema version that should be used. If none is provided, the latest version will be used. |
| branch_name | branchName | typing.Optional[core_models.BranchName] | default None | No additional field description in SDK source. |

```python
class GetSchemaDatasetsBatchRequestElement(core.ModelBase):
    """GetSchemaDatasetsBatchRequestElement"""

    end_transaction_rid: typing.Optional[TransactionRid] = pydantic.Field(alias=str("endTransactionRid"), default=None)  # type: ignore[literal-required]
    """The Resource Identifier (RID) of the end Transaction. If a user does not provide a value, the RID of the latest committed transaction will be used."""

    dataset_rid: core_models.DatasetRid = pydantic.Field(alias=str("datasetRid"))  # type: ignore[literal-required]
    version_id: typing.Optional[core_models.VersionId] = pydantic.Field(alias=str("versionId"), default=None)  # type: ignore[literal-required]
    """The schema version that should be used. If none is provided, the latest version will be used."""

    branch_name: typing.Optional[core_models.BranchName] = pydantic.Field(alias=str("branchName"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.VersionId](../../core/models/VersionId.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](TransactionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetSchemaDatasetsBatchRequestElement.md)
