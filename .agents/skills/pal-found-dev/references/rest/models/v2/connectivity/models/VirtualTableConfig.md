# foundry_sdk.v2.connectivity.models.VirtualTableConfig


VirtualTableConfig

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
VirtualTableConfig: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union[
        "SnowflakeVirtualTableConfig",
        "UnityVirtualTableConfig",
        "GlueVirtualTableConfig",
        "DeltaVirtualTableConfig",
        "IcebergVirtualTableConfig",
        "FilesVirtualTableConfig",
        "BigQueryVirtualTableConfig",
    ],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.BigQueryVirtualTableConfig](BigQueryVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.DeltaVirtualTableConfig](DeltaVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.FilesVirtualTableConfig](FilesVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.GlueVirtualTableConfig](GlueVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.IcebergVirtualTableConfig](IcebergVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.SnowflakeVirtualTableConfig](SnowflakeVirtualTableConfig.md)
- [foundry_sdk.v2.connectivity.models.UnityVirtualTableConfig](UnityVirtualTableConfig.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](VirtualTableConfig.md)
