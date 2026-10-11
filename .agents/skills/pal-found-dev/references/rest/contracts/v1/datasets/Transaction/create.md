# v1.datasets.Transaction.create


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a Transaction on a Branch of a Dataset.

## Public Python client route

With a configured `foundry_sdk.v1.FoundryClient` named `client`, call `client.datasets.Dataset.Transaction.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, dataset_rid: datasets_models.DatasetRid, *, branch_id: typing.Optional[datasets_models.BranchId]=None, transaction_type: typing.Optional[datasets_models.TransactionType]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.Transaction: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | datasets_models.DatasetRid | required | The Resource Identifier (RID) of the Dataset on which to create the Transaction. |
| branch_id | typing.Optional[datasets_models.BranchId] | None | The identifier (name) of the Branch on which to create the Transaction. Defaults to `master` for most enrollments. |
| transaction_type | typing.Optional[datasets_models.TransactionType] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| CreateTransactionPermissionDenied | The provided token does not have permission to create a transaction on this dataset. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| InvalidBranchId | The requested branch name cannot be used. Branch names cannot be empty and must not look like RIDs or UUIDs. |
| OpenTransactionAlreadyExists | A transaction is already open on this dataset and branch. A branch of a dataset can only have one open transaction at a time. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v1/datasets/{datasetRid}/transactions'
```

**query_params**

```python
{'branchId': branch_id}
```

**path_params**

```python
{'datasetRid': dataset_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
datasets_models.CreateTransactionRequest(transaction_type=transaction_type)
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
{'BranchNotFound': datasets_errors.BranchNotFound, 'CreateTransactionPermissionDenied': datasets_errors.CreateTransactionPermissionDenied, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'InvalidBranchId': datasets_errors.InvalidBranchId, 'OpenTransactionAlreadyExists': datasets_errors.OpenTransactionAlreadyExists}
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
- [foundry_sdk.v1.datasets.errors.BranchNotFound](../../../../models/v1/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v1.datasets.errors.BranchNotFoundParameters](../../../../models/v1/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.CreateTransactionPermissionDenied](../../../../models/v1/datasets/errors/CreateTransactionPermissionDenied.md)
- [foundry_sdk.v1.datasets.errors.CreateTransactionPermissionDeniedParameters](../../../../models/v1/datasets/errors/CreateTransactionPermissionDeniedParameters.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFound](../../../../models/v1/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFoundParameters](../../../../models/v1/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v1.datasets.errors.InvalidBranchId](../../../../models/v1/datasets/errors/InvalidBranchId.md)
- [foundry_sdk.v1.datasets.errors.InvalidBranchIdParameters](../../../../models/v1/datasets/errors/InvalidBranchIdParameters.md)
- [foundry_sdk.v1.datasets.errors.OpenTransactionAlreadyExists](../../../../models/v1/datasets/errors/OpenTransactionAlreadyExists.md)
- [foundry_sdk.v1.datasets.errors.OpenTransactionAlreadyExistsParameters](../../../../models/v1/datasets/errors/OpenTransactionAlreadyExistsParameters.md)
- [foundry_sdk.v1.datasets.models.BranchId](../../../../models/v1/datasets/models/BranchId.md)
- [foundry_sdk.v1.datasets.models.CreateTransactionRequest](../../../../models/v1/datasets/models/CreateTransactionRequest.md)
- [foundry_sdk.v1.datasets.models.DatasetRid](../../../../models/v1/datasets/models/DatasetRid.md)
- [foundry_sdk.v1.datasets.models.Transaction](../../../../models/v1/datasets/models/Transaction.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](../../../../models/v1/datasets/models/TransactionRid.md)
- [foundry_sdk.v1.datasets.models.TransactionStatus](../../../../models/v1/datasets/models/TransactionStatus.md)
- [foundry_sdk.v1.datasets.models.TransactionType](../../../../models/v1/datasets/models/TransactionType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/datasets/Transaction.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
