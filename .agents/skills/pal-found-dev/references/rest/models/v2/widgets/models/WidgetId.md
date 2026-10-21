# foundry_sdk.v2.widgets.models.WidgetId



Human readable ID for a widget. Must be unique within a widget set.
Considered unsafe as it may contain user defined data.

- Must only contain the following ASCII characters: a-z, A-Z and 0-9.
- Must not start with a number.
- Must have a maximum length of 100.
- Must be camelCase.


## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

```python
WidgetId: typing_extensions.TypeAlias = str
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](WidgetId.md)
