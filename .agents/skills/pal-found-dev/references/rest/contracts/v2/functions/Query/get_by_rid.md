# v2.functions.Query.get_by_rid


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets a specific query type with the given RID. By default, this gets the latest version of the query.

## SDK invocation contract

```python
def get_by_rid(self, *, rid: functions_models.FunctionRid, include_prerelease: typing.Optional[bool]=None, preview: typing.Optional[core_models.PreviewMode]=None, version: typing.Optional[functions_models.FunctionVersion]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> functions_models.Query: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| rid | functions_models.FunctionRid | required | Value shape and constraints are in its referenced local type definition. |
| include_prerelease | typing.Optional[bool] | None | When no version is specified and this flag is set to true, the latest version resolution will consider prerelease versions (e.g., 1.2.3-beta could be returned as the latest). When false, only stable versions are considered when determining the latest version. Defaults to false. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| version | typing.Optional[functions_models.FunctionVersion] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetByRidPermissionDenied | Could not getByRid the Query. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/functions/queries/getByRid'
```

**query_params**

```python
{'rid': rid, 'includePrerelease': include_prerelease, 'preview': preview, 'version': version}
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
functions_models.Query
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetByRidPermissionDenied': functions_errors.GetByRidPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `functions_models.Query`. Ordinary async return: `typing.Awaitable[functions_models.Query]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | functions_models.Query |
| sync_raw | ApiResponse[functions_models.Query] |
| sync_streaming | StreamingContextManager[functions_models.Query] |
| async_ordinary | typing.Awaitable[functions_models.Query] |
| async_raw | Awaitable[AsyncApiResponse[functions_models.Query]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[functions_models.Query]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
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
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.StringType](../../../../models/v2/core/models/StringType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../../../models/v2/core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.UnsupportedType](../../../../models/v2/core/models/UnsupportedType.md)
- [foundry_sdk.v2.core.models.UnsupportedTypeParamKey](../../../../models/v2/core/models/UnsupportedTypeParamKey.md)
- [foundry_sdk.v2.core.models.UnsupportedTypeParamValue](../../../../models/v2/core/models/UnsupportedTypeParamValue.md)
- [foundry_sdk.v2.core.models.VoidType](../../../../models/v2/core/models/VoidType.md)
- [foundry_sdk.v2.functions.errors.GetByRidPermissionDenied](../../../../models/v2/functions/errors/GetByRidPermissionDenied.md)
- [foundry_sdk.v2.functions.errors.GetByRidPermissionDeniedParameters](../../../../models/v2/functions/errors/GetByRidPermissionDeniedParameters.md)
- [foundry_sdk.v2.functions.models.FunctionRid](../../../../models/v2/functions/models/FunctionRid.md)
- [foundry_sdk.v2.functions.models.FunctionVersion](../../../../models/v2/functions/models/FunctionVersion.md)
- [foundry_sdk.v2.functions.models.Parameter](../../../../models/v2/functions/models/Parameter.md)
- [foundry_sdk.v2.functions.models.ParameterId](../../../../models/v2/functions/models/ParameterId.md)
- [foundry_sdk.v2.functions.models.Query](../../../../models/v2/functions/models/Query.md)
- [foundry_sdk.v2.functions.models.QueryAggregationKeyType](../../../../models/v2/functions/models/QueryAggregationKeyType.md)
- [foundry_sdk.v2.functions.models.QueryAggregationRangeSubType](../../../../models/v2/functions/models/QueryAggregationRangeSubType.md)
- [foundry_sdk.v2.functions.models.QueryAggregationRangeType](../../../../models/v2/functions/models/QueryAggregationRangeType.md)
- [foundry_sdk.v2.functions.models.QueryAggregationValueType](../../../../models/v2/functions/models/QueryAggregationValueType.md)
- [foundry_sdk.v2.functions.models.QueryApiName](../../../../models/v2/functions/models/QueryApiName.md)
- [foundry_sdk.v2.functions.models.QueryArrayType](../../../../models/v2/functions/models/QueryArrayType.md)
- [foundry_sdk.v2.functions.models.QueryDataType](../../../../models/v2/functions/models/QueryDataType.md)
- [foundry_sdk.v2.functions.models.QuerySetType](../../../../models/v2/functions/models/QuerySetType.md)
- [foundry_sdk.v2.functions.models.QueryStructField](../../../../models/v2/functions/models/QueryStructField.md)
- [foundry_sdk.v2.functions.models.QueryStructType](../../../../models/v2/functions/models/QueryStructType.md)
- [foundry_sdk.v2.functions.models.QueryTypeReferenceType](../../../../models/v2/functions/models/QueryTypeReferenceType.md)
- [foundry_sdk.v2.functions.models.QueryUnionType](../../../../models/v2/functions/models/QueryUnionType.md)
- [foundry_sdk.v2.functions.models.StructFieldName](../../../../models/v2/functions/models/StructFieldName.md)
- [foundry_sdk.v2.functions.models.ThreeDimensionalAggregation](../../../../models/v2/functions/models/ThreeDimensionalAggregation.md)
- [foundry_sdk.v2.functions.models.TwoDimensionalAggregation](../../../../models/v2/functions/models/TwoDimensionalAggregation.md)
- [foundry_sdk.v2.functions.models.TypeReferenceIdentifier](../../../../models/v2/functions/models/TypeReferenceIdentifier.md)
- [foundry_sdk.v2.functions.models.ValueTypeReference](../../../../models/v2/functions/models/ValueTypeReference.md)
- [foundry_sdk.v2.functions.models.ValueTypeRid](../../../../models/v2/functions/models/ValueTypeRid.md)
- [foundry_sdk.v2.functions.models.ValueTypeVersionId](../../../../models/v2/functions/models/ValueTypeVersionId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/functions/Query.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_by_rid.md)
