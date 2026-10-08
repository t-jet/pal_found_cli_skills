# v2.orchestration.Job.get_batch


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Execute multiple get requests on Job.

Users are allowed to make a maximum of **4 requests per second** and **25 concurrent requests**.


The maximum batch size for this endpoint is 500.

## SDK invocation contract

```python
def get_batch(self, body: typing_extensions.Annotated[typing.List[orchestration_models.GetJobsBatchRequestElement], annotated_types.Len(min_length=1, max_length=500)], *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> orchestration_models.GetJobsBatchResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| body | typing_extensions.Annotated[typing.List[orchestration_models.GetJobsBatchRequestElement], annotated_types.Len(min_length=1, max_length=500)] | required | Body of the request |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/orchestration/jobs/getBatch'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
body
```

**response_type**

```python
orchestration_models.GetJobsBatchResponse
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
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `orchestration_models.GetJobsBatchResponse`. Ordinary async return: `typing.Awaitable[orchestration_models.GetJobsBatchResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | orchestration_models.GetJobsBatchResponse |
| sync_raw | ApiResponse[orchestration_models.GetJobsBatchResponse] |
| sync_streaming | StreamingContextManager[orchestration_models.GetJobsBatchResponse] |
| async_ordinary | typing.Awaitable[orchestration_models.GetJobsBatchResponse] |
| async_raw | Awaitable[AsyncApiResponse[orchestration_models.GetJobsBatchResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[orchestration_models.GetJobsBatchResponse]] |

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
- [foundry_sdk.v2.orchestration.models.DatasetJobOutput](../../../../models/v2/orchestration/models/DatasetJobOutput.md)
- [foundry_sdk.v2.orchestration.models.GetJobsBatchRequestElement](../../../../models/v2/orchestration/models/GetJobsBatchRequestElement.md)
- [foundry_sdk.v2.orchestration.models.GetJobsBatchResponse](../../../../models/v2/orchestration/models/GetJobsBatchResponse.md)
- [foundry_sdk.v2.orchestration.models.Job](../../../../models/v2/orchestration/models/Job.md)
- [foundry_sdk.v2.orchestration.models.JobOutput](../../../../models/v2/orchestration/models/JobOutput.md)
- [foundry_sdk.v2.orchestration.models.JobStartedTime](../../../../models/v2/orchestration/models/JobStartedTime.md)
- [foundry_sdk.v2.orchestration.models.JobStatus](../../../../models/v2/orchestration/models/JobStatus.md)
- [foundry_sdk.v2.orchestration.models.TransactionalMediaSetJobOutput](../../../../models/v2/orchestration/models/TransactionalMediaSetJobOutput.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/orchestration/Job.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_batch.md)
