# v2.aip_agents.Session.streaming_continue


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Continue a conversation session with an Agent, or add the first exchange to a session after creation.
Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
Returns a stream of the Agent response text (formatted using markdown) for clients to consume as the response is generated.
On completion of the streamed response, clients can load the full details of the exchange that was added to the session by reloading the session content.
Streamed exchanges also support cancellation; see `cancel` for details.
Concurrent requests to continue the same session are not supported.
Clients should wait to receive a response, or cancel the in-progress exchange, before sending the next message.

## SDK invocation contract

```python
def streaming_continue(self, agent_rid: aip_agents_models.AgentRid, session_rid: aip_agents_models.SessionRid, *, parameter_inputs: typing.Dict[aip_agents_models.ParameterId, aip_agents_models.ParameterValue], user_input: aip_agents_models.UserTextInput, contexts_override: typing.Optional[typing.List[aip_agents_models.InputContext]]=None, message_id: typing.Optional[aip_agents_models.MessageId]=None, preview: typing.Optional[core_models.PreviewMode]=None, session_trace_id: typing.Optional[aip_agents_models.SessionTraceId]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> bytes: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| agent_rid | aip_agents_models.AgentRid | required | An RID identifying an Agent created in [AIP Chatbot Studio](../../../../v2/aip_agents/Agent.md). |
| session_rid | aip_agents_models.SessionRid | required | The Resource Identifier (RID) of the conversation session. |
| parameter_inputs | typing.Dict[aip_agents_models.ParameterId, aip_agents_models.ParameterValue] | required | Any supplied values for [application variables](../../../../v2/aip_agents/Session.md) to pass to the Agent for the exchange. |
| user_input | aip_agents_models.UserTextInput | required | The user message for the Agent to respond to. |
| contexts_override | typing.Optional[typing.List[aip_agents_models.InputContext]] | None | If set, automatic [context](../../../../v2/aip_agents/Session.md) retrieval is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session. |
| message_id | typing.Optional[aip_agents_models.MessageId] | None | A client-generated Universally Unique Identifier (UUID) to identify the message, which the client can use to cancel the exchange before the streaming response is complete. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| session_trace_id | typing.Optional[aip_agents_models.SessionTraceId] | None | The unique identifier to use for this continue session trace. By generating and passing this ID to the `streamingContinue` endpoint, clients can use this trace ID to separately load details of the trace used to generate a result, while the result is in progress. If omitted, it will be generated automatically. Clients can check the generated ID by inspecting the `sessionTraceId` in the `SessionExchangeResult`, which can be loaded via the `getContent` endpoint. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ActionTypeNotFound | An action tool configured on the Agent references an action type that could not be found. This can surface at runtime if the action type was deleted or is not accessible to the calling token. Verify the action type exists and is accessible, then review the Agent's tools in AIP Chatbot Studio. |
| AgentNotFound | The given Agent could not be found. |
| FunctionLocatorNotFound | The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access. |
| InvalidParameter | The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Chatbot Studio. The Agent version used for the session can be checked through the API with `getSession`. |
| InvalidParameterType | The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Chatbot Studio. The Agent version used for the session can be checked through the API with `getSession`. |
| ObjectTypeIdsNotFound | Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| ObjectTypeRidsNotFound | Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| OntologyEntitiesNotFound | Some ontology types are configured for use by the Agent but could not be found. The types either do not exist or the client token does not have access. Object types and their link types can be checked by listing available object/link types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| SessionNotFound | The given Session could not be found. |
| SessionTraceIdAlreadyExists | The provided trace ID already exists for the session and cannot be reused. |
| StreamingContinueSessionPermissionDenied | Could not streamingContinue the Session. |
| UnsupportedLanguageModelRid | The Agent is configured with a language model that is not supported or could not be resolved. This can surface at runtime if the model was deprecated or is not accessible to the calling token. Update the Agent's language model in AIP Chatbot Studio. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/streamingContinue'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'agentRid': agent_rid, 'sessionRid': session_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/octet-stream'}
```

**body**

```python
aip_agents_models.StreamingContinueSessionRequest(user_input=user_input, parameter_inputs=parameter_inputs, contexts_override=contexts_override, message_id=message_id, session_trace_id=session_trace_id)
```

**response_type**

```python
bytes
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ActionTypeNotFound': aip_agents_errors.ActionTypeNotFound, 'AgentNotFound': aip_agents_errors.AgentNotFound, 'FunctionLocatorNotFound': aip_agents_errors.FunctionLocatorNotFound, 'InvalidParameter': aip_agents_errors.InvalidParameter, 'InvalidParameterType': aip_agents_errors.InvalidParameterType, 'ObjectTypeIdsNotFound': aip_agents_errors.ObjectTypeIdsNotFound, 'ObjectTypeRidsNotFound': aip_agents_errors.ObjectTypeRidsNotFound, 'OntologyEntitiesNotFound': aip_agents_errors.OntologyEntitiesNotFound, 'SessionNotFound': aip_agents_errors.SessionNotFound, 'SessionTraceIdAlreadyExists': aip_agents_errors.SessionTraceIdAlreadyExists, 'StreamingContinueSessionPermissionDenied': aip_agents_errors.StreamingContinueSessionPermissionDenied, 'UnsupportedLanguageModelRid': aip_agents_errors.UnsupportedLanguageModelRid}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `bytes`. Ordinary async return: `typing.Awaitable[bytes]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | bytes |
| sync_raw | ApiResponse[bytes] |
| sync_streaming | StreamingContextManager[bytes] |
| async_ordinary | typing.Awaitable[bytes] |
| async_raw | Awaitable[AsyncApiResponse[bytes]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[bytes]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

[Part 1](streaming_continue.md) | [Part 2](streaming_continue-2.md)
