# v1.ontologies.ObjectType.list_outgoing_link_types


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List the outgoing links for an object type.

## SDK invocation contract

```python
def list_outgoing_link_types(self, ontology_rid: ontologies_models.OntologyRid, object_type: ontologies_models.ObjectTypeApiName, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[ontologies_models.LinkTypeSide]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology_rid | ontologies_models.OntologyRid | required | The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager** application. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application. |
| page_size | typing.Optional[core_models.PageSize] | None | The desired size of the page to be returned. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
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
'/v1/ontologies/{ontologyRid}/objectTypes/{objectType}/outgoingLinkTypes'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token}
```

**path_params**

```python
{'ontologyRid': ontology_rid, 'objectType': object_type}
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
ontologies_models.ListOutgoingLinkTypesResponse
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

Ordinary sync return: `core.ResourceIterator[ontologies_models.LinkTypeSide]`. Ordinary async return: `core.AsyncResourceIterator[ontologies_models.LinkTypeSide]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[ontologies_models.LinkTypeSide] |
| sync_raw | ApiResponse[ontologies_models.ListOutgoingLinkTypesResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ListOutgoingLinkTypesResponse] |
| async_ordinary | core.AsyncResourceIterator[ontologies_models.LinkTypeSide] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListOutgoingLinkTypesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListOutgoingLinkTypesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.models.DisplayName](../../../../models/v1/core/models/DisplayName.md)
- [foundry_sdk.v1.core.models.PageSize](../../../../models/v1/core/models/PageSize.md)
- [foundry_sdk.v1.core.models.PageToken](../../../../models/v1/core/models/PageToken.md)
- [foundry_sdk.v1.core.models.ReleaseStatus](../../../../models/v1/core/models/ReleaseStatus.md)
- [foundry_sdk.v1.ontologies.models.LinkTypeApiName](../../../../models/v1/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.LinkTypeSide](../../../../models/v1/ontologies/models/LinkTypeSide.md)
- [foundry_sdk.v1.ontologies.models.LinkTypeSideCardinality](../../../../models/v1/ontologies/models/LinkTypeSideCardinality.md)
- [foundry_sdk.v1.ontologies.models.ListOutgoingLinkTypesResponse](../../../../models/v1/ontologies/models/ListOutgoingLinkTypesResponse.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeApiName](../../../../models/v1/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.OntologyRid](../../../../models/v1/ontologies/models/OntologyRid.md)
- [foundry_sdk.v1.ontologies.models.PropertyApiName](../../../../models/v1/ontologies/models/PropertyApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/ObjectType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list_outgoing_link_types.md)
