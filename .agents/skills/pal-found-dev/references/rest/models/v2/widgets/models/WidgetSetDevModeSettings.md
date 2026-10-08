# foundry_sdk.v2.widgets.models.WidgetSetDevModeSettings


The settings for a widget set in development mode, keyed by widget RID.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| base_href | baseHref | str | required; no default | The base path for the HTML file used to render the widget in dev mode. |
| widget_settings | widgetSettings | typing.Dict[WidgetRid, WidgetDevModeSettings] | required; no default | The dev mode settings for each widget in the widget set, keyed by widget RIDs. |

```python
class WidgetSetDevModeSettings(core.ModelBase):
    """The settings for a widget set in development mode, keyed by widget RID."""

    base_href: str = pydantic.Field(alias=str("baseHref"))  # type: ignore[literal-required]
    """The base path for the HTML file used to render the widget in dev mode."""

    widget_settings: typing.Dict[WidgetRid, WidgetDevModeSettings] = pydantic.Field(alias=str("widgetSettings"))  # type: ignore[literal-required]
    """The dev mode settings for each widget in the widget set, keyed by widget RIDs."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.widgets.models.WidgetDevModeSettings](WidgetDevModeSettings.md)
- [foundry_sdk.v2.widgets.models.WidgetRid](WidgetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](WidgetSetDevModeSettings.md)
