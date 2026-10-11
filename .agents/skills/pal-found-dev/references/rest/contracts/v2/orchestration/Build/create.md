# v2.orchestration.Build.create


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning



## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.orchestration.Build.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, *, fallback_branches: orchestration_models.FallbackBranches, target: orchestration_models.BuildTarget, abort_on_failure: typing.Optional[orchestration_models.AbortOnFailure]=None, branch_name: typing.Optional[core_models.BranchName]=None, force_build: typing.Optional[orchestration_models.ForceBuild]=None, notifications_enabled: typing.Optional[orchestration_models.NotificationsEnabled]=None, retry_backoff_duration: typing.Optional[orchestration_models.RetryBackoffDuration]=None, retry_count: typing.Optional[orchestration_models.RetryCount]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> orchestration_models.Build: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| fallback_branches | orchestration_models.FallbackBranches | required | Value shape and constraints are in its referenced local type definition. |
| target | orchestration_models.BuildTarget | required | The targets of the schedule. |
| abort_on_failure | typing.Optional[orchestration_models.AbortOnFailure] | None | Value shape and constraints are in its referenced local type definition. |
| branch_name | typing.Optional[core_models.BranchName] | None | The target branch the build should run on. |
| force_build | typing.Optional[orchestration_models.ForceBuild] | None | Value shape and constraints are in its referenced local type definition. |
| notifications_enabled | typing.Optional[orchestration_models.NotificationsEnabled] | None | Value shape and constraints are in its referenced local type definition. |
| retry_backoff_duration | typing.Optional[orchestration_models.RetryBackoffDuration] | None | Value shape and constraints are in its referenced local type definition. |
| retry_count | typing.Optional[orchestration_models.RetryCount] | None | The number of retry attempts for failed jobs. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateBuildPermissionDenied | Could not create the Build. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/orchestration/builds/create'
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
orchestration_models.CreateBuildRequest(target=target, branch_name=branch_name, fallback_branches=fallback_branches, force_build=force_build, retry_count=retry_count, retry_backoff_duration=retry_backoff_duration, abort_on_failure=abort_on_failure, notifications_enabled=notifications_enabled)
```

**response_type**

```python
orchestration_models.Build
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CreateBuildPermissionDenied': orchestration_errors.CreateBuildPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `orchestration_models.Build`. Ordinary async return: `typing.Awaitable[orchestration_models.Build]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | orchestration_models.Build |
| sync_raw | ApiResponse[orchestration_models.Build] |
| sync_streaming | StreamingContextManager[orchestration_models.Build] |
| async_ordinary | typing.Awaitable[orchestration_models.Build] |
| async_raw | Awaitable[AsyncApiResponse[orchestration_models.Build]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[orchestration_models.Build]] |

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
- [foundry_sdk.v2.orchestration.errors.CreateBuildPermissionDenied](../../../../models/v2/orchestration/errors/CreateBuildPermissionDenied.md)
- [foundry_sdk.v2.orchestration.errors.CreateBuildPermissionDeniedParameters](../../../../models/v2/orchestration/errors/CreateBuildPermissionDeniedParameters.md)
- [foundry_sdk.v2.orchestration.models.AbortOnFailure](../../../../models/v2/orchestration/models/AbortOnFailure.md)
- [foundry_sdk.v2.orchestration.models.Build](../../../../models/v2/orchestration/models/Build.md)
- [foundry_sdk.v2.orchestration.models.BuildStatus](../../../../models/v2/orchestration/models/BuildStatus.md)
- [foundry_sdk.v2.orchestration.models.BuildTarget](../../../../models/v2/orchestration/models/BuildTarget.md)
- [foundry_sdk.v2.orchestration.models.BuildableRid](../../../../models/v2/orchestration/models/BuildableRid.md)
- [foundry_sdk.v2.orchestration.models.ConnectingTarget](../../../../models/v2/orchestration/models/ConnectingTarget.md)
- [foundry_sdk.v2.orchestration.models.CreateBuildRequest](../../../../models/v2/orchestration/models/CreateBuildRequest.md)
- [foundry_sdk.v2.orchestration.models.FallbackBranches](../../../../models/v2/orchestration/models/FallbackBranches.md)
- [foundry_sdk.v2.orchestration.models.ForceBuild](../../../../models/v2/orchestration/models/ForceBuild.md)
- [foundry_sdk.v2.orchestration.models.ManualTarget](../../../../models/v2/orchestration/models/ManualTarget.md)
- [foundry_sdk.v2.orchestration.models.NotificationsEnabled](../../../../models/v2/orchestration/models/NotificationsEnabled.md)
- [foundry_sdk.v2.orchestration.models.RetryBackoffDuration](../../../../models/v2/orchestration/models/RetryBackoffDuration.md)
- [foundry_sdk.v2.orchestration.models.RetryCount](../../../../models/v2/orchestration/models/RetryCount.md)
- [foundry_sdk.v2.orchestration.models.UpstreamTarget](../../../../models/v2/orchestration/models/UpstreamTarget.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/orchestration/Build.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
