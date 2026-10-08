# v2.ontologies.Action.apply


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Applies an action using the given parameters.

Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

Note that a 200 HTTP status code only indicates that the request was received and processed by the server.
See the validation result in the response body to determine if the action was applied successfully.

Note that [parameter default values](../../../../../ontology/actions.md) are not currently supported by
this endpoint.

## SDK invocation contract

```python
def apply(self, ontology: ontologies_models.OntologyIdentifier, action: ontologies_models.ActionTypeApiName, *, parameters: typing.Dict[ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]], branch: typing.Optional[core_models.FoundryBranch]=None, options: typing.Optional[ontologies_models.ApplyActionRequestOptions]=None, scenario_rid: typing.Optional[ontologies_models.OntologyScenarioRid]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, trace_parent: typing.Optional[core_models.TraceParent]=None, trace_state: typing.Optional[core_models.TraceState]=None, transaction_id: typing.Optional[ontologies_models.OntologyTransactionId]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.SyncApplyActionResponseV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| action | ontologies_models.ActionTypeApiName | required | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**. |
| parameters | typing.Dict[ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]] | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to apply the action against. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. |
| options | typing.Optional[ontologies_models.ApplyActionRequestOptions] | None | Value shape and constraints are in its referenced local type definition. |
| scenario_rid | typing.Optional[ontologies_models.OntologyScenarioRid] | None | The resource identifier of an ontology scenario to apply the action against. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package rid of the generated SDK. |
| sdk_version | typing.Optional[ontologies_models.SdkVersion] | None | The version of the generated SDK. |
| trace_parent | typing.Optional[core_models.TraceParent] | None | The W3C trace parent header included in the request. |
| trace_state | typing.Optional[core_models.TraceState] | None | The W3C trace state header included in the request. |
| transaction_id | typing.Optional[ontologies_models.OntologyTransactionId] | None | The ID of an Ontology transaction to apply the action against. Transactions are an experimental feature and all workflows may not be supported. |
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
'/v2/ontologies/{ontology}/actions/{action}/apply'
```

**query_params**

```python
{'branch': branch, 'scenarioRid': scenario_rid, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version, 'transactionId': transaction_id}
```

**path_params**

```python
{'ontology': ontology, 'action': action}
```

**header_params**

```python
{'traceParent': trace_parent, 'traceState': trace_state, 'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.ApplyActionRequestV2(options=options, parameters=parameters)
```

**response_type**

