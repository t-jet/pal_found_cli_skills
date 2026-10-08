# v2.ontologies.Ontology.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists the Ontologies visible to the current user.

## SDK invocation contract

```python
def list(self, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ListOntologiesV2Response: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
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
'/v2/ontologies'
```

**query_params**

```python
{}
```

**path_params**

```python
{}
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
ontologies_models.ListOntologiesV2Response
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

Ordinary sync return: `ontologies_models.ListOntologiesV2Response`. Ordinary async return: `typing.Awaitable[ontologies_models.ListOntologiesV2Response]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ListOntologiesV2Response |
| sync_raw | ApiResponse[ontologies_models.ListOntologiesV2Response] |
| sync_streaming | StreamingContextManager[ontologies_models.ListOntologiesV2Response] |
| async_ordinary | typing.Awaitable[ontologies_models.ListOntologiesV2Response] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListOntologiesV2Response]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListOntologiesV2Response]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.DisplayName](../../../../models/v2/core/models/DisplayName.md)
- [foundry_sdk.v2.ontologies.models.ListOntologiesV2Response](../../../../models/v2/ontologies/models/ListOntologiesV2Response.md)
- [foundry_sdk.v2.ontologies.models.OntologyApiName](../../../../models/v2/ontologies/models/OntologyApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyRid](../../../../models/v2/ontologies/models/OntologyRid.md)
- [foundry_sdk.v2.ontologies.models.OntologyV2](../../../../models/v2/ontologies/models/OntologyV2.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/Ontology.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
