# foundry_sdk.v2.connectivity.models.SnowflakeVirtualTableConfig


Pointer to the table in Snowflake. Uses the Snowflake table identifier of database, schema and table.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| database | database | str | required; no default | The database name. |
| schema_ | schema | str | required; no default | The schema name. |
| table | table | str | required; no default | The table name. |
| type | type | typing.Literal['snowflake'] | 'snowflake' | No additional field description in SDK source. |

```python
class SnowflakeVirtualTableConfig(core.ModelBase):
    """Pointer to the table in Snowflake. Uses the Snowflake table identifier of database, schema and table."""

    database: str
    """The database name."""

    schema_: str = pydantic.Field(alias=str("schema"))  # type: ignore[literal-required]
    """The schema name."""

    table: str
    """The table name."""

    type: typing.Literal["snowflake"] = "snowflake"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](SnowflakeVirtualTableConfig.md)
