# foundry_sdk.v2.datasets.models.GetDatasetSchemaResponse


GetDatasetSchemaResponse

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| branch_name | branchName | core_models.BranchName | required; no default | No additional field description in SDK source. |
| end_transaction_rid | endTransactionRid | TransactionRid | required; no default | No additional field description in SDK source. |
| schema_ | schema | core_models.DatasetSchema | required; no default | No additional field description in SDK source. |
| version_id | versionId | core_models.VersionId | required; no default | No additional field description in SDK source. |

```python
class GetDatasetSchemaResponse(core.ModelBase):
    """GetDatasetSchemaResponse"""

    branch_name: core_models.BranchName = pydantic.Field(alias=str("branchName"))  # type: ignore[literal-required]
    end_transaction_rid: TransactionRid = pydantic.Field(alias=str("endTransactionRid"))  # type: ignore[literal-required]
    schema_: core_models.DatasetSchema = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    version_id: core_models.VersionId = pydantic.Field(alias=str("versionId"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetSchema](../../core/models/DatasetSchema.md)
- [foundry_sdk.v2.core.models.VersionId](../../core/models/VersionId.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](TransactionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetDatasetSchemaResponse.md)
