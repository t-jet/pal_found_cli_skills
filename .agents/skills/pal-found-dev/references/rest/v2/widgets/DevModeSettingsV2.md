# Widget development settings with a manifest

[REST catalog](../../catalog.md) | [Widget development lifecycle](../../../widgets/lifecycle.md)

These Private Beta methods configure a preview for the token's user. The
manifest form addresses widget entries and their development assets as a
single document. It does not publish a release.

## enable

Call `client.widgets.DevModeSettingsV2.enable(preview=True)` with an
identity permitted to preview the widget set. Check the returned
`DevModeSettingsV2` before applying a manifest. A
`EnableDevModeSettingsV2PermissionDenied` result calls for checking the user's
access and preview availability. Read the [exact contract](../../contracts/v2/widgets/DevModeSettingsV2/enable.md)
and run the [offline SDK fixture](../../../../examples/rest/091/v2/widgets/DevModeSettingsV2/invoke_enable.py).

## set_widget_set_manifest

Submit `widget_set_rid` and a `manifest` JSON object. The SDK accepts `Any`,
so validate the payload before the call. It needs `manifestVersion`, then
`devSettings` with `baseHref`, `widgets`, and `inputSpec`. `baseHref` and entrypoint
paths must point to a valid localhost URL with an optional port. Check the
[exact contract and named errors](../../contracts/v2/widgets/DevModeSettingsV2/set_widget_set_manifest.md)
for the available version before adapting the manifest. The source does not
promise that an arbitrary remote URL or arbitrary count of CSS/JavaScript
entrypoints will work.

Call `client.widgets.DevModeSettingsV2.set_widget_set_manifest(
widget_set_rid=..., manifest=..., preview=True)` and compare the returned
settings with the target set. Invalid base URL, file path, entrypoint count or
widget count errors should be fixed in the manifest before retry. For a
permission error, verify the caller and set access. The [offline SDK fixture](../../../../examples/rest/091/v2/widgets/DevModeSettingsV2/invoke_set_widget_set_manifest.py)
checks the serialized JSON and declared errors using a fake transport.
