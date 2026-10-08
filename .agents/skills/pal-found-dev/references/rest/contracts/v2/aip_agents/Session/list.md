# v2.aip_agents.Session.list


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List all conversation sessions between the calling user and an Agent that was created by this client.
This does not list sessions for the user created by other clients.
For example, any sessions created by the user in AIP Chatbot Studio will not be listed here.
Sessions are returned in order of most recently updated first.

## SDK invocation contract

```python
def list(self, agent_rid: aip_agents_models.AgentRid, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[aip_agents_models.Session]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| agent_rid | aip_agents_models.AgentRid | required | An RID identifying an Agent created in [AIP Chatbot Studio](../../../../v2/aip_agents/Agent.md). |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AgentNotFound | The given Agent could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/aipAgents/agents/{agentRid}/sessions'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token, 'preview': preview}
```

**path_params**

```python
{'agentRid': agent_rid}
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
aip_agents_models.ListSessionsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AgentNotFound': aip_agents_errors.AgentNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[aip_agents_models.Session]`. Ordinary async return: `core.AsyncResourceIterator[aip_agents_models.Session]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[aip_agents_models.Session] |
| sync_raw | ApiResponse[aip_agents_models.ListSessionsResponse] |
| sync_streaming | StreamingContextManager[aip_agents_models.ListSessionsResponse] |
| async_ordinary | core.AsyncResourceIterator[aip_agents_models.Session] |
| async_raw | Awaitable[AsyncApiResponse[aip_agents_models.ListSessionsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[aip_agents_models.ListSessionsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.aip_agents.errors.AgentNotFound](../../../../models/v2/aip_agents/errors/AgentNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.AgentNotFoundParameters](../../../../models/v2/aip_agents/errors/AgentNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.models.AgentRid](../../../../models/v2/aip_agents/models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersionString](../../../../models/v2/aip_agents/models/AgentVersionString.md)
- [foundry_sdk.v2.aip_agents.models.ListSessionsResponse](../../../../models/v2/aip_agents/models/ListSessionsResponse.md)
- [foundry_sdk.v2.aip_agents.models.Session](../../../../models/v2/aip_agents/models/Session.md)
- [foundry_sdk.v2.aip_agents.models.SessionMetadata](../../../../models/v2/aip_agents/models/SessionMetadata.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../../../../models/v2/aip_agents/models/SessionRid.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/aip_agents/Session.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- An Agent has a RID and published versions. Select an accessible version before opening a conversation session. [Local procedure](../../../../v2/aip_agents/Agent.md).

[Part 1](list.md)
