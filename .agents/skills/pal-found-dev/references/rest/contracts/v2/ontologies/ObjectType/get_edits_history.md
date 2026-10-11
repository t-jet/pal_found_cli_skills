# v2.ontologies.ObjectType.get_edits_history


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Returns the history of edits (additions, modifications, deletions) for objects of a
specific object type. This endpoint provides visibility into all actions that have
modified objects of this type.

The edits are returned in reverse chronological order (most recent first) by default.

Note that filters are ignored for OSv1 object types.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.Ontology.ObjectType.get_edits_history`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_edits_history(self, ontology: ontologies_models.OntologyIdentifier, object_type: ontologies_models.ObjectTypeApiName, *, branch: typing.Optional[core_models.FoundryBranch]=None, filters: typing.Optional[ontologies_models.EditsHistoryFilter]=None, include_all_previous_properties: typing.Optional[bool]=None, object_primary_key: typing.Optional[ontologies_models.ObjectPrimaryKeyV2]=None, page_size: typing.Optional[int]=None, page_token: typing.Optional[str]=None, preview: typing.Optional[core_models.PreviewMode]=None, scenario_rid: typing.Optional[ontologies_models.OntologyScenarioRid]=None, sort_order: typing.Optional[ontologies_models.EditsHistorySortOrder]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ObjectTypeEditsHistoryResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | The ontology RID or API name |
| object_type | ontologies_models.ObjectTypeApiName | required | The API name of the object type |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch from which we will get edits history. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. |
| filters | typing.Optional[ontologies_models.EditsHistoryFilter] | None | Value shape and constraints are in its referenced local type definition. |
| include_all_previous_properties | typing.Optional[bool] | None | Value shape and constraints are in its referenced local type definition. |
| object_primary_key | typing.Optional[ontologies_models.ObjectPrimaryKeyV2] | None | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[int] | None | The maximum number of edits to return per page. Defaults to 100. |
| page_token | typing.Optional[str] | None | Token for retrieving the next page of results |
| preview | typing.Optional[core_models.PreviewMode] | None | A boolean flag that, when set to true, enables the use of beta features in preview mode. |
| scenario_rid | typing.Optional[ontologies_models.OntologyScenarioRid] | None | The resource identifier of an ontology scenario to get edits history from. |
| sort_order | typing.Optional[ontologies_models.EditsHistorySortOrder] | None | Value shape and constraints are in its referenced local type definition. |
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
'/v2/ontologies/{ontology}/objectTypes/{objectType}/editsHistory'
```

**query_params**

```python
{'branch': branch, 'preview': preview, 'scenarioRid': scenario_rid}
```

**path_params**

```python
{'ontology': ontology, 'objectType': object_type}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.ObjectTypeEditsHistoryRequest(object_primary_key=object_primary_key, filters=filters, sort_order=sort_order, include_all_previous_properties=include_all_previous_properties, page_size=page_size, page_token=page_token)
```

**response_type**

```python
ontologies_models.ObjectTypeEditsHistoryResponse
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

Ordinary sync return: `ontologies_models.ObjectTypeEditsHistoryResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.ObjectTypeEditsHistoryResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ObjectTypeEditsHistoryResponse |
| sync_raw | ApiResponse[ontologies_models.ObjectTypeEditsHistoryResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ObjectTypeEditsHistoryResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.ObjectTypeEditsHistoryResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ObjectTypeEditsHistoryResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ObjectTypeEditsHistoryResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.ontologies.models.ActionRid](../../../../models/v2/ontologies/models/ActionRid.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeRid](../../../../models/v2/ontologies/models/ActionTypeRid.md)
- [foundry_sdk.v2.ontologies.models.BooleanValue](../../../../models/v2/ontologies/models/BooleanValue.md)
- [foundry_sdk.v2.ontologies.models.CreateEdit](../../../../models/v2/ontologies/models/CreateEdit.md)
- [foundry_sdk.v2.ontologies.models.DateValue](../../../../models/v2/ontologies/models/DateValue.md)
- [foundry_sdk.v2.ontologies.models.DeleteEdit](../../../../models/v2/ontologies/models/DeleteEdit.md)
- [foundry_sdk.v2.ontologies.models.DoubleValue](../../../../models/v2/ontologies/models/DoubleValue.md)
- [foundry_sdk.v2.ontologies.models.EditHistoryEdit](../../../../models/v2/ontologies/models/EditHistoryEdit.md)
- [foundry_sdk.v2.ontologies.models.EditsHistoryFilter](../../../../models/v2/ontologies/models/EditsHistoryFilter.md)
- [foundry_sdk.v2.ontologies.models.EditsHistoryOperationIdsFilter](../../../../models/v2/ontologies/models/EditsHistoryOperationIdsFilter.md)
- [foundry_sdk.v2.ontologies.models.EditsHistorySortOrder](../../../../models/v2/ontologies/models/EditsHistorySortOrder.md)
- [foundry_sdk.v2.ontologies.models.EditsHistoryTimestampFilter](../../../../models/v2/ontologies/models/EditsHistoryTimestampFilter.md)
- [foundry_sdk.v2.ontologies.models.IntegerValue](../../../../models/v2/ontologies/models/IntegerValue.md)
- [foundry_sdk.v2.ontologies.models.LongValue](../../../../models/v2/ontologies/models/LongValue.md)
- [foundry_sdk.v2.ontologies.models.ModifyEdit](../../../../models/v2/ontologies/models/ModifyEdit.md)
- [foundry_sdk.v2.ontologies.models.ObjectEditHistoryEntry](../../../../models/v2/ontologies/models/ObjectEditHistoryEntry.md)
- [foundry_sdk.v2.ontologies.models.ObjectPrimaryKeyV2](../../../../models/v2/ontologies/models/ObjectPrimaryKeyV2.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeEditsHistoryRequest](../../../../models/v2/ontologies/models/ObjectTypeEditsHistoryRequest.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeEditsHistoryResponse](../../../../models/v2/ontologies/models/ObjectTypeEditsHistoryResponse.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyScenarioRid](../../../../models/v2/ontologies/models/OntologyScenarioRid.md)
- [foundry_sdk.v2.ontologies.models.PrimaryKeyValueV2](../../../../models/v2/ontologies/models/PrimaryKeyValueV2.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](../../../../models/v2/ontologies/models/PropertyValue.md)
- [foundry_sdk.v2.ontologies.models.StringValue](../../../../models/v2/ontologies/models/StringValue.md)
- [foundry_sdk.v2.ontologies.models.TimestampValue](../../../../models/v2/ontologies/models/TimestampValue.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/ObjectType.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_edits_history.md)
