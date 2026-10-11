# v2.aip_agents.AgentVersion.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get version details for an Agent.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.aip_agents.Agent.AgentVersion.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, agent_rid: aip_agents_models.AgentRid, agent_version_string: aip_agents_models.AgentVersionString, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> aip_agents_models.AgentVersion: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| agent_rid | aip_agents_models.AgentRid | required | An RID identifying an Agent created in [AIP Chatbot Studio](../../../../v2/aip_agents/Agent.md). |
| agent_version_string | aip_agents_models.AgentVersionString | required | The semantic version of the Agent, formatted as "majorVersion.minorVersion". |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AgentNotFound | The given Agent could not be found. |
| AgentVersionNotFound | The given AgentVersion could not be found. |
| InvalidAgentVersion | The provided version string is not a valid format for an Agent version. |
| NoPublishedAgentVersion | Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Chatbot Studio to use the latest published version, or specify the version of the Agent to use. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/aipAgents/agents/{agentRid}/agentVersions/{agentVersionString}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'agentRid': agent_rid, 'agentVersionString': agent_version_string}
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
aip_agents_models.AgentVersion
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AgentNotFound': aip_agents_errors.AgentNotFound, 'AgentVersionNotFound': aip_agents_errors.AgentVersionNotFound, 'InvalidAgentVersion': aip_agents_errors.InvalidAgentVersion, 'NoPublishedAgentVersion': aip_agents_errors.NoPublishedAgentVersion}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `aip_agents_models.AgentVersion`. Ordinary async return: `typing.Awaitable[aip_agents_models.AgentVersion]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | aip_agents_models.AgentVersion |
| sync_raw | ApiResponse[aip_agents_models.AgentVersion] |
| sync_streaming | StreamingContextManager[aip_agents_models.AgentVersion] |
| async_ordinary | typing.Awaitable[aip_agents_models.AgentVersion] |
| async_raw | Awaitable[AsyncApiResponse[aip_agents_models.AgentVersion]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[aip_agents_models.AgentVersion]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.aip_agents.errors.AgentNotFound](../../../../models/v2/aip_agents/errors/AgentNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.AgentNotFoundParameters](../../../../models/v2/aip_agents/errors/AgentNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.AgentVersionNotFound](../../../../models/v2/aip_agents/errors/AgentVersionNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.AgentVersionNotFoundParameters](../../../../models/v2/aip_agents/errors/AgentVersionNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.InvalidAgentVersion](../../../../models/v2/aip_agents/errors/InvalidAgentVersion.md)
- [foundry_sdk.v2.aip_agents.errors.InvalidAgentVersionParameters](../../../../models/v2/aip_agents/errors/InvalidAgentVersionParameters.md)
- [foundry_sdk.v2.aip_agents.errors.NoPublishedAgentVersion](../../../../models/v2/aip_agents/errors/NoPublishedAgentVersion.md)
- [foundry_sdk.v2.aip_agents.errors.NoPublishedAgentVersionParameters](../../../../models/v2/aip_agents/errors/NoPublishedAgentVersionParameters.md)
- [foundry_sdk.v2.aip_agents.models.AgentRid](../../../../models/v2/aip_agents/models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersion](../../../../models/v2/aip_agents/models/AgentVersion.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersionDetails](../../../../models/v2/aip_agents/models/AgentVersionDetails.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersionString](../../../../models/v2/aip_agents/models/AgentVersionString.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/aip_agents/AgentVersion.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- An Agent has a RID and published versions. Select an accessible version before opening a conversation session. [Local procedure](../../../../v2/aip_agents/Agent.md).

[Part 1](get.md)
