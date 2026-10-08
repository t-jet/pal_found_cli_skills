# v2.orchestration.Build.get_batch


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Execute multiple get requests on Build.

Users are allowed to make a maximum of **4 requests per second** and **25 concurrent requests**.


The maximum batch size for this endpoint is 100.

## SDK invocation contract

```python
def get_batch(self, body: typing_extensions.Annotated[typing.List[orchestration_models.GetBuildsBatchRequestElement], annotated_types.Len(min_length=1, max_length=100)], *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> orchestration_models.GetBuildsBatchResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| body | typing_extensions.Annotated[typing.List[orchestration_models.GetBuildsBatchRequestElement], annotated_types.Len(min_length=1, max_length=100)] | required | Body of the request |
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
'/v2/orchestration/builds/getBatch'
```

**query_params**

```python
{}
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
orchestration_models.GetBuildsBatchResponse
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

Ordinary sync return: `orchestration_models.GetBuildsBatchResponse`. Ordinary async return: `typing.Awaitable[orchestration_models.GetBuildsBatchResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | orchestration_models.GetBuildsBatchResponse |
| sync_raw | ApiResponse[orchestration_models.GetBuildsBatchResponse] |
| sync_streaming | StreamingContextManager[orchestration_models.GetBuildsBatchResponse] |
| async_ordinary | typing.Awaitable[orchestration_models.GetBuildsBatchResponse] |
| async_raw | Awaitable[AsyncApiResponse[orchestration_models.GetBuildsBatchResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[orchestration_models.GetBuildsBatchResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.BuildRid](../../../../models/v2/core/models/BuildRid.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.Duration](../../../../models/v2/core/models/Duration.md)
- [foundry_sdk.v2.core.models.JobRid](../../../../models/v2/core/models/JobRid.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../../../models/v2/core/models/ScheduleRid.md)
- [foundry_sdk.v2.core.models.TimeUnit](../../../../models/v2/core/models/TimeUnit.md)
- [foundry_sdk.v2.orchestration.models.AbortOnFailure](../../../../models/v2/orchestration/models/AbortOnFailure.md)
- [foundry_sdk.v2.orchestration.models.Build](../../../../models/v2/orchestration/models/Build.md)
- [foundry_sdk.v2.orchestration.models.BuildStatus](../../../../models/v2/orchestration/models/BuildStatus.md)
- [foundry_sdk.v2.orchestration.models.FallbackBranches](../../../../models/v2/orchestration/models/FallbackBranches.md)
- [foundry_sdk.v2.orchestration.models.GetBuildsBatchRequestElement](../../../../models/v2/orchestration/models/GetBuildsBatchRequestElement.md)
- [foundry_sdk.v2.orchestration.models.GetBuildsBatchResponse](../../../../models/v2/orchestration/models/GetBuildsBatchResponse.md)
- [foundry_sdk.v2.orchestration.models.RetryBackoffDuration](../../../../models/v2/orchestration/models/RetryBackoffDuration.md)
- [foundry_sdk.v2.orchestration.models.RetryCount](../../../../models/v2/orchestration/models/RetryCount.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/orchestration/Build.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_batch.md)
