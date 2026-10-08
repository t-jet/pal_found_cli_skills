# v2.orchestration.ScheduleVersion.schedule


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning



## SDK invocation contract

```python
def schedule(self, schedule_version_rid: orchestration_models.ScheduleVersionRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> typing.Optional[orchestration_models.Schedule]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| schedule_version_rid | orchestration_models.ScheduleVersionRid | required | The RID of a schedule version |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
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
'/v2/orchestration/scheduleVersions/{scheduleVersionRid}/schedule'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'scheduleVersionRid': schedule_version_rid}
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
typing.Optional[orchestration_models.Schedule]
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

Ordinary sync return: `typing.Optional[orchestration_models.Schedule]`. Ordinary async return: `typing.Awaitable[typing.Optional[orchestration_models.Schedule]]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | typing.Optional[orchestration_models.Schedule] |
| sync_raw | ApiResponse[typing.Optional[orchestration_models.Schedule]] |
| sync_streaming | StreamingContextManager[typing.Optional[orchestration_models.Schedule]] |
| async_ordinary | typing.Awaitable[typing.Optional[orchestration_models.Schedule]] |
| async_raw | Awaitable[AsyncApiResponse[typing.Optional[orchestration_models.Schedule]]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[typing.Optional[orchestration_models.Schedule]]] |

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
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.Duration](../../../../models/v2/core/models/Duration.md)
- [foundry_sdk.v2.core.models.MediaSetRid](../../../../models/v2/core/models/MediaSetRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../../../models/v2/core/models/ScheduleRid.md)
- [foundry_sdk.v2.core.models.TableRid](../../../../models/v2/core/models/TableRid.md)
- [foundry_sdk.v2.core.models.TimeUnit](../../../../models/v2/core/models/TimeUnit.md)
- [foundry_sdk.v2.core.models.UpdatedBy](../../../../models/v2/core/models/UpdatedBy.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../../../models/v2/core/models/UpdatedTime.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)
- [foundry_sdk.v2.core.models.ZoneId](../../../../models/v2/core/models/ZoneId.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)
- [foundry_sdk.v2.orchestration.models.AbortOnFailure](../../../../models/v2/orchestration/models/AbortOnFailure.md)
- [foundry_sdk.v2.orchestration.models.Action](../../../../models/v2/orchestration/models/Action.md)
- [foundry_sdk.v2.orchestration.models.AndTrigger](../../../../models/v2/orchestration/models/AndTrigger.md)
- [foundry_sdk.v2.orchestration.models.BuildTarget](../../../../models/v2/orchestration/models/BuildTarget.md)
- [foundry_sdk.v2.orchestration.models.BuildableRid](../../../../models/v2/orchestration/models/BuildableRid.md)
- [foundry_sdk.v2.orchestration.models.ConnectingTarget](../../../../models/v2/orchestration/models/ConnectingTarget.md)
- [foundry_sdk.v2.orchestration.models.CronExpression](../../../../models/v2/orchestration/models/CronExpression.md)
- [foundry_sdk.v2.orchestration.models.DatasetUpdatedTrigger](../../../../models/v2/orchestration/models/DatasetUpdatedTrigger.md)
- [foundry_sdk.v2.orchestration.models.FallbackBranches](../../../../models/v2/orchestration/models/FallbackBranches.md)
- [foundry_sdk.v2.orchestration.models.ForceBuild](../../../../models/v2/orchestration/models/ForceBuild.md)
- [foundry_sdk.v2.orchestration.models.JobSucceededTrigger](../../../../models/v2/orchestration/models/JobSucceededTrigger.md)
- [foundry_sdk.v2.orchestration.models.ManualTarget](../../../../models/v2/orchestration/models/ManualTarget.md)
- [foundry_sdk.v2.orchestration.models.ManualTrigger](../../../../models/v2/orchestration/models/ManualTrigger.md)
- [foundry_sdk.v2.orchestration.models.MediaSetUpdatedTrigger](../../../../models/v2/orchestration/models/MediaSetUpdatedTrigger.md)
- [foundry_sdk.v2.orchestration.models.NewLogicTrigger](../../../../models/v2/orchestration/models/NewLogicTrigger.md)
- [foundry_sdk.v2.orchestration.models.NotificationsEnabled](../../../../models/v2/orchestration/models/NotificationsEnabled.md)
- [foundry_sdk.v2.orchestration.models.OrTrigger](../../../../models/v2/orchestration/models/OrTrigger.md)
- [foundry_sdk.v2.orchestration.models.ProjectScope](../../../../models/v2/orchestration/models/ProjectScope.md)
- [foundry_sdk.v2.orchestration.models.RetryBackoffDuration](../../../../models/v2/orchestration/models/RetryBackoffDuration.md)
- [foundry_sdk.v2.orchestration.models.RetryCount](../../../../models/v2/orchestration/models/RetryCount.md)
- [foundry_sdk.v2.orchestration.models.Schedule](../../../../models/v2/orchestration/models/Schedule.md)
- [foundry_sdk.v2.orchestration.models.SchedulePaused](../../../../models/v2/orchestration/models/SchedulePaused.md)
- [foundry_sdk.v2.orchestration.models.ScheduleSucceededTrigger](../../../../models/v2/orchestration/models/ScheduleSucceededTrigger.md)
- [foundry_sdk.v2.orchestration.models.ScheduleVersionRid](../../../../models/v2/orchestration/models/ScheduleVersionRid.md)
- [foundry_sdk.v2.orchestration.models.ScopeMode](../../../../models/v2/orchestration/models/ScopeMode.md)
- [foundry_sdk.v2.orchestration.models.TableUpdatedTrigger](../../../../models/v2/orchestration/models/TableUpdatedTrigger.md)
- [foundry_sdk.v2.orchestration.models.TimeTrigger](../../../../models/v2/orchestration/models/TimeTrigger.md)
- [foundry_sdk.v2.orchestration.models.Trigger](../../../../models/v2/orchestration/models/Trigger.md)
- [foundry_sdk.v2.orchestration.models.UpstreamTarget](../../../../models/v2/orchestration/models/UpstreamTarget.md)
- [foundry_sdk.v2.orchestration.models.UserScope](../../../../models/v2/orchestration/models/UserScope.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/orchestration/ScheduleVersion.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](schedule.md)
