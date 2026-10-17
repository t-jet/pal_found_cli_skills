# v2.ontologies.OntologyScenario.list_scenario_edited_entity_types


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Returns the object types and link types that have been modified within a given scenario.

The response contains the list of object type API names that have been modified, and the list of
many-to-many link types that have been modified, grouped by their source object type. One-to-many
link type edits are surfaced as object edits on the object type that owns the foreign key property.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.OntologyScenario.list_scenario_edited_entity_types`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list_scenario_edited_entity_types(self, ontology: ontologies_models.OntologyIdentifier, scenario_rid: ontologies_models.OntologyScenarioRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ListScenarioEditedEntityTypesResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| scenario_rid | ontologies_models.OntologyScenarioRid | required | The unique resource identifier of the scenario. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/ontologies/{ontology}/scenarios/{scenarioRid}/editedEntityTypes'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'ontology': ontology, 'scenarioRid': scenario_rid}
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
ontologies_models.ListScenarioEditedEntityTypesResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `ontologies_models.ListScenarioEditedEntityTypesResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.ListScenarioEditedEntityTypesResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ListScenarioEditedEntityTypesResponse |
| sync_raw | ApiResponse[ontologies_models.ListScenarioEditedEntityTypesResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ListScenarioEditedEntityTypesResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.ListScenarioEditedEntityTypesResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListScenarioEditedEntityTypesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListScenarioEditedEntityTypesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ListScenarioEditedEntityTypesResponse](../../../../models/v2/ontologies/models/ListScenarioEditedEntityTypesResponse.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeLinkTypeApiNameMapping](../../../../models/v2/ontologies/models/ObjectTypeLinkTypeApiNameMapping.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyScenarioRid](../../../../models/v2/ontologies/models/OntologyScenarioRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/OntologyScenario.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list_scenario_edited_entity_types.md)
