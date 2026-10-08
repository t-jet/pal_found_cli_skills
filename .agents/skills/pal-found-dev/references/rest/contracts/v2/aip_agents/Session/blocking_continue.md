# v2.aip_agents.Session.blocking_continue


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Continue a conversation session with an Agent, or add the first exchange to a session after creation.
Adds a new exchange to the session with the provided inputs, and generates a response from the Agent.
Blocks on returning the result of the added exchange until the response is fully generated.
Streamed responses are also supported; see `streamingContinue` for details.
Concurrent requests to continue the same session are not supported.
Clients should wait to receive a response before sending the next message.

## SDK invocation contract

```python
def blocking_continue(self, agent_rid: aip_agents_models.AgentRid, session_rid: aip_agents_models.SessionRid, *, parameter_inputs: typing.Dict[aip_agents_models.ParameterId, aip_agents_models.ParameterValue], user_input: aip_agents_models.UserTextInput, contexts_override: typing.Optional[typing.List[aip_agents_models.InputContext]]=None, preview: typing.Optional[core_models.PreviewMode]=None, session_trace_id: typing.Optional[aip_agents_models.SessionTraceId]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> aip_agents_models.SessionExchangeResult: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| agent_rid | aip_agents_models.AgentRid | required | An RID identifying an Agent created in [AIP Chatbot Studio](../../../../v2/aip_agents/Agent.md). |
| session_rid | aip_agents_models.SessionRid | required | The Resource Identifier (RID) of the conversation session. |
| parameter_inputs | typing.Dict[aip_agents_models.ParameterId, aip_agents_models.ParameterValue] | required | Any supplied values for [application variables](../../../../v2/aip_agents/Session.md) to pass to the Agent for the exchange. |
| user_input | aip_agents_models.UserTextInput | required | The user message for the Agent to respond to. |
| contexts_override | typing.Optional[typing.List[aip_agents_models.InputContext]] | None | If set, automatic [context retrieval](../../../../v2/aip_agents/Session.md) is skipped and the list of specified context is provided to the Agent instead. If omitted, relevant context for the user message is automatically retrieved and included in the prompt, based on data sources configured on the Agent for the session. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| session_trace_id | typing.Optional[aip_agents_models.SessionTraceId] | None | The unique identifier to use for this continue session trace. By generating and passing this ID to the `blockingContinue` endpoint, clients can use this trace ID to separately load details of the trace used to generate a result, while the result is in progress. If omitted, it will be generated automatically. Clients can check the generated ID by inspecting the `sessionTraceId` in the `SessionExchangeResult`. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ActionTypeNotFound | An action tool configured on the Agent references an action type that could not be found. This can surface at runtime if the action type was deleted or is not accessible to the calling token. Verify the action type exists and is accessible, then review the Agent's tools in AIP Chatbot Studio. |
| AgentIterationsExceededLimit | The Agent was unable to produce an answer in the set number of maximum iterations. This can happen if the Agent gets confused or stuck in a loop, or if the query is too complex. Try a different query or review the Agent configuration in AIP Chatbot Studio. |
| AgentNotFound | The given Agent could not be found. |
| BlockingContinueSessionPermissionDenied | Could not blockingContinue the Session. |
| ContextSizeExceededLimit | Failed to generate a response for a session because the context size of the LLM has been exceeded. Clients should either retry with a shorter message or create a new session and try re-sending the message. |
| FunctionLocatorNotFound | The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access. |
| InvalidParameter | The provided application variable is not valid for the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Chatbot Studio. The Agent version used for the session can be checked through the API with `getSession`. |
| InvalidParameterType | The provided value does not match the expected type for the application variable configured on the Agent for this session. Check the available application variables for the Agent under the `parameters` property, and version through the API with `getAgent`, or in AIP Chatbot Studio. The Agent version used for the session can be checked through the API with `getSession`. |
| ObjectTypeIdsNotFound | Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| ObjectTypeRidsNotFound | Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| OntologyEntitiesNotFound | Some ontology types are configured for use by the Agent but could not be found. The types either do not exist or the client token does not have access. Object types and their link types can be checked by listing available object/link types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| RateLimitExceeded | Failed to generate a response as the model rate limits were exceeded. Clients should wait and retry. |
| RetryAttemptsExceeded | Failed to generate a response after retrying up to the configured number of retry attempts. Clients should wait and retry. |
| RetryDeadlineExceeded | Failed to generate a response after retrying up to the configured retry deadline. Clients should wait and retry. |
| SessionExecutionFailed | Failed to generate a response for a session due to an unexpected error. |
| SessionNotFound | The given Session could not be found. |
| SessionTraceIdAlreadyExists | The provided trace ID already exists for the session and cannot be reused. |
| UnsupportedLanguageModelRid | The Agent is configured with a language model that is not supported or could not be resolved. This can surface at runtime if the model was deprecated or is not accessible to the calling token. Update the Agent's language model in AIP Chatbot Studio. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/blockingContinue'
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
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
aip_agents_models.BlockingContinueSessionRequest(user_input=user_input, parameter_inputs=parameter_inputs, contexts_override=contexts_override, session_trace_id=session_trace_id)
```

**response_type**

```python
aip_agents_models.SessionExchangeResult
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ActionTypeNotFound': aip_agents_errors.ActionTypeNotFound, 'AgentIterationsExceededLimit': aip_agents_errors.AgentIterationsExceededLimit, 'AgentNotFound': aip_agents_errors.AgentNotFound, 'BlockingContinueSessionPermissionDenied': aip_agents_errors.BlockingContinueSessionPermissionDenied, 'ContextSizeExceededLimit': aip_agents_errors.ContextSizeExceededLimit, 'FunctionLocatorNotFound': aip_agents_errors.FunctionLocatorNotFound, 'InvalidParameter': aip_agents_errors.InvalidParameter, 'InvalidParameterType': aip_agents_errors.InvalidParameterType, 'ObjectTypeIdsNotFound': aip_agents_errors.ObjectTypeIdsNotFound, 'ObjectTypeRidsNotFound': aip_agents_errors.ObjectTypeRidsNotFound, 'OntologyEntitiesNotFound': aip_agents_errors.OntologyEntitiesNotFound, 'RateLimitExceeded': aip_agents_errors.RateLimitExceeded, 'RetryAttemptsExceeded': aip_agents_errors.RetryAttemptsExceeded, 'RetryDeadlineExceeded': aip_agents_errors.RetryDeadlineExceeded, 'SessionExecutionFailed': aip_agents_errors.SessionExecutionFailed, 'SessionNotFound': aip_agents_errors.SessionNotFound, 'SessionTraceIdAlreadyExists': aip_agents_errors.SessionTraceIdAlreadyExists, 'UnsupportedLanguageModelRid': aip_agents_errors.UnsupportedLanguageModelRid}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `aip_agents_models.SessionExchangeResult`. Ordinary async return: `typing.Awaitable[aip_agents_models.SessionExchangeResult]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | aip_agents_models.SessionExchangeResult |
| sync_raw | ApiResponse[aip_agents_models.SessionExchangeResult] |
| sync_streaming | StreamingContextManager[aip_agents_models.SessionExchangeResult] |
| async_ordinary | typing.Awaitable[aip_agents_models.SessionExchangeResult] |
| async_raw | Awaitable[AsyncApiResponse[aip_agents_models.SessionExchangeResult]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[aip_agents_models.SessionExchangeResult]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

[Part 1](blocking_continue.md) | [Part 2](blocking_continue-2.md)
