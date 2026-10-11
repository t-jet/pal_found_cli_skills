# v2.orchestration.Schedule.runs


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the most recent runs of a Schedule. If no page size is provided, a page size of 100 will be used.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.orchestration.Schedule.runs`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def runs(self, schedule_rid: core_models.ScheduleRid, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[orchestration_models.ScheduleRun]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| schedule_rid | core_models.ScheduleRid | required | Value shape and constraints are in its referenced local type definition. |
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
'/v2/orchestration/schedules/{scheduleRid}/runs'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token}
```

**path_params**

```python
{'scheduleRid': schedule_rid}
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
orchestration_models.ListRunsOfScheduleResponse
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

Ordinary sync return: `core.ResourceIterator[orchestration_models.ScheduleRun]`. Ordinary async return: `core.AsyncResourceIterator[orchestration_models.ScheduleRun]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[orchestration_models.ScheduleRun] |
| sync_raw | ApiResponse[orchestration_models.ListRunsOfScheduleResponse] |
| sync_streaming | StreamingContextManager[orchestration_models.ListRunsOfScheduleResponse] |
| async_ordinary | core.AsyncResourceIterator[orchestration_models.ScheduleRun] |
| async_raw | Awaitable[AsyncApiResponse[orchestration_models.ListRunsOfScheduleResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[orchestration_models.ListRunsOfScheduleResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.BuildRid](../../../../models/v2/core/models/BuildRid.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../../../models/v2/core/models/ScheduleRid.md)
- [foundry_sdk.v2.orchestration.models.ListRunsOfScheduleResponse](../../../../models/v2/orchestration/models/ListRunsOfScheduleResponse.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRun](../../../../models/v2/orchestration/models/ScheduleRun.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunError](../../../../models/v2/orchestration/models/ScheduleRunError.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunErrorName](../../../../models/v2/orchestration/models/ScheduleRunErrorName.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunIgnored](../../../../models/v2/orchestration/models/ScheduleRunIgnored.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunResult](../../../../models/v2/orchestration/models/ScheduleRunResult.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunRid](../../../../models/v2/orchestration/models/ScheduleRunRid.md)
- [foundry_sdk.v2.orchestration.models.ScheduleRunSubmitted](../../../../models/v2/orchestration/models/ScheduleRunSubmitted.md)
- [foundry_sdk.v2.orchestration.models.ScheduleVersionRid](../../../../models/v2/orchestration/models/ScheduleVersionRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/orchestration/Schedule-2.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](runs.md)
