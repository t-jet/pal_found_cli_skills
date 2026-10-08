# v2.audit.LogFile.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all LogFiles.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

## SDK invocation contract

```python
def list(self, organization_rid: core_models.OrganizationRid, *, end_date: typing.Optional[date]=None, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, start_date: typing.Optional[date]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[audit_models.LogFile]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| organization_rid | core_models.OrganizationRid | required | Value shape and constraints are in its referenced local type definition. |
| end_date | typing.Optional[date] | None | List log files for audit events up until this date (inclusive). If absent, defaults to no end date. Use the returned `nextPageToken` to continually poll the `listLogFiles` endpoint to list the latest available logs. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| start_date | typing.Optional[date] | None | List log files for audit events starting from this date. This parameter is required for the initial request (when `pageToken` is not provided). |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ListLogFilesPermissionDenied | The provided token does not have permission to list audit log files. |
| MissingStartDate | Start date is required to list audit log files. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/audit/organizations/{organizationRid}/logFiles'
```

**query_params**

```python
{'endDate': end_date, 'pageSize': page_size, 'pageToken': page_token, 'startDate': start_date}
```

**path_params**

```python
{'organizationRid': organization_rid}
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
audit_models.ListLogFilesResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ListLogFilesPermissionDenied': audit_errors.ListLogFilesPermissionDenied, 'MissingStartDate': audit_errors.MissingStartDate}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[audit_models.LogFile]`. Ordinary async return: `core.AsyncResourceIterator[audit_models.LogFile]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[audit_models.LogFile] |
| sync_raw | ApiResponse[audit_models.ListLogFilesResponse] |
| sync_streaming | StreamingContextManager[audit_models.ListLogFilesResponse] |
| async_ordinary | core.AsyncResourceIterator[audit_models.LogFile] |
| async_raw | Awaitable[AsyncApiResponse[audit_models.ListLogFilesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[audit_models.ListLogFilesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.audit.errors.ListLogFilesPermissionDenied](../../../../models/v2/audit/errors/ListLogFilesPermissionDenied.md)
- [foundry_sdk.v2.audit.errors.ListLogFilesPermissionDeniedParameters](../../../../models/v2/audit/errors/ListLogFilesPermissionDeniedParameters.md)
- [foundry_sdk.v2.audit.errors.MissingStartDate](../../../../models/v2/audit/errors/MissingStartDate.md)
- [foundry_sdk.v2.audit.errors.MissingStartDateParameters](../../../../models/v2/audit/errors/MissingStartDateParameters.md)
- [foundry_sdk.v2.audit.models.FileId](../../../../models/v2/audit/models/FileId.md)
- [foundry_sdk.v2.audit.models.ListLogFilesResponse](../../../../models/v2/audit/models/ListLogFilesResponse.md)
- [foundry_sdk.v2.audit.models.LogFile](../../../../models/v2/audit/models/LogFile.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/audit/LogFile.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
