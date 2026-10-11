# v2.ontologies.QueryType.get


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets a specific query type with the given API name.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.Ontology.QueryType.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, ontology: ontologies_models.OntologyIdentifier, query_api_name: ontologies_models.QueryApiName, *, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, version: typing.Optional[ontologies_models.FunctionVersion]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.QueryTypeV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| query_api_name | ontologies_models.QueryApiName | required | The API name of the query type. To find the API name, use the **List query types** endpoint or check the **Ontology Manager**. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package rid of the generated SDK. |
| sdk_version | typing.Optional[ontologies_models.SdkVersion] | None | The version of the generated SDK. |
| version | typing.Optional[ontologies_models.FunctionVersion] | None | The version of the Query to get. |
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
'/v2/ontologies/{ontology}/queryTypes/{queryApiName}'
```

**query_params**

```python
{'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version, 'version': version}
```

**path_params**

```python
{'ontology': ontology, 'queryApiName': query_api_name}
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
ontologies_models.QueryTypeV2
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

Ordinary sync return: `ontologies_models.QueryTypeV2`. Ordinary async return: `typing.Awaitable[ontologies_models.QueryTypeV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.QueryTypeV2 |
| sync_raw | ApiResponse[ontologies_models.QueryTypeV2] |
| sync_streaming | StreamingContextManager[ontologies_models.QueryTypeV2] |
| async_ordinary | typing.Awaitable[ontologies_models.QueryTypeV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.QueryTypeV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.QueryTypeV2]] |

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
- [foundry_sdk.v2.core.models.IntegerType](../../../../models/v2/core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../../../models/v2/core/models/LongType.md)
- [foundry_sdk.v2.core.models.MediaReferenceType](../../../../models/v2/core/models/MediaReferenceType.md)
- [foundry_sdk.v2.core.models.NullType](../../../../models/v2/core/models/NullType.md)
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
- [foundry_sdk.v2.ontologies.models.SdkPackageRid](../../../../models/v2/ontologies/models/SdkPackageRid.md)
- [foundry_sdk.v2.ontologies.models.SdkVersion](../../../../models/v2/ontologies/models/SdkVersion.md)
- [foundry_sdk.v2.ontologies.models.ThreeDimensionalAggregation](../../../../models/v2/ontologies/models/ThreeDimensionalAggregation.md)
- [foundry_sdk.v2.ontologies.models.TwoDimensionalAggregation](../../../../models/v2/ontologies/models/TwoDimensionalAggregation.md)
- [foundry_sdk.v2.ontologies.models.TypeReferenceIdentifier](../../../../models/v2/ontologies/models/TypeReferenceIdentifier.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/QueryType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
