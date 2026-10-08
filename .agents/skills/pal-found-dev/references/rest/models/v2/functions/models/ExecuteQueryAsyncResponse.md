# foundry_sdk.v2.functions.models.ExecuteQueryAsyncResponse


Response from submitting a query for async execution.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ExecuteQueryAsyncResponse: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["ExecutionSubmitted", "ExecutionCompleted"], pydantic.Field(discriminator="type")
]
```

## Referenced definitions

- [foundry_sdk.v2.functions.models.ExecutionCompleted](ExecutionCompleted.md)
- [foundry_sdk.v2.functions.models.ExecutionSubmitted](ExecutionSubmitted.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExecuteQueryAsyncResponse.md)
