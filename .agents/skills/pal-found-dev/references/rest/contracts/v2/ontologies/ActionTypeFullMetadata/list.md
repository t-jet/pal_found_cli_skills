# v2.ontologies.ActionTypeFullMetadata.list


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists the action types (with full metadata) for the given Ontology.

Each page may be smaller than the requested page size. However, it is guaranteed that if there are more
results available, at least one result will be present in the response.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.ActionTypeFullMetadata.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, ontology: ontologies_models.OntologyIdentifier, *, branch: typing.Optional[core_models.FoundryBranch]=None, object_type_api_names: typing.Optional[typing.List[ontologies_models.ObjectTypeApiName]]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[ontologies_models.ActionTypeFullMetadata]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to list the action types from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
| object_type_api_names | typing.Optional[typing.List[ontologies_models.ObjectTypeApiName]] | None | An set of object type api names that can be used to filter which actions are returned. Currently this only works for one object type, specifying more will cause the request to fail. |
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
'/v2/ontologies/{ontology}/actionTypesFullMetadata'
```

**query_params**

```python
{'branch': branch, 'objectTypeApiNames': object_type_api_names, 'pageSize': page_size, 'pageToken': page_token, 'preview': preview}
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
ontologies_models.ListActionTypesFullMetadataResponse
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

