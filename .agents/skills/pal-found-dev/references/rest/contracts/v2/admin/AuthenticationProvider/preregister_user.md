# v2.admin.AuthenticationProvider.preregister_user


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Register a User with a given username before they log in to the platform for the first time through this
Authentication Provider. Preregistered users can be assigned to groups and roles prior to first login.

## SDK invocation contract

```python
def preregister_user(self, enrollment_rid: core_models.EnrollmentRid, authentication_provider_rid: admin_models.AuthenticationProviderRid, *, organization: core_models.OrganizationRid, username: admin_models.UserUsername, attributes: typing.Optional[typing.Dict[admin_models.AttributeName, admin_models.AttributeValues]]=None, email: typing.Optional[str]=None, family_name: typing.Optional[str]=None, given_name: typing.Optional[str]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core_models.PrincipalId: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| enrollment_rid | core_models.EnrollmentRid | required | Value shape and constraints are in its referenced local type definition. |
| authentication_provider_rid | admin_models.AuthenticationProviderRid | required | Value shape and constraints are in its referenced local type definition. |
| organization | core_models.OrganizationRid | required | The RID of the user's primary Organization. This may be changed when the user logs in for the first time depending on any configured Organization assignment rules. |
| username | admin_models.UserUsername | required | The new user's username. This must match one of the provider's supported username patterns. |
| attributes | typing.Optional[typing.Dict[admin_models.AttributeName, admin_models.AttributeValues]] | None | Value shape and constraints are in its referenced local type definition. |
| email | typing.Optional[str] | None | Value shape and constraints are in its referenced local type definition. |
| family_name | typing.Optional[str] | None | Value shape and constraints are in its referenced local type definition. |
| given_name | typing.Optional[str] | None | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AuthenticationProviderNotFound | The given AuthenticationProvider could not be found. |
| PreregisterUserPermissionDenied | Could not preregisterUser the AuthenticationProvider. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/enrollments/{enrollmentRid}/authenticationProviders/{authenticationProviderRid}/preregisterUser'
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
admin_models.PreregisterUserRequest(username=username, organization=organization, given_name=given_name, family_name=family_name, email=email, attributes=attributes)
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
{'AuthenticationProviderNotFound': admin_errors.AuthenticationProviderNotFound, 'PreregisterUserPermissionDenied': admin_errors.PreregisterUserPermissionDenied}
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
- [foundry_sdk.v2.admin.errors.PreregisterUserPermissionDenied](../../../../models/v2/admin/errors/PreregisterUserPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.PreregisterUserPermissionDeniedParameters](../../../../models/v2/admin/errors/PreregisterUserPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.AttributeName](../../../../models/v2/admin/models/AttributeName.md)
- [foundry_sdk.v2.admin.models.AttributeValue](../../../../models/v2/admin/models/AttributeValue.md)
- [foundry_sdk.v2.admin.models.AttributeValues](../../../../models/v2/admin/models/AttributeValues.md)
- [foundry_sdk.v2.admin.models.AuthenticationProviderRid](../../../../models/v2/admin/models/AuthenticationProviderRid.md)
- [foundry_sdk.v2.admin.models.PreregisterUserRequest](../../../../models/v2/admin/models/PreregisterUserRequest.md)
- [foundry_sdk.v2.admin.models.UserUsername](../../../../models/v2/admin/models/UserUsername.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../../../models/v2/core/models/EnrollmentRid.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/AuthenticationProvider.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](preregister_user.md)
