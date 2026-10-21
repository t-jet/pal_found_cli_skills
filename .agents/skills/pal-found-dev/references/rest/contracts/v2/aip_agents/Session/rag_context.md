# v2.aip_agents.Session.rag_context


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Retrieve relevant [context](../../../../v2/aip_agents/Session.md) for a user message from the data sources configured for the session.
This allows clients to pre-retrieve context for a user message before sending it to the Agent with the `contextsOverride` option when continuing a session, to allow any pre-processing of the context before sending it to the Agent.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.aip_agents.Agent.Session.rag_context`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def rag_context(self, agent_rid: aip_agents_models.AgentRid, session_rid: aip_agents_models.SessionRid, *, parameter_inputs: typing.Dict[aip_agents_models.ParameterId, aip_agents_models.ParameterValue], user_input: aip_agents_models.UserTextInput, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> aip_agents_models.AgentSessionRagContextResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| agent_rid | aip_agents_models.AgentRid | required | An RID identifying an Agent created in [AIP Chatbot Studio](../../../../v2/aip_agents/Agent.md). |
| session_rid | aip_agents_models.SessionRid | required | The Resource Identifier (RID) of the conversation session. |
| parameter_inputs | typing.Dict[aip_agents_models.ParameterId, aip_agents_models.ParameterValue] | required | Any values for [application variables](../../../../v2/aip_agents/Session.md) to use for the context retrieval. |
| user_input | aip_agents_models.UserTextInput | required | The user message to retrieve relevant context for from the configured Agent data sources. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AgentNotFound | The given Agent could not be found. |
| FunctionLocatorNotFound | The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access. |
| GetRagContextForSessionPermissionDenied | Could not ragContext the Session. |
| ObjectTypeIdsNotFound | Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| ObjectTypeRidsNotFound | Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| OntologyEntitiesNotFound | Some ontology types are configured for use by the Agent but could not be found. The types either do not exist or the client token does not have access. Object types and their link types can be checked by listing available object/link types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| SessionNotFound | The given Session could not be found. |

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/ragContext'
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
aip_agents_models.GetRagContextForSessionRequest(user_input=user_input, parameter_inputs=parameter_inputs)
```

**response_type**

```python
aip_agents_models.AgentSessionRagContextResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AgentNotFound': aip_agents_errors.AgentNotFound, 'FunctionLocatorNotFound': aip_agents_errors.FunctionLocatorNotFound, 'GetRagContextForSessionPermissionDenied': aip_agents_errors.GetRagContextForSessionPermissionDenied, 'ObjectTypeIdsNotFound': aip_agents_errors.ObjectTypeIdsNotFound, 'ObjectTypeRidsNotFound': aip_agents_errors.ObjectTypeRidsNotFound, 'OntologyEntitiesNotFound': aip_agents_errors.OntologyEntitiesNotFound, 'SessionNotFound': aip_agents_errors.SessionNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `aip_agents_models.AgentSessionRagContextResponse`. Ordinary async return: `typing.Awaitable[aip_agents_models.AgentSessionRagContextResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | aip_agents_models.AgentSessionRagContextResponse |
| sync_raw | ApiResponse[aip_agents_models.AgentSessionRagContextResponse] |
| sync_streaming | StreamingContextManager[aip_agents_models.AgentSessionRagContextResponse] |
| async_ordinary | typing.Awaitable[aip_agents_models.AgentSessionRagContextResponse] |
| async_raw | Awaitable[AsyncApiResponse[aip_agents_models.AgentSessionRagContextResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[aip_agents_models.AgentSessionRagContextResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

[Part 1](rag_context.md) | [Part 2](rag_context-2.md)
