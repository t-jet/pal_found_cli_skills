# v2.admin.Role.get


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the Role with the specified id.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.Role.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, role_id: core_models.RoleId, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.Role: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| role_id | core_models.RoleId | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| RoleNotFound | The given Role could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/roles/{roleId}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'roleId': role_id}
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
admin_models.Role
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'RoleNotFound': admin_errors.RoleNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.Role`. Ordinary async return: `typing.Awaitable[admin_models.Role]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.Role |
| sync_raw | ApiResponse[admin_models.Role] |
| sync_streaming | StreamingContextManager[admin_models.Role] |
| async_ordinary | typing.Awaitable[admin_models.Role] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.Role]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.Role]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.admin.errors.RoleNotFound](../../../../models/v2/admin/errors/RoleNotFound.md)
- [foundry_sdk.v2.admin.errors.RoleNotFoundParameters](../../../../models/v2/admin/errors/RoleNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.Role](../../../../models/v2/admin/models/Role.md)
- [foundry_sdk.v2.admin.models.RoleDescription](../../../../models/v2/admin/models/RoleDescription.md)
- [foundry_sdk.v2.admin.models.RoleDisplayName](../../../../models/v2/admin/models/RoleDisplayName.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.RoleId](../../../../models/v2/core/models/RoleId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Role.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
