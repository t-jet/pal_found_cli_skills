# v2.filesystem.Space.get


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the Space with the specified rid.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.filesystem.Space.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, space_rid: filesystem_models.SpaceRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> filesystem_models.Space: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| space_rid | filesystem_models.SpaceRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| SpaceNotFound | The given Space could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/filesystem/spaces/{spaceRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'spaceRid': space_rid}
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
filesystem_models.Space
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'SpaceNotFound': filesystem_errors.SpaceNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `filesystem_models.Space`. Ordinary async return: `typing.Awaitable[filesystem_models.Space]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | filesystem_models.Space |
| sync_raw | ApiResponse[filesystem_models.Space] |
| sync_streaming | StreamingContextManager[filesystem_models.Space] |
| async_ordinary | typing.Awaitable[filesystem_models.Space] |
| async_raw | Awaitable[AsyncApiResponse[filesystem_models.Space]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[filesystem_models.Space]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.OrganizationRid](../../../../models/v2/core/models/OrganizationRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.RoleSetId](../../../../models/v2/core/models/RoleSetId.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNotFound](../../../../models/v2/filesystem/errors/SpaceNotFound.md)
- [foundry_sdk.v2.filesystem.errors.SpaceNotFoundParameters](../../../../models/v2/filesystem/errors/SpaceNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.FileSystemId](../../../../models/v2/filesystem/models/FileSystemId.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)
- [foundry_sdk.v2.filesystem.models.ResourcePath](../../../../models/v2/filesystem/models/ResourcePath.md)
- [foundry_sdk.v2.filesystem.models.Space](../../../../models/v2/filesystem/models/Space.md)
- [foundry_sdk.v2.filesystem.models.SpaceMavenIdentifier](../../../../models/v2/filesystem/models/SpaceMavenIdentifier.md)
- [foundry_sdk.v2.filesystem.models.SpaceRid](../../../../models/v2/filesystem/models/SpaceRid.md)
- [foundry_sdk.v2.filesystem.models.UsageAccountRid](../../../../models/v2/filesystem/models/UsageAccountRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/Space.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
