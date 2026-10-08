# foundry_sdk.v2.datasets.models.PutDatasetSchemaRequest


PutDatasetSchemaRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| branch_name | branchName | typing.Optional[core_models.BranchName] | default None | No additional field description in SDK source. |
| dataframe_reader | dataframeReader | typing.Optional[DataframeReader] | default None | The dataframe reader used for reading the dataset schema. Defaults to PARQUET. |
| end_transaction_rid | endTransactionRid | typing.Optional[TransactionRid] | default None | The Resource Identifier (RID) of the end Transaction. |
| schema_ | schema | core_models.DatasetSchema | required; no default | The schema that will be added. |

```python
class PutDatasetSchemaRequest(core.ModelBase):
    """PutDatasetSchemaRequest"""

    branch_name: typing.Optional[core_models.BranchName] = pydantic.Field(alias=str("branchName"), default=None)  # type: ignore[literal-required]
    dataframe_reader: typing.Optional[DataframeReader] = pydantic.Field(alias=str("dataframeReader"), default=None)  # type: ignore[literal-required]
    """The dataframe reader used for reading the dataset schema. Defaults to PARQUET."""

    end_transaction_rid: typing.Optional[TransactionRid] = pydantic.Field(alias=str("endTransactionRid"), default=None)  # type: ignore[literal-required]
    """The Resource Identifier (RID) of the end Transaction."""

    schema_: core_models.DatasetSchema = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    """The schema that will be added."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetSchema](../../core/models/DatasetSchema.md)
- [foundry_sdk.v2.datasets.models.DataframeReader](DataframeReader.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](TransactionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](PutDatasetSchemaRequest.md)
