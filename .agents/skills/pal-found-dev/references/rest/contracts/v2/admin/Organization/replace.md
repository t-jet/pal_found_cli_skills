# v2.admin.Organization.replace


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Replace the Organization with the specified rid.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Organization.replace`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def replace(self, organization_rid: core_models.OrganizationRid, *, name: admin_models.OrganizationName, description: typing.Optional[str]=None, host: typing.Optional[admin_models.HostName]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.Organization: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| organization_rid | core_models.OrganizationRid | required | Value shape and constraints are in its referenced local type definition. |
| name | admin_models.OrganizationName | required | Value shape and constraints are in its referenced local type definition. |
| description | typing.Optional[str] | None | Value shape and constraints are in its referenced local type definition. |
| host | typing.Optional[admin_models.HostName] | None | The primary host name of the Organization. This should be used when constructing URLs for users of this Organization. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| InvalidHostName | The provided hostname must be a valid domain name. The only allowed characters are letters, numbers, periods, and hyphens. |
| OrganizationNameAlreadyExists | An organization with the same name already exists. |
| OrganizationNotFound | The given Organization could not be found. |
| ReplaceOrganizationPermissionDenied | Could not replace the Organization. |

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/admin/organizations/{organizationRid}'
```

**query_params**

```python
{}
```

**path_params**

```python
{'organizationRid': organization_rid}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
admin_models.ReplaceOrganizationRequest(name=name, host=host, description=description)
```

**response_type**

```python
admin_models.Organization
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'InvalidHostName': admin_errors.InvalidHostName, 'OrganizationNameAlreadyExists': admin_errors.OrganizationNameAlreadyExists, 'OrganizationNotFound': admin_errors.OrganizationNotFound, 'ReplaceOrganizationPermissionDenied': admin_errors.ReplaceOrganizationPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.Organization`. Ordinary async return: `typing.Awaitable[admin_models.Organization]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.Organization |
| sync_raw | ApiResponse[admin_models.Organization] |
| sync_streaming | StreamingContextManager[admin_models.Organization] |
| async_ordinary | typing.Awaitable[admin_models.Organization] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.Organization]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.Organization]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.admin.errors.InvalidHostName](../../../../models/v2/admin/errors/InvalidHostName.md)
- [foundry_sdk.v2.admin.errors.InvalidHostNameParameters](../../../../models/v2/admin/errors/InvalidHostNameParameters.md)
- [foundry_sdk.v2.admin.errors.OrganizationNameAlreadyExists](../../../../models/v2/admin/errors/OrganizationNameAlreadyExists.md)
- [foundry_sdk.v2.admin.errors.OrganizationNameAlreadyExistsParameters](../../../../models/v2/admin/errors/OrganizationNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFound](../../../../models/v2/admin/errors/OrganizationNotFound.md)
- [foundry_sdk.v2.admin.errors.OrganizationNotFoundParameters](../../../../models/v2/admin/errors/OrganizationNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.ReplaceOrganizationPermissionDenied](../../../../models/v2/admin/errors/ReplaceOrganizationPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ReplaceOrganizationPermissionDeniedParameters](../../../../models/v2/admin/errors/ReplaceOrganizationPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.HostName](../../../../models/v2/admin/models/HostName.md)
- [foundry_sdk.v2.admin.models.Organization](../../../../models/v2/admin/models/Organization.md)
- [foundry_sdk.v2.admin.models.OrganizationName](../../../../models/v2/admin/models/OrganizationName.md)
- [foundry_sdk.v2.admin.models.ReplaceOrganizationRequest](../../../../models/v2/admin/models/ReplaceOrganizationRequest.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Organization.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](replace.md)
