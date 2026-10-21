# foundry_sdk.v2.connectivity.models.FilesCountLimitFilter


Only retain `filesCount` number of files in each transaction.
The choice of files to retain is made without any guarantee of order.
This option can increase the reliability of incremental syncs.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| files_count | filesCount | int | required; no default | The number of files to import in the transaction. The value specified must be positive. |
| type | type | typing.Literal['filesCountLimitFilter'] | 'filesCountLimitFilter' | No additional field description in SDK source. |

```python
class FilesCountLimitFilter(core.ModelBase):
    """
    Only retain `filesCount` number of files in each transaction.
    The choice of files to retain is made without any guarantee of order.
    This option can increase the reliability of incremental syncs.
    """

    files_count: int = pydantic.Field(alias=str("filesCount"))  # type: ignore[literal-required]
    """The number of files to import in the transaction. The value specified must be positive."""

    type: typing.Literal["filesCountLimitFilter"] = "filesCountLimitFilter"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FilesCountLimitFilter.md)
