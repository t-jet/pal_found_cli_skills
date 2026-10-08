# v2.aip_agents.Session.create


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Create a new conversation session between the calling user and an Agent.
Use `blockingContinue` or `streamingContinue` to start adding exchanges to the session.

## SDK invocation contract

```python
def create(self, agent_rid: aip_agents_models.AgentRid, *, agent_version: typing.Optional[aip_agents_models.AgentVersionString]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> aip_agents_models.Session: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| agent_rid | aip_agents_models.AgentRid | required | An RID identifying an Agent created in [AIP Chatbot Studio](../../../../v2/aip_agents/Agent.md). |
| agent_version | typing.Optional[aip_agents_models.AgentVersionString] | None | The version of the Agent associated with the session. This can be set by clients on session creation. If not specified, defaults to use the latest published version of the Agent at session creation time. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ActionTypeNotFound | An action tool configured on the Agent references an action type that could not be found. This can surface at runtime if the action type was deleted or is not accessible to the calling token. Verify the action type exists and is accessible, then review the Agent's tools in AIP Chatbot Studio. |
| AgentNotFound | The given Agent could not be found. |
| AgentVersionNotFound | The given AgentVersion could not be found. |
| CreateSessionPermissionDenied | Could not create the Session. |
| FunctionLocatorNotFound | The specified function locator is configured for use by the Agent but could not be found. The function type or version may not exist or the client token does not have access. |
| InvalidAgentVersion | The provided version string is not a valid format for an Agent version. |
| NoPublishedAgentVersion | Failed to retrieve the latest published version of the Agent because the Agent has no published versions. Try publishing the Agent in AIP Chatbot Studio to use the latest published version, or specify the version of the Agent to use. |
| ObjectTypeIdsNotFound | Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| ObjectTypeRidsNotFound | Some object types are configured for use by the Agent but could not be found. The object types either do not exist or the client token does not have access. Object types can be checked by listing available object types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| OntologyEntitiesNotFound | Some ontology types are configured for use by the Agent but could not be found. The types either do not exist or the client token does not have access. Object types and their link types can be checked by listing available object/link types through the API, or searching in [Ontology Manager](../../../../../ontology/modeling.md). |
| SessionNotFound | The given Session could not be found. |
| UnsupportedLanguageModelRid | The Agent is configured with a language model that is not supported or could not be resolved. This can surface at runtime if the model was deprecated or is not accessible to the calling token. Update the Agent's language model in AIP Chatbot Studio. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/aipAgents/agents/{agentRid}/sessions'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'agentRid': agent_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
aip_agents_models.CreateSessionRequest(agent_version=agent_version)
```

**response_type**

