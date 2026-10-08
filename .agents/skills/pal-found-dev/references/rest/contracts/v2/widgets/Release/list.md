# v2.widgets.Release.list


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Lists all Releases.

This is a paged endpoint. Each page may be smaller or larger than the requested page size. However, it is guaranteed that if there are more results available, the `nextPageToken` field will be populated. To get the next page, make the same request again, but set the value of the `pageToken` query parameter to be value of the `nextPageToken` value of the previous response. If there is no `nextPageToken` field in the response, you are on the last page.

## SDK invocation contract

```python
def list(self, widget_set_rid: widgets_models.WidgetSetRid, *, page_size: typing.Optional[core_models.PageSize]=None, page_token: typing.Optional[core_models.PageToken]=None, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> core.ResourceIterator[widgets_models.Release]: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| widget_set_rid | widgets_models.WidgetSetRid | required | A Resource Identifier (RID) identifying a widget set. |
| page_size | typing.Optional[core_models.PageSize] | None | The page size to use for the endpoint. |
| page_token | typing.Optional[core_models.PageToken] | None | The page token indicates where to start paging. This should be omitted from the first page's request. To fetch the next page, clients should take the value from the `nextPageToken` field of the previous response and use it to populate the `pageToken` field of the next request. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

No named operation errors are listed in this method's docstring; transport and generic API failures remain possible.

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/widgets/widgetSets/{widgetSetRid}/releases'
```

**query_params**

```python
{'pageSize': page_size, 'pageToken': page_token, 'preview': preview}
```

**path_params**

```python
{'widgetSetRid': widget_set_rid}
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
widgets_models.ListReleasesResponse
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{}
```

**response_mode**

```python
_sdk_internal.get('response_mode', 'ITERATOR')
```

## Response modes

Ordinary sync return: `core.ResourceIterator[widgets_models.Release]`. Ordinary async return: `core.AsyncResourceIterator[widgets_models.Release]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | core.ResourceIterator[widgets_models.Release] |
| sync_raw | ApiResponse[widgets_models.ListReleasesResponse] |
| sync_streaming | StreamingContextManager[widgets_models.ListReleasesResponse] |
| async_ordinary | core.AsyncResourceIterator[widgets_models.Release] |
| async_raw | Awaitable[AsyncApiResponse[widgets_models.ListReleasesResponse]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[widgets_models.ListReleasesResponse]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PageSize](../../../../models/v2/core/models/PageSize.md)
- [foundry_sdk.v2.core.models.PageToken](../../../../models/v2/core/models/PageToken.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.widgets.models.ListReleasesResponse](../../../../models/v2/widgets/models/ListReleasesResponse.md)
- [foundry_sdk.v2.widgets.models.Release](../../../../models/v2/widgets/models/Release.md)
- [foundry_sdk.v2.widgets.models.ReleaseLocator](../../../../models/v2/widgets/models/ReleaseLocator.md)
- [foundry_sdk.v2.widgets.models.ReleaseVersion](../../../../models/v2/widgets/models/ReleaseVersion.md)
- [foundry_sdk.v2.widgets.models.RepositoryRid](../../../../models/v2/widgets/models/RepositoryRid.md)
- [foundry_sdk.v2.widgets.models.RepositoryVersion](../../../../models/v2/widgets/models/RepositoryVersion.md)
- [foundry_sdk.v2.widgets.models.WidgetSetRid](../../../../models/v2/widgets/models/WidgetSetRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/widgets/Release.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](list.md)
