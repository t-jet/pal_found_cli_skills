# foundry_sdk.v2.widgets.models.DevModeSettings


DevModeSettings

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| status | status | DevModeStatus | required; no default | No additional field description in SDK source. |
| widget_set_settings | widgetSetSettings | typing.Dict[WidgetSetRid, WidgetSetDevModeSettings] | required; no default | The dev mode settings for each widget set, keyed by widget set RID. |

```python
class DevModeSettings(core.ModelBase):
    """DevModeSettings"""

    status: DevModeStatus
    widget_set_settings: typing.Dict[WidgetSetRid, WidgetSetDevModeSettings] = pydantic.Field(alias=str("widgetSetSettings"))  # type: ignore[literal-required]
    """The dev mode settings for each widget set, keyed by widget set RID."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.widgets.models.DevModeStatus](DevModeStatus.md)
- [foundry_sdk.v2.widgets.models.WidgetSetDevModeSettings](WidgetSetDevModeSettings.md)
- [foundry_sdk.v2.widgets.models.WidgetSetRid](WidgetSetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DevModeSettings.md)
