# v1.ontologies.OntologyObject.get


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets a specific object with the given primary key.

## SDK invocation contract

```python
def get(self, ontology_rid: ontologies_models.OntologyRid, object_type: ontologies_models.ObjectTypeApiName, primary_key: ontologies_models.PropertyValueEscapedString, *, properties: typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.OntologyObject: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology_rid | ontologies_models.OntologyRid | required | The unique Resource Identifier (RID) of the Ontology that contains the object. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |
| primary_key | ontologies_models.PropertyValueEscapedString | required | The primary key of the requested object. To look up the expected primary key for your object type, use the `Get object type` endpoint or the **Ontology Manager**. |
| properties | typing.Optional[typing.List[ontologies_models.SelectedPropertyApiName]] | None | The properties of the object type that should be included in the response. Omit this parameter to get all the properties. |
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
'/v1/ontologies/{ontologyRid}/objects/{objectType}/{primaryKey}'
```

**query_params**

```python
{'properties': properties}
```

**path_params**

```python
{'ontologyRid': ontology_rid, 'objectType': object_type, 'primaryKey': primary_key}
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
ontologies_models.OntologyObject
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

Ordinary sync return: `ontologies_models.OntologyObject`. Ordinary async return: `typing.Awaitable[ontologies_models.OntologyObject]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.OntologyObject |
| sync_raw | ApiResponse[ontologies_models.OntologyObject] |
| sync_streaming | StreamingContextManager[ontologies_models.OntologyObject] |
| async_ordinary | typing.Awaitable[ontologies_models.OntologyObject] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.OntologyObject]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.OntologyObject]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.ontologies.models.ObjectRid](../../../../models/v1/ontologies/models/ObjectRid.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeApiName](../../../../models/v1/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.OntologyObject](../../../../models/v1/ontologies/models/OntologyObject.md)
- [foundry_sdk.v1.ontologies.models.OntologyRid](../../../../models/v1/ontologies/models/OntologyRid.md)
- [foundry_sdk.v1.ontologies.models.PropertyApiName](../../../../models/v1/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v1.ontologies.models.PropertyValue](../../../../models/v1/ontologies/models/PropertyValue.md)
- [foundry_sdk.v1.ontologies.models.PropertyValueEscapedString](../../../../models/v1/ontologies/models/PropertyValueEscapedString.md)
- [foundry_sdk.v1.ontologies.models.SelectedPropertyApiName](../../../../models/v1/ontologies/models/SelectedPropertyApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/OntologyObject.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
