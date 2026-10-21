# v2.ontologies.ObjectType.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists the object types for the given Ontology.

Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are
more results available, at least one result will be present in the
response.

Note: the `aliases` field is not populated on this endpoint and will always be empty. To retrieve object type
aliases, use the get-by-RID read paths (e.g. `getObjectTypeV2`).

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.Ontology.ObjectType.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, ontology: ontologies_models.OntologyIdentifier, *, branch: typing.Optional[core_models.FoundryBranch]=None, include_datasources: typing.Optional[bool]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[ontologies_models.ObjectTypeV2]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to list the object types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
| include_datasources | typing.Optional[bool] | None | When set to `true`, the `datasources` field on each returned object type is populated with the datasources backing it. Defaults to `false`. |
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
'/v2/ontologies/{ontology}/objectTypes'
```

**query_params**

```python
{'branch': branch, 'includeDatasources': include_datasources, 'pageSize': page_size, 'pageToken': page_token}
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
ontologies_models.ListObjectTypesV2Response
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

Ordinary sync return: `core.ResourceIterator[ontologies_models.ObjectTypeV2]`. Ordinary async return: `core.AsyncResourceIterator[ontologies_models.ObjectTypeV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[ontologies_models.ObjectTypeV2] |
| sync_raw | ApiResponse[ontologies_models.ListObjectTypesV2Response] |
| sync_streaming | StreamingContextManager[ontologies_models.ListObjectTypesV2Response] |
| async_ordinary | core.AsyncResourceIterator[ontologies_models.ObjectTypeV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListObjectTypesV2Response]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListObjectTypesV2Response]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
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
- [foundry_sdk.v2.core.models.MediaSetViewRid](../../../../models/v2/core/models/MediaSetViewRid.md)
- [foundry_sdk.v2.core.models.NumericOrNonNumericType](../../../../models/v2/core/models/NumericOrNonNumericType.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.ReleaseStatus](../../../../models/v2/core/models/ReleaseStatus.md)
- [foundry_sdk.v2.core.models.ShortType](../../../../models/v2/core/models/ShortType.md)
- [foundry_sdk.v2.core.models.StringType](../../../../models/v2/core/models/StringType.md)
- [foundry_sdk.v2.core.models.StructFieldName](../../../../models/v2/core/models/StructFieldName.md)
- [foundry_sdk.v2.core.models.TimeSeriesItemType](../../../../models/v2/core/models/TimeSeriesItemType.md)
- [foundry_sdk.v2.core.models.TimeseriesType](../../../../models/v2/core/models/TimeseriesType.md)
- [foundry_sdk.v2.core.models.TimestampType](../../../../models/v2/core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.VectorSimilarityFunction](../../../../models/v2/core/models/VectorSimilarityFunction.md)
- [foundry_sdk.v2.core.models.VectorSimilarityFunctionValue](../../../../models/v2/core/models/VectorSimilarityFunctionValue.md)
- [foundry_sdk.v2.core.models.VectorType](../../../../models/v2/core/models/VectorType.md)
- [foundry_sdk.v2.datasets.models.DatasetRid](../../../../models/v2/datasets/models/DatasetRid.md)
- [foundry_sdk.v2.ontologies.models.ActivePropertyTypeStatus](../../../../models/v2/ontologies/models/ActivePropertyTypeStatus.md)
- [foundry_sdk.v2.ontologies.models.Affix](../../../../models/v2/ontologies/models/Affix.md)
- [foundry_sdk.v2.ontologies.models.BlueprintIcon](../../../../models/v2/ontologies/models/BlueprintIcon.md)
- [foundry_sdk.v2.ontologies.models.ColumnName](../../../../models/v2/ontologies/models/ColumnName.md)
- [foundry_sdk.v2.ontologies.models.ColumnPropertyMapping](../../../../models/v2/ontologies/models/ColumnPropertyMapping.md)
- [foundry_sdk.v2.ontologies.models.DatasourceBranchId](../../../../models/v2/ontologies/models/DatasourceBranchId.md)
- [foundry_sdk.v2.ontologies.models.DatasourceRid](../../../../models/v2/ontologies/models/DatasourceRid.md)
- [foundry_sdk.v2.ontologies.models.DatetimeFormat](../../../../models/v2/ontologies/models/DatetimeFormat.md)
- [foundry_sdk.v2.ontologies.models.DatetimeLocalizedFormat](../../../../models/v2/ontologies/models/DatetimeLocalizedFormat.md)
- [foundry_sdk.v2.ontologies.models.DatetimeLocalizedFormatType](../../../../models/v2/ontologies/models/DatetimeLocalizedFormatType.md)
- [foundry_sdk.v2.ontologies.models.DatetimeStringFormat](../../../../models/v2/ontologies/models/DatetimeStringFormat.md)
- [foundry_sdk.v2.ontologies.models.DatetimeTimezone](../../../../models/v2/ontologies/models/DatetimeTimezone.md)
- [foundry_sdk.v2.ontologies.models.DatetimeTimezoneStatic](../../../../models/v2/ontologies/models/DatetimeTimezoneStatic.md)
- [foundry_sdk.v2.ontologies.models.DatetimeTimezoneUser](../../../../models/v2/ontologies/models/DatetimeTimezoneUser.md)
- [foundry_sdk.v2.ontologies.models.DeprecatedPropertyTypeStatus](../../../../models/v2/ontologies/models/DeprecatedPropertyTypeStatus.md)
- [foundry_sdk.v2.ontologies.models.DirectSourceRid](../../../../models/v2/ontologies/models/DirectSourceRid.md)
- [foundry_sdk.v2.ontologies.models.DurationBaseValue](../../../../models/v2/ontologies/models/DurationBaseValue.md)
- [foundry_sdk.v2.ontologies.models.DurationFormatStyle](../../../../models/v2/ontologies/models/DurationFormatStyle.md)
- [foundry_sdk.v2.ontologies.models.DurationPrecision](../../../../models/v2/ontologies/models/DurationPrecision.md)
- [foundry_sdk.v2.ontologies.models.EditOnlyPropertyMapping](../../../../models/v2/ontologies/models/EditOnlyPropertyMapping.md)
- [foundry_sdk.v2.ontologies.models.ExamplePropertyTypeStatus](../../../../models/v2/ontologies/models/ExamplePropertyTypeStatus.md)
- [foundry_sdk.v2.ontologies.models.ExperimentalPropertyTypeStatus](../../../../models/v2/ontologies/models/ExperimentalPropertyTypeStatus.md)
- [foundry_sdk.v2.ontologies.models.FixedValuesMapKey](../../../../models/v2/ontologies/models/FixedValuesMapKey.md)
- [foundry_sdk.v2.ontologies.models.GeotimeSeriesIntegrationRid](../../../../models/v2/ontologies/models/GeotimeSeriesIntegrationRid.md)
- [foundry_sdk.v2.ontologies.models.HumanReadableFormat](../../../../models/v2/ontologies/models/HumanReadableFormat.md)
- [foundry_sdk.v2.ontologies.models.Icon](../../../../models/v2/ontologies/models/Icon.md)
- [foundry_sdk.v2.ontologies.models.KnownType](../../../../models/v2/ontologies/models/KnownType.md)
- [foundry_sdk.v2.ontologies.models.ListObjectTypesV2Response](../../../../models/v2/ontologies/models/ListObjectTypesV2Response.md)
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
- [foundry_sdk.v2.ontologies.models.ObjectTypeDatasetDatasource](../../../../models/v2/ontologies/models/ObjectTypeDatasetDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeDatasource](../../../../models/v2/ontologies/models/ObjectTypeDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeDatasourceDefinition](../../../../models/v2/ontologies/models/ObjectTypeDatasourceDefinition.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeDirectDatasource](../../../../models/v2/ontologies/models/ObjectTypeDirectDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeEditsOnlyDatasource](../../../../models/v2/ontologies/models/ObjectTypeEditsOnlyDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeGeotimeSeriesDatasource](../../../../models/v2/ontologies/models/ObjectTypeGeotimeSeriesDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeMediaSetViewDatasource](../../../../models/v2/ontologies/models/ObjectTypeMediaSetViewDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeRestrictedViewDatasource](../../../../models/v2/ontologies/models/ObjectTypeRestrictedViewDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeRid](../../../../models/v2/ontologies/models/ObjectTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeStreamDatasource](../../../../models/v2/ontologies/models/ObjectTypeStreamDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeTableDatasource](../../../../models/v2/ontologies/models/ObjectTypeTableDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeTimeSeriesDatasource](../../../../models/v2/ontologies/models/ObjectTypeTimeSeriesDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeUnsupportedDatasource](../../../../models/v2/ontologies/models/ObjectTypeUnsupportedDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeV2](../../../../models/v2/ontologies/models/ObjectTypeV2.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeVisibility](../../../../models/v2/ontologies/models/ObjectTypeVisibility.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectArrayType](../../../../models/v2/ontologies/models/OntologyObjectArrayType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectArrayTypeReducer](../../../../models/v2/ontologies/models/OntologyObjectArrayTypeReducer.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectArrayTypeReducerSortDirection](../../../../models/v2/ontologies/models/OntologyObjectArrayTypeReducerSortDirection.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyBooleanFormattingRule](../../../../models/v2/ontologies/models/PropertyBooleanFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyDateFormattingRule](../../../../models/v2/ontologies/models/PropertyDateFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyKnownTypeFormattingRule](../../../../models/v2/ontologies/models/PropertyKnownTypeFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyNumberFormattingRule](../../../../models/v2/ontologies/models/PropertyNumberFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyNumberFormattingRuleType](../../../../models/v2/ontologies/models/PropertyNumberFormattingRuleType.md)
- [foundry_sdk.v2.ontologies.models.PropertyTimestampFormattingRule](../../../../models/v2/ontologies/models/PropertyTimestampFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeMappingInfo](../../../../models/v2/ontologies/models/PropertyTypeMappingInfo.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeReference](../../../../models/v2/ontologies/models/PropertyTypeReference.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeReferenceOrStringConstant](../../../../models/v2/ontologies/models/PropertyTypeReferenceOrStringConstant.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeRid](../../../../models/v2/ontologies/models/PropertyTypeRid.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeStatus](../../../../models/v2/ontologies/models/PropertyTypeStatus.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeVisibility](../../../../models/v2/ontologies/models/PropertyTypeVisibility.md)
- [foundry_sdk.v2.ontologies.models.PropertyV2](../../../../models/v2/ontologies/models/PropertyV2.md)
- [foundry_sdk.v2.ontologies.models.PropertyValueFormattingRule](../../../../models/v2/ontologies/models/PropertyValueFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.RestrictedViewRid](../../../../models/v2/ontologies/models/RestrictedViewRid.md)
- [foundry_sdk.v2.ontologies.models.StreamRid](../../../../models/v2/ontologies/models/StreamRid.md)
- [foundry_sdk.v2.ontologies.models.StringConstant](../../../../models/v2/ontologies/models/StringConstant.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](../../../../models/v2/ontologies/models/StructFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldPropertyMapping](../../../../models/v2/ontologies/models/StructFieldPropertyMapping.md)
- [foundry_sdk.v2.ontologies.models.StructFieldType](../../../../models/v2/ontologies/models/StructFieldType.md)
- [foundry_sdk.v2.ontologies.models.StructFieldTypeRid](../../../../models/v2/ontologies/models/StructFieldTypeRid.md)
- [foundry_sdk.v2.ontologies.models.StructPropertyMapping](../../../../models/v2/ontologies/models/StructPropertyMapping.md)
- [foundry_sdk.v2.ontologies.models.StructType](../../../../models/v2/ontologies/models/StructType.md)
- [foundry_sdk.v2.ontologies.models.StructTypeMainValue](../../../../models/v2/ontologies/models/StructTypeMainValue.md)
- [foundry_sdk.v2.ontologies.models.TableRid](../../../../models/v2/ontologies/models/TableRid.md)
- [foundry_sdk.v2.ontologies.models.TimeCodeFormat](../../../../models/v2/ontologies/models/TimeCodeFormat.md)
- [foundry_sdk.v2.ontologies.models.TimeseriesSyncRid](../../../../models/v2/ontologies/models/TimeseriesSyncRid.md)
- [foundry_sdk.v2.ontologies.models.TypeClass](../../../../models/v2/ontologies/models/TypeClass.md)
- [foundry_sdk.v2.ontologies.models.ValueTypeApiName](../../../../models/v2/ontologies/models/ValueTypeApiName.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/ObjectType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Page size is a request hint. Continue with the returned nextPageToken until absent; bound pages and reject a repeated token. [Local procedure](../../../../client-behavior.md).

[Part 1](list.md)
