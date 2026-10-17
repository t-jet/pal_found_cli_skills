# v2.admin.AuthenticationProvider.list


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all AuthenticationProviders.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Enrollment.AuthenticationProvider.list`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def list(self, enrollment_rid: core_models.EnrollmentRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.ListAuthenticationProvidersResponse: ...
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

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/enrollments/{enrollmentRid}/authenticationProviders'
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
admin_models.ListAuthenticationProvidersResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'EnrollmentNotFound': admin_errors.EnrollmentNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.ListAuthenticationProvidersResponse`. Ordinary async return: `typing.Awaitable[admin_models.ListAuthenticationProvidersResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.ListAuthenticationProvidersResponse |
| sync_raw | ApiResponse[admin_models.ListAuthenticationProvidersResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListAuthenticationProvidersResponse] |
| async_ordinary | typing.Awaitable[admin_models.ListAuthenticationProvidersResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListAuthenticationProvidersResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListAuthenticationProvidersResponse]] |

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
- [foundry_sdk.v2.admin.models.AuthenticationProtocol](../../../../models/v2/admin/models/AuthenticationProtocol.md)
- [foundry_sdk.v2.admin.models.AuthenticationProvider](../../../../models/v2/admin/models/AuthenticationProvider.md)
- [foundry_sdk.v2.admin.models.AuthenticationProviderEnabled](../../../../models/v2/admin/models/AuthenticationProviderEnabled.md)
- [foundry_sdk.v2.admin.models.AuthenticationProviderName](../../../../models/v2/admin/models/AuthenticationProviderName.md)
- [foundry_sdk.v2.admin.models.AuthenticationProviderRid](../../../../models/v2/admin/models/AuthenticationProviderRid.md)
- [foundry_sdk.v2.admin.models.CertificateInfo](../../../../models/v2/admin/models/CertificateInfo.md)
- [foundry_sdk.v2.admin.models.CertificateUsageType](../../../../models/v2/admin/models/CertificateUsageType.md)
- [foundry_sdk.v2.admin.models.HostName](../../../../models/v2/admin/models/HostName.md)
- [foundry_sdk.v2.admin.models.ListAuthenticationProvidersResponse](../../../../models/v2/admin/models/ListAuthenticationProvidersResponse.md)
- [foundry_sdk.v2.admin.models.OidcAuthenticationProtocol](../../../../models/v2/admin/models/OidcAuthenticationProtocol.md)
- [foundry_sdk.v2.admin.models.SamlAuthenticationProtocol](../../../../models/v2/admin/models/SamlAuthenticationProtocol.md)
- [foundry_sdk.v2.admin.models.SamlServiceProviderMetadata](../../../../models/v2/admin/models/SamlServiceProviderMetadata.md)
- [foundry_sdk.v2.core.models.EnrollmentRid](../../../../models/v2/core/models/EnrollmentRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.Realm](../../../../models/v2/core/models/Realm.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/AuthenticationProvider.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
