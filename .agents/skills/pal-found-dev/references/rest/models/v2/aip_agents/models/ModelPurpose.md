# foundry_sdk.v2.aip_agents.models.ModelPurpose


The purpose for which a language model is configured on an Agent.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ModelPurpose: typing_extensions.TypeAlias = typing.Literal["PRIMARY_AGENT", "QUESTION_SUGGESTER"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ModelPurpose.md)
