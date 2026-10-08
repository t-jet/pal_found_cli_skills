# foundry_sdk.v2.datasets.models.Branch


Branch

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| name | name | core_models.BranchName | required; no default | No additional field description in SDK source. |
| transaction_rid | transactionRid | typing.Optional[TransactionRid] | default None | The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction. |

```python
class Branch(core.ModelBase):
    """Branch"""

    name: core_models.BranchName
    transaction_rid: typing.Optional[TransactionRid] = pydantic.Field(alias=str("transactionRid"), default=None)  # type: ignore[literal-required]
    """The most recent OPEN or COMMITTED transaction on the branch. This will never be an ABORTED transaction."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.core.models.BranchName](../../core/models/BranchName.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](TransactionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Branch.md)
