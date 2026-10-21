# foundry_sdk.v2.widgets.models.DevModeSnapshot


A content-addressed snapshot of the dev mode settings. Snapshots are immutable
and identified by their content-addressed ID.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| snapshot_id | snapshotId | DevModeSnapshotId | required; no default | The content-addressed identifier for this snapshot. |
| widget_set_settings | widgetSetSettings | typing.Dict[WidgetSetRid, WidgetSetDevModeSettingsV2] | required; no default | The dev mode settings for each widget set, keyed by widget set RID. |

```python
class DevModeSnapshot(core.ModelBase):
    """
    A content-addressed snapshot of the dev mode settings. Snapshots are immutable
    and identified by their content-addressed ID.
    """

    snapshot_id: DevModeSnapshotId = pydantic.Field(alias=str("snapshotId"))  # type: ignore[literal-required]
    """The content-addressed identifier for this snapshot."""

    widget_set_settings: typing.Dict[WidgetSetRid, WidgetSetDevModeSettingsV2] = pydantic.Field(alias=str("widgetSetSettings"))  # type: ignore[literal-required]
    """The dev mode settings for each widget set, keyed by widget set RID."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.widgets.models.DevModeSnapshotId](DevModeSnapshotId.md)
- [foundry_sdk.v2.widgets.models.WidgetSetDevModeSettingsV2](WidgetSetDevModeSettingsV2.md)
- [foundry_sdk.v2.widgets.models.WidgetSetRid](WidgetSetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](DevModeSnapshot.md)
