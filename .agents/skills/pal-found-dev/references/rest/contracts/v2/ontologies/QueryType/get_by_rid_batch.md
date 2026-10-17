# v2.ontologies.QueryType.get_by_rid_batch


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets a list of query types by RID in bulk.

Query types are filtered from the response if they don't exist or the requesting token lacks the required
permissions.

The maximum batch size for this endpoint is 100.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.Ontology.QueryType.get_by_rid_batch`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_by_rid_batch(self, ontology: ontologies_models.OntologyIdentifier, *, requests: typing_extensions.Annotated[typing.List[ontologies_models.GetQueryTypeByRidBatchRequestElement], annotated_types.Len(min_length=1, max_length=100)], branch: typing.Optional[core_models.FoundryBranch]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.GetQueryTypeByRidBatchResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| requests | typing_extensions.Annotated[typing.List[ontologies_models.GetQueryTypeByRidBatchRequestElement], annotated_types.Len(min_length=1, max_length=100)] | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to load the query type definitions from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
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
'/v2/ontologies/{ontology}/queryTypes/getByRidBatch'
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
ontologies_models.GetQueryTypeByRidBatchRequest(requests=requests)
```

**response_type**

```python
ontologies_models.GetQueryTypeByRidBatchResponse
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

Ordinary sync return: `ontologies_models.GetQueryTypeByRidBatchResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.GetQueryTypeByRidBatchResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.GetQueryTypeByRidBatchResponse |
| sync_raw | ApiResponse[ontologies_models.GetQueryTypeByRidBatchResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.GetQueryTypeByRidBatchResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.GetQueryTypeByRidBatchResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.GetQueryTypeByRidBatchResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.GetQueryTypeByRidBatchResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.AttachmentType](../../../../models/v2/core/models/AttachmentType.md)
- [foundry_sdk.v2.core.models.BooleanType](../../../../models/v2/core/models/BooleanType.md)
- [foundry_sdk.v2.core.models.DateType](../../../../models/v2/core/models/DateType.md)
- [foundry_sdk.v2.core.models.DisplayName](../../../../models/v2/core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.DoubleType](../../../../models/v2/core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.FloatType](../../../../models/v2/core/models/FloatType.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.IntegerType](../../../../models/v2/core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../../../models/v2/core/models/LongType.md)
- [foundry_sdk.v2.core.models.MediaReferenceType](../../../../models/v2/core/models/MediaReferenceType.md)
- [foundry_sdk.v2.core.models.NullType](../../../../models/v2/core/models/NullType.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.StringType](../../../../models/v2/core/models/StringType.md)
- [foundry_sdk.v2.core.models.StructFieldName](../../../../models/v2/core/models/StructFieldName.md)
- [foundry_sdk.v2.core.models.TimestampType](../../../../models/v2/core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.UnsupportedType](../../../../models/v2/core/models/UnsupportedType.md)
- [foundry_sdk.v2.core.models.UnsupportedTypeParamKey](../../../../models/v2/core/models/UnsupportedTypeParamKey.md)
- [foundry_sdk.v2.core.models.UnsupportedTypeParamValue](../../../../models/v2/core/models/UnsupportedTypeParamValue.md)
- [foundry_sdk.v2.core.models.VoidType](../../../../models/v2/core/models/VoidType.md)
- [foundry_sdk.v2.ontologies.models.EntrySetType](../../../../models/v2/ontologies/models/EntrySetType.md)
- [foundry_sdk.v2.ontologies.models.FunctionRid](../../../../models/v2/ontologies/models/FunctionRid.md)
- [foundry_sdk.v2.ontologies.models.FunctionVersion](../../../../models/v2/ontologies/models/FunctionVersion.md)
- [foundry_sdk.v2.ontologies.models.GetQueryTypeByRidBatchRequest](../../../../models/v2/ontologies/models/GetQueryTypeByRidBatchRequest.md)
- [foundry_sdk.v2.ontologies.models.GetQueryTypeByRidBatchRequestElement](../../../../models/v2/ontologies/models/GetQueryTypeByRidBatchRequestElement.md)
- [foundry_sdk.v2.ontologies.models.GetQueryTypeByRidBatchResponse](../../../../models/v2/ontologies/models/GetQueryTypeByRidBatchResponse.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](../../../../models/v2/ontologies/models/InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyInterfaceObjectSetType](../../../../models/v2/ontologies/models/OntologyInterfaceObjectSetType.md)
- [foundry_sdk.v2.ontologies.models.OntologyInterfaceObjectType](../../../../models/v2/ontologies/models/OntologyInterfaceObjectType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectSetType](../../../../models/v2/ontologies/models/OntologyObjectSetType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectType](../../../../models/v2/ontologies/models/OntologyObjectType.md)
- [foundry_sdk.v2.ontologies.models.ParameterId](../../../../models/v2/ontologies/models/ParameterId.md)
- [foundry_sdk.v2.ontologies.models.QueryAggregationKeyType](../../../../models/v2/ontologies/models/QueryAggregationKeyType.md)
- [foundry_sdk.v2.ontologies.models.QueryAggregationRangeSubType](../../../../models/v2/ontologies/models/QueryAggregationRangeSubType.md)
- [foundry_sdk.v2.ontologies.models.QueryAggregationRangeType](../../../../models/v2/ontologies/models/QueryAggregationRangeType.md)
- [foundry_sdk.v2.ontologies.models.QueryAggregationValueType](../../../../models/v2/ontologies/models/QueryAggregationValueType.md)
- [foundry_sdk.v2.ontologies.models.QueryApiName](../../../../models/v2/ontologies/models/QueryApiName.md)
- [foundry_sdk.v2.ontologies.models.QueryArrayType](../../../../models/v2/ontologies/models/QueryArrayType.md)
- [foundry_sdk.v2.ontologies.models.QueryDataType](../../../../models/v2/ontologies/models/QueryDataType.md)
- [foundry_sdk.v2.ontologies.models.QueryParameterV2](../../../../models/v2/ontologies/models/QueryParameterV2.md)
- [foundry_sdk.v2.ontologies.models.QuerySetType](../../../../models/v2/ontologies/models/QuerySetType.md)
- [foundry_sdk.v2.ontologies.models.QueryStructField](../../../../models/v2/ontologies/models/QueryStructField.md)
- [foundry_sdk.v2.ontologies.models.QueryStructType](../../../../models/v2/ontologies/models/QueryStructType.md)
- [foundry_sdk.v2.ontologies.models.QueryTypeReferenceType](../../../../models/v2/ontologies/models/QueryTypeReferenceType.md)
- [foundry_sdk.v2.ontologies.models.QueryTypeV2](../../../../models/v2/ontologies/models/QueryTypeV2.md)
- [foundry_sdk.v2.ontologies.models.QueryUnionType](../../../../models/v2/ontologies/models/QueryUnionType.md)
- [foundry_sdk.v2.ontologies.models.ThreeDimensionalAggregation](../../../../models/v2/ontologies/models/ThreeDimensionalAggregation.md)
- [foundry_sdk.v2.ontologies.models.TwoDimensionalAggregation](../../../../models/v2/ontologies/models/TwoDimensionalAggregation.md)
- [foundry_sdk.v2.ontologies.models.TypeReferenceIdentifier](../../../../models/v2/ontologies/models/TypeReferenceIdentifier.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/QueryType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_by_rid_batch.md)
