# foundry_sdk.v2.aip_agents.models.StreamingContinueSessionRequest


StreamingContinueSessionRequest

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| user_input | userInput | UserTextInput | required; no default | The user message for the Agent to respond to. |
| parameter_inputs | parameterInputs | typing.Dict[ParameterId, ParameterValue] | required; no default | Any supplied values for [application variables](https://palantir.com/docs/foundry/chatbot-studio/application-state/) to pass to the Agent for the exchange. |
| contexts_override | contextsOverride | typing.Optional[typing.List[InputContext]] | default None | If set, automatic [context](https://palantir.com/docs/foundry/chatbot-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead.<br>    If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session. |
| message_id | messageId | typing.Optional[MessageId] | default None | A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete. |
| session_trace_id | sessionTraceId | typing.Optional[SessionTraceId] | default None | The unique identifier to use for this continue session trace. By generating and passing this ID to the<br>    `streamingContinue` endpoint, clients can use this trace ID to separately load details of the trace used<br>    to generate a result, while the result is in progress. If omitted, it will be generated automatically.<br>    Clients can check the generated ID by inspecting the `sessionTraceId` in the `SessionExchangeResult`,<br>    which can be loaded via the `getContent` endpoint. |

```python
class StreamingContinueSessionRequest(core.ModelBase):
    """StreamingContinueSessionRequest"""

    user_input: UserTextInput = pydantic.Field(alias=str("userInput"))  # type: ignore[literal-required]
    """The user message for the Agent to respond to."""

    parameter_inputs: typing.Dict[ParameterId, ParameterValue] = pydantic.Field(alias=str("parameterInputs"))  # type: ignore[literal-required]
    """Any supplied values for [application variables](https://palantir.com/docs/foundry/chatbot-studio/application-state/) to pass to the Agent for the exchange."""

    contexts_override: typing.Optional[typing.List[InputContext]] = pydantic.Field(alias=str("contextsOverride"), default=None)  # type: ignore[literal-required]
    """
    If set, automatic [context](https://palantir.com/docs/foundry/chatbot-studio/retrieval-context/) retrieval is skipped and the list of specified context is provided to the Agent instead.
    If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session.
    """

    message_id: typing.Optional[MessageId] = pydantic.Field(alias=str("messageId"), default=None)  # type: ignore[literal-required]
    """A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete."""

    session_trace_id: typing.Optional[SessionTraceId] = pydantic.Field(alias=str("sessionTraceId"), default=None)  # type: ignore[literal-required]
    """
    The unique identifier to use for this continue session trace. By generating and passing this ID to the
    `streamingContinue` endpoint, clients can use this trace ID to separately load details of the trace used
    to generate a result, while the result is in progress. If omitted, it will be generated automatically.
    Clients can check the generated ID by inspecting the `sessionTraceId` in the `SessionExchangeResult`,
    which can be loaded via the `getContent` endpoint.
    """
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.aip_agents.models.InputContext](InputContext.md)
- [foundry_sdk.v2.aip_agents.models.MessageId](MessageId.md)
- [foundry_sdk.v2.aip_agents.models.ParameterId](ParameterId.md)
- [foundry_sdk.v2.aip_agents.models.ParameterValue](ParameterValue.md)
- [foundry_sdk.v2.aip_agents.models.SessionTraceId](SessionTraceId.md)
- [foundry_sdk.v2.aip_agents.models.UserTextInput](UserTextInput.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](StreamingContinueSessionRequest.md)
