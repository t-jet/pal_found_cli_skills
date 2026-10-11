# v2.admin.User.get_batch


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Execute multiple get requests on User.

The maximum batch size for this endpoint is 500.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.User.get_batch`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get_batch(self, body: typing_extensions.Annotated[typing.List[admin_models.GetUsersBatchRequestElement], annotated_types.Len(min_length=1, max_length=500)], *, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.GetUsersBatchResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| body | typing_extensions.Annotated[typing.List[admin_models.GetUsersBatchRequestElement], annotated_types.Len(min_length=1, max_length=500)] | required | Body of the request |
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
'/v2/admin/users/getBatch'
```

**query_params**

```python
{}
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
admin_models.GetUsersBatchResponse
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

Ordinary sync return: `admin_models.GetUsersBatchResponse`. Ordinary async return: `typing.Awaitable[admin_models.GetUsersBatchResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.GetUsersBatchResponse |
| sync_raw | ApiResponse[admin_models.GetUsersBatchResponse] |
| sync_streaming | StreamingContextManager[admin_models.GetUsersBatchResponse] |
| async_ordinary | typing.Awaitable[admin_models.GetUsersBatchResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.GetUsersBatchResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.GetUsersBatchResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.models.AttributeName](../../../../models/v2/admin/models/AttributeName.md)
- [foundry_sdk.v2.admin.models.AttributeValue](../../../../models/v2/admin/models/AttributeValue.md)
- [foundry_sdk.v2.admin.models.AttributeValues](../../../../models/v2/admin/models/AttributeValues.md)
- [foundry_sdk.v2.admin.models.GetUsersBatchRequestElement](../../../../models/v2/admin/models/GetUsersBatchRequestElement.md)
- [foundry_sdk.v2.admin.models.GetUsersBatchResponse](../../../../models/v2/admin/models/GetUsersBatchResponse.md)
- [foundry_sdk.v2.admin.models.User](../../../../models/v2/admin/models/User.md)
- [foundry_sdk.v2.admin.models.UserUsername](../../../../models/v2/admin/models/UserUsername.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.Realm](../../../../models/v2/core/models/Realm.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)
- [foundry_sdk.v2.core.models.UserStatus](../../../../models/v2/core/models/UserStatus.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/User.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get_batch.md)
