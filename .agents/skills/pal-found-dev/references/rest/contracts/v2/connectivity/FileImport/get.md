# v2.connectivity.FileImport.get


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the FileImport with the specified rid.

## SDK invocation contract

```python
def get(self, connection_rid: connectivity_models.ConnectionRid, file_import_rid: connectivity_models.FileImportRid, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> connectivity_models.FileImport: ...
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
| FileImportNotFound | The given FileImport could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/connectivity/connections/{connectionRid}/fileImports/{fileImportRid}'
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
connectivity_models.FileImport
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'FileImportNotFound': connectivity_errors.FileImportNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `connectivity_models.FileImport`. Ordinary async return: `typing.Awaitable[connectivity_models.FileImport]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | connectivity_models.FileImport |
| sync_raw | ApiResponse[connectivity_models.FileImport] |
| sync_streaming | StreamingContextManager[connectivity_models.FileImport] |
| async_ordinary | typing.Awaitable[connectivity_models.FileImport] |
| async_raw | Awaitable[AsyncApiResponse[connectivity_models.FileImport]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[connectivity_models.FileImport]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.connectivity.errors.FileImportNotFound](../../../../models/v2/connectivity/errors/FileImportNotFound.md)
- [foundry_sdk.v2.connectivity.errors.FileImportNotFoundParameters](../../../../models/v2/connectivity/errors/FileImportNotFoundParameters.md)
- [foundry_sdk.v2.connectivity.models.ConnectionRid](../../../../models/v2/connectivity/models/ConnectionRid.md)
- [foundry_sdk.v2.connectivity.models.FileAnyPathMatchesFilter](../../../../models/v2/connectivity/models/FileAnyPathMatchesFilter.md)
- [foundry_sdk.v2.connectivity.models.FileAtLeastCountFilter](../../../../models/v2/connectivity/models/FileAtLeastCountFilter.md)
- [foundry_sdk.v2.connectivity.models.FileChangedSinceLastUploadFilter](../../../../models/v2/connectivity/models/FileChangedSinceLastUploadFilter.md)
- [foundry_sdk.v2.connectivity.models.FileImport](../../../../models/v2/connectivity/models/FileImport.md)
- [foundry_sdk.v2.connectivity.models.FileImportCustomFilter](../../../../models/v2/connectivity/models/FileImportCustomFilter.md)
- [foundry_sdk.v2.connectivity.models.FileImportDisplayName](../../../../models/v2/connectivity/models/FileImportDisplayName.md)
- [foundry_sdk.v2.connectivity.models.FileImportFilter](../../../../models/v2/connectivity/models/FileImportFilter.md)
- [foundry_sdk.v2.connectivity.models.FileImportMode](../../../../models/v2/connectivity/models/FileImportMode.md)
- [foundry_sdk.v2.connectivity.models.FileImportRid](../../../../models/v2/connectivity/models/FileImportRid.md)
- [foundry_sdk.v2.connectivity.models.FileLastModifiedAfterFilter](../../../../models/v2/connectivity/models/FileLastModifiedAfterFilter.md)
- [foundry_sdk.v2.connectivity.models.FilePathMatchesFilter](../../../../models/v2/connectivity/models/FilePathMatchesFilter.md)
- [foundry_sdk.v2.connectivity.models.FilePathNotMatchesFilter](../../../../models/v2/connectivity/models/FilePathNotMatchesFilter.md)
- [foundry_sdk.v2.connectivity.models.FileProperty](../../../../models/v2/connectivity/models/FileProperty.md)
- [foundry_sdk.v2.connectivity.models.FileSizeFilter](../../../../models/v2/connectivity/models/FileSizeFilter.md)
- [foundry_sdk.v2.connectivity.models.FilesCountLimitFilter](../../../../models/v2/connectivity/models/FilesCountLimitFilter.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.SizeBytes](../../../../models/v2/core/models/SizeBytes.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/FileImport.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
