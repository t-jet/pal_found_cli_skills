# v2.aip_agents.Agent.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get details for an Agent.

## SDK invocation contract

```python
def get(self, agent_rid: aip_agents_models.AgentRid, *, preview: typing.Optional[core_models.PreviewMode]=None, version: typing.Optional[aip_agents_models.AgentVersionString]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> aip_agents_models.Agent: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| agent_rid | aip_agents_models.AgentRid | required | An RID identifying an Agent created in [AIP Chatbot Studio](../../../../v2/aip_agents/Agent.md). |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| version | typing.Optional[aip_agents_models.AgentVersionString] | None | The version of the Agent to retrieve. If not specified, the latest published version will be returned. |
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
'/v2/aipAgents/agents/{agentRid}'
```

**query_params**

```python
{'preview': preview, 'version': version}
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
aip_agents_models.Agent
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

Ordinary sync return: `aip_agents_models.Agent`. Ordinary async return: `typing.Awaitable[aip_agents_models.Agent]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | aip_agents_models.Agent |
| sync_raw | ApiResponse[aip_agents_models.Agent] |
| sync_streaming | StreamingContextManager[aip_agents_models.Agent] |
| async_ordinary | typing.Awaitable[aip_agents_models.Agent] |
| async_raw | Awaitable[AsyncApiResponse[aip_agents_models.Agent]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[aip_agents_models.Agent]] |

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
- [foundry_sdk.v2.aip_agents.models.Agent](../../../../models/v2/aip_agents/models/Agent.md)
- [foundry_sdk.v2.aip_agents.models.AgentMetadata](../../../../models/v2/aip_agents/models/AgentMetadata.md)
- [foundry_sdk.v2.aip_agents.models.AgentRid](../../../../models/v2/aip_agents/models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersionString](../../../../models/v2/aip_agents/models/AgentVersionString.md)
- [foundry_sdk.v2.aip_agents.models.ObjectSetParameter](../../../../models/v2/aip_agents/models/ObjectSetParameter.md)
- [foundry_sdk.v2.aip_agents.models.Parameter](../../../../models/v2/aip_agents/models/Parameter.md)
- [foundry_sdk.v2.aip_agents.models.ParameterAccessMode](../../../../models/v2/aip_agents/models/ParameterAccessMode.md)
- [foundry_sdk.v2.aip_agents.models.ParameterId](../../../../models/v2/aip_agents/models/ParameterId.md)
- [foundry_sdk.v2.aip_agents.models.ParameterType](../../../../models/v2/aip_agents/models/ParameterType.md)
- [foundry_sdk.v2.aip_agents.models.StringParameter](../../../../models/v2/aip_agents/models/StringParameter.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeId](../../../../models/v2/ontologies/models/ObjectTypeId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/aip_agents/Agent.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- An Agent has a RID and published versions. Select an accessible version before opening a conversation session. [Local procedure](../../../../v2/aip_agents/Agent.md).

[Part 1](get.md)
