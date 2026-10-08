# v2.admin.GroupMembershipExpirationPolicy.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the GroupMembershipExpirationPolicy.

## SDK invocation contract

```python
def get(self, group_id: core_models.GroupId, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> admin_models.GroupMembershipExpirationPolicy: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| group_id | core_models.GroupId | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| GroupMembershipExpirationPolicyNotFound | The given GroupMembershipExpirationPolicy could not be found. |
| GroupNotFound | The given Group could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/admin/groups/{groupId}/membershipExpirationPolicy'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'groupId': group_id}
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
admin_models.GroupMembershipExpirationPolicy
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'GroupMembershipExpirationPolicyNotFound': admin_errors.GroupMembershipExpirationPolicyNotFound, 'GroupNotFound': admin_errors.GroupNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `admin_models.GroupMembershipExpirationPolicy`. Ordinary async return: `typing.Awaitable[admin_models.GroupMembershipExpirationPolicy]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | admin_models.GroupMembershipExpirationPolicy |
| sync_raw | ApiResponse[admin_models.GroupMembershipExpirationPolicy] |
| sync_streaming | StreamingContextManager[admin_models.GroupMembershipExpirationPolicy] |
| async_ordinary | typing.Awaitable[admin_models.GroupMembershipExpirationPolicy] |
| async_raw | Awaitable[AsyncApiResponse[admin_models.GroupMembershipExpirationPolicy]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[admin_models.GroupMembershipExpirationPolicy]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.admin.errors.GroupMembershipExpirationPolicyNotFound](../../../../models/v2/admin/errors/GroupMembershipExpirationPolicyNotFound.md)
- [foundry_sdk.v2.admin.errors.GroupMembershipExpirationPolicyNotFoundParameters](../../../../models/v2/admin/errors/GroupMembershipExpirationPolicyNotFoundParameters.md)
- [foundry_sdk.v2.admin.errors.GroupNotFound](../../../../models/v2/admin/errors/GroupNotFound.md)
- [foundry_sdk.v2.admin.errors.GroupNotFoundParameters](../../../../models/v2/admin/errors/GroupNotFoundParameters.md)
- [foundry_sdk.v2.admin.models.GroupMembershipExpiration](../../../../models/v2/admin/models/GroupMembershipExpiration.md)
- [foundry_sdk.v2.admin.models.GroupMembershipExpirationPolicy](../../../../models/v2/admin/models/GroupMembershipExpirationPolicy.md)
- [foundry_sdk.v2.core.models.DurationSeconds](../../../../models/v2/core/models/DurationSeconds.md)
- [foundry_sdk.v2.core.models.GroupId](../../../../models/v2/core/models/GroupId.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/admin/GroupMembershipExpirationPolicy.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