```python
aip_agents_models.Session
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ActionTypeNotFound': aip_agents_errors.ActionTypeNotFound, 'AgentNotFound': aip_agents_errors.AgentNotFound, 'AgentVersionNotFound': aip_agents_errors.AgentVersionNotFound, 'CreateSessionPermissionDenied': aip_agents_errors.CreateSessionPermissionDenied, 'FunctionLocatorNotFound': aip_agents_errors.FunctionLocatorNotFound, 'InvalidAgentVersion': aip_agents_errors.InvalidAgentVersion, 'NoPublishedAgentVersion': aip_agents_errors.NoPublishedAgentVersion, 'ObjectTypeIdsNotFound': aip_agents_errors.ObjectTypeIdsNotFound, 'ObjectTypeRidsNotFound': aip_agents_errors.ObjectTypeRidsNotFound, 'OntologyEntitiesNotFound': aip_agents_errors.OntologyEntitiesNotFound, 'SessionNotFound': aip_agents_errors.SessionNotFound, 'UnsupportedLanguageModelRid': aip_agents_errors.UnsupportedLanguageModelRid}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `aip_agents_models.Session`. Ordinary async return: `typing.Awaitable[aip_agents_models.Session]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | aip_agents_models.Session |
| sync_raw | ApiResponse[aip_agents_models.Session] |
| sync_streaming | StreamingContextManager[aip_agents_models.Session] |
| async_ordinary | typing.Awaitable[aip_agents_models.Session] |
| async_raw | Awaitable[AsyncApiResponse[aip_agents_models.Session]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[aip_agents_models.Session]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.aip_agents.errors.ActionTypeNotFound](../../../../models/v2/aip_agents/errors/ActionTypeNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.ActionTypeNotFoundParameters](../../../../models/v2/aip_agents/errors/ActionTypeNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.AgentNotFound](../../../../models/v2/aip_agents/errors/AgentNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.AgentNotFoundParameters](../../../../models/v2/aip_agents/errors/AgentNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.AgentVersionNotFound](../../../../models/v2/aip_agents/errors/AgentVersionNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.AgentVersionNotFoundParameters](../../../../models/v2/aip_agents/errors/AgentVersionNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.CreateSessionPermissionDenied](../../../../models/v2/aip_agents/errors/CreateSessionPermissionDenied.md)
- [foundry_sdk.v2.aip_agents.errors.CreateSessionPermissionDeniedParameters](../../../../models/v2/aip_agents/errors/CreateSessionPermissionDeniedParameters.md)
- [foundry_sdk.v2.aip_agents.errors.FunctionLocatorNotFound](../../../../models/v2/aip_agents/errors/FunctionLocatorNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.FunctionLocatorNotFoundParameters](../../../../models/v2/aip_agents/errors/FunctionLocatorNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.InvalidAgentVersion](../../../../models/v2/aip_agents/errors/InvalidAgentVersion.md)
- [foundry_sdk.v2.aip_agents.errors.InvalidAgentVersionParameters](../../../../models/v2/aip_agents/errors/InvalidAgentVersionParameters.md)
- [foundry_sdk.v2.aip_agents.errors.NoPublishedAgentVersion](../../../../models/v2/aip_agents/errors/NoPublishedAgentVersion.md)
- [foundry_sdk.v2.aip_agents.errors.NoPublishedAgentVersionParameters](../../../../models/v2/aip_agents/errors/NoPublishedAgentVersionParameters.md)
- [foundry_sdk.v2.aip_agents.errors.ObjectTypeIdsNotFound](../../../../models/v2/aip_agents/errors/ObjectTypeIdsNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.ObjectTypeIdsNotFoundParameters](../../../../models/v2/aip_agents/errors/ObjectTypeIdsNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.ObjectTypeRidsNotFound](../../../../models/v2/aip_agents/errors/ObjectTypeRidsNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.ObjectTypeRidsNotFoundParameters](../../../../models/v2/aip_agents/errors/ObjectTypeRidsNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.OntologyEntitiesNotFound](../../../../models/v2/aip_agents/errors/OntologyEntitiesNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.OntologyEntitiesNotFoundParameters](../../../../models/v2/aip_agents/errors/OntologyEntitiesNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.SessionNotFound](../../../../models/v2/aip_agents/errors/SessionNotFound.md)
- [foundry_sdk.v2.aip_agents.errors.SessionNotFoundParameters](../../../../models/v2/aip_agents/errors/SessionNotFoundParameters.md)
- [foundry_sdk.v2.aip_agents.errors.UnsupportedLanguageModelRid](../../../../models/v2/aip_agents/errors/UnsupportedLanguageModelRid.md)
- [foundry_sdk.v2.aip_agents.errors.UnsupportedLanguageModelRidParameters](../../../../models/v2/aip_agents/errors/UnsupportedLanguageModelRidParameters.md)
- [foundry_sdk.v2.aip_agents.models.AgentRid](../../../../models/v2/aip_agents/models/AgentRid.md)
- [foundry_sdk.v2.aip_agents.models.AgentVersionString](../../../../models/v2/aip_agents/models/AgentVersionString.md)
- [foundry_sdk.v2.aip_agents.models.CreateSessionRequest](../../../../models/v2/aip_agents/models/CreateSessionRequest.md)
- [foundry_sdk.v2.aip_agents.models.ModelPurpose](../../../../models/v2/aip_agents/models/ModelPurpose.md)
- [foundry_sdk.v2.aip_agents.models.Session](../../../../models/v2/aip_agents/models/Session.md)
- [foundry_sdk.v2.aip_agents.models.SessionMetadata](../../../../models/v2/aip_agents/models/SessionMetadata.md)
- [foundry_sdk.v2.aip_agents.models.SessionRid](../../../../models/v2/aip_agents/models/SessionRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.language_models.models.LanguageModelRid](../../../../models/v2/language_models/models/LanguageModelRid.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeRid](../../../../models/v2/ontologies/models/ActionTypeRid.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeRid](../../../../models/v2/ontologies/models/LinkTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeId](../../../../models/v2/ontologies/models/ObjectTypeId.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeRid](../../../../models/v2/ontologies/models/ObjectTypeRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/aip_agents/Session.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- An Agent has a RID and published versions. Select an accessible version before opening a conversation session. [Local procedure](../../../../v2/aip_agents/Agent.md).
- Ontology object types define the records and properties an Agent or application can access; check the caller's visibility. [Local procedure](../../../../../ontology/modeling.md).

[Part 1](create.md)
