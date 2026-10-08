# v2.ontologies.OntologyScenario.list_scenario_edited_links


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Returns the list of edited links within a given scenario for a specific object type and link type, grouped
by source object. Only works for many-to-many link types. Only links where the user has permission to view
both objects are returned.

Each page may be smaller than the requested page size.

## SDK invocation contract

```python
def list_scenario_edited_links(self, ontology: ontologies_models.OntologyIdentifier, scenario_rid: ontologies_models.OntologyScenarioRid, object_type: ontologies_models.ObjectTypeApiName, link_type: ontologies_models.LinkTypeApiName, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[ontologies_models.LinksFromObject]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| scenario_rid | ontologies_models.OntologyScenarioRid | required | The unique resource identifier of the scenario. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. |
| link_type | ontologies_models.LinkTypeApiName | required | The API name of the link type. |
| page_size | typing.Optional[core_models.PageSize] | None | The maximum number of links to return per page. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token to use for pagination. |
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
'/v2/ontologies/{ontology}/scenarios/{scenarioRid}/objects/{objectType}/links/{linkType}/edited'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token, 'preview': preview}
```

**path_params**

```python
{'ontology': ontology, 'scenarioRid': scenario_rid, 'objectType': object_type, 'linkType': link_type}
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
ontologies_models.ListScenarioEditedLinksResponse
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
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[ontologies_models.LinksFromObject]`. Ordinary async return: `core.AsyncResourceIterator[ontologies_models.LinksFromObject]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[ontologies_models.LinksFromObject] |
| sync_raw | ApiResponse[ontologies_models.ListScenarioEditedLinksResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ListScenarioEditedLinksResponse] |
| async_ordinary | core.AsyncResourceIterator[ontologies_models.LinksFromObject] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListScenarioEditedLinksResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListScenarioEditedLinksResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkedObjectLocator](../../../../models/v2/ontologies/models/LinkedObjectLocator.md)
- [foundry_sdk.v2.ontologies.models.LinksFromObject](../../../../models/v2/ontologies/models/LinksFromObject.md)
- [foundry_sdk.v2.ontologies.models.ListScenarioEditedLinksResponse](../../../../models/v2/ontologies/models/ListScenarioEditedLinksResponse.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectV2](../../../../models/v2/ontologies/models/OntologyObjectV2.md)
- [foundry_sdk.v2.ontologies.models.OntologyScenarioRid](../../../../models/v2/ontologies/models/OntologyScenarioRid.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](../../../../models/v2/ontologies/models/PropertyValue.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/OntologyScenario.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list_scenario_edited_links.md)
