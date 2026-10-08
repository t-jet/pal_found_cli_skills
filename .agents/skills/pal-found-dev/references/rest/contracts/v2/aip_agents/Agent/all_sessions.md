# v2.aip_agents.Agent.all_sessions


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List all conversation sessions between the calling user and all accessible Agents that were created by this client.
Sessions are returned in order of most recently updated first.

## SDK invocation contract

```python
def all_sessions(self, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[aip_agents_models.Session]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| page_size | typing.Optional[core_models.PageSize] | None | The maximum number of sessions to return in a single page. The maximum allowed value is 100. Defaults to 100 if not specified. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetAllSessionsAgentsPermissionDenied | The calling user does not have permission to list all sessions across all Agents. Listing all sessions across all agents requires the `api:aip-agents-write` scope. |
| ListSessionsForAgentsPermissionDenied | Could not allSessions the Agent. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/aipAgents/agents/allSessions'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token, 'preview': preview}
```

**path_params**

```python
{}
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
aip_agents_models.AgentsSessionsPage
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetAllSessionsAgentsPermissionDenied': aip_agents_errors.GetAllSessionsAgentsPermissionDenied, 'ListSessionsForAgentsPermissionDenied': aip_agents_errors.ListSessionsForAgentsPermissionDenied}
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
| sync_raw | ApiResponse[aip_agents_models.AgentsSessionsPage] |
| sync_streaming | StreamingContextManager[aip_agents_models.AgentsSessionsPage] |
| async_ordinary | core.AsyncResourceIterator[aip_agents_models.Session] |
| async_raw | Awaitable[AsyncApiResponse[aip_agents_models.AgentsSessionsPage]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[aip_agents_models.AgentsSessionsPage]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.aip_agents.errors.GetAllSessionsAgentsPermissionDenied](../../../../models/v2/aip_agents/errors/GetAllSessionsAgentsPermissionDenied.md)
- [foundry_sdk.v2.aip_agents.errors.GetAllSessionsAgentsPermissionDeniedParameters](../../../../models/v2/aip_agents/errors/GetAllSessionsAgentsPermissionDeniedParameters.md)
- [foundry_sdk.v2.aip_agents.errors.ListSessionsForAgentsPermissionDenied](../../../../models/v2/aip_agents/errors/ListSessionsForAgentsPermissionDenied.md)
- [foundry_sdk.v2.aip_agents.errors.ListSessionsForAgentsPermissionDeniedParameters](../../../../models/v2/aip_agents/errors/ListSessionsForAgentsPermissionDeniedParameters.md)
- [foundry_sdk.v2.aip_agents.models.AgentRid](../../../../models/v2/aip_agents/models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersionString](../../../../models/v2/aip_agents/models/AgentVersionString.md)
- [foundry_sdk.v2.aip_agents.models.AgentsSessionsPage](../../../../models/v2/aip_agents/models/AgentsSessionsPage.md)
- [foundry_sdk.v2.aip_agents.models.Session](../../../../models/v2/aip_agents/models/Session.md)
- [foundry_sdk.v2.aip_agents.models.SessionMetadata](../../../../models/v2/aip_agents/models/SessionMetadata.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../../../../models/v2/aip_agents/models/SessionRid.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/aip_agents/Agent.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](all_sessions.md)
