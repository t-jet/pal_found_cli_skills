# v2.audit.LogFile.content


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning



## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.audit.Organization.LogFile.content`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def content(self, organization_rid: core_models.OrganizationRid, log_file_id: audit_models.FileId, *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> bytes: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| organization_rid | core_models.OrganizationRid | required | Value shape and constraints are in its referenced local type definition. |
| log_file_id | audit_models.FileId | required | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetLogFileContentPermissionDenied | Could not content the LogFile. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/audit/organizations/{organizationRid}/logFiles/{logFileId}/content'
```

**query_params**

```python
{}
```

**path_params**

```python
{'organizationRid': organization_rid, 'logFileId': log_file_id}
```

**header_params**

```python
{'Accept': 'application/octet-stream'}
```

**body**

```python
None
```

**response_type**

```python
bytes
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetLogFileContentPermissionDenied': audit_errors.GetLogFileContentPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `bytes`. Ordinary async return: `typing.Awaitable[bytes]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | bytes |
| sync_raw | ApiResponse[bytes] |
| sync_streaming | StreamingContextManager[bytes] |
| async_ordinary | typing.Awaitable[bytes] |
| async_raw | Awaitable[AsyncApiResponse[bytes]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[bytes]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.audit.errors.GetLogFileContentPermissionDenied](../../../../models/v2/audit/errors/GetLogFileContentPermissionDenied.md)
- [foundry_sdk.v2.audit.errors.GetLogFileContentPermissionDeniedParameters](../../../../models/v2/audit/errors/GetLogFileContentPermissionDeniedParameters.md)
- [foundry_sdk.v2.audit.models.FileId](../../../../models/v2/audit/models/FileId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/audit/LogFile.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](content.md)
