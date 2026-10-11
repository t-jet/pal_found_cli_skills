# v2.datasets.Dataset.get_schedules


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the RIDs of the Schedules that target the given Dataset.

Note: It may take up to an hour for recent changes to schedules to be reflected in this response,
especially for schedules managed by Marketplace. This operation will return outdated results in the
meantime.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.Dataset.get_schedules`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_schedules(self, dataset_rid: core_models.DatasetRid, *, branch_name: typing.Optional[core_models.BranchName]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[core_models.ScheduleRid]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| branch_name | typing.Optional[core_models.BranchName] | None | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used. |
| page_size | typing.Optional[core_models.PageSize] | None | Value shape and constraints are in its referenced local type definition. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| GetDatasetSchedulesPermissionDenied | Could not getSchedules the Dataset. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/datasets/{datasetRid}/getSchedules'
```

**query_params**

```python
{'branchName': branch_name, 'pageSize': page_size, 'pageToken': page_token}
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
datasets_models.ListSchedulesResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'BranchNotFound': datasets_errors.BranchNotFound, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'GetDatasetSchedulesPermissionDenied': datasets_errors.GetDatasetSchedulesPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[core_models.ScheduleRid]`. Ordinary async return: `core.AsyncResourceIterator[core_models.ScheduleRid]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[core_models.ScheduleRid] |
| sync_raw | ApiResponse[datasets_models.ListSchedulesResponse] |
| sync_streaming | StreamingContextManager[datasets_models.ListSchedulesResponse] |
| async_ordinary | core.AsyncResourceIterator[core_models.ScheduleRid] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.ListSchedulesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.ListSchedulesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../../../models/v2/core/models/ScheduleRid.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFound](../../../../models/v2/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFoundParameters](../../../../models/v2/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFound](../../../../models/v2/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFoundParameters](../../../../models/v2/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.GetDatasetSchedulesPermissionDenied](../../../../models/v2/datasets/errors/GetDatasetSchedulesPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.GetDatasetSchedulesPermissionDeniedParameters](../../../../models/v2/datasets/errors/GetDatasetSchedulesPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.models.ListSchedulesResponse](../../../../models/v2/datasets/models/ListSchedulesResponse.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/Dataset.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_schedules.md)
