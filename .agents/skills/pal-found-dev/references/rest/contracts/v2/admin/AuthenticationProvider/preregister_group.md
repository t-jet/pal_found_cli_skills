# v2.admin.AuthenticationProvider.preregister_group


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Register a Group with a given name before any users with this group log in through this Authentication Provider.
Preregistered groups can be used anywhere other groups are used in the platform.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Enrollment.AuthenticationProvider.preregister_group`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def preregister_group(self, enrollment_rid: core_models.EnrollmentRid, authentication_provider_rid: admin_models.AuthenticationProviderRid, *, name: admin_models.GroupName, organizations: typing.List[core_models.OrganizationRid], preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core_models.PrincipalId: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| enrollment_rid | core_models.EnrollmentRid | required | Value shape and constraints are in its referenced local type definition. |
| authentication_provider_rid | admin_models.AuthenticationProviderRid | required | Value shape and constraints are in its referenced local type definition. |
| name | admin_models.GroupName | required | Value shape and constraints are in its referenced local type definition. |
| organizations | typing.List[core_models.OrganizationRid] | required | The RIDs of the Organizations that can view this group. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AuthenticationProviderNotFound | The given AuthenticationProvider could not be found. |
| PreregisterGroupPermissionDenied | Could not preregisterGroup the AuthenticationProvider. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterGroup'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'enrollmentRid': enrollment_rid, 'authenticationProviderRid': authentication_provider_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
admin_models.PreregisterGroupRequest(name=name, organizations=organizations)
```

**response_type**

```python
core_models.PrincipalId
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AuthenticationProviderNotFound': admin_errors.AuthenticationProviderNotFound, 'PreregisterGroupPermissionDenied': admin_errors.PreregisterGroupPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `core_models.PrincipalId`. Ordinary async return: `typing.Awaitable[core_models.PrincipalId]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core_models.PrincipalId |
| sync_raw | ApiResponse[core_models.PrincipalId] |
| sync_streaming | StreamingContextManager[core_models.PrincipalId] |
| async_ordinary | typing.Awaitable[core_models.PrincipalId] |
| async_raw | Awaitable[AsyncApiResponse[core_models.PrincipalId]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[core_models.PrincipalId]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.AuthenticationProviderNotFound](../../../../models/v2/admin/errors/AuthenticationProviderNotFound.md)
- [foundry_sdk.v2.admin.errors.AuthenticationProviderNotFoundParameters](../../../../models/v2/admin/errors/AuthenticationProviderNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.PreregisterGroupPermissionDenied](../../../../models/v2/admin/errors/PreregisterGroupPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.PreregisterGroupPermissionDeniedParameters](../../../../models/v2/admin/errors/PreregisterGroupPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.AuthenticationProviderRid](../../../../models/v2/admin/models/AuthenticationProviderRid.md)
- [foundry_sdk.v2.admin.models.GroupName](../../../../models/v2/admin/models/GroupName.md)
- [foundry_sdk.v2.admin.models.PreregisterGroupRequest](../../../../models/v2/admin/models/PreregisterGroupRequest.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../../../models/v2/core/models/EnrollmentRid.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/AuthenticationProvider.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](preregister_group.md)
