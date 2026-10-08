# v1.ontologies.ObjectType.get


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets a specific object type with the given API name.

## SDK invocation contract

```python
def get(self, ontology_rid: ontologies_models.OntologyRid, object_type: ontologies_models.ObjectTypeApiName, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ObjectType: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology_rid | ontologies_models.OntologyRid | required | The unique Resource Identifier (RID) of the Ontology that contains the object type. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |
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
'/v1/ontologies/{ontologyRid}/objectTypes/{objectType}'
```

**query_params**

```python
{}
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
ontologies_models.ObjectType
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

Ordinary sync return: `ontologies_models.ObjectType`. Ordinary async return: `typing.Awaitable[ontologies_models.ObjectType]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ObjectType |
| sync_raw | ApiResponse[ontologies_models.ObjectType] |
| sync_streaming | StreamingContextManager[ontologies_models.ObjectType] |
| async_ordinary | typing.Awaitable[ontologies_models.ObjectType] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ObjectType]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ObjectType]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.models.DisplayName](../../../../models/v1/core/models/DisplayName.md)
- [foundry_sdk.v1.core.models.ReleaseStatus](../../../../models/v1/core/models/ReleaseStatus.md)
- [foundry_sdk.v1.ontologies.models.LegacyObjectTypeId](../../../../models/v1/ontologies/models/LegacyObjectTypeId.md)
- [foundry_sdk.v1.ontologies.models.LegacyPropertyId](../../../../models/v1/ontologies/models/LegacyPropertyId.md)
- [foundry_sdk.v1.ontologies.models.ObjectType](../../../../models/v1/ontologies/models/ObjectType.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeApiName](../../../../models/v1/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeRid](../../../../models/v1/ontologies/models/ObjectTypeRid.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeVisibility](../../../../models/v1/ontologies/models/ObjectTypeVisibility.md)
- [foundry_sdk.v1.ontologies.models.OntologyRid](../../../../models/v1/ontologies/models/OntologyRid.md)
- [foundry_sdk.v1.ontologies.models.Property](../../../../models/v1/ontologies/models/Property.md)
- [foundry_sdk.v1.ontologies.models.PropertyApiName](../../../../models/v1/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v1.ontologies.models.ValueType](../../../../models/v1/ontologies/models/ValueType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/ObjectType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
