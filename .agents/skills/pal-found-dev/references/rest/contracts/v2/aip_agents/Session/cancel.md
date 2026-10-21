# v2.aip_agents.Session.cancel


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Cancel an in-progress streamed exchange with an Agent which was initiated with `streamingContinue`.
Canceling an exchange allows clients to prevent the exchange from being added to the session, or to provide a response to replace the Agent-generated response.
Note that canceling an exchange does not terminate the stream returned by `streamingContinue`; clients should close the stream on triggering the cancellation request to stop reading from the stream.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.aip_agents.Agent.Session.cancel`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def cancel(self, agent_rid: aip_agents_models.AgentRid, session_rid: aip_agents_models.SessionRid, *, message_id: aip_agents_models.MessageId, preview: typing.Optional[core_models.PreviewMode]=None, response: typing.Optional[aip_agents_models.AgentMarkdownResponse]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> aip_agents_models.CancelSessionResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| agent_rid | aip_agents_models.AgentRid | required | An RID identifying an Agent created in [AIP Chatbot Studio](../../../../v2/aip_agents/Agent.md). |
| session_rid | aip_agents_models.SessionRid | required | The Resource Identifier (RID) of the conversation session. |
| message_id | aip_agents_models.MessageId | required | The identifier for the in-progress exchange to cancel. This should match the `messageId` which was provided when initiating the exchange with `streamingContinue`. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| response | typing.Optional[aip_agents_models.AgentMarkdownResponse] | None | When specified, the exchange is added to the session with the client-provided response as the result. When omitted, the exchange is not added to the session. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AgentNotFound | The given Agent could not be found. |
| CancelSessionFailedMessageNotInProgress | Unable to cancel the requested session exchange as no in-progress exchange was found for the provided message identifier. This is expected if no exchange was initiated with the provided message identifier through a `streamingContinue` request, or if the exchange for this identifier has already completed and cannot be canceled, or if the exchange has already been canceled. This error can also occur if the cancellation was requested immediately after requesting the exchange through a `streamingContinue` request, and the exchange has not started yet. Clients should handle these errors gracefully, and can reload the session content to get the latest conversation state. |
| CancelSessionPermissionDenied | Could not cancel the Session. |
| SessionNotFound | The given Session could not be found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/aipAgents/agents/{agentRid}/sessions/{sessionRid}/cancel'
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
aip_agents_models.CancelSessionRequest(message_id=message_id, response=response)
```

**response_type**

```python
aip_agents_models.CancelSessionResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AgentNotFound': aip_agents_errors.AgentNotFound, 'CancelSessionFailedMessageNotInProgress': aip_agents_errors.CancelSessionFailedMessageNotInProgress, 'CancelSessionPermissionDenied': aip_agents_errors.CancelSessionPermissionDenied, 'SessionNotFound': aip_agents_errors.SessionNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `aip_agents_models.CancelSessionResponse`. Ordinary async return: `typing.Awaitable[aip_agents_models.CancelSessionResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | aip_agents_models.CancelSessionResponse |
| sync_raw | ApiResponse[aip_agents_models.CancelSessionResponse] |
| sync_streaming | StreamingContextManager[aip_agents_models.CancelSessionResponse] |
| async_ordinary | typing.Awaitable[aip_agents_models.CancelSessionResponse] |
| async_raw | Awaitable[AsyncApiResponse[aip_agents_models.CancelSessionResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[aip_agents_models.CancelSessionResponse]] |

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
- [foundry_sdk.v2.aip_agents.errors.CancelSessionFailedMessageNotInProgress](../../../../models/v2/aip_agents/errors/CancelSessionFailedMessageNotInProgress.md)
- [foundry_sdk.v2.aip_agents.errors.CancelSessionFailedMessageNotInProgressParameters](../../../../models/v2/aip_agents/errors/CancelSessionFailedMessageNotInProgressParameters.md)
- [foundry_sdk.v2.aip_agents.errors.CancelSessionPermissionDenied](../../../../models/v2/aip_agents/errors/CancelSessionPermissionDenied.md)
- [foundry_sdk.v2.aip_agents.errors.CancelSessionPermissionDeniedParameters](../../../../models/v2/aip_agents/errors/CancelSessionPermissionDeniedParameters.md)
- [foundry_sdk.v2.aip_agents.errors.SessionNotFound](../../../../models/v2/aip_agents/errors/SessionNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.SessionNotFoundParameters](../../../../models/v2/aip_agents/errors/SessionNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.models.AgentMarkdownResponse](../../../../models/v2/aip_agents/models/AgentMarkdownResponse.md)
- [foundry_sdk.v2.aip_agents.models.AgentRid](../../../../models/v2/aip_agents/models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.CancelSessionRequest](../../../../models/v2/aip_agents/models/CancelSessionRequest.md)
- [foundry_sdk.v2.aip_agents.models.CancelSessionResponse](../../../../models/v2/aip_agents/models/CancelSessionResponse.md)
- [foundry_sdk.v2.aip_agents.models.MessageId](../../../../models/v2/aip_agents/models/MessageId.md)
- [foundry_sdk.v2.aip_agents.models.ObjectSetParameterValueUpdate](../../../../models/v2/aip_agents/models/ObjectSetParameterValueUpdate.md)
- [foundry_sdk.v2.aip_agents.models.ParameterId](../../../../models/v2/aip_agents/models/ParameterId.md)
- [foundry_sdk.v2.aip_agents.models.ParameterValueUpdate](../../../../models/v2/aip_agents/models/ParameterValueUpdate.md)
- [foundry_sdk.v2.aip_agents.models.SessionExchangeResult](../../../../models/v2/aip_agents/models/SessionExchangeResult.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../../../../models/v2/aip_agents/models/SessionRid.md)
- [foundry_sdk.v2.aip_agents.models.SessionTraceId](../../../../models/v2/aip_agents/models/SessionTraceId.md)
- [foundry_sdk.v2.aip_agents.models.StringParameterValue](../../../../models/v2/aip_agents/models/StringParameterValue.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.ontologies.models.ObjectSetRid](../../../../models/v2/ontologies/models/ObjectSetRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/aip_agents/Session.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- An Agent has a RID and published versions. Select an accessible version before opening a conversation session. [Local procedure](../../../../v2/aip_agents/Agent.md).

[Part 1](cancel.md)
