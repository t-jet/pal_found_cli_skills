# v2.admin.EnrollmentRoleAssignment.list


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List all principals who are assigned a role for the given Enrollment.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Enrollment.EnrollmentRoleAssignment.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, enrollment_rid: core_models.EnrollmentRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.ListEnrollmentRoleAssignmentsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| enrollment_rid | core_models.EnrollmentRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| EnrollmentNotFound | The given Enrollment could not be found. |
| ListEnrollmentRoleAssignmentsPermissionDenied | The provided token does not have permission to list assigned roles for this enrollment. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/enrollments/{enrollmentRid}/roleAssignments'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'enrollmentRid': enrollment_rid}
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
admin_models.ListEnrollmentRoleAssignmentsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'EnrollmentNotFound': admin_errors.EnrollmentNotFound, 'ListEnrollmentRoleAssignmentsPermissionDenied': admin_errors.ListEnrollmentRoleAssignmentsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.ListEnrollmentRoleAssignmentsResponse`. Ordinary async return: `typing.Awaitable[admin_models.ListEnrollmentRoleAssignmentsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.ListEnrollmentRoleAssignmentsResponse |
| sync_raw | ApiResponse[admin_models.ListEnrollmentRoleAssignmentsResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListEnrollmentRoleAssignmentsResponse] |
| async_ordinary | typing.Awaitable[admin_models.ListEnrollmentRoleAssignmentsResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListEnrollmentRoleAssignmentsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListEnrollmentRoleAssignmentsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.EnrollmentNotFound](../../../../models/v2/admin/errors/EnrollmentNotFound.md)
- [foundry_sdk.v2.admin.errors.EnrollmentNotFoundParameters](../../../../models/v2/admin/errors/EnrollmentNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.ListEnrollmentRoleAssignmentsPermissionDenied](../../../../models/v2/admin/errors/ListEnrollmentRoleAssignmentsPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ListEnrollmentRoleAssignmentsPermissionDeniedParameters](../../../../models/v2/admin/errors/ListEnrollmentRoleAssignmentsPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.EnrollmentRoleAssignment](../../../../models/v2/admin/models/EnrollmentRoleAssignment.md)
- [foundry_sdk.v2.admin.models.ListEnrollmentRoleAssignmentsResponse](../../../../models/v2/admin/models/ListEnrollmentRoleAssignmentsResponse.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../../../models/v2/core/models/EnrollmentRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.PrincipalType](../../../../models/v2/core/models/PrincipalType.md)
- [foundry_sdk.v2.core.models.RoleId](../../../../models/v2/core/models/RoleId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/EnrollmentRoleAssignment.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
