# foundry_sdk.v2.connectivity.models.CreateConnectionRequestConnectionWorker



[The worker of a Connection](https://palantir.com/docs/foundry/data-connection/core-concepts/#workers), which defines where
compute for capabilities are run.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
CreateConnectionRequestConnectionWorker: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["CreateConnectionRequestUnknownWorker", "CreateConnectionRequestFoundryWorker"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestFoundryWorker](CreateConnectionRequestFoundryWorker.md)
- [foundry_sdk.v2.connectivity.models.CreateConnectionRequestUnknownWorker](CreateConnectionRequestUnknownWorker.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](CreateConnectionRequestConnectionWorker.md)
