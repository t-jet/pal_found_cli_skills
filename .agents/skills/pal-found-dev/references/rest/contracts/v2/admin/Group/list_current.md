# v2.admin.Group.list_current


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Returns all Groups which contain the current user as a direct or transitive member. For example if the current user is a member of Group A and Group A is a member of Group B, this endpoint will return Group A and Group B.

Unlike the list Group Memberships endpoint which requires the `api:admin-read` scope, this endpoint
does not require any particular scopes and can be used by any authenticated user to retrieve their own
group memberships.

## SDK invocation contract

```python
def list_current(self, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.ListCurrentGroupsResponse: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ListCurrentGroupsPermissionDenied | Could not listCurrent the Group. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/groups/listCurrent'
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
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
admin_models.ListCurrentGroupsResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ListCurrentGroupsPermissionDenied': admin_errors.ListCurrentGroupsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.ListCurrentGroupsResponse`. Ordinary async return: `typing.Awaitable[admin_models.ListCurrentGroupsResponse]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.ListCurrentGroupsResponse |
| sync_raw | ApiResponse[admin_models.ListCurrentGroupsResponse] |
| sync_streaming | StreamingContextManager[admin_models.ListCurrentGroupsResponse] |
| async_ordinary | typing.Awaitable[admin_models.ListCurrentGroupsResponse] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.ListCurrentGroupsResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.ListCurrentGroupsResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.ListCurrentGroupsPermissionDenied](../../../../models/v2/admin/errors/ListCurrentGroupsPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ListCurrentGroupsPermissionDeniedParameters](../../../../models/v2/admin/errors/ListCurrentGroupsPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.AttributeName](../../../../models/v2/admin/models/AttributeName.md)
- [foundry_sdk.v2.admin.models.AttributeValue](../../../../models/v2/admin/models/AttributeValue.md)
- [foundry_sdk.v2.admin.models.AttributeValues](../../../../models/v2/admin/models/AttributeValues.md)
- [foundry_sdk.v2.admin.models.Group](../../../../models/v2/admin/models/Group.md)
- [foundry_sdk.v2.admin.models.GroupName](../../../../models/v2/admin/models/GroupName.md)
- [foundry_sdk.v2.admin.models.ListCurrentGroupsResponse](../../../../models/v2/admin/models/ListCurrentGroupsResponse.md)
- [foundry_sdk.v2.core.models.GroupId](../../../../models/v2/core/models/GroupId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.Realm](../../../../models/v2/core/models/Realm.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Group.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list_current.md)
