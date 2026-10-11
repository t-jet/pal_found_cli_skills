# foundry_sdk.v2.connectivity.models.ConnectionWorker


This read model distinguishes a configured `FoundryWorker` from `UnknownWorker`. A Foundry worker executes source capability compute in Foundry and uses approved network egress policies for direct or agent-proxy reachability. `UnknownWorker` represents a worker configuration this SDK cannot describe; it is not an agent-host configuration to copy into a new Connection.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ConnectionWorker: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["UnknownWorker", "FoundryWorker"], pydantic.Field(discriminator="type")
]
```

## Referenced definitions

- [foundry_sdk.v2.connectivity.models.FoundryWorker](FoundryWorker.md)
- [foundry_sdk.v2.connectivity.models.UnknownWorker](UnknownWorker.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ConnectionWorker.md)
