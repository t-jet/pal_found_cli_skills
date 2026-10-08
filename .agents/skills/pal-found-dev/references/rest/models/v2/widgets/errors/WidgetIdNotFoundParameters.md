# foundry_sdk.v2.widgets.errors.WidgetIdNotFoundParameters


A non-existent widget id was provided. If creating a new widget, you must first publish your changes before
previewing with developer mode.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

TypedDict keys use Required/NotRequired and the declared total setting. A nullable value does not by itself permit key omission.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| widgetSetRid | widgetSetRid | widgets_models.WidgetSetRid | TypedDict key required | No additional field description in SDK source. |
| widgetId | widgetId | str | TypedDict key required | No additional field description in SDK source. |

```python
class WidgetIdNotFoundParameters(typing_extensions.TypedDict):
    """
    A non-existent widget id was provided. If creating a new widget, you must first publish your changes before
    previewing with developer mode.
    """

    __pydantic_config__ = {"extra": "allow"}  # type: ignore

    widgetSetRid: widgets_models.WidgetSetRid
    widgetId: str
```

## Referenced definitions

- [foundry_sdk.v2.widgets.models.WidgetSetRid](../models/WidgetSetRid.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](WidgetIdNotFoundParameters.md)
