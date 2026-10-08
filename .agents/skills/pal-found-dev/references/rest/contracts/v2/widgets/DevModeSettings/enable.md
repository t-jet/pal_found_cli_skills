# v2.widgets.DevModeSettings.enable


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Enable dev mode for the user associated with the provided token.

## SDK invocation contract

```python
def enable(self, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> widgets_models.DevModeSettings: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| EnableDevModeSettingsPermissionDenied | Could not enable the DevModeSettings. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/widgets/devModeSettings/enable'
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
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
widgets_models.DevModeSettings
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'EnableDevModeSettingsPermissionDenied': widgets_errors.EnableDevModeSettingsPermissionDenied}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `widgets_models.DevModeSettings`. Ordinary async return: `typing.Awaitable[widgets_models.DevModeSettings]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | widgets_models.DevModeSettings |
| sync_raw | ApiResponse[widgets_models.DevModeSettings] |
| sync_streaming | StreamingContextManager[widgets_models.DevModeSettings] |
| async_ordinary | typing.Awaitable[widgets_models.DevModeSettings] |
| async_raw | Awaitable[AsyncApiResponse[widgets_models.DevModeSettings]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[widgets_models.DevModeSettings]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.widgets.errors.EnableDevModeSettingsPermissionDenied](../../../../models/v2/widgets/errors/EnableDevModeSettingsPermissionDenied.md)
- [foundry_sdk.v2.widgets.errors.EnableDevModeSettingsPermissionDeniedParameters](../../../../models/v2/widgets/errors/EnableDevModeSettingsPermissionDeniedParameters.md)
- [foundry_sdk.v2.widgets.models.DevModeSettings](../../../../models/v2/widgets/models/DevModeSettings.md)
- [foundry_sdk.v2.widgets.models.DevModeStatus](../../../../models/v2/widgets/models/DevModeStatus.md)
- [foundry_sdk.v2.widgets.models.FilePath](../../../../models/v2/widgets/models/FilePath.md)
- [foundry_sdk.v2.widgets.models.ScriptEntrypoint](../../../../models/v2/widgets/models/ScriptEntrypoint.md)
- [foundry_sdk.v2.widgets.models.ScriptType](../../../../models/v2/widgets/models/ScriptType.md)
- [foundry_sdk.v2.widgets.models.StylesheetEntrypoint](../../../../models/v2/widgets/models/StylesheetEntrypoint.md)
- [foundry_sdk.v2.widgets.models.WidgetDevModeSettings](../../../../models/v2/widgets/models/WidgetDevModeSettings.md)
- [foundry_sdk.v2.widgets.models.WidgetRid](../../../../models/v2/widgets/models/WidgetRid.md)
- [foundry_sdk.v2.widgets.models.WidgetSetDevModeSettings](../../../../models/v2/widgets/models/WidgetSetDevModeSettings.md)
- [foundry_sdk.v2.widgets.models.WidgetSetRid](../../../../models/v2/widgets/models/WidgetSetRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/widgets/DevModeSettings.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](enable.md)
