# v2.orchestration.Build.jobs


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the Jobs in the Build.

## SDK invocation contract

```python
def jobs(self, build_rid: core_models.BuildRid, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[orchestration_models.Job]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| build_rid | core_models.BuildRid | required | The RID of a Build. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/orchestration/builds/{buildRid}/jobs'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token}
```

**path_params**

```python
{'buildRid': build_rid}
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
orchestration_models.ListJobsOfBuildResponse
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
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[orchestration_models.Job]`. Ordinary async return: `core.AsyncResourceIterator[orchestration_models.Job]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[orchestration_models.Job] |
| sync_raw | ApiResponse[orchestration_models.ListJobsOfBuildResponse] |
| sync_streaming | StreamingContextManager[orchestration_models.ListJobsOfBuildResponse] |
| async_ordinary | core.AsyncResourceIterator[orchestration_models.Job] |
| async_raw | Awaitable[AsyncApiResponse[orchestration_models.ListJobsOfBuildResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[orchestration_models.ListJobsOfBuildResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BuildRid](../../../../models/v2/core/models/BuildRid.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.JobRid](../../../../models/v2/core/models/JobRid.md)
- [foundry_sdk.v2.core.models.MediaSetRid](../../../../models/v2/core/models/MediaSetRid.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../../../../models/v2/datasets/models/TransactionRid.md)
- [foundry_sdk.v2.orchestration.models.DatasetJobOutput](../../../../models/v2/orchestration/models/DatasetJobOutput.md)
- [foundry_sdk.v2.orchestration.models.Job](../../../../models/v2/orchestration/models/Job.md)
- [foundry_sdk.v2.orchestration.models.JobOutput](../../../../models/v2/orchestration/models/JobOutput.md)
- [foundry_sdk.v2.orchestration.models.JobStartedTime](../../../../models/v2/orchestration/models/JobStartedTime.md)
- [foundry_sdk.v2.orchestration.models.JobStatus](../../../../models/v2/orchestration/models/JobStatus.md)
- [foundry_sdk.v2.orchestration.models.ListJobsOfBuildResponse](../../../../models/v2/orchestration/models/ListJobsOfBuildResponse.md)
- [foundry_sdk.v2.orchestration.models.TransactionalMediaSetJobOutput](../../../../models/v2/orchestration/models/TransactionalMediaSetJobOutput.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/orchestration/Build.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](jobs.md)
