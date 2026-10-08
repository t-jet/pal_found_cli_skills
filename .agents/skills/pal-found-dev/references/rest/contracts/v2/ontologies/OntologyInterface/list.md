# v2.ontologies.OntologyInterface.list


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists the interface types for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

## SDK invocation contract

```python
def list(self, ontology: ontologies_models.OntologyIdentifier, *, branch: typing.Optional[core_models.FoundryBranch]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[ontologies_models.InterfaceType]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to list the interface types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
| page_size | typing.Optional[core_models.PageSize] | None | The desired size of the page to be returned. Defaults to 500. See [page sizes](../../../../client-behavior.md) for details. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
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
'/v2/ontologies/{ontology}/interfaceTypes'
```

**query_params**

```python
{'branch': branch, 'pageSize': page_size, 'pageToken': page_token, 'preview': preview}
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
ontologies_models.ListInterfaceTypesResponse
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

Ordinary sync return: `core.ResourceIterator[ontologies_models.InterfaceType]`. Ordinary async return: `core.AsyncResourceIterator[ontologies_models.InterfaceType]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[ontologies_models.InterfaceType] |
| sync_raw | ApiResponse[ontologies_models.ListInterfaceTypesResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ListInterfaceTypesResponse] |
| async_ordinary | core.AsyncResourceIterator[ontologies_models.InterfaceType] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListInterfaceTypesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListInterfaceTypesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.AttachmentType](../../../../models/v2/core/models/AttachmentType.md)
- [foundry_sdk.v2.core.models.BooleanType](../../../../models/v2/core/models/BooleanType.md)
- [foundry_sdk.v2.core.models.ByteType](../../../../models/v2/core/models/ByteType.md)
- [foundry_sdk.v2.core.models.CipherTextType](../../../../models/v2/core/models/CipherTextType.md)
- [foundry_sdk.v2.core.models.DateType](../../../../models/v2/core/models/DateType.md)
- [foundry_sdk.v2.core.models.DecimalType](../../../../models/v2/core/models/DecimalType.md)
- [foundry_sdk.v2.core.models.DisplayName](../../../../models/v2/core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.DoubleType](../../../../models/v2/core/models/DoubleType.md)
- [foundry_sdk.v2.core.models.EmbeddingModel](../../../../models/v2/core/models/EmbeddingModel.md)
- [foundry_sdk.v2.core.models.FloatType](../../../../models/v2/core/models/FloatType.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.FoundryLiveDeployment](../../../../models/v2/core/models/FoundryLiveDeployment.md)
- [foundry_sdk.v2.core.models.GeoPointType](../../../../models/v2/core/models/GeoPointType.md)
- [foundry_sdk.v2.core.models.GeoShapeType](../../../../models/v2/core/models/GeoShapeType.md)
- [foundry_sdk.v2.core.models.GeotimeSeriesReferenceType](../../../../models/v2/core/models/GeotimeSeriesReferenceType.md)
- [foundry_sdk.v2.core.models.IntegerType](../../../../models/v2/core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LmsEmbeddingModel](../../../../models/v2/core/models/LmsEmbeddingModel.md)
- [foundry_sdk.v2.core.models.LmsEmbeddingModelValue](../../../../models/v2/core/models/LmsEmbeddingModelValue.md)
- [foundry_sdk.v2.core.models.LongType](../../../../models/v2/core/models/LongType.md)
- [foundry_sdk.v2.core.models.MarkingType](../../../../models/v2/core/models/MarkingType.md)
- [foundry_sdk.v2.core.models.MarkingTypeValue](../../../../models/v2/core/models/MarkingTypeValue.md)
- [foundry_sdk.v2.core.models.MediaReferenceType](../../../../models/v2/core/models/MediaReferenceType.md)
- [foundry_sdk.v2.core.models.NumericOrNonNumericType](../../../../models/v2/core/models/NumericOrNonNumericType.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.ShortType](../../../../models/v2/core/models/ShortType.md)
- [foundry_sdk.v2.core.models.StringType](../../../../models/v2/core/models/StringType.md)
- [foundry_sdk.v2.core.models.TimeSeriesItemType](../../../../models/v2/core/models/TimeSeriesItemType.md)
- [foundry_sdk.v2.core.models.TimeseriesType](../../../../models/v2/core/models/TimeseriesType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../../../models/v2/core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.VectorSimilarityFunction](../../../../models/v2/core/models/VectorSimilarityFunction.md)
- [foundry_sdk.v2.core.models.VectorSimilarityFunctionValue](../../../../models/v2/core/models/VectorSimilarityFunctionValue.md)
- [foundry_sdk.v2.core.models.VectorType](../../../../models/v2/core/models/VectorType.md)
- [foundry_sdk.v2.ontologies.models.Affix](../../../../models/v2/ontologies/models/Affix.md)
- [foundry_sdk.v2.ontologies.models.DatetimeFormat](../../../../models/v2/ontologies/models/DatetimeFormat.md)
- [foundry_sdk.v2.ontologies.models.DatetimeLocalizedFormat](../../../../models/v2/ontologies/models/DatetimeLocalizedFormat.md)
- [foundry_sdk.v2.ontologies.models.DatetimeLocalizedFormatType](../../../../models/v2/ontologies/models/DatetimeLocalizedFormatType.md)
- [foundry_sdk.v2.ontologies.models.DatetimeStringFormat](../../../../models/v2/ontologies/models/DatetimeStringFormat.md)
- [foundry_sdk.v2.ontologies.models.DatetimeTimezone](../../../../models/v2/ontologies/models/DatetimeTimezone.md)
- [foundry_sdk.v2.ontologies.models.DatetimeTimezoneStatic](../../../../models/v2/ontologies/models/DatetimeTimezoneStatic.md)
- [foundry_sdk.v2.ontologies.models.DatetimeTimezoneUser](../../../../models/v2/ontologies/models/DatetimeTimezoneUser.md)
- [foundry_sdk.v2.ontologies.models.DurationBaseValue](../../../../models/v2/ontologies/models/DurationBaseValue.md)
- [foundry_sdk.v2.ontologies.models.DurationFormatStyle](../../../../models/v2/ontologies/models/DurationFormatStyle.md)
- [foundry_sdk.v2.ontologies.models.DurationPrecision](../../../../models/v2/ontologies/models/DurationPrecision.md)
- [foundry_sdk.v2.ontologies.models.FixedValuesMapKey](../../../../models/v2/ontologies/models/FixedValuesMapKey.md)
- [foundry_sdk.v2.ontologies.models.HumanReadableFormat](../../../../models/v2/ontologies/models/HumanReadableFormat.md)
- [foundry_sdk.v2.ontologies.models.InterfaceDefinedPropertyType](../../../../models/v2/ontologies/models/InterfaceDefinedPropertyType.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkType](../../../../models/v2/ontologies/models/InterfaceLinkType.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeApiName](../../../../models/v2/ontologies/models/InterfaceLinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeCardinality](../../../../models/v2/ontologies/models/InterfaceLinkTypeCardinality.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeLinkedEntityApiName](../../../../models/v2/ontologies/models/InterfaceLinkTypeLinkedEntityApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeRid](../../../../models/v2/ontologies/models/InterfaceLinkTypeRid.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyApiName](../../../../models/v2/ontologies/models/InterfacePropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyType](../../../../models/v2/ontologies/models/InterfacePropertyType.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyTypeRid](../../../../models/v2/ontologies/models/InterfacePropertyTypeRid.md)
- [foundry_sdk.v2.ontologies.models.InterfaceSharedPropertyType](../../../../models/v2/ontologies/models/InterfaceSharedPropertyType.md)
- [foundry_sdk.v2.ontologies.models.InterfaceType](../../../../models/v2/ontologies/models/InterfaceType.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](../../../../models/v2/ontologies/models/InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeRid](../../../../models/v2/ontologies/models/InterfaceTypeRid.md)
- [foundry_sdk.v2.ontologies.models.KnownType](../../../../models/v2/ontologies/models/KnownType.md)
- [foundry_sdk.v2.ontologies.models.LinkedInterfaceTypeApiName](../../../../models/v2/ontologies/models/LinkedInterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkedObjectTypeApiName](../../../../models/v2/ontologies/models/LinkedObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ListInterfaceTypesResponse](../../../../models/v2/ontologies/models/ListInterfaceTypesResponse.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatAffix](../../../../models/v2/ontologies/models/NumberFormatAffix.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatCurrency](../../../../models/v2/ontologies/models/NumberFormatCurrency.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatCurrencyStyle](../../../../models/v2/ontologies/models/NumberFormatCurrencyStyle.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatCustomUnit](../../../../models/v2/ontologies/models/NumberFormatCustomUnit.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatDuration](../../../../models/v2/ontologies/models/NumberFormatDuration.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatFixedValues](../../../../models/v2/ontologies/models/NumberFormatFixedValues.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatNotation](../../../../models/v2/ontologies/models/NumberFormatNotation.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatOptions](../../../../models/v2/ontologies/models/NumberFormatOptions.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatRatio](../../../../models/v2/ontologies/models/NumberFormatRatio.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatScale](../../../../models/v2/ontologies/models/NumberFormatScale.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatStandard](../../../../models/v2/ontologies/models/NumberFormatStandard.md)
- [foundry_sdk.v2.ontologies.models.NumberFormatStandardUnit](../../../../models/v2/ontologies/models/NumberFormatStandardUnit.md)
- [foundry_sdk.v2.ontologies.models.NumberRatioType](../../../../models/v2/ontologies/models/NumberRatioType.md)
- [foundry_sdk.v2.ontologies.models.NumberRoundingMode](../../../../models/v2/ontologies/models/NumberRoundingMode.md)
- [foundry_sdk.v2.ontologies.models.NumberScaleType](../../../../models/v2/ontologies/models/NumberScaleType.md)
- [foundry_sdk.v2.ontologies.models.ObjectPropertyType](../../../../models/v2/ontologies/models/ObjectPropertyType.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectArrayType](../../../../models/v2/ontologies/models/OntologyObjectArrayType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectArrayTypeReducer](../../../../models/v2/ontologies/models/OntologyObjectArrayTypeReducer.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectArrayTypeReducerSortDirection](../../../../models/v2/ontologies/models/OntologyObjectArrayTypeReducerSortDirection.md)
- [foundry_sdk.v2.ontologies.models.PropertyBooleanFormattingRule](../../../../models/v2/ontologies/models/PropertyBooleanFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyDateFormattingRule](../../../../models/v2/ontologies/models/PropertyDateFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyKnownTypeFormattingRule](../../../../models/v2/ontologies/models/PropertyKnownTypeFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyNumberFormattingRule](../../../../models/v2/ontologies/models/PropertyNumberFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyNumberFormattingRuleType](../../../../models/v2/ontologies/models/PropertyNumberFormattingRuleType.md)
- [foundry_sdk.v2.ontologies.models.PropertyTimestampFormattingRule](../../../../models/v2/ontologies/models/PropertyTimestampFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeReference](../../../../models/v2/ontologies/models/PropertyTypeReference.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeReferenceOrStringConstant](../../../../models/v2/ontologies/models/PropertyTypeReferenceOrStringConstant.md)
- [foundry_sdk.v2.ontologies.models.PropertyValueFormattingRule](../../../../models/v2/ontologies/models/PropertyValueFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.ResolvedInterfacePropertyType](../../../../models/v2/ontologies/models/ResolvedInterfacePropertyType.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeApiName](../../../../models/v2/ontologies/models/SharedPropertyTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeRid](../../../../models/v2/ontologies/models/SharedPropertyTypeRid.md)
- [foundry_sdk.v2.ontologies.models.StringConstant](../../../../models/v2/ontologies/models/StringConstant.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](../../../../models/v2/ontologies/models/StructFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldType](../../../../models/v2/ontologies/models/StructFieldType.md)
- [foundry_sdk.v2.ontologies.models.StructFieldTypeRid](../../../../models/v2/ontologies/models/StructFieldTypeRid.md)
- [foundry_sdk.v2.ontologies.models.StructType](../../../../models/v2/ontologies/models/StructType.md)
- [foundry_sdk.v2.ontologies.models.StructTypeMainValue](../../../../models/v2/ontologies/models/StructTypeMainValue.md)
- [foundry_sdk.v2.ontologies.models.TimeCodeFormat](../../../../models/v2/ontologies/models/TimeCodeFormat.md)
- [foundry_sdk.v2.ontologies.models.TypeClass](../../../../models/v2/ontologies/models/TypeClass.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeApiName](../../../../models/v2/ontologies/models/ValueTypeApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/OntologyInterface.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Page size is a request hint. Continue with the returned nextPageToken until absent; bound pages and reject a repeated token. [Local procedure](../../../../client-behavior.md).

[Part 1](list.md)
