# v2.ontologies.Ontology.get_full_metadata


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the full Ontology metadata. This includes the objects, links, actions, queries, and interfaces.
This endpoint is designed to return as much metadata as possible in a single request to support OSDK workflows.
It may omit certain entities rather than fail the request.

## SDK invocation contract

```python
def get_full_metadata(self, ontology: ontologies_models.OntologyIdentifier, *, branch: typing.Optional[core_models.FoundryBranch]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.OntologyFullMetadata: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to load metadata from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
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
'/v2/ontologies/{ontology}/fullMetadata'
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
{'Accept': 'application/json'}
```

**body**

```python
None
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

[Part 1](get_full_metadata.md) | [Part 2](get_full_metadata-2.md)
