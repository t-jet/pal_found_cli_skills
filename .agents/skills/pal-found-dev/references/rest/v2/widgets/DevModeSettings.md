# Widget development settings by widget ID

[REST catalog](../../catalog.md) | [Widget development lifecycle](../../../widgets/lifecycle.md)

Dev mode changes the calling user's preview configuration. It does not publish a
widget release or change the configuration seen by other users. Use an identity
with access to the widget set and its local development server. SDK 1.101.0
marks these operations Private Beta; check availability in the enrollment.

## enable

Call `client.widgets.DevModeSettings.enable(preview=True)` for the user
represented by the token. The returned `DevModeSettings` records that user's
settings. Read the [exact contract](../../contracts/v2/widgets/DevModeSettings/enable.md)
and [model](../../models/v2/widgets/models/DevModeSettings.md) before storing
its fields. An `EnableDevModeSettingsPermissionDenied` response requires checking
the caller's widget access. Repeating the call with a different user's token
would alter a different user's settings.

Run the [offline SDK fixture](../../../../examples/rest/091/v2/widgets/DevModeSettings/invoke_enable.py)
from the skill root. It checks the SDK request, synthetic result and declared
error without contacting Foundry.

## set_widget_set_by_id

After enabling dev mode, choose the target widget-set RID and provide
`WidgetSetDevModeSettingsById` under `settings`. Its widget IDs identify entries
within that set, so verify each ID against the set's manifest before submitting.
This method changes the calling user's settings for that set. Call
`client.widgets.DevModeSettings.set_widget_set_by_id(settings=...,
widget_set_rid=..., preview=True)`. Read the
[exact contract](../../contracts/v2/widgets/DevModeSettings/set_widget_set_by_id.md)
and [settings model](../../models/v2/widgets/models/WidgetSetDevModeSettingsById.md).

Compare the returned settings with the intended widget-set RID and widget IDs.
For `SetWidgetSetDevModeSettingsByIdPermissionDenied`, check access to that set
and the caller's dev-mode eligibility. For an uncertain write, retrieve the
user's current settings before repeating it. The [offline SDK fixture](../../../../examples/rest/091/v2/widgets/DevModeSettings/invoke_set_widget_set_by_id.py)
shows exact serialization and decoded result.
