# v2.aip_agents.Content.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the conversation content for a session between the calling user and an Agent.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.aip_agents.Agent.Session.Content.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, agent_rid: aip_agents_models.AgentRid, session_rid: aip_agents_models.SessionRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> aip_agents_models.Content: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| agent_rid | aip_agents_models.AgentRid | required | An RID identifying an Agent created in [AIP Chatbot Studio](../../../../v2/aip_agents/Agent.md). |
| session_rid | aip_agents_models.SessionRid | required | The Resource Identifier (RID) of the conversation session. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AgentNotFound | The given Agent could not be found. |
| ContentNotFound | The given Content could not be found. |
| SessionNotFound | The given Session could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/content'
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
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
aip_agents_models.Content
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AgentNotFound': aip_agents_errors.AgentNotFound, 'ContentNotFound': aip_agents_errors.ContentNotFound, 'SessionNotFound': aip_agents_errors.SessionNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `aip_agents_models.Content`. Ordinary async return: `typing.Awaitable[aip_agents_models.Content]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | aip_agents_models.Content |
| sync_raw | ApiResponse[aip_agents_models.Content] |
| sync_streaming | StreamingContextManager[aip_agents_models.Content] |
| async_ordinary | typing.Awaitable[aip_agents_models.Content] |
| async_raw | Awaitable[AsyncApiResponse[aip_agents_models.Content]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[aip_agents_models.Content]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.aip_agents.errors.AgentNotFound](../../../../models/v2/aip_agents/errors/AgentNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.AgentNotFoundParameters](../../../../models/v2/aip_agents/errors/AgentNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.ContentNotFound](../../../../models/v2/aip_agents/errors/ContentNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.ContentNotFoundParameters](../../../../models/v2/aip_agents/errors/ContentNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.SessionNotFound](../../../../models/v2/aip_agents/errors/SessionNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.SessionNotFoundParameters](../../../../models/v2/aip_agents/errors/SessionNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.models.AgentMarkdownResponse](../../../../models/v2/aip_agents/models/AgentMarkdownResponse.md)
- [foundry_sdk.v2.aip_agents.models.AgentRid](../../../../models/v2/aip_agents/models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.Content](../../../../models/v2/aip_agents/models/Content.md)
- [foundry_sdk.v2.aip_agents.models.FunctionRetrievedContext](../../../../models/v2/aip_agents/models/FunctionRetrievedContext.md)
- [foundry_sdk.v2.aip_agents.models.ObjectContext](../../../../models/v2/aip_agents/models/ObjectContext.md)
- [foundry_sdk.v2.aip_agents.models.ObjectSetParameterValueUpdate](../../../../models/v2/aip_agents/models/ObjectSetParameterValueUpdate.md)
- [foundry_sdk.v2.aip_agents.models.ParameterId](../../../../models/v2/aip_agents/models/ParameterId.md)
- [foundry_sdk.v2.aip_agents.models.ParameterValueUpdate](../../../../models/v2/aip_agents/models/ParameterValueUpdate.md)
- [foundry_sdk.v2.aip_agents.models.SessionExchange](../../../../models/v2/aip_agents/models/SessionExchange.md)
- [foundry_sdk.v2.aip_agents.models.SessionExchangeContexts](../../../../models/v2/aip_agents/models/SessionExchangeContexts.md)
- [foundry_sdk.v2.aip_agents.models.SessionExchangeResult](../../../../models/v2/aip_agents/models/SessionExchangeResult.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../../../../models/v2/aip_agents/models/SessionRid.md)
- [foundry_sdk.v2.aip_agents.models.SessionTraceId](../../../../models/v2/aip_agents/models/SessionTraceId.md)
- [foundry_sdk.v2.aip_agents.models.StringParameterValue](../../../../models/v2/aip_agents/models/StringParameterValue.md)
- [foundry_sdk.v2.aip_agents.models.UserTextInput](../../../../models/v2/aip_agents/models/UserTextInput.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.functions.models.FunctionRid](../../../../models/v2/functions/models/FunctionRid.md)
- [foundry_sdk.v2.functions.models.FunctionVersion](../../../../models/v2/functions/models/FunctionVersion.md)
- [foundry_sdk.v2.ontologies.models.ObjectRid](../../../../models/v2/ontologies/models/ObjectRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetRid](../../../../models/v2/ontologies/models/ObjectSetRid.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeRid](../../../../models/v2/ontologies/models/PropertyTypeRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/aip_agents/Content.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- An Agent has a RID and published versions. Select an accessible version before opening a conversation session. [Local procedure](../../../../v2/aip_agents/Agent.md).

[Part 1](get.md)
