# v2.datasets.Transaction.job


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the [Job](../../../../../pipelines/releases.md) that computed the
given Transaction. Not all Transactions have an associated Job. For example, if a Dataset
is updated by a User uploading a CSV file into the browser, no Job will be tied to the Transaction.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.Dataset.Transaction.job`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def job(self, dataset_rid: core_models.DatasetRid, transaction_rid: datasets_models.TransactionRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> typing.Optional[core_models.JobRid]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| transaction_rid | datasets_models.TransactionRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| JobTransactionPermissionDenied | Could not job the Transaction. |
| TransactionNotFound | The requested transaction could not be found on the dataset, or the client token does not have access to it. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/datasets/{datasetRid}/transactions/{transactionRid}/job'
```

**query_params**

```python
{'preview': preview}
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
typing.Optional[core_models.JobRid]
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'DatasetNotFound': datasets_errors.DatasetNotFound, 'JobTransactionPermissionDenied': datasets_errors.JobTransactionPermissionDenied, 'TransactionNotFound': datasets_errors.TransactionNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `typing.Optional[core_models.JobRid]`. Ordinary async return: `typing.Awaitable[typing.Optional[core_models.JobRid]]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | typing.Optional[core_models.JobRid] |
| sync_raw | ApiResponse[typing.Optional[core_models.JobRid]] |
| sync_streaming | StreamingContextManager[typing.Optional[core_models.JobRid]] |
| async_ordinary | typing.Awaitable[typing.Optional[core_models.JobRid]] |
| async_raw | Awaitable[AsyncApiResponse[typing.Optional[core_models.JobRid]]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[typing.Optional[core_models.JobRid]]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.JobRid](../../../../models/v2/core/models/JobRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFound](../../../../models/v2/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFoundParameters](../../../../models/v2/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.JobTransactionPermissionDenied](../../../../models/v2/datasets/errors/JobTransactionPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.JobTransactionPermissionDeniedParameters](../../../../models/v2/datasets/errors/JobTransactionPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.errors.TransactionNotFound](../../../../models/v2/datasets/errors/TransactionNotFound.md)
- [foundry_sdk.v2.datasets.errors.TransactionNotFoundParameters](../../../../models/v2/datasets/errors/TransactionNotFoundParameters.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../../../../models/v2/datasets/models/TransactionRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/Transaction.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A Build runs asynchronously and has its own identity and status. Submission is not completion; poll with a finite budget. [Local procedure](../../../../../pipelines/releases.md).

[Part 1](job.md)
