# v2.ontologies.OntologyTransaction.post_edits


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Applies a set of edits to a transaction in order.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.ontologies.OntologyTransaction.post_edits`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def post_edits(self, ontology: ontologies_models.OntologyIdentifier, transaction_id: ontologies_models.OntologyTransactionId, *, edits: typing.List[ontologies_models.TransactionEdit], preview: typing.Optional[core_models.PreviewMode]=None, sdk_package_rid: typing.Optional[ontologies_models.SdkPackageRid]=None, sdk_version: typing.Optional[ontologies_models.SdkVersion]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> ontologies_models.PostTransactionEditsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| ontology | ontologies_models.OntologyIdentifier | required | Value shape and constraints are in its referenced local type definition. |
| transaction_id | ontologies_models.OntologyTransactionId | required | The ID of the transaction to apply edits to. Transactions are an experimental feature and all workflows may not be supported. |
| edits | typing.List[ontologies_models.TransactionEdit] | required | Value shape and constraints are in its referenced local type definition. |
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
'POST'
```

**resource_path**

```python
'/v2/ontologies/{ontology}/transactions/{transactionId}/edits'
```

**query_params**

```python
{'preview': preview, 'sdkPackageRid': sdk_package_rid, 'sdkVersion': sdk_version}
```

**path_params**

```python
{'ontology': ontology, 'transactionId': transaction_id}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
ontologies_models.PostTransactionEditsRequest(edits=edits)
```

**response_type**

```python
ontologies_models.PostTransactionEditsResponse
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

Ordinary sync return: `ontologies_models.PostTransactionEditsResponse`. Ordinary async return: `typing.Awaitable[ontologies_models.PostTransactionEditsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | ontologies_models.PostTransactionEditsResponse |
| sync_raw | ApiResponse[ontologies_models.PostTransactionEditsResponse] |
| sync_streaming | StreamingContextManager[ontologies_models.PostTransactionEditsResponse] |
| async_ordinary | typing.Awaitable[ontologies_models.PostTransactionEditsResponse] |
| async_raw | Awaitable[AsyncApiResponse[ontologies_models.PostTransactionEditsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[ontologies_models.PostTransactionEditsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.ontologies.models.AddLinkEdit](../../../../models/v2/ontologies/models/AddLinkEdit.md)
- [foundry_sdk.v2.ontologies.models.AddObjectEdit](../../../../models/v2/ontologies/models/AddObjectEdit.md)
- [foundry_sdk.v2.ontologies.models.DataValue](../../../../models/v2/ontologies/models/DataValue.md)
- [foundry_sdk.v2.ontologies.models.DeleteLinkEdit](../../../../models/v2/ontologies/models/DeleteLinkEdit.md)
- [foundry_sdk.v2.ontologies.models.DeleteObjectEdit](../../../../models/v2/ontologies/models/DeleteObjectEdit.md)
- [foundry_sdk.v2.ontologies.models.LinkTypeApiName](../../../../models/v2/ontologies/models/LinkTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.ModifyObjectEdit](../../../../models/v2/ontologies/models/ModifyObjectEdit.md)
- [foundry_sdk.v2.ontologies.models.ObjectTypeApiName](../../../../models/v2/ontologies/models/ObjectTypeApiName.md)
- [foundry_sdk.v2.ontologies.models.OntologyIdentifier](../../../../models/v2/ontologies/models/OntologyIdentifier.md)
- [foundry_sdk.v2.ontologies.models.OntologyTransactionId](../../../../models/v2/ontologies/models/OntologyTransactionId.md)
- [foundry_sdk.v2.ontologies.models.PostTransactionEditsRequest](../../../../models/v2/ontologies/models/PostTransactionEditsRequest.md)
- [foundry_sdk.v2.ontologies.models.PostTransactionEditsResponse](../../../../models/v2/ontologies/models/PostTransactionEditsResponse.md)
- [foundry_sdk.v2.ontologies.models.PrimaryKeyValue](../../../../models/v2/ontologies/models/PrimaryKeyValue.md)
- [foundry_sdk.v2.ontologies.models.PropertyApiName](../../../../models/v2/ontologies/models/PropertyApiName.md)
- [foundry_sdk.v2.ontologies.models.PropertyValue](../../../../models/v2/ontologies/models/PropertyValue.md)
- [foundry_sdk.v2.ontologies.models.SdkPackageRid](../../../../models/v2/ontologies/models/SdkPackageRid.md)
- [foundry_sdk.v2.ontologies.models.SdkVersion](../../../../models/v2/ontologies/models/SdkVersion.md)
- [foundry_sdk.v2.ontologies.models.TransactionEdit](../../../../models/v2/ontologies/models/TransactionEdit.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/ontologies/OntologyTransaction.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](post_edits.md)
