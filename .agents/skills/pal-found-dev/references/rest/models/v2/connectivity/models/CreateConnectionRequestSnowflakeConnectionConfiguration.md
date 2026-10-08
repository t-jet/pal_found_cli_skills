# foundry_sdk.v2.connectivity.models.CreateConnectionRequestSnowflakeConnectionConfiguration


CreateConnectionRequestSnowflakeConnectionConfiguration

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| schema_ | schema | typing.Optional[str] | default None | Specifies the default schema to use for the specified database once connected. If unspecified, <br>    defaults to the empty string.<br>    The specified schema should be an existing schema for which the specified default role has privileges.<br><br>    See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#schema |
| database | database | typing.Optional[str] | None | Specifies the default database to use once connected. If unspecified, defaults to the empty string.<br>    The specified database should be an existing database for which the specified default role has privileges.<br><br>    See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#db |
| role | role | typing.Optional[str] | None | Specifies the default access control role to use in the Snowflake session initiated by the driver. <br>    If unspecified, no role will be used when the session is initiated by the driver.<br><br>    The specified role should be an existing role that has already been assigned to the specified user for <br>    the driver. If the specified role has not already been assigned to the user, the role is not used when <br>    the session is initiated by the driver.<br><br>    See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#role |
| account_identifier | accountIdentifier | str | required; no default | An [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier) uniquely <br>    identifies a Snowflake account within your organization, as well as throughout the global network of <br>    Snowflake-supported cloud platforms and cloud regions.<br><br>    The URL for an account uses the following format: <account_identifier>.snowflakecomputing.com.<br>    An example URL is https://acme-test_aws_us_east_2.snowflakecomputing.com. |
| jdbc_properties | jdbcProperties | JdbcProperties | required; no default | No additional field description in SDK source. |
| warehouse | warehouse | typing.Optional[str] | None | Specifies the virtual warehouse to use once connected. If unspecified, defaults to the empty string. <br>    The specified warehouse should be an existing warehouse for which the specified default role has privileges.<br><br>    See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#warehouse |
| authentication_mode | authenticationMode | CreateConnectionRequestSnowflakeAuthenticationMode | required; no default | The authentication mode to use to connect to the Snowflake database. |
| type | type | typing.Literal['snowflake'] | 'snowflake' | No additional field description in SDK source. |

```python
class CreateConnectionRequestSnowflakeConnectionConfiguration(core.ModelBase):
    """CreateConnectionRequestSnowflakeConnectionConfiguration"""

    schema_: typing.Optional[str] = pydantic.Field(alias=str("schema"), default=None)  # type: ignore[literal-required]
    """
    Specifies the default schema to use for the specified database once connected. If unspecified, 
    defaults to the empty string.
    The specified schema should be an existing schema for which the specified default role has privileges.

    See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#schema
    """

    database: typing.Optional[str] = None
    """
    Specifies the default database to use once connected. If unspecified, defaults to the empty string.
    The specified database should be an existing database for which the specified default role has privileges.

    See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#db
    """

    role: typing.Optional[str] = None
    """
    Specifies the default access control role to use in the Snowflake session initiated by the driver. 
    If unspecified, no role will be used when the session is initiated by the driver.

    The specified role should be an existing role that has already been assigned to the specified user for 
    the driver. If the specified role has not already been assigned to the user, the role is not used when 
    the session is initiated by the driver.

    See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#role
    """

    account_identifier: str = pydantic.Field(alias=str("accountIdentifier"))  # type: ignore[literal-required]
    """
    An [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier) uniquely 
    identifies a Snowflake account within your organization, as well as throughout the global network of 
    Snowflake-supported cloud platforms and cloud regions.

    The URL for an account uses the following format: <account_identifier>.snowflakecomputing.com.
    An example URL is https://acme-test_aws_us_east_2.snowflakecomputing.com.
    """

    jdbc_properties: JdbcProperties = pydantic.Field(alias=str("jdbcProperties"))  # type: ignore[literal-required]
    warehouse: typing.Optional[str] = None
    """
    Specifies the virtual warehouse to use once connected. If unspecified, defaults to the empty string. 
    The specified warehouse should be an existing warehouse for which the specified default role has privileges.

    See https://docs.snowflake.com/developer-guide/jdbc/jdbc-parameters#warehouse
    """

    authentication_mode: CreateConnectionRequestSnowflakeAuthenticationMode = pydantic.Field(alias=str("authenticationMode"))  # type: ignore[literal-required]
    """The authentication mode to use to connect to the Snowflake database."""

    type: typing.Literal["snowflake"] = "snowflake"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestSnowflakeAuthenticationMode](CreateConnectionRequestSnowflakeAuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.JdbcProperties](JdbcProperties.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateConnectionRequestSnowflakeConnectionConfiguration.md)
