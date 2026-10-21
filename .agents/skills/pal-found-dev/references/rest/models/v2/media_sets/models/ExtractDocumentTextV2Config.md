# foundry_sdk.v2.media_sets.models.ExtractDocumentTextV2Config


Configuration for v2 document text extraction.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| format | format | typing.Optional[TextOutputFormat] | None | No additional field description in SDK source. |
| mode | mode | typing.Optional[OcrMode] | None | No additional field description in SDK source. |
| languages | languages | typing.List[OcrLanguageOrScript] | required; no default | List of OCR languages or scripts to use. |

```python
class ExtractDocumentTextV2Config(core.ModelBase):
    """Configuration for v2 document text extraction."""

    format: typing.Optional[TextOutputFormat] = None
    mode: typing.Optional[OcrMode] = None
    languages: typing.List[OcrLanguageOrScript]
    """List of OCR languages or scripts to use."""
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk.v2.media_sets.models.OcrLanguageOrScript](OcrLanguageOrScript.md)
- [foundry_sdk.v2.media_sets.models.OcrMode](OcrMode.md)
- [foundry_sdk.v2.media_sets.models.TextOutputFormat](TextOutputFormat.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](ExtractDocumentTextV2Config.md)
