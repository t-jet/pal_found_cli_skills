# foundry_sdk.v2.ontologies.models.ActionTypeStatusFilter


Filter action types by status.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ActionTypeStatusFilter: typing_extensions.TypeAlias = typing.Literal[
    "EXPERIMENTAL", "ACTIVE", "DEPRECATED", "EXAMPLE"
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ActionTypeStatusFilter.md)
