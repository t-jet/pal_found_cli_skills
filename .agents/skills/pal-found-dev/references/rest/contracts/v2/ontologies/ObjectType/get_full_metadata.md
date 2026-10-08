# v2.ontologies.ObjectType.get_full_metadata


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets the full metadata for a specific object type with the given API name.

## SDK invocation contract

```python
def get_full_metadata(self, ontology: ontologies_models.OntologyIdentifier, object_type: ontologies_models.ObjectTypeApiName, *, branch: typing.Optional[core_models.FoundryBranch]=None, include_datasources: typing.Optional[bool]=None, preview: typing.Optional[core_models.PreviewMode]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ObjectTypeFullMetadata: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type. To find the API name, use the **List object types** endpoint or check the **Ontology Manager**. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
| include_datasources | typing.Optional[bool] | None | When set to `true`, the `datasources` field on the returned object type is populated with the datasources backing it. Defaults to `false`. |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package rid of the generated SDK. |
| sdk_version | typing.Optional[ontologies_models.SdkVersion] | None | The version of the generated SDK. |
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
'/v2/ontologies/{ontology}/objectTypes/{objectType}/fullMetadata'
```

**query_params**

```python
{'branch': branch, 'includeDatasources': include_datasources, 'preview': preview, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version}
```

**path_params**

```python
{'ontology': ontology, 'objectType': object_type}
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
ontologies_models.ObjectTypeFullMetadata
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

Ordinary sync return: `ontologies_models.ObjectTypeFullMetadata`. Ordinary async return: `typing.Awaitable[ontologies_models.ObjectTypeFullMetadata]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ObjectTypeFullMetadata |
| sync_raw | ApiResponse[ontologies_models.ObjectTypeFullMetadata] |
| sync_streaming | StreamingContextManager[ontologies_models.ObjectTypeFullMetadata] |
| async_ordinary | typing.Awaitable[ontologies_models.ObjectTypeFullMetadata] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ObjectTypeFullMetadata]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ObjectTypeFullMetadata]] |

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
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
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
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeApiName](../../../../models/v2/ontologies/models/InterfaceLinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyApiName](../../../../models/v2/ontologies/models/InterfacePropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyLocalPropertyImplementation](../../../../models/v2/ontologies/models/InterfacePropertyLocalPropertyImplementation.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyReducedPropertyImplementation](../../../../models/v2/ontologies/models/InterfacePropertyReducedPropertyImplementation.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyStructFieldImplementation](../../../../models/v2/ontologies/models/InterfacePropertyStructFieldImplementation.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyStructImplementation](../../../../models/v2/ontologies/models/InterfacePropertyStructImplementation.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyStructImplementationMapping](../../../../models/v2/ontologies/models/InterfacePropertyStructImplementationMapping.md)
- [foundry_sdk.v2.ontologies.models.InterfacePropertyTypeImplementation](../../../../models/v2/ontologies/models/InterfacePropertyTypeImplementation.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](../../../../models/v2/ontologies/models/InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeRid](../../../../models/v2/ontologies/models/InterfaceTypeRid.md)
- [foundry_sdk.v2.ontologies.models.KnownType](../../../../models/v2/ontologies/models/KnownType.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeRid](../../../../models/v2/ontologies/models/LinkTypeRid.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeSideCardinality](../../../../models/v2/ontologies/models/LinkTypeSideCardinality.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeSideV2](../../../../models/v2/ontologies/models/LinkTypeSideV2.md)
- [foundry_sdk.v2.ontologies.models.NestedInterfacePropertyTypeImplementation](../../../../models/v2/ontologies/models/NestedInterfacePropertyTypeImplementation.md)
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
- [foundry_sdk.v2.ontologies.models.ObjectTypeFullMetadata](../../../../models/v2/ontologies/models/ObjectTypeFullMetadata.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeGeotimeSeriesDatasource](../../../../models/v2/ontologies/models/ObjectTypeGeotimeSeriesDatasource.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeInterfaceImplementation](../../../../models/v2/ontologies/models/ObjectTypeInterfaceImplementation.md)
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
- [foundry_sdk.v2.ontologies.models.PropertyImplementation](../../../../models/v2/ontologies/models/PropertyImplementation.md)
- [foundry_sdk.v2.ontologies.models.PropertyKnownTypeFormattingRule](../../../../models/v2/ontologies/models/PropertyKnownTypeFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyNumberFormattingRule](../../../../models/v2/ontologies/models/PropertyNumberFormattingRule.md)
- [foundry_sdk.v2.ontologies.models.PropertyNumberFormattingRuleType](../../../../models/v2/ontologies/models/PropertyNumberFormattingRuleType.md)
- [foundry_sdk.v2.ontologies.models.PropertyOrStructFieldOfPropertyImplementation](../../../../models/v2/ontologies/models/PropertyOrStructFieldOfPropertyImplementation.md)
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
- [foundry_sdk.v2.ontologies.models.SdkPackageRid](../../../../models/v2/ontologies/models/SdkPackageRid.md)
- [foundry_sdk.v2.ontologies.models.SdkVersion](../../../../models/v2/ontologies/models/SdkVersion.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeApiName](../../../../models/v2/ontologies/models/SharedPropertyTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.StreamRid](../../../../models/v2/ontologies/models/StreamRid.md)
- [foundry_sdk.v2.ontologies.models.StringConstant](../../../../models/v2/ontologies/models/StringConstant.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](../../../../models/v2/ontologies/models/StructFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldOfPropertyImplementation](../../../../models/v2/ontologies/models/StructFieldOfPropertyImplementation.md)
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

[Part 1](get_full_metadata.md) | [Part 2](get_full_metadata-2.md)
