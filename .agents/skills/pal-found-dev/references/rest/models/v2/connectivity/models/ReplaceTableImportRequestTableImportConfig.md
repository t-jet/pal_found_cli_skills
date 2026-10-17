# foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestTableImportConfig


Choose the replacement table import configuration variant that matches the Connection's connector type. Preserve the chosen union discriminator and validate the source query before replacing the import.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ReplaceTableImportRequestTableImportConfig: typing_extensions.TypeAlias = (
    typing_extensions.Annotated[
        typing.Union[
            "ReplaceTableImportRequestDatabricksTableImportConfig",
            "ReplaceTableImportRequestJdbcTableImportConfig",
            "ReplaceTableImportRequestMicrosoftSqlServerTableImportConfig",
            "ReplaceTableImportRequestPostgreSqlTableImportConfig",
            "ReplaceTableImportRequestMicrosoftAccessTableImportConfig",
            "ReplaceTableImportRequestSnowflakeTableImportConfig",
            "ReplaceTableImportRequestOracleTableImportConfig",
        ],
        pydantic.Field(discriminator="type"),
    ]
)
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestDatabricksTableImportConfig](ReplaceTableImportRequestDatabricksTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestJdbcTableImportConfig](ReplaceTableImportRequestJdbcTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestMicrosoftAccessTableImportConfig](ReplaceTableImportRequestMicrosoftAccessTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestMicrosoftSqlServerTableImportConfig](ReplaceTableImportRequestMicrosoftSqlServerTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestOracleTableImportConfig](ReplaceTableImportRequestOracleTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestPostgreSqlTableImportConfig](ReplaceTableImportRequestPostgreSqlTableImportConfig.md)
- [foundry_sdk.v2.connectivity.models.ReplaceTableImportRequestSnowflakeTableImportConfig](ReplaceTableImportRequestSnowflakeTableImportConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ReplaceTableImportRequestTableImportConfig.md)
