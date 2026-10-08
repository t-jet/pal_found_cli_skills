# foundry_sdk.v1.datasets.models.Transaction


An operation that modifies the files within a dataset.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| rid | rid | TransactionRid | required; no default | No additional field description in SDK source. |
| transaction_type | transactionType | TransactionType | required; no default | No additional field description in SDK source. |
| status | status | TransactionStatus | required; no default | No additional field description in SDK source. |
| created_time | createdTime | core.AwareDatetime | required; no default | The timestamp when the transaction was created, in ISO 8601 timestamp format. |
| closed_time | closedTime | typing.Optional[core.AwareDatetime] | default None | The timestamp when the transaction was closed, in ISO 8601 timestamp format. |

```python
class Transaction(core.ModelBase):
    """An operation that modifies the files within a dataset."""

    rid: TransactionRid
    transaction_type: TransactionType = pydantic.Field(alias=str("transactionType"))  # type: ignore[literal-required]
    status: TransactionStatus
    created_time: core.AwareDatetime = pydantic.Field(alias=str("createdTime"))  # type: ignore[literal-required]
    """The timestamp when the transaction was created, in ISO 8601 timestamp format."""

    closed_time: typing.Optional[core.AwareDatetime] = pydantic.Field(alias=str("closedTime"), default=None)  # type: ignore[literal-required]
    """The timestamp when the transaction was closed, in ISO 8601 timestamp format."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../_core/AwareDatetime.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](TransactionRid.md)
- [foundry_sdk.v1.datasets.models.TransactionStatus](TransactionStatus.md)
- [foundry_sdk.v1.datasets.models.TransactionType](TransactionType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Transaction.md)
