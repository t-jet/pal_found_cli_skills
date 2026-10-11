# v2.datasets.View.get


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get metadata for a View.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.View.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, view_dataset_rid: core_models.DatasetRid, *, branch: typing.Optional[core_models.BranchName]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.View: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| view_dataset_rid | core_models.DatasetRid | required | The rid of the View. |
| branch | typing.Optional[core_models.BranchName] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ViewNotFound | The requested View could not be found. Either the view does not exist, the branch is not valid or the client token does not have access to it. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/datasets/views/{viewDatasetRid}'
```

**query_params**

```python
{'branch': branch}
```

**path_params**

```python
{'viewDatasetRid': view_dataset_rid}
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
datasets_models.View
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ViewNotFound': datasets_errors.ViewNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `datasets_models.View`. Ordinary async return: `typing.Awaitable[datasets_models.View]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | datasets_models.View |
| sync_raw | ApiResponse[datasets_models.View] |
| sync_streaming | StreamingContextManager[datasets_models.View] |
| async_ordinary | typing.Awaitable[datasets_models.View] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.View]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.View]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.datasets.errors.ViewNotFound](../../../../models/v2/datasets/errors/ViewNotFound.md)
- [foundry_sdk.v2.datasets.errors.ViewNotFoundParameters](../../../../models/v2/datasets/errors/ViewNotFoundParameters.md)
- [foundry_sdk.v2.datasets.models.DatasetName](../../../../models/v2/datasets/models/DatasetName.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyLatestWinsResolutionStrategy](../../../../models/v2/datasets/models/PrimaryKeyLatestWinsResolutionStrategy.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyResolutionDuplicate](../../../../models/v2/datasets/models/PrimaryKeyResolutionDuplicate.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyResolutionStrategy](../../../../models/v2/datasets/models/PrimaryKeyResolutionStrategy.md)
- [foundry_sdk.v2.datasets.models.PrimaryKeyResolutionUnique](../../../../models/v2/datasets/models/PrimaryKeyResolutionUnique.md)
- [foundry_sdk.v2.datasets.models.View](../../../../models/v2/datasets/models/View.md)
- [foundry_sdk.v2.datasets.models.ViewBackingDataset](../../../../models/v2/datasets/models/ViewBackingDataset.md)
- [foundry_sdk.v2.datasets.models.ViewPrimaryKey](../../../../models/v2/datasets/models/ViewPrimaryKey.md)
- [foundry_sdk.v2.datasets.models.ViewPrimaryKeyResolution](../../../../models/v2/datasets/models/ViewPrimaryKeyResolution.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/View.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
