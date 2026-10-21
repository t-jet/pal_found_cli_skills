# v2.ontologies.Action.apply_batch


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Applies multiple actions (of the same Action Type) using the given parameters.

Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

Up to 20 actions may be applied in one call. Actions that only modify objects in Object Storage v2 and do not
call Functions may receive a higher limit.

Note that [notifications](../../../../../ontology/actions.md) are not currently supported by this endpoint.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.Action.apply_batch`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def apply_batch(self, ontology: ontologies_models.OntologyIdentifier, action: ontologies_models.ActionTypeApiName, *, requests: typing.List[ontologies_models.BatchApplyActionRequestItem], branch: typing.Optional[core_models.FoundryBranch]=None, options: typing.Optional[ontologies_models.BatchApplyActionRequestOptions]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.BatchApplyActionResponseV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| action | ontologies_models.ActionTypeApiName | required | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**. |
| requests | typing.List[ontologies_models.BatchApplyActionRequestItem] | required | Value shape and constraints are in its referenced local type definition. |
| branch | typing.Optional[core_models.FoundryBranch] | None | The Foundry branch to apply the action against. If not specified, the default branch is used. Branches are an experimental feature and not all workflows are supported. |
| options | typing.Optional[ontologies_models.BatchApplyActionRequestOptions] | None | Value shape and constraints are in its referenced local type definition. |
| sdk_package_rid | typing.Optional[ontologies_models.SdkPackageRid] | None | The package rid of the generated SDK. |
| sdk_version | typing.Optional[ontologies_models.SdkVersion] | None | The version of the generated SDK. |
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
'/v2/ontologies/{ontology}/actions/{action}/applyBatch'
```

**query_params**

```python
{'branch': branch, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version}
```

**path_params**

```python
{'ontology': ontology, 'action': action}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.BatchApplyActionRequestV2(options=options, requests=requests)
```

**response_type**

```python
ontologies_models.BatchApplyActionResponseV2
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

Ordinary sync return: `ontologies_models.BatchApplyActionResponseV2`. Ordinary async return: `typing.Awaitable[ontologies_models.BatchApplyActionResponseV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.BatchApplyActionResponseV2 |
| sync_raw | ApiResponse[ontologies_models.BatchApplyActionResponseV2] |
| sync_streaming | StreamingContextManager[ontologies_models.BatchApplyActionResponseV2] |
| async_ordinary | typing.Awaitable[ontologies_models.BatchApplyActionResponseV2] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.BatchApplyActionResponseV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.BatchApplyActionResponseV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.FoundryBranch](../../../../models/v2/core/models/FoundryBranch.md)
- [foundry_sdk.v2.ontologies.models.ActionTypeApiName](../../../../models/v2/ontologies/models/ActionTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.AddLink](../../../../models/v2/ontologies/models/AddLink.md)
- [foundry_sdk.v2.ontologies.models.AddObject](../../../../models/v2/ontologies/models/AddObject.md)
- [foundry_sdk.v2.ontologies.models.BatchActionObjectEdit](../../../../models/v2/ontologies/models/BatchActionObjectEdit.md)
- [foundry_sdk.v2.ontologies.models.BatchActionObjectEdits](../../../../models/v2/ontologies/models/BatchActionObjectEdits.md)
- [foundry_sdk.v2.ontologies.models.BatchActionResults](../../../../models/v2/ontologies/models/BatchActionResults.md)
- [foundry_sdk.v2.ontologies.models.BatchApplyActionRequestItem](../../../../models/v2/ontologies/models/BatchApplyActionRequestItem.md)
- [foundry_sdk.v2.ontologies.models.BatchApplyActionRequestOptions](../../../../models/v2/ontologies/models/BatchApplyActionRequestOptions.md)
- [foundry_sdk.v2.ontologies.models.BatchApplyActionRequestV2](../../../../models/v2/ontologies/models/BatchApplyActionRequestV2.md)
- [foundry_sdk.v2.ontologies.models.BatchApplyActionResponseV2](../../../../models/v2/ontologies/models/BatchApplyActionResponseV2.md)
- [foundry_sdk.v2.ontologies.models.BatchReturnEditsMode](../../../../models/v2/ontologies/models/BatchReturnEditsMode.md)
- [foundry_sdk.v2.ontologies.models.DataValue](../../../../models/v2/ontologies/models/DataValue.md)
- [foundry_sdk.v2.ontologies.models.LinkSideObject](../../../../models/v2/ontologies/models/LinkSideObject.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ModifyObject](../../../../models/v2/ontologies/models/ModifyObject.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeEdits](../../../../models/v2/ontologies/models/ObjectTypeEdits.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.ParameterId](../../../../models/v2/ontologies/models/ParameterId.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](../../../../models/v2/ontologies/models/PropertyValue.md)
- [foundry_sdk.v2.ontologies.models.SdkPackageRid](../../../../models/v2/ontologies/models/SdkPackageRid.md)
- [foundry_sdk.v2.ontologies.models.SdkVersion](../../../../models/v2/ontologies/models/SdkVersion.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/Action.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- This endpoint does not trigger Action notifications; design notification behavior separately when required. [Local procedure](../../../../../ontology/actions.md).

[Part 1](apply_batch.md)
