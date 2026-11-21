# v2.datasets.Branch.get


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get a Branch of a Dataset.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.Dataset.Branch.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, dataset_rid: core_models.DatasetRid, branch_name: core_models.BranchName, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.Branch: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| branch_name | core_models.BranchName | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/datasets/{datasetRid}/branches/{branchName}'
```

**query_params**

```python
{}
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
datasets_models.Branch
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'BranchNotFound': datasets_errors.BranchNotFound, 'DatasetNotFound': datasets_errors.DatasetNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `datasets_models.Branch`. Ordinary async return: `typing.Awaitable[datasets_models.Branch]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | datasets_models.Branch |
| sync_raw | ApiResponse[datasets_models.Branch] |
| sync_streaming | StreamingContextManager[datasets_models.Branch] |
| async_ordinary | typing.Awaitable[datasets_models.Branch] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.Branch]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.Branch]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFound](../../../../models/v2/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFoundParameters](../../../../models/v2/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFound](../../../../models/v2/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFoundParameters](../../../../models/v2/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v2.datasets.models.Branch](../../../../models/v2/datasets/models/Branch.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../../../../models/v2/datasets/models/TransactionRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/Branch.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
