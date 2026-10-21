# foundry_sdk.v2.connectivity.models.CreateConnectionRequestJdbcConnectionConfiguration


CreateConnectionRequestJdbcConnectionConfiguration

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| credentials | credentials | typing.Optional[BasicCredentials] | None | No additional field description in SDK source. |
| driver_class | driverClass | str | required; no default | The fully-qualified driver class name that is used to connect to the database. |
| jdbc_properties | jdbcProperties | JdbcProperties | required; no default | No additional field description in SDK source. |
| url | url | str | required; no default | The URL that the JDBC driver uses to connect to a database. |
| type | type | typing.Literal['jdbc'] | 'jdbc' | No additional field description in SDK source. |

```python
class CreateConnectionRequestJdbcConnectionConfiguration(core.ModelBase):
    """CreateConnectionRequestJdbcConnectionConfiguration"""

    credentials: typing.Optional[BasicCredentials] = None
    driver_class: str = pydantic.Field(alias=str("driverClass"))  # type: ignore[literal-required]
    """The fully-qualified driver class name that is used to connect to the database."""

    jdbc_properties: JdbcProperties = pydantic.Field(alias=str("jdbcProperties"))  # type: ignore[literal-required]
    url: str
    """The URL that the JDBC driver uses to connect to a database."""

    type: typing.Literal["jdbc"] = "jdbc"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.BasicCredentials](BasicCredentials.md)
- [foundry_sdk.v2.connectivity.models.JdbcProperties](JdbcProperties.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateConnectionRequestJdbcConnectionConfiguration.md)
