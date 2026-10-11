# v2.connectivity.FileImport.execute


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Executes the FileImport, which runs asynchronously as a [Foundry Build](../../../../../pipelines/releases.md).
The returned BuildRid can be used to check the status via the Orchestration API.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.connectivity.Connection.FileImport.execute`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def execute(self, connection_rid: connectivity_models.ConnectionRid, file_import_rid: connectivity_models.FileImportRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core_models.BuildRid: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| connection_rid | connectivity_models.ConnectionRid | required | Value shape and constraints are in its referenced local type definition. |
| file_import_rid | connectivity_models.FileImportRid | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ExecuteFileImportPermissionDenied | Could not execute the FileImport. |
| FileImportNotFound | The given FileImport could not be found. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}/execute'
```

**query_params**

```python
{}
```

**path_params**

```python
{'connectionRid': connection_rid, 'fileImportRid': file_import_rid}
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
core_models.BuildRid
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ExecuteFileImportPermissionDenied': connectivity_errors.ExecuteFileImportPermissionDenied, 'FileImportNotFound': connectivity_errors.FileImportNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `core_models.BuildRid`. Ordinary async return: `typing.Awaitable[core_models.BuildRid]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core_models.BuildRid |
| sync_raw | ApiResponse[core_models.BuildRid] |
| sync_streaming | StreamingContextManager[core_models.BuildRid] |
| async_ordinary | typing.Awaitable[core_models.BuildRid] |
| async_raw | Awaitable[AsyncApiResponse[core_models.BuildRid]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[core_models.BuildRid]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.connectivity.errors.ExecuteFileImportPermissionDenied](../../../../models/v2/connectivity/errors/ExecuteFileImportPermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.ExecuteFileImportPermissionDeniedParameters](../../../../models/v2/connectivity/errors/ExecuteFileImportPermissionDeniedParameters.md)
- [foundry_sdk.v2.connectivity.errors.FileImportNotFound](../../../../models/v2/connectivity/errors/FileImportNotFound.md)
- [foundry_sdk.v2.connectivity.errors.FileImportNotFoundParameters](../../../../models/v2/connectivity/errors/FileImportNotFoundParameters.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](../../../../models/v2/connectivity/models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.FileImportRid](../../../../models/v2/connectivity/models/FileImportRid.md)
- [foundry_sdk.v2.core.models.BuildRid](../../../../models/v2/core/models/BuildRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/FileImport.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- A Build runs asynchronously and has its own identity and status. Submission is not completion; poll with a finite budget. [Local procedure](../../../../../pipelines/releases.md).

[Part 1](execute.md)
