# foundry_sdk.v2.media_sets.models.ConvertSheetToJsonOperation


Converts a specified sheet to JSON format.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| sheet_name | sheetName | str | required; no default | The sheet name. |
| type | type | typing.Literal['convertSheetToJson'] | 'convertSheetToJson' | No additional field description in SDK source. |

```python
class ConvertSheetToJsonOperation(core.ModelBase):
    """Converts a specified sheet to JSON format."""

    sheet_name: str = pydantic.Field(alias=str("sheetName"))  # type: ignore[literal-required]
    """The sheet name."""

    type: typing.Literal["convertSheetToJson"] = "convertSheetToJson"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ConvertSheetToJsonOperation.md)