```python
ontologies_models.SyncApplyActionResponseV2
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

Ordinary sync return: `ontologies_models.SyncApplyActionResponseV2`. Ordinary async return: `typing.Awaitable[ontologies_models.SyncApplyActionResponseV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.SyncApplyActionResponseV2 |
| sync_raw | ApiResponse[ontologies_models.SyncApplyActionResponseV2] |
| sync_streaming | StreamingContextManager[ontologies_models.SyncApplyActionResponseV2] |
| async_ordinary | typing.Awaitable[ontologies_models.SyncApplyActionResponseV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.SyncApplyActionResponseV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.SyncApplyActionResponseV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.DisplayName](../../../../models/v2/core/models/DisplayName.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.core.models.TraceParent](../../../../models/v2/core/models/TraceParent.md)
- [foundry_sdk.v2.core.models.TraceState](../../../../models/v2/core/models/TraceState.md)
- [foundry_sdk.v2.ontologies.models.ActionResults](../../../../models/v2/ontologies/models/ActionResults.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeApiName](../../../../models/v2/ontologies/models/ActionTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.AddLink](../../../../models/v2/ontologies/models/AddLink.md)
- [foundry_sdk.v2.ontologies.models.AddObject](../../../../models/v2/ontologies/models/AddObject.md)
- [foundry_sdk.v2.ontologies.models.ApplyActionMode](../../../../models/v2/ontologies/models/ApplyActionMode.md)
- [foundry_sdk.v2.ontologies.models.ApplyActionRequestOptions](../../../../models/v2/ontologies/models/ApplyActionRequestOptions.md)
- [foundry_sdk.v2.ontologies.models.ApplyActionRequestV2](../../../../models/v2/ontologies/models/ApplyActionRequestV2.md)
- [foundry_sdk.v2.ontologies.models.ArrayEntryEvaluatedConstraint](../../../../models/v2/ontologies/models/ArrayEntryEvaluatedConstraint.md)
- [foundry_sdk.v2.ontologies.models.ArrayEvaluatedConstraint](../../../../models/v2/ontologies/models/ArrayEvaluatedConstraint.md)
- [foundry_sdk.v2.ontologies.models.ArraySizeConstraint](../../../../models/v2/ontologies/models/ArraySizeConstraint.md)
- [foundry_sdk.v2.ontologies.models.DataValue](../../../../models/v2/ontologies/models/DataValue.md)
- [foundry_sdk.v2.ontologies.models.DeleteLink](../../../../models/v2/ontologies/models/DeleteLink.md)
- [foundry_sdk.v2.ontologies.models.DeleteObject](../../../../models/v2/ontologies/models/DeleteObject.md)
- [foundry_sdk.v2.ontologies.models.GroupMemberConstraint](../../../../models/v2/ontologies/models/GroupMemberConstraint.md)
- [foundry_sdk.v2.ontologies.models.LinkSideObject](../../../../models/v2/ontologies/models/LinkSideObject.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ModifyObject](../../../../models/v2/ontologies/models/ModifyObject.md)
- [foundry_sdk.v2.ontologies.models.ObjectEdit](../../../../models/v2/ontologies/models/ObjectEdit.md)
- [foundry_sdk.v2.ontologies.models.ObjectEdits](../../../../models/v2/ontologies/models/ObjectEdits.md)
- [foundry_sdk.v2.ontologies.models.ObjectPropertyValueConstraint](../../../../models/v2/ontologies/models/ObjectPropertyValueConstraint.md)
- [foundry_sdk.v2.ontologies.models.ObjectQueryResultConstraint](../../../../models/v2/ontologies/models/ObjectQueryResultConstraint.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeEdits](../../../../models/v2/ontologies/models/ObjectTypeEdits.md)
- [foundry_sdk.v2.ontologies.models.OneOfConstraint](../../../../models/v2/ontologies/models/OneOfConstraint.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyScenarioRid](../../../../models/v2/ontologies/models/OntologyScenarioRid.md)
- [foundry_sdk.v2.ontologies.models.OntologyTransactionId](../../../../models/v2/ontologies/models/OntologyTransactionId.md)
- [foundry_sdk.v2.ontologies.models.ParameterEvaluatedConstraint](../../../../models/v2/ontologies/models/ParameterEvaluatedConstraint.md)
- [foundry_sdk.v2.ontologies.models.ParameterEvaluationResult](../../../../models/v2/ontologies/models/ParameterEvaluationResult.md)
- [foundry_sdk.v2.ontologies.models.ParameterId](../../../../models/v2/ontologies/models/ParameterId.md)
- [foundry_sdk.v2.ontologies.models.ParameterOption](../../../../models/v2/ontologies/models/ParameterOption.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](../../../../models/v2/ontologies/models/PropertyValue.md)
- [foundry_sdk.v2.ontologies.models.RangeConstraint](../../../../models/v2/ontologies/models/RangeConstraint.md)
- [foundry_sdk.v2.ontologies.models.ReturnEditsMode](../../../../models/v2/ontologies/models/ReturnEditsMode.md)
- [foundry_sdk.v2.ontologies.models.SdkPackageRid](../../../../models/v2/ontologies/models/SdkPackageRid.md)
- [foundry_sdk.v2.ontologies.models.SdkVersion](../../../../models/v2/ontologies/models/SdkVersion.md)
- [foundry_sdk.v2.ontologies.models.StringLengthConstraint](../../../../models/v2/ontologies/models/StringLengthConstraint.md)
- [foundry_sdk.v2.ontologies.models.StringRegexMatchConstraint](../../../../models/v2/ontologies/models/StringRegexMatchConstraint.md)
- [foundry_sdk.v2.ontologies.models.StructEvaluatedConstraint](../../../../models/v2/ontologies/models/StructEvaluatedConstraint.md)
- [foundry_sdk.v2.ontologies.models.StructFieldEvaluatedConstraint](../../../../models/v2/ontologies/models/StructFieldEvaluatedConstraint.md)
- [foundry_sdk.v2.ontologies.models.StructFieldEvaluationResult](../../../../models/v2/ontologies/models/StructFieldEvaluationResult.md)
- [foundry_sdk.v2.ontologies.models.StructParameterFieldApiName](../../../../models/v2/ontologies/models/StructParameterFieldApiName.md)
- [foundry_sdk.v2.ontologies.models.SubmissionCriteriaEvaluation](../../../../models/v2/ontologies/models/SubmissionCriteriaEvaluation.md)
- [foundry_sdk.v2.ontologies.models.SyncApplyActionResponseV2](../../../../models/v2/ontologies/models/SyncApplyActionResponseV2.md)
- [foundry_sdk.v2.ontologies.models.UnevaluableConstraint](../../../../models/v2/ontologies/models/UnevaluableConstraint.md)
- [foundry_sdk.v2.ontologies.models.ValidateActionResponseV2](../../../../models/v2/ontologies/models/ValidateActionResponseV2.md)
- [foundry_sdk.v2.ontologies.models.ValidationResult](../../../../models/v2/ontologies/models/ValidationResult.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/Action.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Check every required Action input explicitly. This endpoint does not apply Action parameter defaults. [Local procedure](../../../../../ontology/actions.md).

[Part 1](apply.md)
