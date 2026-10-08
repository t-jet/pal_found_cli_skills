# v2.ontologies.ActionType.get_by_rid


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Gets a specific action type with the given RID.

## SDK invocation contract

```python
def get_by_rid(self, ontology: ontologies_models.OntologyIdentifier, action_type_rid: ontologies_models.ActionTypeRid, *, branch: typing.Optional[core_models.FoundryBranch]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ActionTypeV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| action_type_rid | ontologies_models.ActionTypeRid | required | The RID of the action type. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to load the action type definition from. If not specified, the default branch will be used. Branches are an experimental feature and not all workflows are supported. |
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
'/v2/ontologies/{ontology}/actionTypes/byRid/{actionTypeRid}'
```

**query_params**

```python
{'branch': branch}
```

**path_params**

```python
{'ontology': ontology, 'actionTypeRid': action_type_rid}
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
ontologies_models.ActionTypeV2
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

Ordinary sync return: `ontologies_models.ActionTypeV2`. Ordinary async return: `typing.Awaitable[ontologies_models.ActionTypeV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ActionTypeV2 |
| sync_raw | ApiResponse[ontologies_models.ActionTypeV2] |
| sync_streaming | StreamingContextManager[ontologies_models.ActionTypeV2] |
| async_ordinary | typing.Awaitable[ontologies_models.ActionTypeV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ActionTypeV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ActionTypeV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
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
- [foundry_sdk.v2.ontologies.models.ActionParameterArrayType](../../../../models/v2/ontologies/models/ActionParameterArrayType.md)
- [foundry_sdk.v2.ontologies.models.ActionParameterType](../../../../models/v2/ontologies/models/ActionParameterType.md)
- [foundry_sdk.v2.ontologies.models.ActionParameterV2](../../../../models/v2/ontologies/models/ActionParameterV2.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeApiName](../../../../models/v2/ontologies/models/ActionTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeRid](../../../../models/v2/ontologies/models/ActionTypeRid.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeV2](../../../../models/v2/ontologies/models/ActionTypeV2.md)
- [foundry_sdk.v2.ontologies.models.ApplyScenarioRule](../../../../models/v2/ontologies/models/ApplyScenarioRule.md)
- [foundry_sdk.v2.ontologies.models.CreateInterfaceObjectRule](../../../../models/v2/ontologies/models/CreateInterfaceObjectRule.md)
- [foundry_sdk.v2.ontologies.models.CreateLinkRule](../../../../models/v2/ontologies/models/CreateLinkRule.md)
- [foundry_sdk.v2.ontologies.models.CreateObjectRule](../../../../models/v2/ontologies/models/CreateObjectRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteInterfaceObjectRule](../../../../models/v2/ontologies/models/DeleteInterfaceObjectRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteLinkRule](../../../../models/v2/ontologies/models/DeleteLinkRule.md)
- [foundry_sdk.v2.ontologies.models.DeleteObjectRule](../../../../models/v2/ontologies/models/DeleteObjectRule.md)
- [foundry_sdk.v2.ontologies.models.InterfaceTypeApiName](../../../../models/v2/ontologies/models/InterfaceTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.LogicRule](../../../../models/v2/ontologies/models/LogicRule.md)
- [foundry_sdk.v2.ontologies.models.ModifyInterfaceObjectRule](../../../../models/v2/ontologies/models/ModifyInterfaceObjectRule.md)
- [foundry_sdk.v2.ontologies.models.ModifyObjectRule](../../../../models/v2/ontologies/models/ModifyObjectRule.md)
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
- [foundry_sdk.v2.ontologies.models.TypeClass](../../../../models/v2/ontologies/models/TypeClass.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/ActionType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_by_rid.md)
