# foundry_sdk.v2.aip_agents.models.Parameter


An Agent application-state variable with the name and type configured for that Agent. Read the Agent metadata before supplying a value.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| parameter_type | parameterType | ParameterType | required; no default | Details of the types of values accepted and defaults for this variable. |
| access | access | ParameterAccessMode | required; no default | The access mode controls how the Agent is able to interact with the variable. |
| description | description | typing.Optional[str] | None | A description to explain the use of this variable.<br>    This description is injected into the Agent's prompt to provide context for when to use the variable. |

```python
class Parameter(core.ModelBase):
    """A variable configured in the application state of an Agent in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/)."""

    parameter_type: ParameterType = pydantic.Field(alias=str("parameterType"))  # type: ignore[literal-required]
    """Details of the types of values accepted and defaults for this variable."""

    access: ParameterAccessMode
    """The access mode controls how the Agent is able to interact with the variable."""

    description: typing.Optional[str] = None
    """
    A description to explain the use of this variable.
    This description is injected into the Agent's prompt to provide context for when to use the variable.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.ParameterAccessMode](ParameterAccessMode.md)
- [foundry_sdk.v2.aip_agents.models.ParameterType](ParameterType.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](Parameter.md)
