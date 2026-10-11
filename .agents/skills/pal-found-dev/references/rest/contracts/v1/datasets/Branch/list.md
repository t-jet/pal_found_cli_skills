# v1.datasets.Branch.list


API v1; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists the Branches of a Dataset.

## Public Python client route

With a configured `foundry_sdk.v1.FoundryClient` named `client`, call `client.datasets.Dataset.Branch.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, dataset_rid: datasets_models.DatasetRid, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[datasets_models.Branch]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | datasets_models.DatasetRid | required | The Resource Identifier (RID) of the Dataset on which to list Branches. |
| page_size | typing.Optional[core_models.PageSize] | None | The desired size of the page to be returned. Defaults to 1,000. See [page sizes](../../../../client-behavior.md) for details. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v1/datasets/{datasetRid}/branches'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token}
```

**path_params**

```python
{'datasetRid': dataset_rid}
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
datasets_models.ListBranchesResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'DatasetNotFound': datasets_errors.DatasetNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[datasets_models.Branch]`. Ordinary async return: `core.AsyncResourceIterator[datasets_models.Branch]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[datasets_models.Branch] |
| sync_raw | ApiResponse[datasets_models.ListBranchesResponse] |
| sync_streaming | StreamingContextManager[datasets_models.ListBranchesResponse] |
| async_ordinary | core.AsyncResourceIterator[datasets_models.Branch] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.ListBranchesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.ListBranchesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v1.core.models.PageSize](../../../../models/v1/core/models/PageSize.md)
- [foundry_sdk.v1.core.models.PageToken](../../../../models/v1/core/models/PageToken.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFound](../../../../models/v1/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v1.datasets.errors.DatasetNotFoundParameters](../../../../models/v1/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v1.datasets.models.Branch](../../../../models/v1/datasets/models/Branch.md)
- [foundry_sdk.v1.datasets.models.BranchId](../../../../models/v1/datasets/models/BranchId.md)
- [foundry_sdk.v1.datasets.models.DatasetRid](../../../../models/v1/datasets/models/DatasetRid.md)
- [foundry_sdk.v1.datasets.models.ListBranchesResponse](../../../../models/v1/datasets/models/ListBranchesResponse.md)
- [foundry_sdk.v1.datasets.models.TransactionRid](../../../../models/v1/datasets/models/TransactionRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v1/datasets/Branch.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Page size is a request hint. Continue with the returned nextPageToken until absent; bound pages and reject a repeated token. [Local procedure](../../../../client-behavior.md).

[Part 1](list.md)
