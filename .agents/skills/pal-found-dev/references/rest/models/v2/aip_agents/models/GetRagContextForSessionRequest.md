# foundry_sdk.v2.aip_agents.models.GetRagContextForSessionRequest


GetRagContextForSessionRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| user_input | userInput | UserTextInput | required; no default | The user message to retrieve relevant context for from the configured Agent data sources. |
| parameter_inputs | parameterInputs | typing.Dict[ParameterId, ParameterValue] | required; no default | Any values for application variables to use for the context retrieval. |

```python
class GetRagContextForSessionRequest(core.ModelBase):
    """GetRagContextForSessionRequest"""

    user_input: UserTextInput = pydantic.Field(alias=str("userInput"))  # type: ignore[literal-required]
    """The user message to retrieve relevant context for from the configured Agent data sources."""

    parameter_inputs: typing.Dict[ParameterId, ParameterValue] = pydantic.Field(alias=str("parameterInputs"))  # type: ignore[literal-required]
    """Any values for [application variables](https://palantir.com/docs/foundry/chatbot-studio/application-state/) to use for the context retrieval."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.ParameterId](ParameterId.md)
- [foundry_sdk.v2.aip_agents.models.ParameterValue](ParameterValue.md)
- [foundry_sdk.v2.aip_agents.models.UserTextInput](UserTextInput.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](GetRagContextForSessionRequest.md)
