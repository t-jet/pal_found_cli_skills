# v2.admin.Role.get_batch


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Execute multiple get requests on Role.

The maximum batch size for this endpoint is 500.

## SDK invocation contract

```python
def get_batch(self, body: typing_extensions.Annotated[typing.List[admin_models.GetRolesBatchRequestElement], annotated_types.Len(min_length=1, max_length=500)], *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.GetRolesBatchResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| body | typing_extensions.Annotated[typing.List[admin_models.GetRolesBatchRequestElement], annotated_types.Len(min_length=1, max_length=500)] | required | Body of the request |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/admin/roles/getBatch'
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
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
body
```

**response_type**

```python
admin_models.GetRolesBatchResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.GetRolesBatchResponse`. Ordinary async return: `typing.Awaitable[admin_models.GetRolesBatchResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.GetRolesBatchResponse |
| sync_raw | ApiResponse[admin_models.GetRolesBatchResponse] |
| sync_streaming | StreamingContextManager[admin_models.GetRolesBatchResponse] |
| async_ordinary | typing.Awaitable[admin_models.GetRolesBatchResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.GetRolesBatchResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.GetRolesBatchResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.admin.models.GetRolesBatchRequestElement](../../../../models/v2/admin/models/GetRolesBatchRequestElement.md)
- [foundry_sdk.v2.admin.models.GetRolesBatchResponse](../../../../models/v2/admin/models/GetRolesBatchResponse.md)
- [foundry_sdk.v2.admin.models.Role](../../../../models/v2/admin/models/Role.md)
- [foundry_sdk.v2.admin.models.RoleDescription](../../../../models/v2/admin/models/RoleDescription.md)
- [foundry_sdk.v2.admin.models.RoleDisplayName](../../../../models/v2/admin/models/RoleDisplayName.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.RoleId](../../../../models/v2/core/models/RoleId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Role.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_batch.md)
