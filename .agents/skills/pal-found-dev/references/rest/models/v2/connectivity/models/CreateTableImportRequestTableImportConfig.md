# foundry_sdk.v2.connectivity.models.CreateTableImportRequestTableImportConfig


The import configuration for a specific [connector type](https://palantir.com/docs/foundry/data-integration/source-type-overview).

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CreateTableImportRequestTableImportConfig: typing_extensions.TypeAlias = (
    typing_extensions.Annotated[
        typing.Union[
            "CreateTableImportRequestDatabricksTableImportConfig",
            "CreateTableImportRequestJdbcTableImportConfig",
            "CreateTableImportRequestMicrosoftSqlServerTableImportConfig",
            "CreateTableImportRequestPostgreSqlTableImportConfig",
            "CreateTableImportRequestMicrosoftAccessTableImportConfig",
            "CreateTableImportRequestSnowflakeTableImportConfig",
            "CreateTableImportRequestOracleTableImportConfig",
        ],
        pydantic.Field(discriminator="type"),
    ]
)
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.CreateTableImportRequestDatabricksTableImportConfig](CreateTableImportRequestDatabricksTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.CreateTableImportRequestJdbcTableImportConfig](CreateTableImportRequestJdbcTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.CreateTableImportRequestMicrosoftAccessTableImportConfig](CreateTableImportRequestMicrosoftAccessTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.CreateTableImportRequestMicrosoftSqlServerTableImportConfig](CreateTableImportRequestMicrosoftSqlServerTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.CreateTableImportRequestOracleTableImportConfig](CreateTableImportRequestOracleTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.CreateTableImportRequestPostgreSqlTableImportConfig](CreateTableImportRequestPostgreSqlTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.CreateTableImportRequestSnowflakeTableImportConfig](CreateTableImportRequestSnowflakeTableImportConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateTableImportRequestTableImportConfig.md)
