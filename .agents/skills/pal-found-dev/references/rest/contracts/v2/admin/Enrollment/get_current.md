# v2.admin.Enrollment.get_current


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Returns the Enrollment associated with the current User's primary organization.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Enrollment.get_current`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_current(self, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.Enrollment: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| EnrollmentNotFound | The given Enrollment could not be found. |
| GetCurrentEnrollmentPermissionDenied | Could not getCurrent the Enrollment. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/enrollments/getCurrent'
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
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
admin_models.Enrollment
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'EnrollmentNotFound': admin_errors.EnrollmentNotFound, 'GetCurrentEnrollmentPermissionDenied': admin_errors.GetCurrentEnrollmentPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.Enrollment`. Ordinary async return: `typing.Awaitable[admin_models.Enrollment]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.Enrollment |
| sync_raw | ApiResponse[admin_models.Enrollment] |
| sync_streaming | StreamingContextManager[admin_models.Enrollment] |
| async_ordinary | typing.Awaitable[admin_models.Enrollment] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.Enrollment]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.Enrollment]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.admin.errors.EnrollmentNotFound](../../../../models/v2/admin/errors/EnrollmentNotFound.md)
- [foundry_sdk.v2.admin.errors.EnrollmentNotFoundParameters](../../../../models/v2/admin/errors/EnrollmentNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.GetCurrentEnrollmentPermissionDenied](../../../../models/v2/admin/errors/GetCurrentEnrollmentPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetCurrentEnrollmentPermissionDeniedParameters](../../../../models/v2/admin/errors/GetCurrentEnrollmentPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.Enrollment](../../../../models/v2/admin/models/Enrollment.md)
- [foundry_sdk.v2.admin.models.EnrollmentName](../../../../models/v2/admin/models/EnrollmentName.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../../../models/v2/core/models/EnrollmentRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Enrollment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_current.md)
