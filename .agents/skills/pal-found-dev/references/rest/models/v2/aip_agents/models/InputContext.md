# foundry_sdk.v2.aip_agents.models.InputContext


Custom retrieved context supplied to an Agent when continuing a session. Use the typed fields below and only content the caller is allowed to provide.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
InputContext: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["FunctionRetrievedContext", "ObjectContext"], pydantic.Field(discriminator="type")
]
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.FunctionRetrievedContext](FunctionRetrievedContext.md)
- [foundry_sdk.v2.aip_agents.models.ObjectContext](ObjectContext.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](InputContext.md)
