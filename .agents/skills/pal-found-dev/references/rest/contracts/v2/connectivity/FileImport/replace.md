# v2.connectivity.FileImport.replace


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Replace the FileImport with the specified rid.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.connectivity.Connection.FileImport.replace`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def replace(self, connection_rid: connectivity_models.ConnectionRid, file_import_rid: connectivity_models.FileImportRid, *, display_name: connectivity_models.FileImportDisplayName, file_import_filters: typing.List[connectivity_models.FileImportFilter], import_mode: connectivity_models.FileImportMode, subfolder: typing.Optional[str]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> connectivity_models.FileImport: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| connection_rid | connectivity_models.ConnectionRid | required | Value shape and constraints are in its referenced local type definition. |
| file_import_rid | connectivity_models.FileImportRid | required | Value shape and constraints are in its referenced local type definition. |
| display_name | connectivity_models.FileImportDisplayName | required | Value shape and constraints are in its referenced local type definition. |
| file_import_filters | typing.List[connectivity_models.FileImportFilter] | required | Use filters to limit which files should be imported. Filters are applied in the order they are defined. A different ordering of filters may lead to a more optimized import. [Learn more about optimizing file imports.](../../../../v2/connectivity/index.md) |
| import_mode | connectivity_models.FileImportMode | required | Value shape and constraints are in its referenced local type definition. |
| subfolder | typing.Optional[str] | None | A subfolder in the external system that will be imported. If not specified, defaults to the root folder of the external system. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| FileAtLeastCountFilterInvalidMinCount | The provided `minFilesCount` property in the FileAtLeastCountFilter must be strictly greater than 0. |
| FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports | Custom file import filters can be fetched but cannot currently be used when creating or updating file imports. |
| FileImportNotFound | The given FileImport could not be found. |
| FileSizeFilterGreaterThanCannotBeNegative | The `gt` property in the FileSizeFilter cannot be a negative number. |
| FileSizeFilterInvalidGreaterThanAndLessThanRange | The provided `gt` and `lt` properties in the FileSizeFilter are invalid. No files will ever satisfy the provided range. The value specified for `gt` must be strictly less than `lt - 1`. |
| FileSizeFilterLessThanMustBeOneByteOrLarger | The `lt` property in the FileSizeFilter must be at least 1 byte. |
| FileSizeFilterMissingGreaterThanAndLessThan | Both the `gt` and `lt` properties are missing from the FileSizeFilter. At least one of these properties must be present |
| ReplaceFileImportPermissionDenied | Could not replace the FileImport. |

## Wire request

**method**

```python
'PUT'
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
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
connectivity_models.ReplaceFileImportRequest(import_mode=import_mode, display_name=display_name, subfolder=subfolder, file_import_filters=file_import_filters)
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
{'FileAtLeastCountFilterInvalidMinCount': connectivity_errors.FileAtLeastCountFilterInvalidMinCount, 'FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports': connectivity_errors.FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports, 'FileImportNotFound': connectivity_errors.FileImportNotFound, 'FileSizeFilterGreaterThanCannotBeNegative': connectivity_errors.FileSizeFilterGreaterThanCannotBeNegative, 'FileSizeFilterInvalidGreaterThanAndLessThanRange': connectivity_errors.FileSizeFilterInvalidGreaterThanAndLessThanRange, 'FileSizeFilterLessThanMustBeOneByteOrLarger': connectivity_errors.FileSizeFilterLessThanMustBeOneByteOrLarger, 'FileSizeFilterMissingGreaterThanAndLessThan': connectivity_errors.FileSizeFilterMissingGreaterThanAndLessThan, 'ReplaceFileImportPermissionDenied': connectivity_errors.ReplaceFileImportPermissionDenied}
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
- [foundry_sdk.v2.connectivity.errors.FileAtLeastCountFilterInvalidMinCount](../../../../models/v2/connectivity/errors/FileAtLeastCountFilterInvalidMinCount.md)
- [foundry_sdk.v2.connectivity.errors.FileAtLeastCountFilterInvalidMinCountParameters](../../../../models/v2/connectivity/errors/FileAtLeastCountFilterInvalidMinCountParameters.md)
- [foundry_sdk.v2.connectivity.errors.FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports](../../../../models/v2/connectivity/errors/FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImports.md)
- [foundry_sdk.v2.connectivity.errors.FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImportsParameters](../../../../models/v2/connectivity/errors/FileImportCustomFilterCannotBeUsedToCreateOrUpdateFileImportsParameters.md)
- [foundry_sdk.v2.connectivity.errors.FileImportNotFound](../../../../models/v2/connectivity/errors/FileImportNotFound.md)
- [foundry_sdk.v2.connectivity.errors.FileImportNotFoundParameters](../../../../models/v2/connectivity/errors/FileImportNotFoundParameters.md)
- [foundry_sdk.v2.connectivity.errors.FileSizeFilterGreaterThanCannotBeNegative](../../../../models/v2/connectivity/errors/FileSizeFilterGreaterThanCannotBeNegative.md)
- [foundry_sdk.v2.connectivity.errors.FileSizeFilterGreaterThanCannotBeNegativeParameters](../../../../models/v2/connectivity/errors/FileSizeFilterGreaterThanCannotBeNegativeParameters.md)
- [foundry_sdk.v2.connectivity.errors.FileSizeFilterInvalidGreaterThanAndLessThanRange](../../../../models/v2/connectivity/errors/FileSizeFilterInvalidGreaterThanAndLessThanRange.md)
- [foundry_sdk.v2.connectivity.errors.FileSizeFilterInvalidGreaterThanAndLessThanRangeParameters](../../../../models/v2/connectivity/errors/FileSizeFilterInvalidGreaterThanAndLessThanRangeParameters.md)
- [foundry_sdk.v2.connectivity.errors.FileSizeFilterLessThanMustBeOneByteOrLarger](../../../../models/v2/connectivity/errors/FileSizeFilterLessThanMustBeOneByteOrLarger.md)
- [foundry_sdk.v2.connectivity.errors.FileSizeFilterLessThanMustBeOneByteOrLargerParameters](../../../../models/v2/connectivity/errors/FileSizeFilterLessThanMustBeOneByteOrLargerParameters.md)
- [foundry_sdk.v2.connectivity.errors.FileSizeFilterMissingGreaterThanAndLessThan](../../../../models/v2/connectivity/errors/FileSizeFilterMissingGreaterThanAndLessThan.md)
- [foundry_sdk.v2.connectivity.errors.FileSizeFilterMissingGreaterThanAndLessThanParameters](../../../../models/v2/connectivity/errors/FileSizeFilterMissingGreaterThanAndLessThanParameters.md)
- [foundry_sdk.v2.connectivity.errors.ReplaceFileImportPermissionDenied](../../../../models/v2/connectivity/errors/ReplaceFileImportPermissionDenied.md)
- [foundry_sdk.v2.connectivity.errors.ReplaceFileImportPermissionDeniedParameters](../../../../models/v2/connectivity/errors/ReplaceFileImportPermissionDeniedParameters.md)
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
- [foundry_sdk.v2.connectivity.models.ReplaceFileImportRequest](../../../../models/v2/connectivity/models/ReplaceFileImportRequest.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.SizeBytes](../../../../models/v2/core/models/SizeBytes.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/connectivity/FileImport.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- File import filters are evaluated in declared order. Review a sample path set before executing a changed import. [Local procedure](../../../../v2/connectivity/index.md).

[Part 1](replace.md)
