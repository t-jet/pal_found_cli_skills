# v1.datasets.Transaction.commit


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Commits an open Transaction. File modifications made on this Transaction are preserved and the Branch is
updated to point to the Transaction.

## SDK invocation contract

```python
def commit(self, dataset_rid: datasets_models.DatasetRid, transaction_rid: datasets_models.TransactionRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.Transaction: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | datasets_models.DatasetRid | required | The Resource Identifier (RID) of the Dataset that contains the Transaction. |
| transaction_rid | datasets_models.TransactionRid | required | The Resource Identifier (RID) of the Transaction. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CommitTransactionPermissionDenied | The provided token does not have permission to commit the given transaction on the given dataset. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |
| TransactionNotOpen | The given transaction is not open. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v1/datasets/{datasetRid}/transactions/{transactionRid}/commit'
```

**query_params**

```python
{}
```

**path_params**

```python
{'datasetRid': dataset_rid, 'transactionRid': transaction_rid}
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
datasets_models.Transaction
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CommitTransactionPermissionDenied': datasets_errors.CommitTransactionPermissionDenied, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'TransactionNotFound': datasets_errors.TransactionNotFound, 'TransactionNotOpen': datasets_errors.TransactionNotOpen}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `datasets_models.Transaction`. Ordinary async return: `typing.Awaitable[datasets_models.Transaction]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | datasets_models.Transaction |
| sync_raw | ApiResponse[datasets_models.Transaction] |
| sync_streaming | StreamingContextManager[datasets_models.Transaction] |
| async_ordinary | typing.Awaitable[datasets_models.Transaction] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.Transaction]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.Transaction]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.datasets.errors.CommitTransactionPermissionDenied](../../../../models/v1/datasets/errors/CommitTransactionPermissionDenied.md)
- [foundry_sdk.v1.datasets.errors.CommitTransactionPermissionDeniedParameters](../../../../models/v1/datasets/errors/CommitTransactionPermissionDeniedParameters.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFound](../../../../models/v1/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFoundParameters](../../../../models/v1/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotFound](../../../../models/v1/datasets/errors/TransactionNotFound.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotFoundParameters](../../../../models/v1/datasets/errors/TransactionNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotOpen](../../../../models/v1/datasets/errors/TransactionNotOpen.md)
- [foundry_sdk.v1.datasets.errors.TransactionNotOpenParameters](../../../../models/v1/datasets/errors/TransactionNotOpenParameters.md)
- [foundry_sdk.v1.datasets.models.DatasetRid](../../../../models/v1/datasets/models/DatasetRid.md)
- [foundry_sdk.v1.datasets.models.Transaction](../../../../models/v1/datasets/models/Transaction.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](../../../../models/v1/datasets/models/TransactionRid.md)
- [foundry_sdk.v1.datasets.models.TransactionStatus](../../../../models/v1/datasets/models/TransactionStatus.md)
- [foundry_sdk.v1.datasets.models.TransactionType](../../../../models/v1/datasets/models/TransactionType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/datasets/Transaction.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](commit.md)
