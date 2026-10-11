# v2.functions.VersionId.get


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets a specific version of a value type with the given RID and version ID.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.functions.ValueType.VersionId.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, value_type_rid: functions_models.ValueTypeRid, version_id_version_id: functions_models.ValueTypeVersionId, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> functions_models.VersionId: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| value_type_rid | functions_models.ValueTypeRid | required | Value shape and constraints are in its referenced local type definition. |
| version_id_version_id | functions_models.ValueTypeVersionId | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| VersionIdNotFound | The given VersionId could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/functions/valueTypes/{valueTypeRid}/versionIds/{versionIdVersionId}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'valueTypeRid': value_type_rid, 'versionIdVersionId': version_id_version_id}
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
functions_models.VersionId
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'VersionIdNotFound': functions_errors.VersionIdNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `functions_models.VersionId`. Ordinary async return: `typing.Awaitable[functions_models.VersionId]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | functions_models.VersionId |
| sync_raw | ApiResponse[functions_models.VersionId] |
| sync_streaming | StreamingContextManager[functions_models.VersionId] |
| async_ordinary | typing.Awaitable[functions_models.VersionId] |
| async_raw | Awaitable[AsyncApiResponse[functions_models.VersionId]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[functions_models.VersionId]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.DisplayName](../../../../models/v2/core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.functions.errors.VersionIdNotFound](../../../../models/v2/functions/errors/VersionIdNotFound.md)
- [foundry_sdk.v2.functions.errors.VersionIdNotFoundParameters](../../../../models/v2/functions/errors/VersionIdNotFoundParameters.md)
- [foundry_sdk.v2.functions.models.ArrayConstraint](../../../../models/v2/functions/models/ArrayConstraint.md)
- [foundry_sdk.v2.functions.models.EnumConstraint](../../../../models/v2/functions/models/EnumConstraint.md)
- [foundry_sdk.v2.functions.models.LengthConstraint](../../../../models/v2/functions/models/LengthConstraint.md)
- [foundry_sdk.v2.functions.models.MapConstraint](../../../../models/v2/functions/models/MapConstraint.md)
- [foundry_sdk.v2.functions.models.NullableConstraint](../../../../models/v2/functions/models/NullableConstraint.md)
- [foundry_sdk.v2.functions.models.NullableConstraintValue](../../../../models/v2/functions/models/NullableConstraintValue.md)
- [foundry_sdk.v2.functions.models.RangesConstraint](../../../../models/v2/functions/models/RangesConstraint.md)
- [foundry_sdk.v2.functions.models.RegexConstraint](../../../../models/v2/functions/models/RegexConstraint.md)
- [foundry_sdk.v2.functions.models.RidConstraint](../../../../models/v2/functions/models/RidConstraint.md)
- [foundry_sdk.v2.functions.models.StructConstraint](../../../../models/v2/functions/models/StructConstraint.md)
- [foundry_sdk.v2.functions.models.StructFieldApiName](../../../../models/v2/functions/models/StructFieldApiName.md)
- [foundry_sdk.v2.functions.models.StructV1Constraint](../../../../models/v2/functions/models/StructV1Constraint.md)
- [foundry_sdk.v2.functions.models.UuidConstraint](../../../../models/v2/functions/models/UuidConstraint.md)
- [foundry_sdk.v2.functions.models.ValueTypeApiName](../../../../models/v2/functions/models/ValueTypeApiName.md)
- [foundry_sdk.v2.functions.models.ValueTypeConstraint](../../../../models/v2/functions/models/ValueTypeConstraint.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataType](../../../../models/v2/functions/models/ValueTypeDataType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeArrayType](../../../../models/v2/functions/models/ValueTypeDataTypeArrayType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeBinaryType](../../../../models/v2/functions/models/ValueTypeDataTypeBinaryType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeBooleanType](../../../../models/v2/functions/models/ValueTypeDataTypeBooleanType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeByteType](../../../../models/v2/functions/models/ValueTypeDataTypeByteType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeDateType](../../../../models/v2/functions/models/ValueTypeDataTypeDateType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeDecimalType](../../../../models/v2/functions/models/ValueTypeDataTypeDecimalType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeDoubleType](../../../../models/v2/functions/models/ValueTypeDataTypeDoubleType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeFloatType](../../../../models/v2/functions/models/ValueTypeDataTypeFloatType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeIntegerType](../../../../models/v2/functions/models/ValueTypeDataTypeIntegerType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeLongType](../../../../models/v2/functions/models/ValueTypeDataTypeLongType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeMapType](../../../../models/v2/functions/models/ValueTypeDataTypeMapType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeOptionalType](../../../../models/v2/functions/models/ValueTypeDataTypeOptionalType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeShortType](../../../../models/v2/functions/models/ValueTypeDataTypeShortType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeStringType](../../../../models/v2/functions/models/ValueTypeDataTypeStringType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeStructElement](../../../../models/v2/functions/models/ValueTypeDataTypeStructElement.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeStructFieldIdentifier](../../../../models/v2/functions/models/ValueTypeDataTypeStructFieldIdentifier.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeStructType](../../../../models/v2/functions/models/ValueTypeDataTypeStructType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeTimestampType](../../../../models/v2/functions/models/ValueTypeDataTypeTimestampType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeUnionType](../../../../models/v2/functions/models/ValueTypeDataTypeUnionType.md)
- [foundry_sdk.v2.functions.models.ValueTypeDataTypeValueTypeReference](../../../../models/v2/functions/models/ValueTypeDataTypeValueTypeReference.md)
- [foundry_sdk.v2.functions.models.ValueTypeDescription](../../../../models/v2/functions/models/ValueTypeDescription.md)
- [foundry_sdk.v2.functions.models.ValueTypeRid](../../../../models/v2/functions/models/ValueTypeRid.md)
- [foundry_sdk.v2.functions.models.ValueTypeVersion](../../../../models/v2/functions/models/ValueTypeVersion.md)
- [foundry_sdk.v2.functions.models.ValueTypeVersionId](../../../../models/v2/functions/models/ValueTypeVersionId.md)
- [foundry_sdk.v2.functions.models.VersionId](../../../../models/v2/functions/models/VersionId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/functions/VersionId.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
