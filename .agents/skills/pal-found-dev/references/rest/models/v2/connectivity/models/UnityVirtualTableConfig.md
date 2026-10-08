# foundry_sdk.v2.connectivity.models.UnityVirtualTableConfig


Pointer to the table in Unity Catalog. Uses the Databricks table identifier of catalog, schema and table.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| catalog | catalog | str | required; no default | The catalog name. |
| schema_ | schema | str | required; no default | The schema name. |
| table | table | str | required; no default | The table name. |
| type | type | typing.Literal['unity'] | 'unity' | No additional field description in SDK source. |

```python
class UnityVirtualTableConfig(core.ModelBase):
    """Pointer to the table in Unity Catalog. Uses the Databricks table identifier of catalog, schema and table."""

    catalog: str
    """The catalog name."""

    schema_: str = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    """The schema name."""

    table: str
    """The table name."""

    type: typing.Literal["unity"] = "unity"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](UnityVirtualTableConfig.md)
