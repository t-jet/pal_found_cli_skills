# v2.orchestration.Schedule.get_affected_resources


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning



## SDK invocation contract

```python
def get_affected_resources(self, schedule_rid: core_models.ScheduleRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> orchestration_models.AffectedResourcesResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| schedule_rid | core_models.ScheduleRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetAffectedResourcesSchedulePermissionDenied | Could not getAffectedResources the Schedule. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/orchestration/schedules/{scheduleRid}/getAffectedResources'
```

**query_params**

```python
{'preview': preview}
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
orchestration_models.AffectedResourcesResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetAffectedResourcesSchedulePermissionDenied': orchestration_errors.GetAffectedResourcesSchedulePermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `orchestration_models.AffectedResourcesResponse`. Ordinary async return: `typing.Awaitable[orchestration_models.AffectedResourcesResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | orchestration_models.AffectedResourcesResponse |
| sync_raw | ApiResponse[orchestration_models.AffectedResourcesResponse] |
| sync_streaming | StreamingContextManager[orchestration_models.AffectedResourcesResponse] |
| async_ordinary | typing.Awaitable[orchestration_models.AffectedResourcesResponse] |
| async_raw | Awaitable[AsyncApiResponse[orchestration_models.AffectedResourcesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[orchestration_models.AffectedResourcesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../../../models/v2/core/models/ScheduleRid.md)
- [foundry_sdk.v2.orchestration.errors.GetAffectedResourcesSchedulePermissionDenied](../../../../models/v2/orchestration/errors/GetAffectedResourcesSchedulePermissionDenied.md)
- [foundry_sdk.v2.orchestration.errors.GetAffectedResourcesSchedulePermissionDeniedParameters](../../../../models/v2/orchestration/errors/GetAffectedResourcesSchedulePermissionDeniedParameters.md)
- [foundry_sdk.v2.orchestration.models.AffectedResourcesResponse](../../../../models/v2/orchestration/models/AffectedResourcesResponse.md)
- [foundry_sdk.v2.orchestration.models.BuildableRid](../../../../models/v2/orchestration/models/BuildableRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/orchestration/Schedule.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_affected_resources.md)
