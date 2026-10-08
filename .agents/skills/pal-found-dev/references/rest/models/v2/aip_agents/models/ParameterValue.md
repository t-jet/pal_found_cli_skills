# foundry_sdk.v2.aip_agents.models.ParameterValue


The value provided for a variable configured in the [application state](https://palantir.com/docs/foundry/chatbot-studio/application-state/) of an Agent.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
ParameterValue: typing_extensions.TypeAlias = typing_extensions.Annotated[
    typing.Union["StringParameterValue", "ObjectSetParameterValue"],
    pydantic.Field(discriminator="type"),
]
```

## Referenced definitions

- [foundry_sdk.v2.aip_agents.models.ObjectSetParameterValue](ObjectSetParameterValue.md)
- [foundry_sdk.v2.aip_agents.models.StringParameterValue](StringParameterValue.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ParameterValue.md)
