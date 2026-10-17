# foundry_sdk.v2.media_sets.models.BatchTransactionsTransactionPolicy


All writes must be part of a transaction. Transactions are branch-scoped and created by calling
create transaction. Writes are not visible until commit transaction is called.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| type | type | typing.Literal['batchTransactions'] | 'batchTransactions' | No additional field description in SDK source. |

```python
class BatchTransactionsTransactionPolicy(core.ModelBase):
    """
    All writes must be part of a transaction. Transactions are branch-scoped and created by calling
    create transaction. Writes are not visible until commit transaction is called.
    """

    type: typing.Literal["batchTransactions"] = "batchTransactions"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](BatchTransactionsTransactionPolicy.md)
