# v2.orchestration.Build.search


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Search for Builds.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.orchestration.Build.search`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def search(self, *, where: orchestration_models.SearchBuildsFilter, order_by: typing.Optional[orchestration_models.SearchBuildsOrderBy]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> orchestration_models.SearchBuildsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| where | orchestration_models.SearchBuildsFilter | required | Value shape and constraints are in its referenced local type definition. |
| order_by | typing.Optional[orchestration_models.SearchBuildsOrderBy] | None | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size for the search request. If no value is provided, a default of `100` will be used. |
| page_token | typing.Optional[core_models.PageToken] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| SearchBuildsPermissionDenied | Could not search the Build. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/orchestration/builds/search'
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
orchestration_models.SearchBuildsRequest(where=where, order_by=order_by, page_token=page_token, page_size=page_size)
```

**response_type**

```python
orchestration_models.SearchBuildsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'SearchBuildsPermissionDenied': orchestration_errors.SearchBuildsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `orchestration_models.SearchBuildsResponse`. Ordinary async return: `typing.Awaitable[orchestration_models.SearchBuildsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | orchestration_models.SearchBuildsResponse |
| sync_raw | ApiResponse[orchestration_models.SearchBuildsResponse] |
| sync_streaming | StreamingContextManager[orchestration_models.SearchBuildsResponse] |
| async_ordinary | typing.Awaitable[orchestration_models.SearchBuildsResponse] |
| async_raw | Awaitable[AsyncApiResponse[orchestration_models.SearchBuildsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[orchestration_models.SearchBuildsResponse]] |

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
- [foundry_sdk.v2.core.models.OrderByDirection](../../../../models/v2/core/models/OrderByDirection.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.ScheduleRid](../../../../models/v2/core/models/ScheduleRid.md)
- [foundry_sdk.v2.core.models.TimeUnit](../../../../models/v2/core/models/TimeUnit.md)
- [foundry_sdk.v2.orchestration.errors.SearchBuildsPermissionDenied](../../../../models/v2/orchestration/errors/SearchBuildsPermissionDenied.md)
- [foundry_sdk.v2.orchestration.errors.SearchBuildsPermissionDeniedParameters](../../../../models/v2/orchestration/errors/SearchBuildsPermissionDeniedParameters.md)
- [foundry_sdk.v2.orchestration.models.AbortOnFailure](../../../../models/v2/orchestration/models/AbortOnFailure.md)
- [foundry_sdk.v2.orchestration.models.Build](../../../../models/v2/orchestration/models/Build.md)
- [foundry_sdk.v2.orchestration.models.BuildStatus](../../../../models/v2/orchestration/models/BuildStatus.md)
- [foundry_sdk.v2.orchestration.models.FallbackBranches](../../../../models/v2/orchestration/models/FallbackBranches.md)
- [foundry_sdk.v2.orchestration.models.RetryBackoffDuration](../../../../models/v2/orchestration/models/RetryBackoffDuration.md)
- [foundry_sdk.v2.orchestration.models.RetryCount](../../../../models/v2/orchestration/models/RetryCount.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsAndFilter](../../../../models/v2/orchestration/models/SearchBuildsAndFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsEqualsFilter](../../../../models/v2/orchestration/models/SearchBuildsEqualsFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsEqualsFilterField](../../../../models/v2/orchestration/models/SearchBuildsEqualsFilterField.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsFilter](../../../../models/v2/orchestration/models/SearchBuildsFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsGteFilter](../../../../models/v2/orchestration/models/SearchBuildsGteFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsGteFilterField](../../../../models/v2/orchestration/models/SearchBuildsGteFilterField.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsLtFilter](../../../../models/v2/orchestration/models/SearchBuildsLtFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsLtFilterField](../../../../models/v2/orchestration/models/SearchBuildsLtFilterField.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsNotFilter](../../../../models/v2/orchestration/models/SearchBuildsNotFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsOrFilter](../../../../models/v2/orchestration/models/SearchBuildsOrFilter.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsOrderBy](../../../../models/v2/orchestration/models/SearchBuildsOrderBy.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsOrderByField](../../../../models/v2/orchestration/models/SearchBuildsOrderByField.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsOrderByItem](../../../../models/v2/orchestration/models/SearchBuildsOrderByItem.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsRequest](../../../../models/v2/orchestration/models/SearchBuildsRequest.md)
- [foundry_sdk.v2.orchestration.models.SearchBuildsResponse](../../../../models/v2/orchestration/models/SearchBuildsResponse.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/orchestration/Build.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](search.md)
