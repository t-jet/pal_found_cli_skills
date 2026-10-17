# v2.models.Model.create


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Creates a new Model with no versions.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.models.Model.create`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def create(self, *, name: models_models.ModelName, parent_folder_rid: filesystem_models.FolderRid, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> models_models.Model: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| name | models_models.ModelName | required | Value shape and constraints are in its referenced local type definition. |
| parent_folder_rid | filesystem_models.FolderRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CreateModelPermissionDenied | Could not create the Model. |
| InvalidDisplayName | The display name of a resource should not be exactly `.` or `..`, contain a forward slash `/` and must be less than or equal to 700 characters. |
| ResourceNameAlreadyExists | The provided resource name is already in use by another resource in the same folder. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/models'
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
models_models.CreateModelRequest(name=name, parent_folder_rid=parent_folder_rid)
```

**response_type**

```python
models_models.Model
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CreateModelPermissionDenied': models_errors.CreateModelPermissionDenied, 'InvalidDisplayName': filesystem_errors.InvalidDisplayName, 'ResourceNameAlreadyExists': filesystem_errors.ResourceNameAlreadyExists}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `models_models.Model`. Ordinary async return: `typing.Awaitable[models_models.Model]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | models_models.Model |
| sync_raw | ApiResponse[models_models.Model] |
| sync_streaming | StreamingContextManager[models_models.Model] |
| async_ordinary | typing.Awaitable[models_models.Model] |
| async_raw | Awaitable[AsyncApiResponse[models_models.Model]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[models_models.Model]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayName](../../../../models/v2/filesystem/errors/InvalidDisplayName.md)
- [foundry_sdk.v2.filesystem.errors.InvalidDisplayNameParameters](../../../../models/v2/filesystem/errors/InvalidDisplayNameParameters.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExists](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExists.md)
- [foundry_sdk.v2.filesystem.errors.ResourceNameAlreadyExistsParameters](../../../../models/v2/filesystem/errors/ResourceNameAlreadyExistsParameters.md)
- [foundry_sdk.v2.filesystem.models.FolderRid](../../../../models/v2/filesystem/models/FolderRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceDisplayName](../../../../models/v2/filesystem/models/ResourceDisplayName.md)
- [foundry_sdk.v2.models.errors.CreateModelPermissionDenied](../../../../models/v2/models/errors/CreateModelPermissionDenied.md)
- [foundry_sdk.v2.models.errors.CreateModelPermissionDeniedParameters](../../../../models/v2/models/errors/CreateModelPermissionDeniedParameters.md)
- [foundry_sdk.v2.models.models.CreateModelRequest](../../../../models/v2/models/models/CreateModelRequest.md)
- [foundry_sdk.v2.models.models.Model](../../../../models/v2/models/models/Model.md)
- [foundry_sdk.v2.models.models.ModelName](../../../../models/v2/models/models/ModelName.md)
- [foundry_sdk.v2.models.models.ModelRid](../../../../models/v2/models/models/ModelRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/models/Model.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](create.md)
