# foundry_sdk.v2.datasets.models.File


File

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| path | path | core_models.FilePath | required; no default | No additional field description in SDK source. |
| transaction_rid | transactionRid | TransactionRid | required; no default | No additional field description in SDK source. |
| size_bytes | sizeBytes | typing.Optional[core.Long] | default None | No additional field description in SDK source. |
| updated_time | updatedTime | FileUpdatedTime | required; no default | No additional field description in SDK source. |

```python
class File(core.ModelBase):
    """File"""

    path: core_models.FilePath
    transaction_rid: TransactionRid = pydantic.Field(alias=str("transactionRid"))  # type: ignore[literal-required]
    size_bytes: typing.Optional[core.Long] = pydantic.Field(alias=str("sizeBytes"), default=None)  # type: ignore[literal-required]
    updated_time: FileUpdatedTime = pydantic.Field(alias=str("updatedTime"))
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../_core/Long.md)
- [foundry_sdk.v2.core.models.FilePath](../../core/models/FilePath.md)
- [foundry_sdk.v2.datasets.models.FileUpdatedTime](FileUpdatedTime.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](TransactionRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](File.md)
