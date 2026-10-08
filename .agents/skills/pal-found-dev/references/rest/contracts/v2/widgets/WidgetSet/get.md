# v2.widgets.WidgetSet.get


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the WidgetSet with the specified rid.

## SDK invocation contract

```python
def get(self, widget_set_rid: widgets_models.WidgetSetRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> widgets_models.WidgetSet: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| widget_set_rid | widgets_models.WidgetSetRid | required | A Resource Identifier (RID) identifying a widget set. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| WidgetSetNotFound | The given WidgetSet could not be found. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/widgets/widgetSets/{widgetSetRid}'
```

**query_params**

```python
{'preview': preview}
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
widgets_models.WidgetSet
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'WidgetSetNotFound': widgets_errors.WidgetSetNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `widgets_models.WidgetSet`. Ordinary async return: `typing.Awaitable[widgets_models.WidgetSet]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | widgets_models.WidgetSet |
| sync_raw | ApiResponse[widgets_models.WidgetSet] |
| sync_streaming | StreamingContextManager[widgets_models.WidgetSet] |
| async_ordinary | typing.Awaitable[widgets_models.WidgetSet] |
| async_raw | Awaitable[AsyncApiResponse[widgets_models.WidgetSet]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[widgets_models.WidgetSet]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.widgets.errors.WidgetSetNotFound](../../../../models/v2/widgets/errors/WidgetSetNotFound.md)
- [foundry_sdk.v2.widgets.errors.WidgetSetNotFoundParameters](../../../../models/v2/widgets/errors/WidgetSetNotFoundParameters.md)
- [foundry_sdk.v2.widgets.models.RepositoryRid](../../../../models/v2/widgets/models/RepositoryRid.md)
- [foundry_sdk.v2.widgets.models.WidgetSet](../../../../models/v2/widgets/models/WidgetSet.md)
- [foundry_sdk.v2.widgets.models.WidgetSetRid](../../../../models/v2/widgets/models/WidgetSetRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/widgets/WidgetSet.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
