# v2.datasets.Dataset.jobs


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the RIDs of the Jobs for the given dataset. By default, returned Jobs are sorted in descending order by the Job start time.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.Dataset.jobs`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def jobs(self, dataset_rid: core_models.DatasetRid, *, order_by: typing.List[datasets_models.GetDatasetJobsSort], branch_name: typing.Optional[core_models.BranchName]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, where: typing.Optional[datasets_models.GetDatasetJobsQuery]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[datasets_models.JobDetails]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| order_by | typing.List[datasets_models.GetDatasetJobsSort] | required | Value shape and constraints are in its referenced local type definition. |
| branch_name | typing.Optional[core_models.BranchName] | None | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used. |
| page_size | typing.Optional[core_models.PageSize] | None | Max number of results to return. A limit of 1000 on if no limit is supplied in the search request |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| where | typing.Optional[datasets_models.GetDatasetJobsQuery] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| GetDatasetJobsPermissionDenied | Could not jobs the Dataset. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/datasets/{datasetRid}/jobs'
```

**query_params**

```python
{'branchName': branch_name, 'pageSize': page_size, 'pageToken': page_token, 'preview': preview}
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
datasets_models.GetDatasetJobsRequest(where=where, order_by=order_by)
```

**response_type**

```python
datasets_models.GetJobResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'BranchNotFound': datasets_errors.BranchNotFound, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'GetDatasetJobsPermissionDenied': datasets_errors.GetDatasetJobsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[datasets_models.JobDetails]`. Ordinary async return: `core.AsyncResourceIterator[datasets_models.JobDetails]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[datasets_models.JobDetails] |
| sync_raw | ApiResponse[datasets_models.GetJobResponse] |
| sync_streaming | StreamingContextManager[datasets_models.GetJobResponse] |
| async_ordinary | core.AsyncResourceIterator[datasets_models.JobDetails] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.GetJobResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.GetJobResponse]] |

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
- [foundry_sdk.v2.core.models.JobRid](../../../../models/v2/core/models/JobRid.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFound](../../../../models/v2/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFoundParameters](../../../../models/v2/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFound](../../../../models/v2/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFoundParameters](../../../../models/v2/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.GetDatasetJobsPermissionDenied](../../../../models/v2/datasets/errors/GetDatasetJobsPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.GetDatasetJobsPermissionDeniedParameters](../../../../models/v2/datasets/errors/GetDatasetJobsPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsAndFilter](../../../../models/v2/datasets/models/GetDatasetJobsAndFilter.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsComparisonType](../../../../models/v2/datasets/models/GetDatasetJobsComparisonType.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsOrFilter](../../../../models/v2/datasets/models/GetDatasetJobsOrFilter.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsQuery](../../../../models/v2/datasets/models/GetDatasetJobsQuery.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsRequest](../../../../models/v2/datasets/models/GetDatasetJobsRequest.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsSort](../../../../models/v2/datasets/models/GetDatasetJobsSort.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsSortDirection](../../../../models/v2/datasets/models/GetDatasetJobsSortDirection.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsSortType](../../../../models/v2/datasets/models/GetDatasetJobsSortType.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsTimeFilter](../../../../models/v2/datasets/models/GetDatasetJobsTimeFilter.md)
- [foundry_sdk.v2.datasets.models.GetDatasetJobsTimeFilterField](../../../../models/v2/datasets/models/GetDatasetJobsTimeFilterField.md)
- [foundry_sdk.v2.datasets.models.GetJobResponse](../../../../models/v2/datasets/models/GetJobResponse.md)
- [foundry_sdk.v2.datasets.models.JobDetails](../../../../models/v2/datasets/models/JobDetails.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/Dataset-2.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](jobs.md)
