# v2.admin.Group.replace


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

When replacing groups, you must send all attributes that begin with `multipass:` exactly as they appear when calling the Get Group endpoint.

## SDK invocation contract

```python
def replace(self, group_id: core_models.GroupId, *, attributes: typing.Dict[admin_models.AttributeName, admin_models.AttributeValues], name: admin_models.GroupName, organizations: typing.List[core_models.OrganizationRid], description: typing.Optional[str]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.Group: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| group_id | core_models.GroupId | required | Value shape and constraints are in its referenced local type definition. |
| attributes | typing.Dict[admin_models.AttributeName, admin_models.AttributeValues] | required | A map of the Group's attributes. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are subject to change. |
| name | admin_models.GroupName | required | The name of the Group. |
| organizations | typing.List[core_models.OrganizationRid] | required | The RIDs of the Organizations whose members can see this group. At least one Organization RID must be listed. |
| description | typing.Optional[str] | None | A description of the Group. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| AttributesNotEditable | One or more attributes are not editable. Attributes prefixed with "multipass:" are reserved for internal use by Foundry and are not editable. |
| GroupNameAlreadyExists | A group with this name already exists |
| GroupNotFound | The given Group could not be found. |
| InvalidGroupOrganizations | At least one Organization RID must be provided for a group |
| ReplaceGroupPermissionDenied | Could not replace the Group. |

## Wire request

**method**

```python
'PUT'
```

**resource_path**

```python
'/v2/admin/groups/{groupId}'
```

**query_params**

```python
{}
```

**path_params**

```python
{'groupId': group_id}
```

**header_params**

```python
{'Content-Type': 'application/json', 'Accept': 'application/json'}
```

**body**

```python
admin_models.ReplaceGroupRequest(name=name, organizations=organizations, description=description, attributes=attributes)
```

**response_type**

```python
admin_models.Group
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'AttributesNotEditable': admin_errors.AttributesNotEditable, 'GroupNameAlreadyExists': admin_errors.GroupNameAlreadyExists, 'GroupNotFound': admin_errors.GroupNotFound, 'InvalidGroupOrganizations': admin_errors.InvalidGroupOrganizations, 'ReplaceGroupPermissionDenied': admin_errors.ReplaceGroupPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.Group`. Ordinary async return: `typing.Awaitable[admin_models.Group]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.Group |
| sync_raw | ApiResponse[admin_models.Group] |
| sync_streaming | StreamingContextManager[admin_models.Group] |
| async_ordinary | typing.Awaitable[admin_models.Group] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.Group]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.Group]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.AttributesNotEditable](../../../../models/v2/admin/errors/AttributesNotEditable.md)
- [foundry_sdk.v2.admin.errors.AttributesNotEditableParameters](../../../../models/v2/admin/errors/AttributesNotEditableParameters.md)
- [foundry_sdk.v2.admin.errors.GroupNameAlreadyExists](../../../../models/v2/admin/errors/GroupNameAlreadyExists.md)
- [foundry_sdk.v2.admin.errors.GroupNameAlreadyExistsParameters](../../../../models/v2/admin/errors/GroupNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.admin.errors.GroupNotFound](../../../../models/v2/admin/errors/GroupNotFound.md)
- [foundry_sdk.v2.admin.errors.GroupNotFoundParameters](../../../../models/v2/admin/errors/GroupNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.InvalidGroupOrganizations](../../../../models/v2/admin/errors/InvalidGroupOrganizations.md)
- [foundry_sdk.v2.admin.errors.InvalidGroupOrganizationsParameters](../../../../models/v2/admin/errors/InvalidGroupOrganizationsParameters.md)
- [foundry_sdk.v2.admin.errors.ReplaceGroupPermissionDenied](../../../../models/v2/admin/errors/ReplaceGroupPermissionDenied.md)
- [foundry_sdk.v2.admin.errors.ReplaceGroupPermissionDeniedParameters](../../../../models/v2/admin/errors/ReplaceGroupPermissionDeniedParameters.md)
- [foundry_sdk.v2.admin.models.AttributeName](../../../../models/v2/admin/models/AttributeName.md)
- [foundry_sdk.v2.admin.models.AttributeValue](../../../../models/v2/admin/models/AttributeValue.md)
- [foundry_sdk.v2.admin.models.AttributeValues](../../../../models/v2/admin/models/AttributeValues.md)
- [foundry_sdk.v2.admin.models.Group](../../../../models/v2/admin/models/Group.md)
- [foundry_sdk.v2.admin.models.GroupName](../../../../models/v2/admin/models/GroupName.md)
- [foundry_sdk.v2.admin.models.ReplaceGroupRequest](../../../../models/v2/admin/models/ReplaceGroupRequest.md)
- [foundry_sdk.v2.core.models.GroupId](../../../../models/v2/core/models/GroupId.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.Realm](../../../../models/v2/core/models/Realm.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/Group.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](replace.md)
