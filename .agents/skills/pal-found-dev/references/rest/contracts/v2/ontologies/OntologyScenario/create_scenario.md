# v2.ontologies.OntologyScenario.create_scenario


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates an ontology scenario.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.OntologyScenario.create_scenario`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create_scenario(self, ontology: ontologies_models.OntologyIdentifier, *, base: typing.Optional[ontologies_models.OntologyBase]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.CreateOntologyScenarioResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| base | typing.Optional[ontologies_models.OntologyBase] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/ontologies/{ontology}/scenarios/create'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'ontology': ontology}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.CreateOntologyScenarioRequest(base=base)
```

**response_type**

```python
ontologies_models.CreateOntologyScenarioResponse
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

Ordinary sync return: `ontologies_models.CreateOntologyScenarioResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.CreateOntologyScenarioResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.CreateOntologyScenarioResponse |
| sync_raw | ApiResponse[ontologies_models.CreateOntologyScenarioResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.CreateOntologyScenarioResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.CreateOntologyScenarioResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.CreateOntologyScenarioResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.CreateOntologyScenarioResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.ontologies.models.CreateOntologyScenarioRequest](../../../../models/v2/ontologies/models/CreateOntologyScenarioRequest.md)
- [foundry_sdk.v2.ontologies.models.CreateOntologyScenarioResponse](../../../../models/v2/ontologies/models/CreateOntologyScenarioResponse.md)
- [foundry_sdk.v2.ontologies.models.OntologyBase](../../../../models/v2/ontologies/models/OntologyBase.md)
- [foundry_sdk.v2.ontologies.models.OntologyBaseBranch](../../../../models/v2/ontologies/models/OntologyBaseBranch.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyScenarioRid](../../../../models/v2/ontologies/models/OntologyScenarioRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/OntologyScenario.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create_scenario.md)
