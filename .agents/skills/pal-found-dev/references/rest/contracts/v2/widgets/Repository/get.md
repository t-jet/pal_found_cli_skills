# v2.widgets.Repository.get


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the Repository with the specified rid.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.widgets.Repository.get`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def get(self, repository_rid: widgets_models.RepositoryRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> widgets_models.Repository: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| repository_rid | widgets_models.RepositoryRid | required | A Resource Identifier (RID) identifying a repository. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| RepositoryNotFound | The given Repository could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/widgets/repositories/{repositoryRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'repositoryRid': repository_rid}
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
widgets_models.Repository
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'RepositoryNotFound': widgets_errors.RepositoryNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `widgets_models.Repository`. Ordinary async return: `typing.Awaitable[widgets_models.Repository]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | widgets_models.Repository |
| sync_raw | ApiResponse[widgets_models.Repository] |
| sync_streaming | StreamingContextManager[widgets_models.Repository] |
| async_ordinary | typing.Awaitable[widgets_models.Repository] |
| async_raw | Awaitable[AsyncApiResponse[widgets_models.Repository]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[widgets_models.Repository]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.widgets.errors.RepositoryNotFound](../../../../models/v2/widgets/errors/RepositoryNotFound.md)
- [foundry_sdk.v2.widgets.errors.RepositoryNotFoundParameters](../../../../models/v2/widgets/errors/RepositoryNotFoundParameters.md)
- [foundry_sdk.v2.widgets.models.Repository](../../../../models/v2/widgets/models/Repository.md)
- [foundry_sdk.v2.widgets.models.RepositoryRid](../../../../models/v2/widgets/models/RepositoryRid.md)
- [foundry_sdk.v2.widgets.models.WidgetSetRid](../../../../models/v2/widgets/models/WidgetSetRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/widgets/Repository.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
