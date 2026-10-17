# v1.ontologies.Action.validate


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Validates if an action can be run with the given set of parameters.
The response contains the evaluation of parameters and **submission criteria**
that determine if the request is `VALID` or `INVALID`.
For performance reasons, validations will not consider existing objects or other data in Foundry.
For example, the uniqueness of a primary key or the existence of a user ID will not be checked.
Note that [parameter default values](../../../../../ontology/actions.md) are not currently supported by
this endpoint. Unspecified parameters will be given a default value of `null`.

## Public Python client route

With a configured `foundry_sdk.v1.FoundryClient` named `client`, call `client.ontologies.Action.validate`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def validate(self, ontology_rid: ontologies_models.OntologyRid, action_type: ontologies_models.ActionTypeApiName, *, parameters: typing.Dict[ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]], request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ValidateActionResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology_rid | ontologies_models.OntologyRid | required | The unique Resource Identifier (RID) of the Ontology that contains the action. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. |
| action_type | ontologies_models.ActionTypeApiName | required | The API name of the action to validate. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**. |
| parameters | typing.Dict[ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]] | required | Value shape and constraints are in its referenced local type definition. |
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
'/v1/ontologies/{ontologyRid}/actions/{actionType}/validate'
```

**query_params**

```python
{}
```

**path_params**

```python
{'ontologyRid': ontology_rid, 'actionType': action_type}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.ValidateActionRequest(parameters=parameters)
```

**response_type**

```python
ontologies_models.ValidateActionResponse
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

Ordinary sync return: `ontologies_models.ValidateActionResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.ValidateActionResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ValidateActionResponse |
| sync_raw | ApiResponse[ontologies_models.ValidateActionResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ValidateActionResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.ValidateActionResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ValidateActionResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ValidateActionResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.models.DisplayName](../../../../models/v1/core/models/DisplayName.md)
- [foundry_sdk.v1.ontologies.models.ActionTypeApiName](../../../../models/v1/ontologies/models/ActionTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.ArrayEntryEvaluatedConstraint](../../../../models/v1/ontologies/models/ArrayEntryEvaluatedConstraint.md)
- [foundry_sdk.v1.ontologies.models.ArrayEvaluatedConstraint](../../../../models/v1/ontologies/models/ArrayEvaluatedConstraint.md)
- [foundry_sdk.v1.ontologies.models.ArraySizeConstraint](../../../../models/v1/ontologies/models/ArraySizeConstraint.md)
- [foundry_sdk.v1.ontologies.models.DataValue](../../../../models/v1/ontologies/models/DataValue.md)
- [foundry_sdk.v1.ontologies.models.GroupMemberConstraint](../../../../models/v1/ontologies/models/GroupMemberConstraint.md)
- [foundry_sdk.v1.ontologies.models.ObjectPropertyValueConstraint](../../../../models/v1/ontologies/models/ObjectPropertyValueConstraint.md)
- [foundry_sdk.v1.ontologies.models.ObjectQueryResultConstraint](../../../../models/v1/ontologies/models/ObjectQueryResultConstraint.md)
- [foundry_sdk.v1.ontologies.models.OneOfConstraint](../../../../models/v1/ontologies/models/OneOfConstraint.md)
- [foundry_sdk.v1.ontologies.models.OntologyRid](../../../../models/v1/ontologies/models/OntologyRid.md)
- [foundry_sdk.v1.ontologies.models.ParameterEvaluatedConstraint](../../../../models/v1/ontologies/models/ParameterEvaluatedConstraint.md)
- [foundry_sdk.v1.ontologies.models.ParameterEvaluationResult](../../../../models/v1/ontologies/models/ParameterEvaluationResult.md)
- [foundry_sdk.v1.ontologies.models.ParameterId](../../../../models/v1/ontologies/models/ParameterId.md)
- [foundry_sdk.v1.ontologies.models.ParameterOption](../../../../models/v1/ontologies/models/ParameterOption.md)
- [foundry_sdk.v1.ontologies.models.RangeConstraint](../../../../models/v1/ontologies/models/RangeConstraint.md)
- [foundry_sdk.v1.ontologies.models.StringLengthConstraint](../../../../models/v1/ontologies/models/StringLengthConstraint.md)
- [foundry_sdk.v1.ontologies.models.StringRegexMatchConstraint](../../../../models/v1/ontologies/models/StringRegexMatchConstraint.md)
- [foundry_sdk.v1.ontologies.models.StructEvaluatedConstraint](../../../../models/v1/ontologies/models/StructEvaluatedConstraint.md)
- [foundry_sdk.v1.ontologies.models.StructFieldEvaluatedConstraint](../../../../models/v1/ontologies/models/StructFieldEvaluatedConstraint.md)
- [foundry_sdk.v1.ontologies.models.StructFieldEvaluationResult](../../../../models/v1/ontologies/models/StructFieldEvaluationResult.md)
- [foundry_sdk.v1.ontologies.models.StructParameterFieldApiName](../../../../models/v1/ontologies/models/StructParameterFieldApiName.md)
- [foundry_sdk.v1.ontologies.models.SubmissionCriteriaEvaluation](../../../../models/v1/ontologies/models/SubmissionCriteriaEvaluation.md)
- [foundry_sdk.v1.ontologies.models.UnevaluableConstraint](../../../../models/v1/ontologies/models/UnevaluableConstraint.md)
- [foundry_sdk.v1.ontologies.models.ValidateActionRequest](../../../../models/v1/ontologies/models/ValidateActionRequest.md)
- [foundry_sdk.v1.ontologies.models.ValidateActionResponse](../../../../models/v1/ontologies/models/ValidateActionResponse.md)
- [foundry_sdk.v1.ontologies.models.ValidationResult](../../../../models/v1/ontologies/models/ValidationResult.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/Action.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Check every required Action input explicitly. This endpoint does not apply Action parameter defaults. [Local procedure](../../../../../ontology/actions.md).

[Part 1](validate.md)
