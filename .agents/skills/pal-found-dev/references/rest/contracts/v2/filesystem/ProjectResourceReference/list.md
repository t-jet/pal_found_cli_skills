# v2.filesystem.ProjectResourceReference.list


API v2; release stage: Stable. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

List all references in the given project

## SDK invocation contract

```python
def list(self, project_rid: filesystem_models.ProjectRid, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, reference_type: typing.Optional[filesystem_models.ProjectResourceReferenceType]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[filesystem_models.ProjectResourceReference]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| project_rid | filesystem_models.ProjectRid | required | Value shape and constraints are in its referenced local type definition. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| reference_type | typing.Optional[filesystem_models.ProjectResourceReferenceType] | None | Filter references by type. If not provided, all references are returned. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| ProjectNotFound | The given Project could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/filesystem/projects/{projectRid}/references'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token, 'referenceType': reference_type}
```

**path_params**

```python
{'projectRid': project_rid}
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
filesystem_models.ListProjectResourceReferencesResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'ProjectNotFound': filesystem_errors.ProjectNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[filesystem_models.ProjectResourceReference]`. Ordinary async return: `core.AsyncResourceIterator[filesystem_models.ProjectResourceReference]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[filesystem_models.ProjectResourceReference] |
| sync_raw | ApiResponse[filesystem_models.ListProjectResourceReferencesResponse] |
| sync_streaming | StreamingContextManager[filesystem_models.ListProjectResourceReferencesResponse] |
| async_ordinary | core.AsyncResourceIterator[filesystem_models.ProjectResourceReference] |
| async_raw | Awaitable[AsyncApiResponse[filesystem_models.ListProjectResourceReferencesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[filesystem_models.ListProjectResourceReferencesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.UserId](../../../../models/v2/core/models/UserId.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFound](../../../../models/v2/filesystem/errors/ProjectNotFound.md)
- [foundry_sdk.v2.filesystem.errors.ProjectNotFoundParameters](../../../../models/v2/filesystem/errors/ProjectNotFoundParameters.md)
- [foundry_sdk.v2.filesystem.models.ListProjectResourceReferencesResponse](../../../../models/v2/filesystem/models/ListProjectResourceReferencesResponse.md)
- [foundry_sdk.v2.filesystem.models.ProjectExternalResourceReference](../../../../models/v2/filesystem/models/ProjectExternalResourceReference.md)
- [foundry_sdk.v2.filesystem.models.ProjectFilesystemResourceReference](../../../../models/v2/filesystem/models/ProjectFilesystemResourceReference.md)
- [foundry_sdk.v2.filesystem.models.ProjectResourceReference](../../../../models/v2/filesystem/models/ProjectResourceReference.md)
- [foundry_sdk.v2.filesystem.models.ProjectResourceReferenceType](../../../../models/v2/filesystem/models/ProjectResourceReferenceType.md)
- [foundry_sdk.v2.filesystem.models.ProjectResourceReferenceUnion](../../../../models/v2/filesystem/models/ProjectResourceReferenceUnion.md)
- [foundry_sdk.v2.filesystem.models.ProjectRid](../../../../models/v2/filesystem/models/ProjectRid.md)
- [foundry_sdk.v2.filesystem.models.ResourceRid](../../../../models/v2/filesystem/models/ResourceRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/filesystem/ProjectResourceReference.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
