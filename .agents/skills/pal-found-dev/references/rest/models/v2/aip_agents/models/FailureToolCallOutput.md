# foundry_sdk.v2.aip_agents.models.FailureToolCallOutput


The failed output of a tool call.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| correction_message | correctionMessage | str | required; no default | The correction message returned by the tool if the tool call was not successful.<br>    This is a message that the tool returned to the Agent, which may be used to correct the<br>    Agent's input to the tool. |
| type | type | typing.Literal['failure'] | 'failure' | No additional field description in SDK source. |

```python
class FailureToolCallOutput(core.ModelBase):
    """The failed output of a tool call."""

    correction_message: str = pydantic.Field(alias=str("correctionMessage"))  # type: ignore[literal-required]
    """
    The correction message returned by the tool if the tool call was not successful.
    This is a message that the tool returned to the Agent, which may be used to correct the
    Agent's input to the tool.
    """

    type: typing.Literal["failure"] = "failure"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](FailureToolCallOutput.md)
