# v2.datasets.Dataset.get_health_checks


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the RIDs of the Data Health Checks that are configured for the given Dataset.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.datasets.Dataset.get_health_checks`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_health_checks(self, dataset_rid: core_models.DatasetRid, *, branch_name: typing.Optional[core_models.BranchName]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> datasets_models.ListHealthChecksResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| dataset_rid | core_models.DatasetRid | required | Value shape and constraints are in its referenced local type definition. |
| branch_name | typing.Optional[core_models.BranchName] | None | The name of the Branch. If none is provided, the default Branch name - `master` for most enrollments - will be used. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| BranchNotFound | The requested branch could not be found, or the client token does not have access to it. |
| DatasetNotFound | The requested dataset could not be found, or the client token does not have access to it. |
| GetDatasetHealthChecksPermissionDenied | Could not getHealthChecks the Dataset. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/datasets/{datasetRid}/getHealthChecks'
```

**query_params**

```python
{'branchName': branch_name, 'preview': preview}
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
datasets_models.ListHealthChecksResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'BranchNotFound': datasets_errors.BranchNotFound, 'DatasetNotFound': datasets_errors.DatasetNotFound, 'GetDatasetHealthChecksPermissionDenied': datasets_errors.GetDatasetHealthChecksPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `datasets_models.ListHealthChecksResponse`. Ordinary async return: `typing.Awaitable[datasets_models.ListHealthChecksResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | datasets_models.ListHealthChecksResponse |
| sync_raw | ApiResponse[datasets_models.ListHealthChecksResponse] |
| sync_streaming | StreamingContextManager[datasets_models.ListHealthChecksResponse] |
| async_ordinary | typing.Awaitable[datasets_models.ListHealthChecksResponse] |
| async_raw | Awaitable[AsyncApiResponse[datasets_models.ListHealthChecksResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[datasets_models.ListHealthChecksResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.CheckRid](../../../../models/v2/core/models/CheckRid.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFound](../../../../models/v2/datasets/errors/BranchNotFound.md)
- [foundry_sdk.v2.datasets.errors.BranchNotFoundParameters](../../../../models/v2/datasets/errors/BranchNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFound](../../../../models/v2/datasets/errors/DatasetNotFound.md)
- [foundry_sdk.v2.datasets.errors.DatasetNotFoundParameters](../../../../models/v2/datasets/errors/DatasetNotFoundParameters.md)
- [foundry_sdk.v2.datasets.errors.GetDatasetHealthChecksPermissionDenied](../../../../models/v2/datasets/errors/GetDatasetHealthChecksPermissionDenied.md)
- [foundry_sdk.v2.datasets.errors.GetDatasetHealthChecksPermissionDeniedParameters](../../../../models/v2/datasets/errors/GetDatasetHealthChecksPermissionDeniedParameters.md)
- [foundry_sdk.v2.datasets.models.ListHealthChecksResponse](../../../../models/v2/datasets/models/ListHealthChecksResponse.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/datasets/Dataset.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_health_checks.md)
