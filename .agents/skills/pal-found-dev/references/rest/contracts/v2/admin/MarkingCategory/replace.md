# v2.admin.MarkingCategory.replace


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Replace the MarkingCategory with the specified id.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.admin.MarkingCategory.replace`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def replace(self, marking_category_id: admin_models.MarkingCategoryId, *, description: admin_models.MarkingCategoryDescription, name: admin_models.MarkingCategoryName, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.MarkingCategory: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| marking_category_id | admin_models.MarkingCategoryId | required | Value shape and constraints are in its referenced local type definition. |
| description | admin_models.MarkingCategoryDescription | required | Value shape and constraints are in its referenced local type definition. |
| name | admin_models.MarkingCategoryName | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetMarkingCategoryPermissionDenied | The provided token does not have permission to view the marking category. |
| MarkingCategoryNotFound | The given MarkingCategory could not be found. |
| ReplaceMarkingCategoryPermissionDenied | Could not replace the MarkingCategory. |

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/admin/markingCategories/{markingCategoryId}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'markingCategoryId': marking_category_id}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
admin_models.ReplaceMarkingCategoryRequest(name=name, description=description)
```

**response_type**

```python
admin_models.MarkingCategory
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetMarkingCategoryPermissionDenied': admin_errors.GetMarkingCategoryPermissionDenied, 'MarkingCategoryNotFound': admin_errors.MarkingCategoryNotFound, 'ReplaceMarkingCategoryPermissionDenied': admin_errors.ReplaceMarkingCategoryPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.MarkingCategory`. Ordinary async return: `typing.Awaitable[admin_models.MarkingCategory]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.MarkingCategory |
| sync_raw | ApiResponse[admin_models.MarkingCategory] |
| sync_streaming | StreamingContextManager[admin_models.MarkingCategory] |
| async_ordinary | typing.Awaitable[admin_models.MarkingCategory] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.MarkingCategory]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.MarkingCategory]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.GetMarkingCategoryPermissionDenied](../../../../models/v2/admin/errors/GetMarkingCategoryPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetMarkingCategoryPermissionDeniedParameters](../../../../models/v2/admin/errors/GetMarkingCategoryPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingCategoryNotFound](../../../../models/v2/admin/errors/MarkingCategoryNotFound.md)
- [foundry_sdk.v2.admin.errors.MarkingCategoryNotFoundParameters](../../../../models/v2/admin/errors/MarkingCategoryNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.ReplaceMarkingCategoryPermissionDenied](../../../../models/v2/admin/errors/ReplaceMarkingCategoryPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ReplaceMarkingCategoryPermissionDeniedParameters](../../../../models/v2/admin/errors/ReplaceMarkingCategoryPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.MarkingCategory](../../../../models/v2/admin/models/MarkingCategory.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryDescription](../../../../models/v2/admin/models/MarkingCategoryDescription.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryId](../../../../models/v2/admin/models/MarkingCategoryId.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryName](../../../../models/v2/admin/models/MarkingCategoryName.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryType](../../../../models/v2/admin/models/MarkingCategoryType.md)
- [foundry_sdk.v2.admin.models.MarkingType](../../../../models/v2/admin/models/MarkingType.md)
- [foundry_sdk.v2.admin.models.ReplaceMarkingCategoryRequest](../../../../models/v2/admin/models/ReplaceMarkingCategoryRequest.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/MarkingCategory.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](replace.md)
