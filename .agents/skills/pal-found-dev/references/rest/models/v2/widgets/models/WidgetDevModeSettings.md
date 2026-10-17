# foundry_sdk.v2.widgets.models.WidgetDevModeSettings


The settings for a given widget in development mode.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| script_entrypoints | scriptEntrypoints | typing.List[ScriptEntrypoint] | required; no default | The entrypoint JavaScript files for the widget. |
| stylesheet_entrypoints | stylesheetEntrypoints | typing.List[StylesheetEntrypoint] | required; no default | The entrypoint CSS files for the widget. |

```python
class WidgetDevModeSettings(core.ModelBase):
    """The settings for a given widget in development mode."""

    script_entrypoints: typing.List[ScriptEntrypoint] = pydantic.Field(alias=str("scriptEntrypoints"))  # type: ignore[literal-required]
    """The entrypoint JavaScript files for the widget."""

    stylesheet_entrypoints: typing.List[StylesheetEntrypoint] = pydantic.Field(alias=str("stylesheetEntrypoints"))  # type: ignore[literal-required]
    """The entrypoint CSS files for the widget."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.widgets.models.ScriptEntrypoint](ScriptEntrypoint.md)
- [foundry_sdk.v2.widgets.models.StylesheetEntrypoint](StylesheetEntrypoint.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](WidgetDevModeSettings.md)
