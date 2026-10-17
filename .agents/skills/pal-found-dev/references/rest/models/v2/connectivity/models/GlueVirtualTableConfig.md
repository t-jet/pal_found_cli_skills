# foundry_sdk.v2.connectivity.models.GlueVirtualTableConfig


Pointer to the table in AWS Glue.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| database | database | str | required; no default | The database name. |
| table | table | str | required; no default | The table name. |
| type | type | typing.Literal['glue'] | 'glue' | No additional field description in SDK source. |

```python
class GlueVirtualTableConfig(core.ModelBase):
    """Pointer to the table in AWS Glue."""

    database: str
    """The database name."""

    table: str
    """The table name."""

    type: typing.Literal["glue"] = "glue"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GlueVirtualTableConfig.md)
