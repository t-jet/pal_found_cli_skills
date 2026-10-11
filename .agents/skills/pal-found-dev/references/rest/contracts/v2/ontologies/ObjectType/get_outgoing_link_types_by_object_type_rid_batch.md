# v2.ontologies.ObjectType.get_outgoing_link_types_by_object_type_rid_batch


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets outgoing link types for a batch of object types, identified by their RIDs.

For each requested object type, returns the list of outgoing link types visible to the
requesting token. Optionally, results can be filtered to only include specific link type RIDs.

Object types that don't exist or that the requesting token lacks permissions for are
silently omitted from the response.

The maximum batch size for this endpoint is 100.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.Ontology.ObjectType.get_outgoing_link_types_by_object_type_rid_batch`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_outgoing_link_types_by_object_type_rid_batch(self, ontology: ontologies_models.OntologyIdentifier, *, filter_link_type_rids: typing.List[ontologies_models.LinkTypeRid], requests: typing_extensions.Annotated[typing.List[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement], annotated_types.Len(min_length=1, max_length=100)], branch: typing.Optional[core_models.FoundryBranch]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| filter_link_type_rids | typing.List[ontologies_models.LinkTypeRid] | required | If provided, only return outgoing link types with RIDs in this list. If omitted, all outgoing link types for each requested object type are returned. |
| requests | typing_extensions.Annotated[typing.List[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement], annotated_types.Len(min_length=1, max_length=100)] | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to load the outgoing link type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
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
'/v2/ontologies/{ontology}/outgoingLinkTypes/getByRidBatch'
```

**query_params**

```python
{'branch': branch, 'preview': preview}
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
ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchRequest(requests=requests, filter_link_type_rids=filter_link_type_rids)
```

**response_type**

```python
ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse
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

Ordinary sync return: `ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse |
| sync_raw | ApiResponse[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.DisplayName](../../../../models/v2/core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.ReleaseStatus](../../../../models/v2/core/models/ReleaseStatus.md)
- [foundry_sdk.v2.ontologies.models.GetOutgoingLinkTypesByObjectTypeRidBatchRequest](../../../../models/v2/ontologies/models/GetOutgoingLinkTypesByObjectTypeRidBatchRequest.md)
- [foundry_sdk.v2.ontologies.models.GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement](../../../../models/v2/ontologies/models/GetOutgoingLinkTypesByObjectTypeRidBatchRequestElement.md)
- [foundry_sdk.v2.ontologies.models.GetOutgoingLinkTypesByObjectTypeRidBatchResponse](../../../../models/v2/ontologies/models/GetOutgoingLinkTypesByObjectTypeRidBatchResponse.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeRid](../../../../models/v2/ontologies/models/LinkTypeRid.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeSideCardinality](../../../../models/v2/ontologies/models/LinkTypeSideCardinality.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeSideV2](../../../../models/v2/ontologies/models/LinkTypeSideV2.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeRid](../../../../models/v2/ontologies/models/ObjectTypeRid.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/ObjectType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_outgoing_link_types_by_object_type_rid_batch.md)
