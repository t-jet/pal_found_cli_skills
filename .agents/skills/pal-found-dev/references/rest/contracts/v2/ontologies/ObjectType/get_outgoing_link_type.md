# v2.ontologies.ObjectType.get_outgoing_link_type


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get an outgoing link for an object type.

## SDK invocation contract

```python
def get_outgoing_link_type(self, ontology: ontologies_models.OntologyIdentifier, object_type: ontologies_models.ObjectTypeApiName, link_type: ontologies_models.LinkTypeApiName, *, branch: typing.Optional[core_models.FoundryBranch]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.LinkTypeSideV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager** application. |
| link_type | ontologies_models.LinkTypeApiName | required | The API name of the outgoing link. To find the API name for your link type, check the **Ontology Manager**. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to get the outgoing link types for an object type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
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
'/v2/ontologies/{ontology}/objectTypes/{objectType}/outgoingLinkTypes/{linkType}'
```

**query_params**

```python
{'branch': branch}
```

**path_params**

```python
{'ontology': ontology, 'objectType': object_type, 'linkType': link_type}
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
ontologies_models.LinkTypeSideV2
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

Ordinary sync return: `ontologies_models.LinkTypeSideV2`. Ordinary async return: `typing.Awaitable[ontologies_models.LinkTypeSideV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.LinkTypeSideV2 |
| sync_raw | ApiResponse[ontologies_models.LinkTypeSideV2] |
| sync_streaming | StreamingContextManager[ontologies_models.LinkTypeSideV2] |
| async_ordinary | typing.Awaitable[ontologies_models.LinkTypeSideV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.LinkTypeSideV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.LinkTypeSideV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.DisplayName](../../../../models/v2/core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.ReleaseStatus](../../../../models/v2/core/models/ReleaseStatus.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeRid](../../../../models/v2/ontologies/models/LinkTypeRid.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeSideCardinality](../../../../models/v2/ontologies/models/LinkTypeSideCardinality.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeSideV2](../../../../models/v2/ontologies/models/LinkTypeSideV2.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/ObjectType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_outgoing_link_type.md)
