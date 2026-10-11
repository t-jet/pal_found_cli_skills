# v2.datasets.Branch.transactions


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the Transaction history for the given Dataset. When requesting all transactions, the endpoint returns them in reverse chronological order.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.Dataset.Branch.transactions`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def transactions(self, dataset_rid: core_models.DatasetRid, branch_name: core_models.BranchName, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[datasets_models.Transaction]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| branch_name | core_models.BranchName | required | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The default pageSize is 20 transactions and the maximum allowed pageSize is 50 transactions |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| GetBranchTransactionHistoryPermissionDenied | Could not transactions the Branch. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/datasets/{datasetRid}/branches/{branchName}/transactions'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token, 'preview': preview}
```

**path_params**

```python
{'datasetRid': dataset_rid, 'branchName': branch_name}
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
datasets_models.ListTransactionsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'BranchNotFound': datasets_errors.BranchNotFound, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'GetBranchTransactionHistoryPermissionDenied': datasets_errors.GetBranchTransactionHistoryPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[datasets_models.Transaction]`. Ordinary async return: `core.AsyncResourceIterator[datasets_models.Transaction]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[datasets_models.Transaction] |
| sync_raw | ApiResponse[datasets_models.ListTransactionsResponse] |
| sync_streaming | StreamingContextManager[datasets_models.ListTransactionsResponse] |
| async_ordinary | core.AsyncResourceIterator[datasets_models.Transaction] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.ListTransactionsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.ListTransactionsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFound](../../../../models/v2/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFoundParameters](../../../../models/v2/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFound](../../../../models/v2/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFoundParameters](../../../../models/v2/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.GetBranchTransactionHistoryPermissionDenied](../../../../models/v2/datasets/errors/GetBranchTransactionHistoryPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.GetBranchTransactionHistoryPermissionDeniedParameters](../../../../models/v2/datasets/errors/GetBranchTransactionHistoryPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.models.ListTransactionsResponse](../../../../models/v2/datasets/models/ListTransactionsResponse.md)
- [foundry_sdk.v2.datasets.models.Transaction](../../../../models/v2/datasets/models/Transaction.md)
- [foundry_sdk.v2.datasets.models.TransactionCreatedTime](../../../../models/v2/datasets/models/TransactionCreatedTime.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../../../../models/v2/datasets/models/TransactionRid.md)
- [foundry_sdk.v2.datasets.models.TransactionStatus](../../../../models/v2/datasets/models/TransactionStatus.md)
- [foundry_sdk.v2.datasets.models.TransactionType](../../../../models/v2/datasets/models/TransactionType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/Branch.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](transactions.md)
