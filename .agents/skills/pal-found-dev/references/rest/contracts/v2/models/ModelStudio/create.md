# v2.models.ModelStudio.create


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new Model Studio.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.ModelStudio.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, *, name: str, parent_folder_rid: filesystem_models.FolderRid, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.ModelStudio: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| name | str | required | The name of the Model Studio. |
| parent_folder_rid | filesystem_models.FolderRid | required | The RID of the parent folder where the studio will be created. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateModelStudioPermissionDenied | Permission denied to create a Model Studio. |
| InvalidDisplayName | The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters. |
| InvalidModelStudioCreateRequest | The request to create a Model Studio contains invalid arguments. |
| ResourceNameAlreadyExists | The provided resource name is already in use by another resource in the same folder. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/models/modelStudios'
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
models_models.CreateModelStudioRequest(name=name, parent_folder_rid=parent_folder_rid)
```

**response_type**

```python
models_models.ModelStudio
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CreateModelStudioPermissionDenied': models_errors.CreateModelStudioPermissionDenied, 'InvalidDisplayName': filesystem_errors.InvalidDisplayName, 'InvalidModelStudioCreateRequest': models_errors.InvalidModelStudioCreateRequest, 'ResourceNameAlreadyExists': filesystem_errors.ResourceNameAlreadyExists}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.ModelStudio`. Ordinary async return: `typing.Awaitable[models_models.ModelStudio]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.ModelStudio |
| sync_raw | ApiResponse[models_models.ModelStudio] |
| sync_streaming | StreamingContextManager[models_models.ModelStudio] |
| async_ordinary | typing.Awaitable[models_models.ModelStudio] |
| async_raw | Awaitable[AsyncApiResponse[models_models.ModelStudio]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.ModelStudio]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayName](../../../../models/v2/filesystem/errors/InvalidDisplayName.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayNameParameters](../../../../models/v2/filesystem/errors/InvalidDisplayNameParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExists](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExists.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExistsParameters](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)
- [foundry_sdk.v2.models.errors.CreateModelStudioPermissionDenied](../../../../models/v2/models/errors/CreateModelStudioPermissionDenied.md)
- [foundry_sdk.v2.models.errors.CreateModelStudioPermissionDeniedParameters](../../../../models/v2/models/errors/CreateModelStudioPermissionDeniedParameters.md)
- [foundry_sdk.v2.models.errors.InvalidModelStudioCreateRequest](../../../../models/v2/models/errors/InvalidModelStudioCreateRequest.md)
- [foundry_sdk.v2.models.errors.InvalidModelStudioCreateRequestParameters](../../../../models/v2/models/errors/InvalidModelStudioCreateRequestParameters.md)
- [foundry_sdk.v2.models.models.CreateModelStudioRequest](../../../../models/v2/models/models/CreateModelStudioRequest.md)
- [foundry_sdk.v2.models.models.ModelStudio](../../../../models/v2/models/models/ModelStudio.md)
- [foundry_sdk.v2.models.models.ModelStudioRid](../../../../models/v2/models/models/ModelStudioRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/ModelStudio.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
