# foundry_sdk.v1.datasets.models.CreateBranchRequest


CreateBranchRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| branch_id | branchId | BranchId | required; no default | No additional field description in SDK source. |
| transaction_rid | transactionRid | typing.Optional[TransactionRid] | default None | No additional field description in SDK source. |

```python
class CreateBranchRequest(core.ModelBase):
    """CreateBranchRequest"""

    branch_id: BranchId = pydantic.Field(alias=str("branchId"))  # type: ignore[literal-required]
    transaction_rid: typing.Optional[TransactionRid] = pydantic.Field(alias=str("transactionRid"), default=None)
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v1.datasets.models.BranchId](BranchId.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](TransactionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateBranchRequest.md)
