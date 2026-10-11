# foundry_sdk.v2.language_models.models.AnthropicEffort


`effort` controls the response token effort for supported Claude models beginning with Opus 4.5. Use one literal below only when the selected model accepts it. `HIGH` has the same behavior as omitting the parameter according to the frozen SDK.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
AnthropicEffort: typing_extensions.TypeAlias = typing.Literal["LOW", "MEDIUM", "HIGH", "MAX"]
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](AnthropicEffort.md)
