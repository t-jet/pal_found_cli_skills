# v2.admin.Marking.replace


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Replace the Marking with the specified id.

## SDK invocation contract

```python
def replace(self, marking_id: core_models.MarkingId, *, name: admin_models.MarkingName, description: typing.Optional[str]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.Marking: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| marking_id | core_models.MarkingId | required | Value shape and constraints are in its referenced local type definition. |
| name | admin_models.MarkingName | required | Value shape and constraints are in its referenced local type definition. |
| description | typing.Optional[str] | None | Value shape and constraints are in its referenced local type definition. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GetMarkingCategoryPermissionDenied | The provided token does not have permission to view the marking category. |
| GetMarkingPermissionDenied | The provided token does not have permission to view the marking. |
| MarkingNameInCategoryAlreadyExists | A marking with the same name already exists in the category. |
| MarkingNameIsEmpty | The marking name is empty. |
| MarkingNotFound | The given Marking could not be found. |
| ReplaceMarkingPermissionDenied | Could not replace the Marking. |

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/admin/markings/{markingId}'
```

**query_params**

```python
{}
```

**path_params**

```python
{'markingId': marking_id}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
admin_models.ReplaceMarkingRequest(name=name, description=description)
```

**response_type**

```python
admin_models.Marking
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GetMarkingCategoryPermissionDenied': admin_errors.GetMarkingCategoryPermissionDenied, 'GetMarkingPermissionDenied': admin_errors.GetMarkingPermissionDenied, 'MarkingNameInCategoryAlreadyExists': admin_errors.MarkingNameInCategoryAlreadyExists, 'MarkingNameIsEmpty': admin_errors.MarkingNameIsEmpty, 'MarkingNotFound': admin_errors.MarkingNotFound, 'ReplaceMarkingPermissionDenied': admin_errors.ReplaceMarkingPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.Marking`. Ordinary async return: `typing.Awaitable[admin_models.Marking]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.Marking |
| sync_raw | ApiResponse[admin_models.Marking] |
| sync_streaming | StreamingContextManager[admin_models.Marking] |
| async_ordinary | typing.Awaitable[admin_models.Marking] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.Marking]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.Marking]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.GetMarkingCategoryPermissionDenied](../../../../models/v2/admin/errors/GetMarkingCategoryPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetMarkingCategoryPermissionDeniedParameters](../../../../models/v2/admin/errors/GetMarkingCategoryPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.GetMarkingPermissionDenied](../../../../models/v2/admin/errors/GetMarkingPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.GetMarkingPermissionDeniedParameters](../../../../models/v2/admin/errors/GetMarkingPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingNameInCategoryAlreadyExists](../../../../models/v2/admin/errors/MarkingNameInCategoryAlreadyExists.md)
- [foundry_sdk.v2.admin.errors.MarkingNameInCategoryAlreadyExistsParameters](../../../../models/v2/admin/errors/MarkingNameInCategoryAlreadyExistsParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingNameIsEmpty](../../../../models/v2/admin/errors/MarkingNameIsEmpty.md)
- [foundry_sdk.v2.admin.errors.MarkingNameIsEmptyParameters](../../../../models/v2/admin/errors/MarkingNameIsEmptyParameters.md)
- [foundry_sdk.v2.admin.errors.MarkingNotFound](../../../../models/v2/admin/errors/MarkingNotFound.md)
- [foundry_sdk.v2.admin.errors.MarkingNotFoundParameters](../../../../models/v2/admin/errors/MarkingNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.ReplaceMarkingPermissionDenied](../../../../models/v2/admin/errors/ReplaceMarkingPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ReplaceMarkingPermissionDeniedParameters](../../../../models/v2/admin/errors/ReplaceMarkingPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.Marking](../../../../models/v2/admin/models/Marking.md)
- [foundry_sdk.v2.admin.models.MarkingCategoryId](../../../../models/v2/admin/models/MarkingCategoryId.md)
- [foundry_sdk.v2.admin.models.MarkingName](../../../../models/v2/admin/models/MarkingName.md)
- [foundry_sdk.v2.admin.models.ReplaceMarkingRequest](../../../../models/v2/admin/models/ReplaceMarkingRequest.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.MarkingId](../../../../models/v2/core/models/MarkingId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Marking.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](replace.md)