Ordinary sync return: `core.ResourceIterator[ontologies_models.ActionTypeFullMetadata]`. Ordinary async return: `core.AsyncResourceIterator[ontologies_models.ActionTypeFullMetadata]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[ontologies_models.ActionTypeFullMetadata] |
| sync_raw | ApiResponse[ontologies_models.ListActionTypesFullMetadataResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ListActionTypesFullMetadataResponse] |
| async_ordinary | core.AsyncResourceIterator[ontologies_models.ActionTypeFullMetadata] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ListActionTypesFullMetadataResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ListActionTypesFullMetadataResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.AnyType](../../../../models/v2/core/models/AnyType.md)
- [foundry_sdk.v2.core.models.AttachmentType](../../../../models/v2/core/models/AttachmentType.md)
- [foundry_sdk.v2.core.models.BinaryType](../../../../models/v2/core/models/BinaryType.md)
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
- [foundry_sdk.v2.core.models.GeoShapeType](../../../../models/v2/core/models/GeoShapeType.md)
- [foundry_sdk.v2.core.models.GeohashType](../../../../models/v2/core/models/GeohashType.md)
- [foundry_sdk.v2.core.models.IntegerType](../../../../models/v2/core/models/IntegerType.md)
- [foundry_sdk.v2.core.models.LmsEmbeddingModel](../../../../models/v2/core/models/LmsEmbeddingModel.md)
- [foundry_sdk.v2.core.models.LmsEmbeddingModelValue](../../../../models/v2/core/models/LmsEmbeddingModelValue.md)
- [foundry_sdk.v2.core.models.LongType](../../../../models/v2/core/models/LongType.md)
- [foundry_sdk.v2.core.models.MarkingType](../../../../models/v2/core/models/MarkingType.md)
- [foundry_sdk.v2.core.models.MarkingTypeValue](../../../../models/v2/core/models/MarkingTypeValue.md)
- [foundry_sdk.v2.core.models.MediaReferenceType](../../../../models/v2/core/models/MediaReferenceType.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.ReleaseStatus](../../../../models/v2/core/models/ReleaseStatus.md)
- [foundry_sdk.v2.core.models.ScenarioReferenceType](../../../../models/v2/core/models/ScenarioReferenceType.md)
- [foundry_sdk.v2.core.models.ShortType](../../../../models/v2/core/models/ShortType.md)
- [foundry_sdk.v2.core.models.StringType](../../../../models/v2/core/models/StringType.md)
- [foundry_sdk.v2.core.models.StructFieldName](../../../../models/v2/core/models/StructFieldName.md)
- [foundry_sdk.v2.core.models.TimestampType](../../../../models/v2/core/models/TimestampType.md)
- [foundry_sdk.v2.core.models.UnsupportedType](../../../../models/v2/core/models/UnsupportedType.md)
- [foundry_sdk.v2.core.models.UnsupportedTypeParamKey](../../../../models/v2/core/models/UnsupportedTypeParamKey.md)
- [foundry_sdk.v2.core.models.UnsupportedTypeParamValue](../../../../models/v2/core/models/UnsupportedTypeParamValue.md)
- [foundry_sdk.v2.core.models.VectorSimilarityFunction](../../../../models/v2/core/models/VectorSimilarityFunction.md)
- [foundry_sdk.v2.core.models.VectorSimilarityFunctionValue](../../../../models/v2/core/models/VectorSimilarityFunctionValue.md)
- [foundry_sdk.v2.core.models.VectorType](../../../../models/v2/core/models/VectorType.md)
- [foundry_sdk.v2.ontologies.models.ActionLogicRule](../../../../models/v2/ontologies/models/ActionLogicRule.md)
- [foundry_sdk.v2.ontologies.models.ActionParameterArrayType](../../../../models/v2/ontologies/models/ActionParameterArrayType.md)
- [foundry_sdk.v2.ontologies.models.ActionParameterType](../../../../models/v2/ontologies/models/ActionParameterType.md)
- [foundry_sdk.v2.ontologies.models.ActionParameterV2](../../../../models/v2/ontologies/models/ActionParameterV2.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeApiName](../../../../models/v2/ontologies/models/ActionTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeFullMetadata](../../../../models/v2/ontologies/models/ActionTypeFullMetadata.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeRid](../../../../models/v2/ontologies/models/ActionTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeV2](../../../../models/v2/ontologies/models/ActionTypeV2.md)
- [foundry_sdk.v2.ontologies.models.ApplyScenarioLogicRule](../../../../models/v2/ontologies/models/ApplyScenarioLogicRule.md)
- [foundry_sdk.v2.ontologies.models.ApplyScenarioRule](../../../../models/v2/ontologies/models/ApplyScenarioRule.md)
- [foundry_sdk.v2.ontologies.models.BatchedFunctionLogicRule](../../../../models/v2/ontologies/models/BatchedFunctionLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateInterfaceLinkLogicRule](../../../../models/v2/ontologies/models/CreateInterfaceLinkLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateInterfaceLogicRule](../../../../models/v2/ontologies/models/CreateInterfaceLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateInterfaceObjectRule](../../../../models/v2/ontologies/models/CreateInterfaceObjectRule.md)
- [foundry_sdk.v2.ontologies.models.CreateLinkLogicRule](../../../../models/v2/ontologies/models/CreateLinkLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateLinkRule](../../../../models/v2/ontologies/models/CreateLinkRule.md)
- [foundry_sdk.v2.ontologies.models.CreateObjectLogicRule](../../../../models/v2/ontologies/models/CreateObjectLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateObjectRule](../../../../models/v2/ontologies/models/CreateObjectRule.md)
- [foundry_sdk.v2.ontologies.models.CreateOrModifyObjectLogicRule](../../../../models/v2/ontologies/models/CreateOrModifyObjectLogicRule.md)
- [foundry_sdk.v2.ontologies.models.CreateOrModifyObjectLogicRuleV2](../../../../models/v2/ontologies/models/CreateOrModifyObjectLogicRuleV2.md)
- [foundry_sdk.v2.ontologies.models.CurrentTimeArgument](../../../../models/v2/ontologies/models/CurrentTimeArgument.md)
- [foundry_sdk.v2.ontologies.models.CurrentUserArgument](../../../../models/v2/ontologies/models/CurrentUserArgument.md)
- [foundry_sdk.v2.ontologies.models.DataValue](../../../../models/v2/ontologies/models/DataValue.md)
- [foundry_sdk.v2.ontologies.models.DeleteInterfaceLinkLogicRule](../../../../models/v2/ontologies/models/DeleteInterfaceLinkLogicRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteInterfaceObjectRule](../../../../models/v2/ontologies/models/DeleteInterfaceObjectRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteLinkLogicRule](../../../../models/v2/ontologies/models/DeleteLinkLogicRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteLinkRule](../../../../models/v2/ontologies/models/DeleteLinkRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteObjectLogicRule](../../../../models/v2/ontologies/models/DeleteObjectLogicRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteObjectRule](../../../../models/v2/ontologies/models/DeleteObjectRule.md)
- [foundry_sdk.v2.ontologies.models.FunctionLogicRule](../../../../models/v2/ontologies/models/FunctionLogicRule.md)
- [foundry_sdk.v2.ontologies.models.FunctionParameterName](../../../../models/v2/ontologies/models/FunctionParameterName.md)
- [foundry_sdk.v2.ontologies.models.FunctionRid](../../../../models/v2/ontologies/models/FunctionRid.md)
- [foundry_sdk.v2.ontologies.models.FunctionVersion](../../../../models/v2/ontologies/models/FunctionVersion.md)
- [foundry_sdk.v2.ontologies.models.InterfaceLinkTypeApiName](../../../../models/v2/ontologies/models/InterfaceLinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.InterfaceParameterPropertyArgument](../../../../models/v2/ontologies/models/InterfaceParameterPropertyArgument.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](../../../../models/v2/ontologies/models/InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ListActionTypesFullMetadataResponse](../../../../models/v2/ontologies/models/ListActionTypesFullMetadataResponse.md)
- [foundry_sdk.v2.ontologies.models.LogicRule](../../../../models/v2/ontologies/models/LogicRule.md)
- [foundry_sdk.v2.ontologies.models.LogicRuleArgument](../../../../models/v2/ontologies/models/LogicRuleArgument.md)
- [foundry_sdk.v2.ontologies.models.ModifyInterfaceLogicRule](../../../../models/v2/ontologies/models/ModifyInterfaceLogicRule.md)
- [foundry_sdk.v2.ontologies.models.ModifyInterfaceObjectRule](../../../../models/v2/ontologies/models/ModifyInterfaceObjectRule.md)
- [foundry_sdk.v2.ontologies.models.ModifyObjectLogicRule](../../../../models/v2/ontologies/models/ModifyObjectLogicRule.md)
- [foundry_sdk.v2.ontologies.models.ModifyObjectRule](../../../../models/v2/ontologies/models/ModifyObjectRule.md)
- [foundry_sdk.v2.ontologies.models.ObjectParameterPropertyArgument](../../../../models/v2/ontologies/models/ObjectParameterPropertyArgument.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeLinkTypeApiNameMapping](../../../../models/v2/ontologies/models/ObjectTypeLinkTypeApiNameMapping.md)
- [foundry_sdk.v2.ontologies.models.OntologyArrayType](../../../../models/v2/ontologies/models/OntologyArrayType.md)
- [foundry_sdk.v2.ontologies.models.OntologyDataType](../../../../models/v2/ontologies/models/OntologyDataType.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyInterfaceObjectType](../../../../models/v2/ontologies/models/OntologyInterfaceObjectType.md)
- [foundry_sdk.v2.ontologies.models.OntologyMapType](../../../../models/v2/ontologies/models/OntologyMapType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectSetType](../../../../models/v2/ontologies/models/OntologyObjectSetType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectType](../../../../models/v2/ontologies/models/OntologyObjectType.md)
- [foundry_sdk.v2.ontologies.models.OntologyObjectTypeReferenceType](../../../../models/v2/ontologies/models/OntologyObjectTypeReferenceType.md)
- [foundry_sdk.v2.ontologies.models.OntologySetType](../../../../models/v2/ontologies/models/OntologySetType.md)
- [foundry_sdk.v2.ontologies.models.OntologyStructField](../../../../models/v2/ontologies/models/OntologyStructField.md)
- [foundry_sdk.v2.ontologies.models.OntologyStructType](../../../../models/v2/ontologies/models/OntologyStructType.md)
- [foundry_sdk.v2.ontologies.models.ParameterId](../../../../models/v2/ontologies/models/ParameterId.md)
- [foundry_sdk.v2.ontologies.models.ParameterIdArgument](../../../../models/v2/ontologies/models/ParameterIdArgument.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyTypeApiName](../../../../models/v2/ontologies/models/PropertyTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.SharedPropertyTypeApiName](../../../../models/v2/ontologies/models/SharedPropertyTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.StaticArgument](../../../../models/v2/ontologies/models/StaticArgument.md)
- [foundry_sdk.v2.ontologies.models.StructFieldApiName](../../../../models/v2/ontologies/models/StructFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructFieldArgument](../../../../models/v2/ontologies/models/StructFieldArgument.md)
- [foundry_sdk.v2.ontologies.models.StructListParameterFieldArgument](../../../../models/v2/ontologies/models/StructListParameterFieldArgument.md)
- [foundry_sdk.v2.ontologies.models.StructParameterFieldApiName](../../../../models/v2/ontologies/models/StructParameterFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.StructParameterFieldArgument](../../../../models/v2/ontologies/models/StructParameterFieldArgument.md)
- [foundry_sdk.v2.ontologies.models.SynchronousWebhookOutputArgument](../../../../models/v2/ontologies/models/SynchronousWebhookOutputArgument.md)
- [foundry_sdk.v2.ontologies.models.TypeClass](../../../../models/v2/ontologies/models/TypeClass.md)
- [foundry_sdk.v2.ontologies.models.UniqueIdentifierArgument](../../../../models/v2/ontologies/models/UniqueIdentifierArgument.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/ActionTypeFullMetadata.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Page size is a request hint. Continue with the returned nextPageToken until absent; bound pages and reject a repeated token. [Local procedure](../../../../client-behavior.md).

[Part 1](list.md)
