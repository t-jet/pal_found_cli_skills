# v1.ontologies.Action.apply


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Applies an action using the given parameters.

Changes to objects or links stored in Object Storage V1 are eventually consistent and may take some time to be visible.
Edits to objects or links in Object Storage V2 will be visible immediately after the action completes.

Note that [parameter default values](../../../../../ontology/actions.md) are not currently supported by
this endpoint.

## Public Python client route

With a configured `foundry_sdk.v1.FoundryClient` named `client`, call `client.ontologies.Action.apply`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def apply(self, ontology_rid: ontologies_models.OntologyRid, action_type: ontologies_models.ActionTypeApiName, *, parameters: typing.Dict[ontologies_models.ParameterId, typing.Optional[ontologies_models.DataValue]], request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.ApplyActionResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology_rid | ontologies_models.OntologyRid | required | The unique Resource Identifier (RID) of the Ontology that contains the action. To look up your Ontology RID, please use the **List ontologies** endpoint or check the **Ontology Manager**. |
| action_type | ontologies_models.ActionTypeApiName | required | The API name of the action to apply. To find the API name for your action, use the **List action types** endpoint or check the **Ontology Manager**. |
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
'/v1/ontologies/{ontologyRid}/actions/{actionType}/apply'
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
ontologies_models.ApplyActionRequest(parameters=parameters)
```

**response_type**

```python
ontologies_models.ApplyActionResponse
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

Ordinary sync return: `ontologies_models.ApplyActionResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.ApplyActionResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.ApplyActionResponse |
| sync_raw | ApiResponse[ontologies_models.ApplyActionResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.ApplyActionResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.ApplyActionResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.ApplyActionResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.ApplyActionResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.ontologies.models.ActionTypeApiName](../../../../models/v1/ontologies/models/ActionTypeApiName.md)
- [foundry_sdk.v1.ontologies.models.ApplyActionRequest](../../../../models/v1/ontologies/models/ApplyActionRequest.md)
- [foundry_sdk.v1.ontologies.models.ApplyActionResponse](../../../../models/v1/ontologies/models/ApplyActionResponse.md)
- [foundry_sdk.v1.ontologies.models.DataValue](../../../../models/v1/ontologies/models/DataValue.md)
- [foundry_sdk.v1.ontologies.models.OntologyRid](../../../../models/v1/ontologies/models/OntologyRid.md)
- [foundry_sdk.v1.ontologies.models.ParameterId](../../../../models/v1/ontologies/models/ParameterId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/ontologies/Action.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Check every required Action input explicitly. This endpoint does not apply Action parameter defaults. [Local procedure](../../../../../ontology/actions.md).

[Part 1](apply.md)
