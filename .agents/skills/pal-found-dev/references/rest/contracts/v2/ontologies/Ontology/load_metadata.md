# v2.ontologies.Ontology.load_metadata


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Load Ontology metadata for the requested object, link, action, query, and interface types.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.Ontology.load_metadata`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def load_metadata(self, ontology: ontologies_models.OntologyIdentifier, *, action_types: typing.List[ontologies_models.ActionTypeApiName], interface_types: typing.List[ontologies_models.InterfaceTypeApiName], link_types: typing.List[ontologies_models.LinkTypeApiName], object_types: typing.List[ontologies_models.ObjectTypeApiName], query_types: typing.List[ontologies_models.VersionedQueryTypeApiName], branch: typing.Optional[core_models.FoundryBranch]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.OntologyFullMetadata: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| action_types | typing.List[ontologies_models.ActionTypeApiName] | required | Value shape and constraints are in its referenced local type definition. |
| interface_types | typing.List[ontologies_models.InterfaceTypeApiName] | required | Value shape and constraints are in its referenced local type definition. |
| link_types | typing.List[ontologies_models.LinkTypeApiName] | required | Value shape and constraints are in its referenced local type definition. |
| object_types | typing.List[ontologies_models.ObjectTypeApiName] | required | Value shape and constraints are in its referenced local type definition. |
| query_types | typing.List[ontologies_models.VersionedQueryTypeApiName] | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to load metadata from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
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
'/v2/ontologies/{ontology}/metadata'
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
ontologies_models.LoadOntologyMetadataRequest(object_types=object_types, link_types=link_types, action_types=action_types, query_types=query_types, interface_types=interface_types)
```

**response_type**

```python
ontologies_models.OntologyFullMetadata
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

Ordinary sync return: `ontologies_models.OntologyFullMetadata`. Ordinary async return: `typing.Awaitable[ontologies_models.OntologyFullMetadata]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.OntologyFullMetadata |
| sync_raw | ApiResponse[ontologies_models.OntologyFullMetadata] |
| sync_streaming | StreamingContextManager[ontologies_models.OntologyFullMetadata] |
| async_ordinary | typing.Awaitable[ontologies_models.OntologyFullMetadata] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.OntologyFullMetadata]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.OntologyFullMetadata]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

[Part 1](load_metadata.md) | [Part 2](load_metadata-2.md)
