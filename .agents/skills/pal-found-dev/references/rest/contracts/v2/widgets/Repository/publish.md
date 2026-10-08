# v2.widgets.Repository.publish


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Publish a new release of a widget set.

## SDK invocation contract

```python
def publish(self, repository_rid: widgets_models.RepositoryRid, body: bytes, *, repository_version: widgets_models.RepositoryVersion, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> widgets_models.Release: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| repository_rid | widgets_models.RepositoryRid | required | A Resource Identifier (RID) identifying a repository. |
| body | bytes | required | The zip file that contains the contents of your widget set. It must include a valid manifest file at the path `.palantir/widgets.config.json`. |
| repository_version | widgets_models.RepositoryVersion | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| PublishReleasePermissionDenied | Could not publish the Repository. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/widgets/repositories/{repositoryRid}/publish'
```

**query_params**

```python
{'repositoryVersion': repository_version, 'preview': preview}
```

**path_params**

```python
{'repositoryRid': repository_rid}
```

**header_params**

```python
{'Content-Type': 'application/octet-stream', 'Accept': 'application/json'}
```

**body**

```python
body
```

**response_type**

```python
widgets_models.Release
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'PublishReleasePermissionDenied': widgets_errors.PublishReleasePermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `widgets_models.Release`. Ordinary async return: `typing.Awaitable[widgets_models.Release]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | widgets_models.Release |
| sync_raw | ApiResponse[widgets_models.Release] |
| sync_streaming | StreamingContextManager[widgets_models.Release] |
| async_ordinary | typing.Awaitable[widgets_models.Release] |
| async_raw | Awaitable[AsyncApiResponse[widgets_models.Release]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[widgets_models.Release]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.widgets.errors.PublishReleasePermissionDenied](../../../../models/v2/widgets/errors/PublishReleasePermissionDenied.md)
- [foundry_sdk.v2.widgets.errors.PublishReleasePermissionDeniedParameters](../../../../models/v2/widgets/errors/PublishReleasePermissionDeniedParameters.md)
- [foundry_sdk.v2.widgets.models.Release](../../../../models/v2/widgets/models/Release.md)
- [foundry_sdk.v2.widgets.models.ReleaseLocator](../../../../models/v2/widgets/models/ReleaseLocator.md)
- [foundry_sdk.v2.widgets.models.ReleaseVersion](../../../../models/v2/widgets/models/ReleaseVersion.md)
- [foundry_sdk.v2.widgets.models.RepositoryRid](../../../../models/v2/widgets/models/RepositoryRid.md)
- [foundry_sdk.v2.widgets.models.RepositoryVersion](../../../../models/v2/widgets/models/RepositoryVersion.md)
- [foundry_sdk.v2.widgets.models.WidgetSetRid](../../../../models/v2/widgets/models/WidgetSetRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/widgets/Repository.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](publish.md)
