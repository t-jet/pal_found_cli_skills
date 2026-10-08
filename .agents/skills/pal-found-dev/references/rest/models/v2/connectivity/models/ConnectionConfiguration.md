# foundry_sdk.v2.connectivity.models.ConnectionConfiguration


ConnectionConfiguration

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ConnectionConfiguration: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "S3ConnectionConfiguration",
        "RestConnectionConfiguration",
        "SnowflakeConnectionConfiguration",
        "DatabricksConnectionConfiguration",
        "SmbConnectionConfiguration",
        "JdbcConnectionConfiguration",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.DatabricksConnectionConfiguration](DatabricksConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.JdbcConnectionConfiguration](JdbcConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.RestConnectionConfiguration](RestConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.S3ConnectionConfiguration](S3ConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.SmbConnectionConfiguration](SmbConnectionConfiguration.md)
- [foundry_sdk.v2.connectivity.models.SnowflakeConnectionConfiguration](SnowflakeConnectionConfiguration.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ConnectionConfiguration.md)
