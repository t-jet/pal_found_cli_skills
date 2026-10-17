# foundry_sdk.v2.connectivity.models.CreateConnectionRequestDatabricksConnectionConfiguration


CreateConnectionRequestDatabricksConnectionConfiguration

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| host_name | hostName | str | required; no default | The hostname of the Databricks workspace. |
| http_path | httpPath | str | required; no default | The Databricks compute resource’s HTTP Path value. |
| jdbc_properties | jdbcProperties | JdbcProperties | required; no default | No additional field description in SDK source. |
| authentication | authentication | CreateConnectionRequestDatabricksAuthenticationMode | required; no default | The method of authentication to use. |
| type | type | typing.Literal['databricks'] | 'databricks' | No additional field description in SDK source. |

```python
class CreateConnectionRequestDatabricksConnectionConfiguration(core.ModelBase):
    """CreateConnectionRequestDatabricksConnectionConfiguration"""

    host_name: str = pydantic.Field(alias=str("hostName"))  # type: ignore[literal-required]
    """The hostname of the Databricks workspace."""

    http_path: str = pydantic.Field(alias=str("httpPath"))  # type: ignore[literal-required]
    """The Databricks compute resource’s HTTP Path value."""

    jdbc_properties: JdbcProperties = pydantic.Field(alias=str("jdbcProperties"))  # type: ignore[literal-required]
    authentication: CreateConnectionRequestDatabricksAuthenticationMode
    """The method of authentication to use."""

    type: typing.Literal["databricks"] = "databricks"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestDatabricksAuthenticationMode](CreateConnectionRequestDatabricksAuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.JdbcProperties](JdbcProperties.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateConnectionRequestDatabricksConnectionConfiguration.md)
