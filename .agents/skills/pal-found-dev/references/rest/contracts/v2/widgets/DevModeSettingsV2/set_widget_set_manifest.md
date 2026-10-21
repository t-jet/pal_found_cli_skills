# v2.widgets.DevModeSettingsV2.set_widget_set_manifest


API v2; release stage: Private Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Set the dev mode settings for the given widget set using the manifest format.
The request body is a dev settings manifest JSON object with the following
structure:

  {
    "manifestVersion": "1.0.0",
    "devSettings": {
      "baseHref": "...",
      "widgets": { ... },
      "inputSpec": { ... }
    }
  }

See [local widget development reference](../../../../../widgets/lifecycle.md) for the widget library API types for the
dev settings manifest.

## Public Python client route

With a configured `foundry_sdk.v2.FoundryClient` named `client`, call `client.widgets.DevModeSettingsV2.set_widget_set_manifest`. This is the public composed resource path in SDK 1.101.0; nested resource names and capitalization matter. Use the signature below for required arguments and selectors. The same resource also exposes documented raw and streaming wrappers when the response-mode table lists them.

## SDK invocation contract

```python
def set_widget_set_manifest(self, *, manifest: typing.Any, widget_set_rid: widgets_models.WidgetSetRid, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> widgets_models.DevModeSettingsV2: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| manifest | typing.Any | required | Value shape and constraints are in its referenced local type definition. |
| widget_set_rid | widgets_models.WidgetSetRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| InvalidDevModeBaseHref | The base href in the dev mode settings is invalid. It must be a valid localhost URL with an optional port. |
| InvalidDevModeEntrypointCssCount | The dev mode settings contains too many CSS entrypoints. You must limit the number of CSS entrypoints to the maximum allowed. |
| InvalidDevModeEntrypointJsCount | The dev mode settings contains too many JavaScript entrypoints. You must limit the number of JavaScript entrypoints to the maximum allowed. |
| InvalidDevModeFilePath | The dev mode settings contains an invalid entrypoint file path. The file path must be a valid localhost URL with an optional port and a file path. |
| InvalidDevModeWidgetSettingsCount | The dev mode settings contains too many widget settings. You must limit the number of widget settings to the maximum allowed. |
| InvalidManifest | The provided manifest could not be parsed or is not well formed. |
| SetWidgetSetManifestDevModeSettingsV2PermissionDenied | Could not setWidgetSetManifest the DevModeSettingsV2. |
| WidgetIdNotFound | A non-existent widget id was provided. If creating a new widget, you must first publish your changes before previewing with developer mode. |

## Wire request

**method**

```python
'POST'
```

**resource_path**

```python
'/v2/widgets/devModeSettingsV2/setWidgetSetManifest'
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
widgets_models.SetWidgetSetManifestDevModeSettingsV2Request(widget_set_rid=widget_set_rid, manifest=manifest)
```

**response_type**

```python
widgets_models.DevModeSettingsV2
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'InvalidDevModeBaseHref': widgets_errors.InvalidDevModeBaseHref, 'InvalidDevModeEntrypointCssCount': widgets_errors.InvalidDevModeEntrypointCssCount, 'InvalidDevModeEntrypointJsCount': widgets_errors.InvalidDevModeEntrypointJsCount, 'InvalidDevModeFilePath': widgets_errors.InvalidDevModeFilePath, 'InvalidDevModeWidgetSettingsCount': widgets_errors.InvalidDevModeWidgetSettingsCount, 'InvalidManifest': widgets_errors.InvalidManifest, 'SetWidgetSetManifestDevModeSettingsV2PermissionDenied': widgets_errors.SetWidgetSetManifestDevModeSettingsV2PermissionDenied, 'WidgetIdNotFound': widgets_errors.WidgetIdNotFound}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `widgets_models.DevModeSettingsV2`. Ordinary async return: `typing.Awaitable[widgets_models.DevModeSettingsV2]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | widgets_models.DevModeSettingsV2 |
| sync_raw | ApiResponse[widgets_models.DevModeSettingsV2] |
| sync_streaming | StreamingContextManager[widgets_models.DevModeSettingsV2] |
| async_ordinary | typing.Awaitable[widgets_models.DevModeSettingsV2] |
| async_raw | Awaitable[AsyncApiResponse[widgets_models.DevModeSettingsV2]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[widgets_models.DevModeSettingsV2]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.widgets.errors.InvalidDevModeBaseHref](../../../../models/v2/widgets/errors/InvalidDevModeBaseHref.md)
- [foundry_sdk.v2.widgets.errors.InvalidDevModeBaseHrefParameters](../../../../models/v2/widgets/errors/InvalidDevModeBaseHrefParameters.md)
- [foundry_sdk.v2.widgets.errors.InvalidDevModeEntrypointCssCount](../../../../models/v2/widgets/errors/InvalidDevModeEntrypointCssCount.md)
- [foundry_sdk.v2.widgets.errors.InvalidDevModeEntrypointCssCountParameters](../../../../models/v2/widgets/errors/InvalidDevModeEntrypointCssCountParameters.md)
- [foundry_sdk.v2.widgets.errors.InvalidDevModeEntrypointJsCount](../../../../models/v2/widgets/errors/InvalidDevModeEntrypointJsCount.md)
- [foundry_sdk.v2.widgets.errors.InvalidDevModeEntrypointJsCountParameters](../../../../models/v2/widgets/errors/InvalidDevModeEntrypointJsCountParameters.md)
- [foundry_sdk.v2.widgets.errors.InvalidDevModeFilePath](../../../../models/v2/widgets/errors/InvalidDevModeFilePath.md)
- [foundry_sdk.v2.widgets.errors.InvalidDevModeFilePathParameters](../../../../models/v2/widgets/errors/InvalidDevModeFilePathParameters.md)
- [foundry_sdk.v2.widgets.errors.InvalidDevModeWidgetSettingsCount](../../../../models/v2/widgets/errors/InvalidDevModeWidgetSettingsCount.md)
- [foundry_sdk.v2.widgets.errors.InvalidDevModeWidgetSettingsCountParameters](../../../../models/v2/widgets/errors/InvalidDevModeWidgetSettingsCountParameters.md)
- [foundry_sdk.v2.widgets.errors.InvalidManifest](../../../../models/v2/widgets/errors/InvalidManifest.md)
- [foundry_sdk.v2.widgets.errors.InvalidManifestParameters](../../../../models/v2/widgets/errors/InvalidManifestParameters.md)
- [foundry_sdk.v2.widgets.errors.SetWidgetSetManifestDevModeSettingsV2PermissionDenied](../../../../models/v2/widgets/errors/SetWidgetSetManifestDevModeSettingsV2PermissionDenied.md)
- [foundry_sdk.v2.widgets.errors.SetWidgetSetManifestDevModeSettingsV2PermissionDeniedParameters](../../../../models/v2/widgets/errors/SetWidgetSetManifestDevModeSettingsV2PermissionDeniedParameters.md)
- [foundry_sdk.v2.widgets.errors.WidgetIdNotFound](../../../../models/v2/widgets/errors/WidgetIdNotFound.md)
- [foundry_sdk.v2.widgets.errors.WidgetIdNotFoundParameters](../../../../models/v2/widgets/errors/WidgetIdNotFoundParameters.md)
- [foundry_sdk.v2.widgets.models.DevModeSettingsV2](../../../../models/v2/widgets/models/DevModeSettingsV2.md)
- [foundry_sdk.v2.widgets.models.DevModeSnapshot](../../../../models/v2/widgets/models/DevModeSnapshot.md)
- [foundry_sdk.v2.widgets.models.DevModeSnapshotId](../../../../models/v2/widgets/models/DevModeSnapshotId.md)
- [foundry_sdk.v2.widgets.models.DevModeStatus](../../../../models/v2/widgets/models/DevModeStatus.md)
- [foundry_sdk.v2.widgets.models.FilePath](../../../../models/v2/widgets/models/FilePath.md)
- [foundry_sdk.v2.widgets.models.OntologySdkInputSpec](../../../../models/v2/widgets/models/OntologySdkInputSpec.md)
- [foundry_sdk.v2.widgets.models.OntologySdkPackageRid](../../../../models/v2/widgets/models/OntologySdkPackageRid.md)
- [foundry_sdk.v2.widgets.models.OntologySdkVersion](../../../../models/v2/widgets/models/OntologySdkVersion.md)
- [foundry_sdk.v2.widgets.models.ScriptEntrypoint](../../../../models/v2/widgets/models/ScriptEntrypoint.md)
- [foundry_sdk.v2.widgets.models.ScriptType](../../../../models/v2/widgets/models/ScriptType.md)
- [foundry_sdk.v2.widgets.models.SetWidgetSetManifestDevModeSettingsV2Request](../../../../models/v2/widgets/models/SetWidgetSetManifestDevModeSettingsV2Request.md)
- [foundry_sdk.v2.widgets.models.StylesheetEntrypoint](../../../../models/v2/widgets/models/StylesheetEntrypoint.md)
- [foundry_sdk.v2.widgets.models.WidgetDevModeSettingsV2](../../../../models/v2/widgets/models/WidgetDevModeSettingsV2.md)
- [foundry_sdk.v2.widgets.models.WidgetId](../../../../models/v2/widgets/models/WidgetId.md)
- [foundry_sdk.v2.widgets.models.WidgetSetDevModeSettingsV2](../../../../models/v2/widgets/models/WidgetSetDevModeSettingsV2.md)
- [foundry_sdk.v2.widgets.models.WidgetSetInputSpec](../../../../models/v2/widgets/models/WidgetSetInputSpec.md)
- [foundry_sdk.v2.widgets.models.WidgetSetRid](../../../../models/v2/widgets/models/WidgetSetRid.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/widgets/DevModeSettingsV2.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- Widget dev settings use a manifest with manifestVersion and devSettings; validate localhost URLs and entrypoint paths. [Local procedure](../../../../../widgets/lifecycle.md).

[Part 1](set_widget_set_manifest.md)
