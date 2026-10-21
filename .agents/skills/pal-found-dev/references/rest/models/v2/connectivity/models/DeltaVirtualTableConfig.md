# foundry_sdk.v2.connectivity.models.DeltaVirtualTableConfig


Pointer to the Delta table in cloud object storage (e.g., Azure Data Lake Storage, Google Cloud Storage, S3).

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| path | path | str | required; no default | The path of the Delta table in object storage. |
| type | type | typing.Literal['delta'] | 'delta' | No additional field description in SDK source. |

```python
class DeltaVirtualTableConfig(core.ModelBase):
    """Pointer to the Delta table in cloud object storage (e.g., Azure Data Lake Storage, Google Cloud Storage, S3)."""

    path: str
    """The path of the Delta table in object storage."""

    type: typing.Literal["delta"] = "delta"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DeltaVirtualTableConfig.md)
