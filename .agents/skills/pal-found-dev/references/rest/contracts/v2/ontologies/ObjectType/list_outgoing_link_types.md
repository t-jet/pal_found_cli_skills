# v2.ontologies.ObjectType.list_outgoing_link_types


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List the outgoing links for an object type.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.Ontology.ObjectType.list_outgoing_link_types`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list_outgoing_link_types(self, ontology: ontologies_models.OntologyIdentifier, object_type: ontologies_models.ObjectTypeApiName, *, branch: typing.Optional[core_models.FoundryBranch]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[ontologies_models.LinkTypeSideV2]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to load the outgoing link types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
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
'/v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes'
```

**query_params**

```python
{'branch': branch, 'pageSize': page_size, 'pageToken': page_token}
```

**path_params**

```python
{'ontology': ontology, 'objectType': object_type}
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
ontologies_models.ListOutgoingLinkTypesResponseV2
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

Ordinary sync return: `core.ResourceIterator[ontologies_models.LinkTypeSideV2]`. Ordinary async return: `core.AsyncResourceIterator[ontologies_models.LinkTypeSideV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[ontologies_models.LinkTypeSideV2] |
| sync_raw | ApiResponse[ontologies_models.ListOutgoingLinkTypesResponseV2] |
| sync_streaming | StreamingContextManager[ontologies_models.ListOutgoingLinkTypesResponseV2] |
| async_ordinary | core.AsyncResourceIterator[ontologies_models.LinkTypeSideV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListOutgoingLinkTypesResponseV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListOutgoingLinkTypesResponseV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.DisplayName](../../../../models/v2/core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.ReleaseStatus](../../../../models/v2/core/models/ReleaseStatus.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeRid](../../../../models/v2/ontologies/models/LinkTypeRid.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeSideCardinality](../../../../models/v2/ontologies/models/LinkTypeSideCardinality.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeSideV2](../../../../models/v2/ontologies/models/LinkTypeSideV2.md)
- [foundry_sdk.v2.ontologies.models.ListOutgoingLinkTypesResponseV2](../../../../models/v2/ontologies/models/ListOutgoingLinkTypesResponseV2.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/ObjectType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list_outgoing_link_types.md)
