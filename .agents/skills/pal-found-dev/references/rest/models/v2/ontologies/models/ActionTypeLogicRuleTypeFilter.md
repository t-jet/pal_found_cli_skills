# foundry_sdk.v2.ontologies.models.ActionTypeLogicRuleTypeFilter


Filter action types by the type of logic rule they contain.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ActionTypeLogicRuleTypeFilter: typing_extensions.TypeAlias = typing.Literal[
    "ADD_OBJECT",
    "MODIFY_OBJECT",
    "DELETE_OBJECT",
    "ADD_LINK",
    "DELETE_LINK",
    "FUNCTION",
    "BATCHED_FUNCTION",
    "ADD_OR_MODIFY_OBJECT",
    "ADD_OR_MODIFY_OBJECT_V2",
]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ActionTypeLogicRuleTypeFilter.md)
