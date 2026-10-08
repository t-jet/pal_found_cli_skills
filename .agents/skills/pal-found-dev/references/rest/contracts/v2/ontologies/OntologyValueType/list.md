# v2.ontologies.OntologyValueType.list


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists the latest versions of the value types for the given Ontology.

## SDK invocation contract

```python
def list(self, ontology: ontologies_models.OntologyIdentifier, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ListOntologyValueTypesResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
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
'/v2/ontologies/{ontology}/valueTypes'
```

**query_params**

```python
{'preview': preview}
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
ontologies_models.ListOntologyValueTypesResponse
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

Ordinary sync return: `ontologies_models.ListOntologyValueTypesResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.ListOntologyValueTypesResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ListOntologyValueTypesResponse |
| sync_raw | ApiResponse[ontologies_models.ListOntologyValueTypesResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ListOntologyValueTypesResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.ListOntologyValueTypesResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListOntologyValueTypesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListOntologyValueTypesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BinaryType](../../../../models/v2/core/models/BinaryType.md)
- [foundry_sdk.v2.core.models.BooleanType](../../../../models/v2/core/models/BooleanType.md)
- [foundry_sdk.v2.core.models.ByteType](../../../../models/v2/core/models/ByteType.md)
- [foundry_sdk.v2.core.models.DateType](../../../../models/v2/core/models/DateType.md)
- [foundry_sdk.v2.core.models.DisplayName](../../../../models/v2/core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.DoubleType](../../../../models/v2/core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.FloatType](../../../../models/v2/core/models/FloatType.md)
- [foundry_sdk.v2.core.models.IntegerType](../../../../models/v2/core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LongType](../../../../models/v2/core/models/LongType.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.ShortType](../../../../models/v2/core/models/ShortType.md)
- [foundry_sdk.v2.core.models.StringType](../../../../models/v2/core/models/StringType.md)
- [foundry_sdk.v2.core.models.StructFieldName](../../../../models/v2/core/models/StructFieldName.md)
- [foundry_sdk.v2.core.models.TimestampType](../../../../models/v2/core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.UnsupportedType](../../../../models/v2/core/models/UnsupportedType.md)
- [foundry_sdk.v2.core.models.UnsupportedTypeParamKey](../../../../models/v2/core/models/UnsupportedTypeParamKey.md)
- [foundry_sdk.v2.core.models.UnsupportedTypeParamValue](../../../../models/v2/core/models/UnsupportedTypeParamValue.md)
- [foundry_sdk.v2.ontologies.models.ArrayConstraint](../../../../models/v2/ontologies/models/ArrayConstraint.md)
- [foundry_sdk.v2.ontologies.models.EnumConstraint](../../../../models/v2/ontologies/models/EnumConstraint.md)
- [foundry_sdk.v2.ontologies.models.LengthConstraint](../../../../models/v2/ontologies/models/LengthConstraint.md)
- [foundry_sdk.v2.ontologies.models.ListOntologyValueTypesResponse](../../../../models/v2/ontologies/models/ListOntologyValueTypesResponse.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyValueType](../../../../models/v2/ontologies/models/OntologyValueType.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](../../../../models/v2/ontologies/models/PropertyValue.md)
- [foundry_sdk.v2.ontologies.models.RangesConstraint](../../../../models/v2/ontologies/models/RangesConstraint.md)
- [foundry_sdk.v2.ontologies.models.RegexConstraint](../../../../models/v2/ontologies/models/RegexConstraint.md)
- [foundry_sdk.v2.ontologies.models.RidConstraint](../../../../models/v2/ontologies/models/RidConstraint.md)
- [foundry_sdk.v2.ontologies.models.StructConstraint](../../../../models/v2/ontologies/models/StructConstraint.md)
- [foundry_sdk.v2.ontologies.models.UuidConstraint](../../../../models/v2/ontologies/models/UuidConstraint.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeApiName](../../../../models/v2/ontologies/models/ValueTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeArrayType](../../../../models/v2/ontologies/models/ValueTypeArrayType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeConstraint](../../../../models/v2/ontologies/models/ValueTypeConstraint.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeDecimalType](../../../../models/v2/ontologies/models/ValueTypeDecimalType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeFieldType](../../../../models/v2/ontologies/models/ValueTypeFieldType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeMapType](../../../../models/v2/ontologies/models/ValueTypeMapType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeOptionalType](../../../../models/v2/ontologies/models/ValueTypeOptionalType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeReferenceType](../../../../models/v2/ontologies/models/ValueTypeReferenceType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeRid](../../../../models/v2/ontologies/models/ValueTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeStatus](../../../../models/v2/ontologies/models/ValueTypeStatus.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeStructField](../../../../models/v2/ontologies/models/ValueTypeStructField.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeStructType](../../../../models/v2/ontologies/models/ValueTypeStructType.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeUnionType](../../../../models/v2/ontologies/models/ValueTypeUnionType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/OntologyValueType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
