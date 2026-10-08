# v2.orchestration.Job.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the Job with the specified rid.

Users are allowed to make a maximum of **4 requests per second** and **25 concurrent requests**.

## SDK invocation contract

```python
def get(self, job_rid: core_models.JobRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> orchestration_models.Job: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| job_rid | core_models.JobRid | required | The RID of a Job. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| JobNotFound | The given Job could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/orchestration/jobs/{jobRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'jobRid': job_rid}
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
orchestration_models.Job
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'JobNotFound': orchestration_errors.JobNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `orchestration_models.Job`. Ordinary async return: `typing.Awaitable[orchestration_models.Job]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | orchestration_models.Job |
| sync_raw | ApiResponse[orchestration_models.Job] |
| sync_streaming | StreamingContextManager[orchestration_models.Job] |
| async_ordinary | typing.Awaitable[orchestration_models.Job] |
| async_raw | Awaitable[AsyncApiResponse[orchestration_models.Job]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[orchestration_models.Job]] |

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
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.datasets.models.TransactionRid](../../../../models/v2/datasets/models/TransactionRid.md)
- [foundry_sdk.v2.orchestration.errors.JobNotFound](../../../../models/v2/orchestration/errors/JobNotFound.md)
- [foundry_sdk.v2.orchestration.errors.JobNotFoundParameters](../../../../models/v2/orchestration/errors/JobNotFoundParameters.md)
- [foundry_sdk.v2.orchestration.models.DatasetJobOutput](../../../../models/v2/orchestration/models/DatasetJobOutput.md)
- [foundry_sdk.v2.orchestration.models.Job](../../../../models/v2/orchestration/models/Job.md)
- [foundry_sdk.v2.orchestration.models.JobOutput](../../../../models/v2/orchestration/models/JobOutput.md)
- [foundry_sdk.v2.orchestration.models.JobStartedTime](../../../../models/v2/orchestration/models/JobStartedTime.md)
- [foundry_sdk.v2.orchestration.models.JobStatus](../../../../models/v2/orchestration/models/JobStatus.md)
- [foundry_sdk.v2.orchestration.models.TransactionalMediaSetJobOutput](../../../../models/v2/orchestration/models/TransactionalMediaSetJobOutput.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/orchestration/Job.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
