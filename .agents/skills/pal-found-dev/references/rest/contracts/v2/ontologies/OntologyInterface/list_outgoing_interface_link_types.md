# v2.ontologies.OntologyInterface.list_outgoing_interface_link_types


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List the outgoing interface link types for an interface type.

## SDK invocation contract

```python
def list_outgoing_interface_link_types(self, ontology: ontologies_models.OntologyIdentifier, interface_type: ontologies_models.InterfaceTypeApiName, *, branch: typing.Optional[core_models.FoundryBranch]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ListOutgoingInterfaceLinkTypesResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| interface_type | ontologies_models.InterfaceTypeApiName | required | The API name of the interface type. To find the API name, use the **List interface types** endpoint or check the **Ontology Manager** application. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to get the outgoing link type from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
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
'/v2/ontologies/{ontology}/interfaceTypes/{interfaceType}/outgoingLinkTypes'
```

**query_params**

```python
{'branch': branch, 'preview': preview}
```

**path_params**

```python
{'ontology': ontology, 'interfaceType': interface_type}
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
ontologies_models.ListOutgoingInterfaceLinkTypesResponse
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

Ordinary sync return: `ontologies_models.ListOutgoingInterfaceLinkTypesResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.ListOutgoingInterfaceLinkTypesResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ListOutgoingInterfaceLinkTypesResponse |
| sync_raw | ApiResponse[ontologies_models.ListOutgoingInterfaceLinkTypesResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ListOutgoingInterfaceLinkTypesResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.ListOutgoingInterfaceLinkTypesResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListOutgoingInterfaceLinkTypesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListOutgoingInterfaceLinkTypesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.DisplayName](../../../../models/v2/core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkType](../../../../models/v2/ontologies/models/InterfaceLinkType.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeApiName](../../../../models/v2/ontologies/models/InterfaceLinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeCardinality](../../../../models/v2/ontologies/models/InterfaceLinkTypeCardinality.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeLinkedEntityApiName](../../../../models/v2/ontologies/models/InterfaceLinkTypeLinkedEntityApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeRid](../../../../models/v2/ontologies/models/InterfaceLinkTypeRid.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](../../../../models/v2/ontologies/models/InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkedInterfaceTypeApiName](../../../../models/v2/ontologies/models/LinkedInterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkedObjectTypeApiName](../../../../models/v2/ontologies/models/LinkedObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ListOutgoingInterfaceLinkTypesResponse](../../../../models/v2/ontologies/models/ListOutgoingInterfaceLinkTypesResponse.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/OntologyInterface.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list_outgoing_interface_link_types.md)
