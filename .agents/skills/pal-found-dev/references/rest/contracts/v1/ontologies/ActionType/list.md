# v1.ontologies.ActionType.list


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists the action types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

## Public Python client route

With a configured `foundry_sdk.v1.FoundryClient` named `client`, call `client.ontologies.Ontology.ActionType.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, ontology_rid: ontologies_models.OntologyRid, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[ontologies_models.ActionType]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology_rid | ontologies_models.OntologyRid | required | The unique Resource Identifier (RID) of the Ontology that contains the action types. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. |
| page_size | typing.Optional[core_models.PageSize] | None | The desired size of the page to be returned. Defaults to 500. See [page sizes](../../../../client-behavior.md) for details. |
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
'/v1/ontologies/{ontologyRid}/actionTypes'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token}
```

**path_params**

```python
{'ontologyRid': ontology_rid}
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
ontologies_models.ListActionTypesResponse
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

Ordinary sync return: `core.ResourceIterator[ontologies_models.ActionType]`. Ordinary async return: `core.AsyncResourceIterator[ontologies_models.ActionType]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[ontologies_models.ActionType] |
| sync_raw | ApiResponse[ontologies_models.ListActionTypesResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ListActionTypesResponse] |
| async_ordinary | core.AsyncResourceIterator[ontologies_models.ActionType] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListActionTypesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListActionTypesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.models.AnyType](../../../../models/v1/core/models/AnyType.md)
- [foundry_sdk.v1.core.models.BinaryType](../../../../models/v1/core/models/BinaryType.md)
- [foundry_sdk.v1.core.models.BooleanType](../../../../models/v1/core/models/BooleanType.md)
- [foundry_sdk.v1.core.models.ByteType](../../../../models/v1/core/models/ByteType.md)
- [foundry_sdk.v1.core.models.CipherTextType](../../../../models/v1/core/models/CipherTextType.md)
- [foundry_sdk.v1.core.models.DateType](../../../../models/v1/core/models/DateType.md)
- [foundry_sdk.v1.core.models.DecimalType](../../../../models/v1/core/models/DecimalType.md)
- [foundry_sdk.v1.core.models.DisplayName](../../../../models/v1/core/models/DisplayName.md)
- [foundry_sdk.v1.core.models.DoubleType](../../../../models/v1/core/models/DoubleType.md)
- [foundry_sdk.v1.core.models.FloatType](../../../../models/v1/core/models/FloatType.md)
- [foundry_sdk.v1.core.models.IntegerType](../../../../models/v1/core/models/IntegerType.md)
- [foundry_sdk.v1.core.models.LongType](../../../../models/v1/core/models/LongType.md)
- [foundry_sdk.v1.core.models.MarkingType](../../../../models/v1/core/models/MarkingType.md)
- [foundry_sdk.v1.core.models.MarkingTypeValue](../../../../models/v1/core/models/MarkingTypeValue.md)
- [foundry_sdk.v1.core.models.MediaReferenceType](../../../../models/v1/core/models/MediaReferenceType.md)
- [foundry_sdk.v1.core.models.PageSize](../../../../models/v1/core/models/PageSize.md)
- [foundry_sdk.v1.core.models.PageToken](../../../../models/v1/core/models/PageToken.md)
- [foundry_sdk.v1.core.models.ReleaseStatus](../../../../models/v1/core/models/ReleaseStatus.md)
- [foundry_sdk.v1.core.models.ShortType](../../../../models/v1/core/models/ShortType.md)
- [foundry_sdk.v1.core.models.StringType](../../../../models/v1/core/models/StringType.md)
- [foundry_sdk.v1.core.models.StructFieldName](../../../../models/v1/core/models/StructFieldName.md)
- [foundry_sdk.v1.core.models.TimestampType](../../../../models/v1/core/models/TimestampType.md)
- [foundry_sdk.v1.core.models.UnsupportedType](../../../../models/v1/core/models/UnsupportedType.md)
- [foundry_sdk.v1.core.models.UnsupportedTypeParamKey](../../../../models/v1/core/models/UnsupportedTypeParamKey.md)
- [foundry_sdk.v1.core.models.UnsupportedTypeParamValue](../../../../models/v1/core/models/UnsupportedTypeParamValue.md)
- [foundry_sdk.v1.ontologies.models.ActionType](../../../../models/v1/ontologies/models/ActionType.md)
- [foundry_sdk.v1.ontologies.models.ActionTypeApiName](../../../../models/v1/ontologies/models/ActionTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.ActionTypeRid](../../../../models/v1/ontologies/models/ActionTypeRid.md)
- [foundry_sdk.v1.ontologies.models.ApplyScenarioRule](../../../../models/v1/ontologies/models/ApplyScenarioRule.md)
- [foundry_sdk.v1.ontologies.models.CreateInterfaceObjectRule](../../../../models/v1/ontologies/models/CreateInterfaceObjectRule.md)
- [foundry_sdk.v1.ontologies.models.CreateLinkRule](../../../../models/v1/ontologies/models/CreateLinkRule.md)
- [foundry_sdk.v1.ontologies.models.CreateObjectRule](../../../../models/v1/ontologies/models/CreateObjectRule.md)
- [foundry_sdk.v1.ontologies.models.DeleteInterfaceObjectRule](../../../../models/v1/ontologies/models/DeleteInterfaceObjectRule.md)
- [foundry_sdk.v1.ontologies.models.DeleteLinkRule](../../../../models/v1/ontologies/models/DeleteLinkRule.md)
- [foundry_sdk.v1.ontologies.models.DeleteObjectRule](../../../../models/v1/ontologies/models/DeleteObjectRule.md)
- [foundry_sdk.v1.ontologies.models.InterfaceTypeApiName](../../../../models/v1/ontologies/models/InterfaceTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.LinkTypeApiName](../../../../models/v1/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.ListActionTypesResponse](../../../../models/v1/ontologies/models/ListActionTypesResponse.md)
- [foundry_sdk.v1.ontologies.models.LogicRule](../../../../models/v1/ontologies/models/LogicRule.md)
- [foundry_sdk.v1.ontologies.models.ModifyInterfaceObjectRule](../../../../models/v1/ontologies/models/ModifyInterfaceObjectRule.md)
- [foundry_sdk.v1.ontologies.models.ModifyObjectRule](../../../../models/v1/ontologies/models/ModifyObjectRule.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeApiName](../../../../models/v1/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.ObjectTypeLinkTypeApiNameMapping](../../../../models/v1/ontologies/models/ObjectTypeLinkTypeApiNameMapping.md)
- [foundry_sdk.v1.ontologies.models.OntologyArrayType](../../../../models/v1/ontologies/models/OntologyArrayType.md)
- [foundry_sdk.v1.ontologies.models.OntologyDataType](../../../../models/v1/ontologies/models/OntologyDataType.md)
- [foundry_sdk.v1.ontologies.models.OntologyMapType](../../../../models/v1/ontologies/models/OntologyMapType.md)
- [foundry_sdk.v1.ontologies.models.OntologyObjectSetType](../../../../models/v1/ontologies/models/OntologyObjectSetType.md)
- [foundry_sdk.v1.ontologies.models.OntologyObjectType](../../../../models/v1/ontologies/models/OntologyObjectType.md)
- [foundry_sdk.v1.ontologies.models.OntologyRid](../../../../models/v1/ontologies/models/OntologyRid.md)
- [foundry_sdk.v1.ontologies.models.OntologySetType](../../../../models/v1/ontologies/models/OntologySetType.md)
- [foundry_sdk.v1.ontologies.models.OntologyStructField](../../../../models/v1/ontologies/models/OntologyStructField.md)
- [foundry_sdk.v1.ontologies.models.OntologyStructType](../../../../models/v1/ontologies/models/OntologyStructType.md)
- [foundry_sdk.v1.ontologies.models.Parameter](../../../../models/v1/ontologies/models/Parameter.md)
- [foundry_sdk.v1.ontologies.models.ParameterId](../../../../models/v1/ontologies/models/ParameterId.md)
- [foundry_sdk.v1.ontologies.models.ValueType](../../../../models/v1/ontologies/models/ValueType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/ActionType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Page size is a request hint. Continue with the returned nextPageToken until absent; bound pages and reject a repeated token. [Local procedure](../../../../client-behavior.md).

[Part 1](list.md)
