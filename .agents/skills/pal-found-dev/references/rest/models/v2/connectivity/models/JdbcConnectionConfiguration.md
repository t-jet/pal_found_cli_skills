# foundry_sdk.v2.connectivity.models.JdbcConnectionConfiguration


The configuration needed to connect to an external system using the JDBC protocol.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| url | url | str | required; no default | The URL that the JDBC driver uses to connect to a database. |
| driver_class | driverClass | str | required; no default | The fully-qualified driver class name that is used to connect to the database. |
| uploaded_jdbc_drivers | uploadedJdbcDrivers | typing.List[JdbcDriverArtifactName] | required; no default | The list of uploaded JDBC driver names. <br>    To upload drivers to a JDBC connection, use the uploadCustomJdbcDrivers endpoint |
| jdbc_properties | jdbcProperties | JdbcProperties | required; no default | No additional field description in SDK source. |
| credentials | credentials | typing.Optional[BasicCredentials] | None | No additional field description in SDK source. |
| type | type | typing.Literal['jdbc'] | 'jdbc' | No additional field description in SDK source. |

```python
class JdbcConnectionConfiguration(core.ModelBase):
    """The configuration needed to connect to an external system using the JDBC protocol."""

    url: str
    """The URL that the JDBC driver uses to connect to a database."""

    driver_class: str = pydantic.Field(alias=str("driverClass"))  # type: ignore[literal-required]
    """The fully-qualified driver class name that is used to connect to the database."""

    uploaded_jdbc_drivers: typing.List[JdbcDriverArtifactName] = pydantic.Field(alias=str("uploadedJdbcDrivers"))  # type: ignore[literal-required]
    """
    The list of uploaded JDBC driver names. 
    To upload drivers to a JDBC connection, use the uploadCustomJdbcDrivers endpoint
    """

    jdbc_properties: JdbcProperties = pydantic.Field(alias=str("jdbcProperties"))  # type: ignore[literal-required]
    credentials: typing.Optional[BasicCredentials] = None
    type: typing.Literal["jdbc"] = "jdbc"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.BasicCredentials](BasicCredentials.md)
- [foundry_sdk.v2.connectivity.models.JdbcDriverArtifactName](JdbcDriverArtifactName.md)
- [foundry_sdk.v2.connectivity.models.JdbcProperties](JdbcProperties.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](JdbcConnectionConfiguration.md)
